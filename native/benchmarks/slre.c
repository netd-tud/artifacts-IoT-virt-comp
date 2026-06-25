/* BEEBS slre benchmark

   Copyright (c) 2004-2013 Sergey Lyubka <valenok@gmail.com>
   Copyright (c) 2013 Cesanta Software Limited All rights reserved

   This version, copyright (C) 2014-2019 Embecosm Limited and University of
   Bristol

   Contributor James Pallister <james.pallister@bristol.ac.uk>
   Contributor Jeremy Bennett <jeremy.bennett@embecosm.com>

   This file is part of Embench and was formerly part of the Bristol/Embecosm
   Embedded Benchmark Suite.

   SPDX-License-Identifier: GPL-3.0-or-later */

/* ==========================================
   [Modification Summary]
   ==========================================
   Purpose: Adjustments to be used with RIOT.
   Date: April 21th 2026
   Author: Leonard Herbst <leonard.herbst@tu-dresden.de>
   Details:
      - formated according to the RIOT formating convention
      - used stdint when appropriate
      - inlined functions
      - removed the SLRE_DEBUG related code
   ========================================== */

#include <stdint.h>
#include <stddef.h>

#ifndef SCALE_FACTOR
#  define SCALE_FACTOR 1
#endif

struct slre_cap
{
    const char *ptr;
    int len;
};

/* slre_match() failure codes */
#define SLRE_NO_MATCH               -1
#define SLRE_UNEXPECTED_QUANTIFIER  -2
#define SLRE_UNBALANCED_BRACKETS    -3
#define SLRE_INTERNAL_ERROR         -4
#define SLRE_INVALID_CHARACTER_SET  -5
#define SLRE_INVALID_METACHARACTER  -6
#define SLRE_CAPS_ARRAY_TOO_SMALL   -7
#define SLRE_TOO_MANY_BRANCHES      -8
#define SLRE_TOO_MANY_BRACKETS      -9

#define MAX_BRANCHES 4
#define MAX_BRACKETS 4

struct bracket_pair {
    const char *ptr;  /* Points to the first char after '(' in regex  */
    int len;          /* Length of the text between '(' and ')'       */
    int branches;     /* Index in the branches array for this pair    */
    int num_branches; /* Number of '|' in this bracket pair           */
};

struct branch {
    int bracket_index; /* index for 'struct bracket_pair brackets' */
/* array defined below                      */
    const char *schlong; /* points to the '|' character in the regex */
};

struct match_context {
    const char *re;
    int re_len;
    const char *s;
    int s_len;
};

struct regex_info {
    /*
     * Describes all bracket pairs in the regular expression.
     * First entry is always present, and grabs the whole regex.
     */
    struct bracket_pair brackets[MAX_BRACKETS];
    int num_brackets;

    /*
     * Describes alternations ('|' operators) in the regular expression.
     * Each branch falls into a specific branch pair.
     */
    struct branch branches[MAX_BRANCHES];
    int num_branches;
 
    /* Array of captures provided by the user */
    struct slre_cap *caps;
    int num_caps;

    /* E.g. IGNORE_CASE. See enum below */
    int flags;
};
enum {
    IGNORE_CASE = 1
};

static inline int isspace(int c) {
    return (c == ' ' || c == '\t' || c == '\n' || c == '\v' || c == '\f' || c == '\r');
}

static inline int tolower(int c) {
    return (c >= 'A' && c <= 'Z') ? (c + 32) : c;
}

static inline int isdigit(int c) {
    return (c >= '0' && c <= '9');
}

static inline int isxdigit(int c) {
    return (isdigit(c) || (c >= 'a' && c <= 'f') || (c >= 'A' && c <= 'F'));
}

static inline int memcmp(const void *s1, const void *s2, size_t n) {
    const unsigned char *p1 = (const unsigned char *)s1;
    const unsigned char *p2 = (const unsigned char *)s2;
    for (size_t i = 0; i < n; i++) {
        if (p1[i] != p2[i]) {
            return (p1[i] - p2[i]);
        }
    }
    return 0;
}

static inline size_t strlen(const char *s) {
    const char *start = s;
    while (*s) {
        s++;
    }
    return (size_t)(s - start);
}

static inline int is_metacharacter(const unsigned char *s) {
    static const char *metacharacters = "^$().[]*+?|\\Ssd";
    for (char *cur = (char *) metacharacters; *cur; cur++) {
        if (*s == *cur) {
            return 1;
        }
    }
    return 0;
}

static inline int op_len(const char *re) {
    return re[0] == '\\' && re[1] == 'x' ? 4 : re[0] == '\\' ? 2 : 1;
}

static inline int set_len(const char *re, int re_len) {
    int len = 0;

    while (len < re_len && re[len] != ']') {
        len += op_len(re + len);
    }

    return len <= re_len ? len + 1 : -1;
}

static inline int get_op_len(const char *re, int re_len) {
    return re[0] == '[' ? set_len(re + 1, re_len - 1) + 1 : op_len(re);
}

static inline int is_quantifier(const char *re) {
    return re[0] == '*' || re[0] == '+' || re[0] == '?';
}

static inline int toi(int x) {
    return isdigit(x) ? x - '0' : x - 'W';
}

static inline int hextoi(const unsigned char *s) {
    return (toi(tolower(s[0])) << 4) | toi(tolower(s[1]));
}

static int match_op(const unsigned char *re, const unsigned char *s, struct regex_info *info) {
    int result = 0;
    switch (*re) {
    case '\\':
        /* Metacharacters */
        switch (re[1]) {
        case 'S':
            if (isspace(*s)) {
                return SLRE_NO_MATCH;
            }
            result++;
            break;

        case 's':
            if (!isspace(*s)) {
                return SLRE_NO_MATCH;
            }
            result++;
            break;

        case 'd':
            if (!isdigit(*s)) {
                return SLRE_NO_MATCH;
            }
            result++;
            break;

        case 'x':
            /* Match byte, \xHH where HH is hexadecimal byte representaion */
            if (hextoi(re + 2) != *s) {
                return SLRE_NO_MATCH;
            }
            result++;
            break;

        default:
            /* Valid metacharacter check is done in bar() */
            if (re[1] != s[0]) {
                return SLRE_NO_MATCH;
            }
            result++;
            break;
        }
        break;

    case '|':
        if (1) {
            return SLRE_INTERNAL_ERROR;
        }
        break;
    case '$':
        if (1) {
            return SLRE_NO_MATCH;
        }
        break;
    case '.':
        result++;
        break;

    default:
        if (info->flags & IGNORE_CASE) {
            if (tolower(*re) != tolower(*s)) {
                return SLRE_NO_MATCH;
            }
        } else {
            if (*re != *s) {
                return SLRE_NO_MATCH;
            }
        }
        result++;
        break;
    }

    return result;
}

static int match_set(const char *re, int re_len, const char *s, struct regex_info *info) {
    int len = 0, result = -1, invert = re[0] == '^';

    if (invert)
        re++, re_len--;

    while (len <= re_len && re[len] != ']' && result <= 0) {
        /* Support character range */
        if (re[len] != '-' && re[len + 1] == '-' && re[len + 2] != ']' && re[len + 2] != '\0') {
            result = info->flags && IGNORE_CASE ? *s >= re[len] && *s <= re[len + 2]
                                                : tolower((int)*s) >= tolower((int)re[len]) &&
                                                      tolower((int)*s) <= tolower((int)re[len + 2]);
            len += 3;
        } else {
            result = match_op((unsigned char *)re + len, (unsigned char *)s, info);
            len += op_len(re + len);
        }
    }
    return (!invert && result > 0) || (invert && result <= 0) ? 1 : -1;
}

static int doh(const char *s, int s_len, struct regex_info *info, int bi);

static int bar(struct match_context *ctx, struct regex_info *info,
               int bi) {
    const char *re = ctx->re;
    int re_len = ctx->re_len;
    const char *s = ctx->s;
    int s_len = ctx->s_len;
    /* i is offset in re, j is offset in s, bi is brackets index */
    int i, j, n, step;

    for (i = j = 0; i < re_len && j <= s_len; i += step) {

        /* Handle quantifiers. Get the length of the chunk. */
        step = re[i] == '(' ? info->brackets[bi + 1].len + 2 : get_op_len(re + i, re_len - i);

        if (is_quantifier(&re[i])) {
            return SLRE_UNEXPECTED_QUANTIFIER;
        }
        if (step <= 0) {
            return SLRE_INVALID_CHARACTER_SET;
        }

        if (i + step < re_len && is_quantifier(re + i + step)) {
            if (re[i + step] == '?') {
                int result = bar(&(struct match_context){.re = re + i, .re_len = step, .s = s + j, .s_len = s_len - j}, info, bi);
                j += result > 0 ? result : 0;
                i++;
            } else if (re[i + step] == '+' || re[i + step] == '*') {
                int j2 = j, nj = j, n1, n2 = -1, ni, non_greedy = 0;

                /* Points to the regexp code after the quantifier */
                ni = i + step + 1;
                if (ni < re_len && re[ni] == '?') {
                    non_greedy = 1;
                    ni++;
                }

                do {
                    if ((n1 = bar(&(struct match_context){ .re = re + i, .re_len = step, .s = s + j2, .s_len = s_len - j2 }, info, bi)) > 0) {
                        j2 += n1;
                    }
                    if (re[i + step] == '+' && n1 < 0)
                        break;

                    if (ni >= re_len) {
                        /* After quantifier, there is nothing */
                        nj = j2;
                    } else if ((n2 = bar(&(struct match_context){.re = re + ni, .re_len = re_len - ni, .s = s + j2, s_len = s_len - j2}, info, bi)) >=
                               0) {
                        /* Regex after quantifier matched */
                        nj = j2 + n2;
                    }
                    if (nj > j && non_greedy)
                        break;
                } while (n1 > 0);

                if (n1 < 0 && re[i + step] == '*' &&
                    (n2 = bar(&(struct match_context){ .re = re + ni, .re_len = re_len - ni, .s = s + j, .s_len = s_len - j}, info, bi)) > 0) {
                    nj = j + n2;
                }

                // DBG(("STAR/PLUS END: %d %d %d %d %d\n", j, nj, re_len - ni, n1, n2));
                if (re[i + step] == '+' && nj == j) {
                    return SLRE_NO_MATCH;
                }

                /* If while loop body above was not executed for the *
                 * quantifier,  */
                /* make sure the rest of the regex matches */
                if (nj == j && ni < re_len && n2 < 0) {
                    return SLRE_NO_MATCH;
                }

                /* Returning here cause we've matched the rest of RE already */
                return nj;
            }
            continue;
        }

        if (re[i] == '[') {
            n = match_set(re + i + 1, re_len - (i + 2), s + j, info);
            if (n <= 0) {
                return SLRE_NO_MATCH;
            }
            j += n;
        } else if (re[i] == '(') {
            n = SLRE_NO_MATCH;
            bi++;
            if (bi >= info->num_brackets) {
                return SLRE_INTERNAL_ERROR;
            }

            if (re_len - (i + step) <= 0) {
                /* Nothing follows brackets */
                n = doh(s + j, s_len - j, info, bi);
            } else {
                int j2;
                for (j2 = 0; j2 <= s_len - j; j2++) {
                    if ((n = doh(s + j, s_len - (j + j2), info, bi)) >= 0 &&
                        bar(&(struct match_context){ .re = re + i + step, .re_len = re_len - (i + step), .s = s + j + n, .s_len = s_len - (j + n)}, info,
                            bi) >= 0)
                        break;
                }
            }

            if (n < 0) {
                return n;
            }
            if (info->caps != NULL) {
                info->caps[bi - 1].ptr = s + j;
                info->caps[bi - 1].len = n;
            }
            j += n;
        } else if (re[i] == '^') {
            if (j != 0) {
                return SLRE_NO_MATCH;
            }
        } else if (re[i] == '$') {
            if (j != s_len) {
                return SLRE_NO_MATCH;
            }
        } else {
            if (j >= s_len) {
                return SLRE_NO_MATCH;
            }
            n = match_op((unsigned char *)(re + i), (unsigned char *)(s + j), info);
            if (n <= 0) {
                return n;
            }
            j += n;
        }
    }

    return j;
}

/* Process branch points */
static int doh(const char *s, int s_len, struct regex_info *info, int bi) {
    const struct bracket_pair *b = &info->brackets[bi];
    int i = 0, len, result;
    const char *p;

    do {
        p = i == 0 ? b->ptr : info->branches[b->branches + i - 1].schlong + 1;
        len = b->num_branches == 0   ? b->len
              : i == b->num_branches ? b->ptr + b->len - p
                                     : info->branches[b->branches + i].schlong - p;
        result = bar(&(struct match_context){ .re = p, .re_len = len, .s = s, .s_len = s_len}, info, bi);
    } while (result <= 0 && i++ < b->num_branches); /* At least 1 iteration */

    return result;
}

static int baz(const char *s, int s_len, struct regex_info *info) {
    int i, result = -1, is_anchored = info->brackets[0].ptr[0] == '^';

    for (i = 0; i <= s_len; i++) {
        result = doh(s + i, s_len - i, info, 0);
        if (result >= 0) {
            result += i;
            break;
        }
        if (is_anchored)
            break;
    }

    return result;
}

static void setup_branch_points(struct regex_info *info) {
    int i, j;
    struct branch tmp;

    /* First, sort branches. Must be stable, no qsort. Use bubble algo. */
    for (i = 0; i < info->num_branches; i++) {
        for (j = i + 1; j < info->num_branches; j++) {
            if (info->branches[i].bracket_index > info->branches[j].bracket_index) {
                tmp = info->branches[i];
                info->branches[i] = info->branches[j];
                info->branches[j] = tmp;
            }
        }
    }

    /*
     * For each bracket, set their branch points. This way, for every bracket
     * (i.e. every chunk of regex) we know all branch points before matching.
     */
    for (i = j = 0; i < info->num_brackets; i++) {
        info->brackets[i].num_branches = 0;
        info->brackets[i].branches = j;
        while (j < info->num_branches && info->branches[j].bracket_index == i) {
            info->brackets[i].num_branches++;
            j++;
        }
    }
}

static int foo(const char *re, int re_len, const char *s, int s_len, struct regex_info *info) {
    int i, step, depth = 0;

    /* First bracket captures everything */
    info->brackets[0].ptr = re;
    info->brackets[0].len = re_len;
    info->num_brackets = 1;

    /* Make a single pass over regex string, memorize brackets and branches */
    for (i = 0; i < re_len; i += step) {
        step = get_op_len(re + i, re_len - i);

        if (re[i] == '|') {
            if (info->num_branches >= ((int)sizeof(info->branches) / sizeof((info->branches)[0]))) {
                return SLRE_TOO_MANY_BRANCHES;
            }
            info->branches[info->num_branches].bracket_index =
                info->brackets[info->num_brackets - 1].len == -1 ? info->num_brackets - 1 : depth;
            info->branches[info->num_branches].schlong = &re[i];
            info->num_branches++;
        } else if (re[i] == '\\') {
            if (i >= re_len - 1) {
                return SLRE_INVALID_METACHARACTER;
            }
            if (re[i + 1] == 'x') {
                /* Hex digit specification must follow */
                if (re[i + 1] == 'x' && i >= re_len - 3) {
                    return SLRE_INVALID_METACHARACTER;
                }
                if (re[i + 1] == 'x' && !(isxdigit((unsigned char)re[i + 2]) && isxdigit((unsigned char)re[i + 3]))) {
                    return SLRE_INVALID_METACHARACTER;
                }
            } else {
                if (!is_metacharacter((unsigned char *)re + i + 1)) {
                    return SLRE_INVALID_METACHARACTER;
                }
            }
        } else if (re[i] == '(') {
            if (info->num_brackets >= ((int)sizeof(info->brackets) / sizeof((info->brackets)[0]))) {
                return SLRE_TOO_MANY_BRACKETS;
            }
            depth++; /* Order is important here. Depth increments first. */
            info->brackets[info->num_brackets].ptr = re + i + 1;
            info->brackets[info->num_brackets].len = -1;
            info->num_brackets++;
            if (info->num_caps > 0 && info->num_brackets - 1 > info->num_caps) {
                return SLRE_CAPS_ARRAY_TOO_SMALL;
            }
        } else if (re[i] == ')') {
            int ind =
                info->brackets[info->num_brackets - 1].len == -1 ? info->num_brackets - 1 : depth;
            info->brackets[ind].len = &re[i] - info->brackets[ind].ptr;
            depth--;
            if (depth < 0) {
                return SLRE_UNBALANCED_BRACKETS;
            }
            if (i > 0 && re[i - 1] == '(') {
                return SLRE_NO_MATCH;
            }
        }
    }

    if (depth != 0) {
        return SLRE_UNBALANCED_BRACKETS;
    }
    setup_branch_points(info);

    return baz(s, s_len, info);
}

static int slre_match(const char *regexp, const char *s, int s_len, struct slre_cap *caps, int num_caps) {
    struct regex_info info;

    /* Initialize info structure */
    info.flags = info.num_brackets = info.num_branches = 0;
    info.num_caps = num_caps;
    info.caps = caps;

    /* Handle regexp flags. At the moment, only 'i' is supported */
    if (memcmp(regexp, "(?i)", 4) == 0) {
        info.flags |= IGNORE_CASE;
        regexp += 4;
    }

    return foo(regexp, strlen(regexp), s, s_len, &info);
}

static inline int benchmark_body(unsigned int lsf);
static inline int verify_benchmark(int r);
static inline void initialise_benchmark(void)
{

}

int benchmark(void)
{
    initialise_benchmark();
    int result = benchmark_body(SCALE_FACTOR);
    return verify_benchmark(result);
}

char text[] = "abbbababaabccababcacbcbcbabbabcbabcabcbbcbbac";

static inline int benchmark_body(unsigned int lsf)
{
    int ret;

    for (unsigned int lsf_cnt = 0; lsf_cnt < SCALE_FACTOR; lsf_cnt++) {
            int i;
            int len = strlen(text);
            struct slre_cap captures;
            ret = 0;

            ret += slre_match("(ab)+", text, len, &captures, 1);
            ret += slre_match("(b.+)+", text, len, &captures, 1);
            ret += slre_match("a[ab]*", text, len, &captures, 1);
            ret += slre_match("([ab^c][ab^c])+", text, len, &captures, 1);
        }

    return ret;
}

static inline int verify_benchmark(int r) {
  return 102 == r;
}
