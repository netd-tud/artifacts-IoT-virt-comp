# import micropython

SCALE_FACTOR = 1


class ReturnCodes(int):
    SLRE_NO_MATCH = -1
    SLRE_UNEXPECTED_QUANTIFIER = -2
    SLRE_UNBALANCED_BRACKETS = -3
    SLRE_INTERNAL_ERROR = -4
    SLRE_INVALID_CHARACTER_SET = -5
    SLRE_INVALID_METACHARACTER = -6
    SLRE_CAPS_ARRAY_TOO_SMALL = -7
    SLRE_TOO_MANY_BRANCHES = -8
    SLRE_TOO_MANY_BRACKETS = -9


class OffsetString:
    def __init__(self, data):
        self.data = data
        self.end = len(data)
        self.offset = 0

    def __str__(self):
        return self.data[self.offset:self.end]

    def __len__(self):
        assert self.offset <= self.end
        return self.end - self.offset

    def __getitem__(self, key):
        return str(self)[key]

    def shallow_copy(self):
        return OffsetString(self.data)

    def advance(self, n):
        self.offset += n

    def advance_to(self, offset):
        self.offset += offset

    def abs_slice(self, start, length):
        res = self.shallow_copy()
        res.offset = start
        res.end = start + length
        return res

    def rel_slice(self, rel_start, length):
        return self.abs_slice(self.offset + rel_start, length)


def regex_iterate(re_str):
    # Build and return a list of (offset, op_length) tuples for the regex
    # string. A proper iterator would be prefed here but the micropython
    # implementation on arm crashes when using an iterator here. I did not
    # have time to replicate this issue yet
    result = []
    iter_offset = re_str.offset
    while iter_offset < re_str.end:
        iter_str = re_str.data[iter_offset:]
        op_length = get_op_len(iter_str)
        result.append((iter_offset, op_length))
        iter_offset += op_length
    return result


class BracketPair:
    def __init__(self, start_offset):
        self.start_offset = start_offset
        self.length = None
        self.branch_index = None
        self.num_branches = None


class Branch:
    def __init__(self, bracket_index, offset):
        self.bracket_index = bracket_index
        self.offset = offset


class Capture:
    def __init__(self, start_offset=None, length=None):
        self.start_offset = start_offset
        self.length = length


class RegexInfo:
    def __init__(self, captures):
        self.brackets = []
        self.branches = []
        self.captures = captures
        self.ignore_case = False


def is_metacharacter(s):
    return s in '^$().[]*+?|\\Ssd'


def op_len(re):
    if re[0] == '\\':
        if re[1] == 'x':
            return 4
        return 2
    return 1


def set_len(re):
    i = 0
    while i < len(re) and re[i] != ']':
        i += op_len(re[i])

    if i <= len(re):
        return i + 1
    else:
        # This only happens when a regex ends with \x but does not supply
        # two characters afterward.
        raise ValueError


def get_op_len(re):
    if re[0] == '[':
        return set_len(re[1:]) + 1
    else:
        return op_len(re)


def is_quantifier(re):
    return re[0] in ['*', '+', '?']


def hextoi(s):
    return int(s, 16)


def match_op(re, s, info):
    result = 0
    if re[0] == '\\':
        # Metacharacters
        if re[1] == 'S':
            if s[0].isspace():
                return ReturnCodes.SLRE_NO_MATCH
            result += 1
        elif re[1] == 's':
            if not s[0].isspace():
                return ReturnCodes.SLRE_NO_MATCH
            result += 1
        elif re[1] == 'd':
            if not s[0].isdigit():
                return ReturnCodes.SLRE_NO_MATCH
            result += 1
        elif re[1] == 'x':
            # \xHH where HH is hexadecimal byte representation
            if hextoi(re[2]) != s[0]:
                return ReturnCodes.SLRE_NO_MATCH
            result += 1
        else:
            # Valid metacharacter check is done in bar()
            if re[1] != s[0]:
                return ReturnCodes.SLRE_NO_MATCH
            result += 1
    elif re[0] == '|':
        return ReturnCodes.SLRE_INTERNAL_ERROR
    elif re[0] == '$':
        return ReturnCodes.SLRE_NO_MATCH
    elif re[0] == '.':
        result += 1
    else:
        if not s:
            # String is empty
            return ReturnCodes.SLRE_NO_MATCH
        if info.ignore_case:
            if re[0].lower() != s[0].lower():
                return ReturnCodes.SLRE_NO_MATCH
        else:
            if re[0] != s[0]:
                return ReturnCodes.SLRE_NO_MATCH
        result += 1
    return result


def match_set(re, re_len, s, info):
    i = 0
    result = -1
    invert = re[0] == '^'

    if invert:
        re += 1
        re_len -= 1

    while i <= re_len and re[i] != ']' and result <= 0:
        if re[i] != '-' and re[i + 1] == '-' and re[i + 2] != ']' and i + 2 > len(re):
            if info.ignore_case:
                result = re[i] <= s[0] <= re[i + 2]
            else:
                result = re[i] <= s[0].lower() <= re[i + 2]
            i += 3
        else:
            result = match_op(re[i:], s, info)
            i += op_len(re[i:])

    matched = result > 0
    # we want to return 1 if either inverted is true and matched not True
    # or the other way around.
    # Conversely, If both are true or not true we return -1
    return 1 if matched ^ invert else -1


def bar(re, s, info, bi):
    re_off = 0
    s_off = 0

    while re_off < len(re) and s_off <= len(s):
        if re[re_off] == '(':
            assert info.brackets[bi + 1].length is not None
            step = info.brackets[bi + 1].length + 2
        else:
            step = get_op_len(re[re_off:])
        if step <= 0:
            return ReturnCodes.SLRE_INVALID_CHARACTER_SET
        if is_quantifier(str(re)):
            return ReturnCodes.SLRE_UNEXPECTED_QUANTIFIER

        if re_off + step < len(re) and is_quantifier(re[re_off + step]):
            if re[re_off + step] == '?':
                res = bar(re.rel_slice(re_off, step), s.rel_slice(s_off, len(s) - s_off), info, bi)
                s_off += res if res > 0 else 0
                re_off += 1
            elif re[re_off + step] in ['+', '*']:
                s_off_inner = s_off
                ns_off = s_off
                non_greedy = False

                after_quant = re_off + step + 1
                if after_quant < len(re) and re[after_quant] == '?':
                    non_greedy = True
                    after_quant += 1

                n1 = 1
                n2 = -1
                while n1 > 0:
                    n1 = bar(
                        re.rel_slice(re_off, step),
                        s.rel_slice(s_off_inner, len(s) - s_off_inner),
                        info,
                        bi
                    )
                    if n1 > 0:
                        s_off_inner += n1
                    if re[re_off + step] == '+' and n1 < 0:
                        break

                    if after_quant >= len(re):
                        ns_off = s_off_inner
                    else:
                        n2 = bar(
                            re.rel_slice(after_quant, len(re) - after_quant),
                            s.rel_slice(s_off_inner, len(s) - s_off_inner),
                            info,
                            bi
                        )
                        if n2 >= 0:
                            ns_off = s_off_inner + n2

                    if ns_off > s_off and non_greedy:
                        break

                if n1 < 0 and re[re_off + step] == '*':
                    n2 = bar(
                        re.rel_slice(after_quant, len(re) - after_quant),
                        s.rel_slice(s_off_inner, len(s) - s_off_inner),
                        info,
                        bi
                    )
                    if n2 >= 0:
                        ns_off = s_off_inner + n2

                if re[step] == '+' and ns_off == s_off:
                    return ReturnCodes.SLRE_NO_MATCH

                if ns_off == s_off and after_quant < len(re) and n2 < 0:
                    return ReturnCodes.SLRE_NO_MATCH

                return ns_off
            re_off += step
            continue

        if re[re_off] == '[':
            n = match_set(re[re_off + 1:], len(re) - (re_off + 2), s[s_off:], info)
            if n <= 0:
                return ReturnCodes.SLRE_NO_MATCH
            s_off += n
        elif re[re_off] == '(':
            n = ReturnCodes.SLRE_NO_MATCH
            bi += 1
            if bi >= len(info.brackets):
                return ReturnCodes.SLRE_INTERNAL_ERROR

            if re_off + step >= len(re):
                n = doh(re, s.rel_slice(s_off, len(s) - s_off), info, bi)
            else:
                for j2 in range(0, len(s) - s_off + 1):
                    n = doh(re, s.rel_slice(s_off, len(s) - (s_off + j2)), info, bi)
                    if n < 0:
                        continue
                    tmp = bar(
                        re.rel_slice(re_off + step, len(re) - (re_off + step)),
                        s.rel_slice(s_off + n, len(s) - (s_off + n)),
                        info,
                        bi
                    )
                    if tmp >= 0:
                        break

            if n < 0:
                return n
            while len(info.captures) < bi:
                info.captures.append(Capture())

            info.captures[bi - 1] = Capture(s.offset + s_off, n)
            s_off += n
        elif re[re_off] == '^':
            if s_off != 0:
                return ReturnCodes.SLRE_NO_MATCH
        elif re[re_off] == '$':
            if s_off != len(s):
                return ReturnCodes.SLRE_NO_MATCH
        else:
            if s_off >= len(s):
                return ReturnCodes.SLRE_NO_MATCH
            n = match_op(re[re_off:], s[s_off], info)
            if n <= 0:
                return n
            s_off += n
        re_off += step
    return s_off


# Process branch points
def doh(re, s, info, bi):
    bp = info.brackets[bi]

    # position of the branch we are matching in the regex str
    pos = 0
    # length of the Branch
    length = 0

    for i in [0] + list(range(1, bp.num_branches)):
        if i == 0:
            pos = bp.start_offset
        else:
            pos = info.branches[bp.branch_index + i - 1].offset + 1

        if bp.num_branches == 0:
            length = bp.length
        elif bp.num_branches == i:
            length = bp.start_offset + bp.length - pos
        else:
            length = info.branches[bp.branch_index + i].offset - pos

        result = bar(re.abs_slice(pos, length), s, info, bi)
        if result > 0 or i >= bp.num_branches:
            break
    return result


def baz(re, s, info):
    result = -1
    is_anchored = str(re).startswith('^')

    for i in range(len(str(s))):
        result = doh(re, s, info, 0)
        s.advance(1)
        if result >= 0:
            result += i
            break
        if is_anchored:
            break

    return result


def setup_branch_points(info):
    for i in range(len(info.branches)):
        for j in range(len(info.branches)):
            if info.branches[i].bracket_index > info.branches[j].bracket_index:
                tmp = info.branches[i]
                info.branches[i] = info.branches[j]
                info.branches[j] = tmp

    j = 0

    for i, bp in enumerate(info.brackets):
        bp.num_branches = 0
        bp.branch_index = j
        while j < len(info.branches) and info.branches[j].bracket_index == i:
            bp.num_branches += 1
            j += 1


def foo(re, s, info):
    depth = 0
    hexdigits = "0123456789abcdefABCDEF"

    # First bracket captures everything
    bracket = BracketPair(re.offset)
    bracket.length = len(re)
    info.brackets.append(bracket)

    # Build the list of (offset, op_length) pairs up front
    items = regex_iterate(re)

    # Make a single pass over regex string, memorize brackets and branches
    for (offset, op_length) in items:
        # Build the operator string from the offset and precomputed length
        seq = re.data[offset:offset + op_length]

        if seq[0] == '|':
            if info.brackets[-1].length is None:
                # We are currently in a bracket
                current_bracket_pair = len(info.brackets)
            else:
                # We have left all brackets
                current_bracket_pair = depth
            info.branches.append(Branch(current_bracket_pair, offset))
        elif seq[0] == '\\':
            # this is the case where the iterator raises a ValueError
            if len(seq) < 2 or seq[1] == 'x' \
                    and (len(seq) < 4 or not all(c in hexdigits for c in seq[2:4])):
                return ReturnCodes.SLRE_INVALID_METACHARACTER
        elif seq[0] == '(':
            depth += 1
            info.brackets.append(BracketPair(offset + 1))
        elif seq[0] == ')':
            # I think this (and the original) does not work for arbitrarily
            # nested capture groups.
            # for example (  )  (  (  )  )  (  (  )  )
            #             ^  ^  ^  ^  ^  ^  ^  ^  ^  ^
            #             A     B  C        D  E
            #     depth = 1  0  1  2  1  0  1  2  1  0
            #
            # info.brackets = [A, B, C, D, E]
            #                  0  1  2  3  4
            #
            # When we close a bracket we check if the top most bracket pair (bp)
            # is open (length is None) and if it is we close it.
            # If it is not we instead use the depth as an index to close it.
            # This means for A, C, and E we use the top most bp.
            # For B, we use the depth before closing as an index: 1 => B.
            # For D we also use the depth as an index: 1 => B
            # Here we use the wrong bp pair. We would need a per depth count of
            # closed brackets.
            i = len(info.brackets) - 1 if info.brackets[-1].length is None else depth
            info.brackets[i].length = offset - info.brackets[i].start_offset
            depth -= 1
            if depth < 0:
                return ReturnCodes.SLRE_UNBALANCED_BRACKETS
            if re[offset - 1] == '(':
                # We have a () group
                return ReturnCodes.SLRE_NO_MATCH
        else:
            pass

    if depth != 0:
        return ReturnCodes.SLRE_UNBALANCED_BRACKETS
    setup_branch_points(info)

    return baz(re, s, info)


def slre_match(regexp, s_str, caps):
    info = RegexInfo(caps)
    re = OffsetString(regexp)
    s = OffsetString(s_str)

    if str(re).startswith('(?i)'):
        info.ingnore_case = True
        re.advance(4)

    return foo(re, s, info)


def initialize_benchmark():
    pass


def benchmark():
    initialize_benchmark()
    res = benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(res)


def benchmark_body(lsf):
    text = "abbbababaabccababcacbcbcbabbabcbabcabcbbcbbac"
    regexes = ["(ab)+", "(b.+)+", "a[ab]*", "([ab^c][ab^c])+"]

    ret = 0
    for _ in range(lsf):
        captures = []
        for r in regexes:
            ret += slre_match(r, text, captures)

    return ret


def verify_benchmark(r):
    return 102 * SCALE_FACTOR == r
