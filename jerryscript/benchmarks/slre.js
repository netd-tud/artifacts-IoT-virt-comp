var SCALE_FACTOR = 1;

var SLRE_NO_MATCH = -1;
var SLRE_UNEXPECTED_QUANTIFIER = -2;
var SLRE_UNBALANCED_BRACKETS = -3;
var SLRE_INTERNAL_ERROR = -4;
var SLRE_INVALID_CHARACTER_SET = -5;
var SLRE_INVALID_METACHARACTER = -6;
var SLRE_CAPS_ARRAY_TOO_SMALL = -7;
var SLRE_TOO_MANY_BRANCHES = -8;
var SLRE_TOO_MANY_BRACKETS = -9;

// OffsetString constructor
function OffsetString(data) {
    this.data = data;
    this.offset = 0;
    this.end = data.length;
}

OffsetString.prototype.toString = function () {
    return this.data.slice(this.offset, this.end);
};

OffsetString.prototype.len = function () {
    return this.end - this.offset;
};

OffsetString.prototype.charAt = function (index) {
    var str = this.toString();
    if (index < 0 || index >= str.length) return undefined;
    return str[index];
};

OffsetString.prototype.slice = function (start, stop) {
    var str = this.toString();
    if (stop === undefined) {
        return str.slice(start);
    }
    return str.slice(start, stop);
};

OffsetString.prototype.shallowCopy = function () {
    return new OffsetString(this.data);
};

OffsetString.prototype.advance = function (n) {
    this.offset += n;
};

OffsetString.prototype.advanceTo = function (offset) {
    this.offset += offset;
};

OffsetString.prototype.absSlice = function (start, length) {
    var res = this.shallowCopy();
    res.offset = start;
    res.end = start + length;
    return res;
};

OffsetString.prototype.relSlice = function (relStart, length) {
    return this.absSlice(this.offset + relStart, length);
};

// BracketPair constructor
function BracketPair(startOffset) {
    this.startOffset = startOffset;
    this.length = null;
    this.branchIndex = null;
    this.numBranches = null;
}

// Branch constructor
function Branch(bracketIndex, offset) {
    this.bracketIndex = bracketIndex;
    this.offset = offset;
}

// Capture constructor
function Capture(startOffset, length) {
    this.startOffset = (startOffset !== undefined) ? startOffset : null;
    this.length = (length !== undefined) ? length : null;
}

// RegexInfo constructor
function RegexInfo(captures) {
    this.brackets = [];
    this.branches = [];
    this.captures = captures;
    this.ignoreCase = false;
}

// Helper functions
var HEXDIGITS = "0123456789abcdefABCDEF";

function isHexDigit(c) {
    return HEXDIGITS.indexOf(c) !== -1;
}

function isSpace(ch) {
    return ch === ' ' || ch === '\t' || ch === '\n' || ch === '\r' || ch === '\f' || ch === '\v';
}

function isDigit(ch) {
    return ch >= '0' && ch <= '9';
}

function isMetacharacter(s) {
    return '^$().[]*+?|\\Ssd'.indexOf(s) !== -1;
}

function opLen(re) {
    if (re[0] === '\\') {
        if (re[1] === 'x') {
            return 4;
        }
        return 2;
    }
    return 1;
}

function setLen(re) {
    var i = 0;
    while (i < re.length && re[i] !== ']') {
        i += opLen(re.slice(i));
    }

    if (i <= re.length) {
        return i + 1;
    } else {
        throw new Error("Invalid character set");
    }
}

function getOpLen(re) {
    if (re[0] === '[') {
        return setLen(re.slice(1)) + 1;
    } else {
        return opLen(re);
    }
}

function isQuantifier(re) {
    return re[0] === '*' || re[0] === '+' || re[0] === '?';
}

function hextoi(s) {
    return parseInt(s, 16);
}

function matchOp(re, s, info) {
    var result = 0;

    switch (re[0]) {
        case '\\':
            switch (re[1]) {
                case 'S':
                    if (isSpace(s[0])) return SLRE_NO_MATCH;
                    result += 1;
                    break;
                case 's':
                    if (!isSpace(s[0])) return SLRE_NO_MATCH;
                    result += 1;
                    break;
                case 'd':
                    if (!isDigit(s[0])) return SLRE_NO_MATCH;
                    result += 1;
                    break;
                case 'x':
                    if (hextoi(re.slice(2, 4)) !== s.charCodeAt(0)) return SLRE_NO_MATCH;
                    result += 1;
                    break;
                default:
                    if (re[1] !== s[0]) return SLRE_NO_MATCH;
                    result += 1;
                    break;
            }
            break;
        case '|':
            return SLRE_INTERNAL_ERROR;
        case '$':
            return SLRE_NO_MATCH;
        case '.':
            result += 1;
            break;
        default:
            if (!s) {
                return SLRE_NO_MATCH;
            }
            if (info.ignoreCase) {
                if (re[0].toLowerCase() !== s[0].toLowerCase()) return SLRE_NO_MATCH;
            } else {
                if (re[0] !== s[0]) return SLRE_NO_MATCH;
            }
            result += 1;
            break;
    }
    return result;
}

function matchSet(re, reLen, s, info) {
    var i = 0;
    var result = -1;
    var invert = re[0] === '^';

    if (invert) {
        re = re.slice(1);
        reLen -= 1;
    }

    while (i <= reLen && re[i] !== ']' && result <= 0) {
        if (re[i] !== '-' && re[i + 1] === '-' && re[i + 2] !== ']' && i + 2 < re.length) {
            if (info.ignoreCase) {
                result = (re[i] <= s[0].toLowerCase() && s[0].toLowerCase() <= re[i + 2]) ? 1 : -1;
            } else {
                result = (re[i] <= s[0] && s[0] <= re[i + 2]) ? 1 : -1;
            }
            i += 3;
        } else {
            result = matchOp(re.slice(i), s, info);
            i += opLen(re.slice(i));
        }
    }

    var matched = result > 0;
    return (matched !== invert) ? 1 : -1;
}

function bar(re, s, info, bi) {
    var reOff = 0;
    var sOff = 0;

    while (reOff < re.len() && sOff <= s.len()) {
        var step;
        if (re.charAt(reOff) === '(') {
            step = info.brackets[bi + 1].length + 2;
        } else {
            step = getOpLen(re.slice(reOff));
        }

        if (step <= 0) {
            return SLRE_INVALID_CHARACTER_SET;
        }
        if (isQuantifier(re.toString())) {
            return SLRE_UNEXPECTED_QUANTIFIER;
        }

        if (reOff + step < re.len() && isQuantifier(re.charAt(reOff + step))) {
            if (re.charAt(reOff + step) === '?') {
                var res = bar(re.relSlice(reOff, step), s.relSlice(sOff, s.len() - sOff), info, bi);
                sOff += res > 0 ? res : 0;
                reOff += 1;
            } else if (re.charAt(reOff + step) === '+' || re.charAt(reOff + step) === '*') {
                var sOffInner = sOff;
                var nsOff = sOff;
                var nonGreedy = false;

                var afterQuant = reOff + step + 1;
                if (afterQuant < re.len() && re.charAt(afterQuant) === '?') {
                    nonGreedy = true;
                    afterQuant += 1;
                }

                var n1 = 1;
                var n2 = -1;
                while (n1 > 0) {
                    n1 = bar(
                        re.relSlice(reOff, step),
                        s.relSlice(sOffInner, s.len() - sOffInner),
                        info,
                        bi
                    );
                    if (n1 > 0) {
                        sOffInner += n1;
                    }
                    if (re.charAt(reOff + step) === '+' && n1 < 0) {
                        break;
                    }

                    if (afterQuant >= re.len()) {
                        nsOff = sOffInner;
                    } else {
                        n2 = bar(
                            re.relSlice(afterQuant, re.len() - afterQuant),
                            s.relSlice(sOffInner, s.len() - sOffInner),
                            info,
                            bi
                        );
                        if (n2 >= 0) {
                            nsOff = sOffInner + n2;
                        }
                    }

                    if (nsOff > sOff && nonGreedy) {
                        break;
                    }
                }

                if (n1 < 0 && re.charAt(reOff + step) === '*') {
                    n2 = bar(
                        re.relSlice(afterQuant, re.len() - afterQuant),
                        s.relSlice(sOffInner, s.len() - sOffInner),
                        info,
                        bi
                    );
                    if (n2 >= 0) {
                        nsOff = sOffInner + n2;
                    }
                }

                if (re.charAt(step) === '+' && nsOff === sOff) {
                    return SLRE_NO_MATCH;
                }

                if (nsOff === sOff && afterQuant < re.len() && n2 < 0) {
                    return SLRE_NO_MATCH;
                }

                return nsOff;
            }
            reOff += step;
            continue;
        }

        var reChar = re.charAt(reOff);

        switch (reChar) {
            case '[':
                var n = matchSet(re.slice(reOff + 1), re.len() - (reOff + 2), s.slice(sOff), info);
                if (n <= 0) return SLRE_NO_MATCH;
                sOff += n;
                break;
            case '(':
                var n = SLRE_NO_MATCH;
                bi += 1;
                if (bi >= info.brackets.length) {
                    return SLRE_INTERNAL_ERROR;
                }

                if (reOff + step >= re.len()) {
                    n = doh(re, s.relSlice(sOff, s.len() - sOff), info, bi);
                } else {
                    for (var j2 = 0; j2 <= s.len() - sOff; j2++) {
                        n = doh(re, s.relSlice(sOff, s.len() - (sOff + j2)), info, bi);
                        if (n < 0) continue;
                        var tmp = bar(
                            re.relSlice(reOff + step, re.len() - (reOff + step)),
                            s.relSlice(sOff + n, s.len() - (sOff + n)),
                            info,
                            bi
                        );
                        if (tmp >= 0) break;
                    }
                }

                if (n < 0) return n;

                while (info.captures.length < bi) {
                    info.captures.push(new Capture());
                }

                info.captures[bi - 1] = new Capture(s.offset + sOff, n);
                sOff += n;
                break;
            case '^':
                if (sOff !== 0) return SLRE_NO_MATCH;
                break;
            case '$':
                if (sOff !== s.len()) return SLRE_NO_MATCH;
                break;
            default:
                if (sOff >= s.len()) return SLRE_NO_MATCH;
                var n = matchOp(re.slice(reOff), s.slice(sOff), info);
                if (n <= 0) return n;
                sOff += n;
                break;
        }
        reOff += step;
    }
    return sOff;
}

function doh(re, s, info, bi) {
    var bp = info.brackets[bi];

    var pos;
    var length;
    var result = SLRE_NO_MATCH;

    var iterations = [0];
    for (var k = 1; k < bp.numBranches; k++) {
        iterations.push(k);
    }

    for (var idx = 0; idx < iterations.length; idx++) {
        var i = iterations[idx];
        if (i === 0) {
            pos = bp.startOffset;
        } else {
            pos = info.branches[bp.branchIndex + i - 1].offset + 1;
        }

        if (bp.numBranches === 0) {
            length = bp.length;
        } else if (bp.numBranches === i) {
            length = bp.startOffset + bp.length - pos;
        } else {
            length = info.branches[bp.branchIndex + i].offset - pos;
        }

        result = bar(re.absSlice(pos, length), s, info, bi);
        if (result > 0 || i >= bp.numBranches) {
            break;
        }
    }
    return result;
}

function baz(re, s, info) {
    var result = -1;
    var isAnchored = re.toString().indexOf('^') === 0;

    var sLen = s.toString().length;
    for (var i = 0; i < sLen; i++) {
        result = doh(re, s, info, 0);
        s.advance(1);
        if (result >= 0) {
            result += i;
            break;
        }
        if (isAnchored) {
            break;
        }
    }

    return result;
}

function setupBranchPoints(info) {
    var i, j, tmp;
    for (i = 0; i < info.branches.length; i++) {
        for (j = 0; j < info.branches.length; j++) {
            if (info.branches[i].bracketIndex > info.branches[j].bracketIndex) {
                tmp = info.branches[i];
                info.branches[i] = info.branches[j];
                info.branches[j] = tmp;
            }
        }
    }

    j = 0;

    for (i = 0; i < info.brackets.length; i++) {
        var bp = info.brackets[i];
        bp.numBranches = 0;
        bp.branchIndex = j;
        while (j < info.branches.length && info.branches[j].bracketIndex === i) {
            bp.numBranches += 1;
            j += 1;
        }
    }
}

function foo(re, s, info) {
    var depth = 0;

    var bracket = new BracketPair(re.offset);
    bracket.length = re.len();
    info.brackets.push(bracket);

    var iter = regexIterator(re);
    var iterResult = iter.next();
    while (!iterResult.done) {
        var seq = iterResult.value[0];
        var offset = iterResult.value[1];

        switch (seq[0]) {
            case '|':
                var currentBracketPair;
                if (info.brackets[info.brackets.length - 1].length === null) {
                    currentBracketPair = info.brackets.length;
                } else {
                    currentBracketPair = depth;
                }
                info.branches.push(new Branch(currentBracketPair, offset));
                break;
            case '\\':
                if (seq.length < 2 || (seq[1] === 'x'
                        && (seq.length < 4 || !allHexDigits(seq.slice(2, 4))))) {
                    return SLRE_INVALID_METACHARACTER;
                }
                break;
            case '(':
                depth += 1;
                info.brackets.push(new BracketPair(offset + 1));
                break;
            case ')':
                var idx;
                if (info.brackets[info.brackets.length - 1].length === null) {
                    idx = info.brackets.length - 1;
                } else {
                    idx = depth;
                }
                info.brackets[idx].length = offset - info.brackets[idx].startOffset;
                depth -= 1;
                if (depth < 0) {
                    return SLRE_UNBALANCED_BRACKETS;
                }
                if (re.data[offset - 1] === '(') {
                    return SLRE_NO_MATCH;
                }
                break;
            default:
                break;
        }

        iterResult = iter.next();
    }

    if (depth !== 0) {
        return SLRE_UNBALANCED_BRACKETS;
    }
    setupBranchPoints(info);

    return baz(re, s, info);
}

// Helper to replace [...seq.slice(2,4)].every(c => HEXDIGITS.includes(c))
function allHexDigits(s) {
    for (var i = 0; i < s.length; i++) {
        if (HEXDIGITS.indexOf(s[i]) === -1) {
            return false;
        }
    }
    return true;
}

// Replace generator function with a manual iterator
function regexIterator(reStr) {
    var iterOffset = reStr.offset;
    return {
        next: function () {
            if (iterOffset >= reStr.end) {
                return { done: true, value: undefined };
            }
            var iterStr = reStr.data.slice(iterOffset);
            var opLenVal = getOpLen(iterStr);
            var seq = iterStr.slice(0, opLenVal);
            var currentOffset = iterOffset;
            iterOffset += opLenVal;
            return { done: false, value: [seq, currentOffset] };
        }
    };
}

function slreMatch(regexp, sStr, caps) {
    var info = new RegexInfo(caps);
    var re = new OffsetString(regexp);
    var s = new OffsetString(sStr);

    if (re.toString().indexOf('(?i)') === 0) {
        info.ignoreCase = true;
        re.advance(4);
    }

    return foo(re, s, info);
}

function initialize_benchmark() {

}

function benchmark() {
    initialize_benchmark()
    var res = benchmarkBody(SCALE_FACTOR);
    return verifyBenchmark(res);
}

function benchmarkBody(lsf) {
    var text = "abbbababaabccababcacbcbcbabbabcbabcabcbbcbbac";
    var regexes = ["(ab)+", "(b.+)+", "a[ab]*", "([ab^c][ab^c])+"];

    var ret = 0;
    for (var i = 0; i < lsf; i++) {
        ret = 0;
        var captures = [];
        for (var r = 0; r < regexes.length; r++) {
            ret += slreMatch(regexes[r], text, captures);
        }
    }

    return ret;
}

function verifyBenchmark(r) {
    return 102 === r;
}

benchmark();
