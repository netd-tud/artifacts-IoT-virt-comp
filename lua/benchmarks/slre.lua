SCALE_FACTOR = 1

SLRE_NO_MATCH = -1
SLRE_UNEXPECTED_QUANTIFIER = -2
SLRE_UNBALANCED_BRACKETS = -3
SLRE_INTERNAL_ERROR = -4
SLRE_INVALID_CHARACTER_SET = -5
SLRE_INVALID_METACHARACTER = -6
SLRE_CAPS_ARRAY_TOO_SMALL = -7
SLRE_TOO_MANY_BRANCHES = -8
SLRE_TOO_MANY_BRACKETS = -9

local get_op_len

-- OffsetString "class"
OffsetString = {}
OffsetString.__index = OffsetString

function OffsetString:new(data)
    local o = {}
    setmetatable(o, OffsetString)
    o.data = data
    o.offset = 1          -- 1-based
    o.stop = #data + 1    -- one past the end (exclusive), so length = stop - offset
    return o
end

function OffsetString:tostring()
    return string.sub(self.data, self.offset, self.stop - 1)
end

function OffsetString:len()
    assert(self.offset <= self.stop)
    return self.stop - self.offset
end

-- get character at 1-based position relative to offset
function OffsetString:char_at(i)
    local pos = self.offset + i - 1
    if pos < 1 or pos > #self.data then
        return nil
    end
    return string.sub(self.data, pos, pos)
end

-- substring relative to offset, 1-based start, length-based
-- sub(i) returns from relative position i to end of the slice
-- sub(i, len) returns len characters starting at relative position i
function OffsetString:sub(i, len)
    local start = self.offset + i - 1
    if len == nil then
        return string.sub(self.data, start, self.stop - 1)
    end
    return string.sub(self.data, start, start + len - 1)
end

-- get a raw substring from the underlying data for use with plain string functions
-- positions are absolute (1-based into self.data)
function OffsetString:abs_char(pos)
    return string.sub(self.data, pos, pos)
end

function OffsetString:shallow_copy()
    return OffsetString:new(self.data)
end

function OffsetString:advance(n)
    self.offset = self.offset + n
end

function OffsetString:advance_to(off)
    self.offset = self.offset + off
end

function OffsetString:abs_slice(start, length)
    local res = self:shallow_copy()
    res.offset = start
    res.stop = start + length
    return res
end

function OffsetString:rel_slice(rel_start, length)
    return self:abs_slice(self.offset + rel_start, length)
end

-- BracketPair
local function new_bracket_pair(start_offset)
    return {
        start_offset = start_offset,
        length = nil,
        branch_index = nil,
        num_branches = nil
    }
end

-- Branch
local function new_branch(bracket_index, offset)
    return {
        bracket_index = bracket_index,
        offset = offset
    }
end

-- Capture
local function new_capture(start_offset, length)
    return {
        start_offset = start_offset or nil,
        length = length or nil
    }
end

-- RegexInfo
local function new_regex_info(captures)
    return {
        brackets = {},
        branches = {},
        captures = captures,
        ignore_case = false
    }
end

-- RegexIterator: returns an iterator function
-- Each call returns (seq, offset) where seq is the operator string and offset is absolute position
local function regex_iterator(re_str)
    local iter_offset = re_str.offset
    return function()
        if iter_offset < re_str.stop then
            local iter_str = string.sub(re_str.data, iter_offset)
            local oplen = get_op_len(iter_str)
            local seq = string.sub(iter_str, 1, oplen)
            local current_offset = iter_offset
            iter_offset = iter_offset + oplen
            return seq, current_offset
        else
            return nil
        end
    end
end

-- Helper functions

local function is_space(ch)
    return ch == ' ' or ch == '\t' or ch == '\n' or ch == '\r' or ch == '\f' or ch == '\v'
end

local function is_digit(ch)
    local b = string.byte(ch)
    return b >= string.byte('0') and b <= string.byte('9')
end

local function is_hexdigit(ch)
    local lower = string.lower(ch)
    local b = string.byte(lower)
    return (b >= string.byte('0') and b <= string.byte('9')) or
           (b >= string.byte('a') and b <= string.byte('f'))
end

local function char_lower(ch)
    return string.lower(ch)
end

local function is_metacharacter(s)
    local metas = "^$().[]*+?|\\Ssd"
    return string.find(metas, s, 1, true) ~= nil
end

local function op_len(re)
    if string.sub(re, 1, 1) == '\\' then
        if string.sub(re, 2, 2) == 'x' then
            return 4
        end
        return 2
    end
    return 1
end

local function set_len(re)
    local i = 1
    while i <= #re and string.sub(re, i, i) ~= ']' do
        i = i + op_len(string.sub(re, i))
    end

    if i <= #re then
        return i  -- includes the ']'
    else
        error("Invalid character set")
    end
end

get_op_len = function(re)
    if string.sub(re, 1, 1) == '[' then
        return set_len(string.sub(re, 2)) + 1
    else
        return op_len(re)
    end
end

local function is_quantifier(re)
    local ch = string.sub(re, 1, 1)
    return ch == '*' or ch == '+' or ch == '?'
end

local function hextoi(s)
    return tonumber(s, 16)
end

local function match_op(re, s, info)
    local result = 0
    local re1 = string.sub(re, 1, 1)
    local s1 = string.sub(s, 1, 1)

    if re1 == '\\' then
        local re2 = string.sub(re, 2, 2)
        if re2 == 'S' then
            if is_space(s1) then
                return SLRE_NO_MATCH
            end
            result = result + 1
        elseif re2 == 's' then
            if not is_space(s1) then
                return SLRE_NO_MATCH
            end
            result = result + 1
        elseif re2 == 'd' then
            if not is_digit(s1) then
                return SLRE_NO_MATCH
            end
            result = result + 1
        elseif re2 == 'x' then
            if hextoi(string.sub(re, 3, 4)) ~= string.byte(s1) then
                return SLRE_NO_MATCH
            end
            result = result + 1
        else
            if re2 ~= s1 then
                return SLRE_NO_MATCH
            end
            result = result + 1
        end
    elseif re1 == '|' then
        return SLRE_INTERNAL_ERROR
    elseif re1 == '$' then
        return SLRE_NO_MATCH
    elseif re1 == '.' then
        result = result + 1
    else
        if #s == 0 then
            return SLRE_NO_MATCH
        end
        if info.ignore_case then
            if char_lower(re1) ~= char_lower(s1) then
                return SLRE_NO_MATCH
            end
        else
            if re1 ~= s1 then
                return SLRE_NO_MATCH
            end
        end
        result = result + 1
    end
    return result
end

local function match_set(re, re_len, s, info)
    local i = 1
    local result = -1
    local invert = (string.sub(re, 1, 1) == '^')

    if invert then
        re = string.sub(re, 2)
        re_len = re_len - 1
    end

    local s1 = string.sub(s, 1, 1)

    while i <= re_len and string.sub(re, i, i) ~= ']' and result <= 0 do
        local re_i = string.sub(re, i, i)
        local re_i1 = string.sub(re, i + 1, i + 1)
        local re_i2 = string.sub(re, i + 2, i + 2)

        if re_i ~= '-' and re_i1 == '-' and re_i2 ~= ']' and (i + 2) <= #re then
            if info.ignore_case then
                if re_i <= char_lower(s1) and char_lower(s1) <= re_i2 then
                    result = 1
                else
                    result = -1
                end
            else
                if re_i <= s1 and s1 <= re_i2 then
                    result = 1
                else
                    result = -1
                end
            end
            i = i + 3
        else
            result = match_op(string.sub(re, i), s, info)
            i = i + op_len(string.sub(re, i))
        end
    end

    local matched = result > 0
    -- XOR: return 1 if matched ~= invert, else -1
    if (matched and not invert) or (not matched and invert) then
        return 1
    else
        return -1
    end
end

-- Forward declarations
local bar, doh, baz, foo

bar = function(re, s, info, bi)
    local re_off = 0
    local s_off = 0

    while re_off < re:len() and s_off <= s:len() do
        local step
        if re:char_at(re_off + 1) == '(' then
            assert(info.brackets[bi + 1].length ~= nil)
            step = info.brackets[bi + 1].length + 2
        else
            step = get_op_len(re:sub(re_off + 1))
        end

        --print(string.format('bar [%s] [%s] re_len=%d step=%d i=%d j=%d',
        --    re:sub(re_off + 1), s:sub(s_off + 1), re:len(), step, re_off, s_off))

        if step <= 0 then
            return SLRE_INVALID_CHARACTER_SET
        end
        if is_quantifier(re:tostring()) then
            return SLRE_UNEXPECTED_QUANTIFIER
        end

        if re_off + step < re:len() and is_quantifier(re:sub(re_off + step + 1, 1)) then
            local quant_char = re:sub(re_off + step + 1, 1)
            --print(string.format("QUANTIFIER: [%s]%s [%s]",
            --    re:sub(re_off + 1, step), quant_char, s:sub(s_off + 1)))

            if quant_char == '?' then
                local res = bar(re:rel_slice(re_off, step), s:rel_slice(s_off, s:len() - s_off), info, bi)
                if res > 0 then
                    s_off = s_off + res
                end
                re_off = re_off + 1
            elseif quant_char == '+' or quant_char == '*' then
                local s_off_inner = s_off
                local ns_off = s_off
                local non_greedy = false

                local after_quant = re_off + step + 1
                if after_quant < re:len() and re:char_at(after_quant + 1) == '?' then
                    non_greedy = true
                    after_quant = after_quant + 1
                end

                local n1 = 1
                local n2 = -1
                while n1 > 0 do
                    n1 = bar(
                        re:rel_slice(re_off, step),
                        s:rel_slice(s_off_inner, s:len() - s_off_inner),
                        info,
                        bi
                    )
                    if n1 > 0 then
                        s_off_inner = s_off_inner + n1
                    end
                    if quant_char == '+' and n1 < 0 then
                        break
                    end

                    if after_quant >= re:len() then
                        ns_off = s_off_inner
                    else
                        n2 = bar(
                            re:rel_slice(after_quant, re:len() - after_quant),
                            s:rel_slice(s_off_inner, s:len() - s_off_inner),
                            info,
                            bi
                        )
                        if n2 >= 0 then
                            ns_off = s_off_inner + n2
                        end
                    end

                    if ns_off > s_off and non_greedy then
                        break
                    end
                end

                if n1 < 0 and quant_char == '*' then
                    n2 = bar(
                        re:rel_slice(after_quant, re:len() - after_quant),
                        s:rel_slice(s_off_inner, s:len() - s_off_inner),
                        info,
                        bi
                    )
                    if n2 >= 0 then
                        ns_off = s_off_inner + n2
                    end
                end

                --print(string.format("STAR/PLUS END: %d %d %d %d %d",
                --    s_off, s_off_inner, re:len() - after_quant, n1, n2))

                if quant_char == '+' and ns_off == s_off then
                    return SLRE_NO_MATCH
                end

                if ns_off == s_off and after_quant < re:len() and n2 < 0 then
                    return SLRE_NO_MATCH
                end

                return ns_off
            end
            re_off = re_off + step
            -- continue equivalent: skip the rest of the loop body
            goto continue_bar
        end

        local re_char = re:char_at(re_off + 1)

        if re_char == '[' then
            local n = match_set(re:sub(re_off + 2), re:len() - (re_off + 2), s:sub(s_off + 1), info)
            --print(string.format('SET %s [%s] -> %d', re:sub(re_off + 1, step), s:sub(s_off + 1), n))
            if n <= 0 then
                return SLRE_NO_MATCH
            end
            s_off = s_off + n
        elseif re_char == '(' then
            local n = SLRE_NO_MATCH
            bi = bi + 1
            if bi > #info.brackets then
                return SLRE_INTERNAL_ERROR
            end
            --print(string.format("CAPTURING [%s] [%s] [%s]",
            --    re:sub(re_off + 1, step),
            --    s:sub(s_off + 1),
            --    re:abs_char(re.offset + re_off + step)))

            if re_off + step >= re:len() then
                n = doh(re, s:rel_slice(s_off, s:len() - s_off), info, bi)
            else
                for j2 = 0, s:len() - s_off do
                    n = doh(re, s:rel_slice(s_off, s:len() - (s_off + j2)), info, bi)
                    if n < 0 then
                        goto continue_j2
                    end
                    local tmp = bar(
                        re:rel_slice(re_off + step, re:len() - (re_off + step)),
                        s:rel_slice(s_off + n, s:len() - (s_off + n)),
                        info,
                        bi
                    )
                    if tmp >= 0 then
                        break
                    end
                    ::continue_j2::
                end
            end

            --print(string.format("CAPTURED [%s] [%s]:%d",
            --    re:sub(re_off + 1, step), s:sub(s_off + 1), n))
            if n < 0 then
                return n
            end
            while #info.captures < bi do
                info.captures[#info.captures + 1] = new_capture()
            end

            info.captures[bi] = new_capture(s.offset + s_off, n)
            s_off = s_off + n
        elseif re_char == '^' then
            if s_off ~= 0 then
                return SLRE_NO_MATCH
            end
        elseif re_char == '$' then
            if s_off ~= s:len() then
                return SLRE_NO_MATCH
            end
        else
            if s_off >= s:len() then
                return SLRE_NO_MATCH
            end
            local n = match_op(re:sub(re_off + 1), s:sub(s_off + 1), info)
            if n <= 0 then
                return n
            end
            s_off = s_off + n
        end

        re_off = re_off + step
        ::continue_bar::
    end
    return s_off
end

-- Process branch points
doh = function(re, s, info, bi)
    local bp = info.brackets[bi]

    local pos
    local length
    local result = SLRE_NO_MATCH

    -- Python: for i in [0] + list(range(1, bp.num_branches)):
    -- This iterates: 0, 1, 2, ..., bp.num_branches-1
    local iterations = {0}
    for k = 1, bp.num_branches - 1 do
        iterations[#iterations + 1] = k
    end
    -- If num_branches == 0, iterations is just {0}

    for _, i in ipairs(iterations) do
        if i == 0 then
            pos = bp.start_offset
        else
            pos = info.branches[bp.branch_index + i - 1 + 1].offset + 1  -- +1 for Lua 1-based branches table
            -- In Python: info.branches[bp.branch_index + i - 1].offset + 1
            -- branch_index is 0-based in Python. We need to be careful here.
        end

        if bp.num_branches == 0 then
            length = bp.length
        elseif bp.num_branches == i then
            length = bp.start_offset + bp.length - pos
        else
            -- Python: info.branches[bp.branch_index + i].offset - pos
            length = info.branches[bp.branch_index + i + 1].offset - pos  -- +1 for Lua 1-based
        end

        --print(string.format('doh %d %d [%s] [%s]', bi - 1, i,
        --    re:sub(pos - re.offset + 1, length), s:tostring()))
        result = bar(re:abs_slice(pos, length), s, info, bi)
        --print(string.format('doh <- %d', result))
        if result > 0 or i >= bp.num_branches then
            break
        end
    end
    return result
end

baz = function(re, s, info)
    local result = -1
    local is_anchored = (string.sub(re:tostring(), 1, 1) == '^')

    for i = 0, #(s:tostring()) - 1 do
        result = doh(re, s, info, 1)  -- 1-based: bracket index 1 is the first
        s:advance(1)
        if result >= 0 then
            result = result + i
            break
        end
        if is_anchored then
            break
        end
    end

    return result
end

local function setup_branch_points(info)
    -- Bubble sort branches by bracket_index (descending? The Python sorts so that
    -- higher bracket_index comes first... actually looking at the swap condition:
    -- if info.branches[i].bracket_index > info.branches[j].bracket_index: swap
    -- This is a bubble sort that sorts in ascending order of bracket_index
    for i = 1, #info.branches do
        for j = 1, #info.branches do
            if info.branches[i].bracket_index > info.branches[j].bracket_index then
                local tmp = info.branches[i]
                info.branches[i] = info.branches[j]
                info.branches[j] = tmp
            end
        end
    end

    local j = 1  -- 1-based index into branches

    for i = 1, #info.brackets do
        local bp = info.brackets[i]
        bp.num_branches = 0
        bp.branch_index = j - 1  -- store as 0-based to match Python semantics
        while j <= #info.branches and info.branches[j].bracket_index == (i - 1) do
            -- Python brackets are 0-indexed, so bracket_index comparison uses (i-1)
            bp.num_branches = bp.num_branches + 1
            j = j + 1
        end
    end
end

foo = function(re, s, info)
    local depth = 0

    -- First bracket captures everything
    local bracket = new_bracket_pair(re.offset)
    bracket.length = re:len()
    info.brackets[#info.brackets + 1] = bracket

    -- Make a single pass over regex string, memorize brackets and branches
    for seq, offset in regex_iterator(re) do
        local seq1 = string.sub(seq, 1, 1)

        if seq1 == '|' then
            local current_bracket_pair
            if info.brackets[#info.brackets].length == nil then
                current_bracket_pair = #info.brackets - 1  -- 0-based index for bracket_index
            else
                current_bracket_pair = depth
            end
            info.branches[#info.branches + 1] = new_branch(current_bracket_pair, offset)
        elseif seq1 == '\\' then
            if #seq < 2
              or (
                string.sub(seq, 2, 2) == 'x'
                and (
                  #seq < 4 or not (is_hexdigit(string.sub(seq, 3, 3)) and is_hexdigit(string.sub(seq, 4, 4)))
                )
              )
              or not is_metacharacter(string.sub(seq, 2, 2)) then
                return SLRE_INVALID_METACHARACTER
            end
        elseif seq1 == '(' then
            depth = depth + 1
            info.brackets[#info.brackets + 1] = new_bracket_pair(offset + 1)
        elseif seq1 == ')' then
            local idx
            if info.brackets[#info.brackets].length == nil then
                idx = #info.brackets
            else
                idx = depth + 1  -- +1 for 1-based Lua table
            end
            info.brackets[idx].length = offset - info.brackets[idx].start_offset
            --print(string.format("SETTING BRACKET %d [%s]", idx - 1,
            --    re:abs_slice(info.brackets[idx].start_offset, info.brackets[idx].length):tostring()))
            depth = depth - 1
            if depth < 0 then
                return SLRE_UNBALANCED_BRACKETS
            end
            -- Check for empty group ()
            if re:abs_char(offset - 1) == '(' then
                return SLRE_NO_MATCH
            end
        end
        -- default case: pass (do nothing)
    end

    if depth ~= 0 then
        return SLRE_UNBALANCED_BRACKETS
    end
    setup_branch_points(info)

    return baz(re, s, info)
end

local function slre_match(regexp, s_str, caps)
    local info = new_regex_info(caps)
    local re = OffsetString:new(regexp)
    local s = OffsetString:new(s_str)

    --print(string.format('========================> [%s] [%s]', re:tostring(), s:tostring()))

    if string.sub(re:tostring(), 1, 4) == '(?i)' then
        info.ignore_case = true
        re:advance(4)
    end

    return foo(re, s, info)
end

local function benchmark_body(lsf)
    local text = "abbbababaabccababcacbcbcbabbabcbabcabcbbcbbac"
    local regexes = {"(ab)+", "(b.+)+", "a[ab]*", "([ab^c][ab^c])+"}

    local ret = 0
    for _ = 1, lsf do
        ret = 0
        local captures = {}
        for _, r in ipairs(regexes) do
            ret = ret + slre_match(r, text, captures)
        end
    end

    return ret
end

local function verify_benchmark(r)
    return 102 == r
end

local function benchmark()
    local res = benchmark_body(SCALE_FACTOR)
    return verify_benchmark(res)
end

return benchmark()
