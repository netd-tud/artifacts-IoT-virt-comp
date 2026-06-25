/* BEEBS ud benchmark

   This version, copyright (C) 2014-2019 Embecosm Limited and University of
   Bristol

   Contributor James Pallister <james.pallister@bristol.ac.uk>
   Contributor Jeremy Bennett <jeremy.bennett@embecosm.com>

   This file is part of Embench and was formerly part of the Bristol/Embecosm
   Embedded Benchmark Suite.

   SPDX-License-Identifier: GPL-3.0-or-later */

/* MDH WCET BENCHMARK SUITE. */

/*************************************************************************/
/*                                                                       */
/*   SNU-RT Benchmark Suite for Worst Case Timing Analysis               */
/*   =====================================================               */
/*                              Collected and Modified by S.-S. Lim      */
/*                                           sslim@archi.snu.ac.kr       */
/*                                         Real-Time Research Group      */
/*                                        Seoul National University      */
/*                                                                       */
/*                                                                       */
/*        < Features > - restrictions for our experimental environment   */
/*                                                                       */
/*          1. Completely structured.                                    */
/*               - There are no unconditional jumps.                     */
/*               - There are no exit from loop bodies.                   */
/*                 (There are no 'break' or 'return' in loop bodies)     */
/*          2. No 'switch' statements.                                   */
/*          3. No 'do..while' statements.                                */
/*          4. Expressions are restricted.                               */
/*               - There are no multiple expressions joined by 'or',     */
/*                'and' operations.                                      */
/*          5. No library calls.                                         */
/*               - All the functions needed are implemented in the       */
/*                 source file.                                          */
/*                                                                       */
/*                                                                       */
/*************************************************************************/
/*                                                                       */
/*  FILE: ludcmp.c                                                       */
/*  SOURCE : Turbo C Programming for Engineering                         */
/*                                                                       */
/*  DESCRIPTION :                                                        */
/*                                                                       */
/*     Simultaneous linear equations by LU decomposition.                */
/*     The arrays a[][] and b[] are input and the array x[] is output    */
/*     row vector.                                                       */
/*     The variable n is the number of equations.                        */
/*     The input arrays are initialized in function main.                */
/*                                                                       */
/*                                                                       */
/*  REMARK :                                                             */
/*                                                                       */
/*  EXECUTION TIME :                                                     */
/*                                                                       */
/*                                                                       */
/*************************************************************************/

/*************************************************************************
 *  This file:
 *
 *  - Name changed to "ud.c"
 *  - Modified for use with Uppsala/Paderborn tool
 *    : doubles changed to int
 *    : some tests removed
 *  - Program is much more linear, all loops will run to end
 *  - Purpose: test the effect of conditional flows
 *
 *************************************************************************/

/* ==========================================
   [Modification Summary]
   ==========================================
   Purpose: Adjustments to be used with RIOT.
   Date: April 21th 2026
   Author: Leonard Herbst <leonard.herbst@tu-dresden.de>
   Details:
      - formated according to the RIOT formating convention
      - removed merged both scale factors into one
      - used stdint typen when appropriate
      - inlined functions
   ========================================== */

/*
** Benchmark Suite for Real-Time Applications, by Sung-Soo Lim
**
**    III-4. ludcmp.c : Simultaneous Linear Equations by LU Decomposition
**                 (from the book C Programming for EEs by Hyun Soon Ahn)
*/

#include <stddef.h>
#include <stdint.h>

// #include "helpers.h"

#ifndef SCALE_FACTOR
#  define SCALE_FACTOR 1
#endif /* ifndef SCALE_FACTOR */

int32_t a[20][20], b[20], x[20];

static inline int ludcmp(int32_t nmax, int32_t n);

/*  static double fabs(double n) */
/*  { */
/*    double f; */

/*    if (n >= 0) f = n; */
/*    else f = -n; */
/*    return f; */
/*  } */

/* Write to CHKERR from BENCHMARK to ensure calls are not optimised away.  */
volatile int32_t chkerr;

static inline int benchmark_body(unsigned int lsf);
static inline int verify_benchmark(int r);
static inline void initialise_benchmark(void);

int benchmark(void) {
    initialise_benchmark();
    int result = benchmark_body(SCALE_FACTOR);
    return verify_benchmark(result);
}

static inline int memcmp(const void *s1, const void *s2, size_t n) {
    const unsigned char *p1 = (const unsigned char *)s1;
    const unsigned char *p2 = (const unsigned char *)s2;
    for (size_t i = 0; i < n; ++i) {
        if (p1[i] != p2[i]) {
            return (p1[i] < p2[i]) ? -1 : 1;
        }
    }
    return 0;
}

static inline int verify_benchmark(int res)
{
    int32_t x_ref[20] = { 0L, 0L, 1L, 1L, 1L, 2L, 0L, 0L, 0L, 0L,
                           0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L };

    // bpf_printf("x[0] %d\n", x[0]);

    return (0 == memcmp(x, x_ref, 20 * sizeof(x[0]))) && (0 == res);
}

void initialise_benchmark(void)
{
}

static inline int benchmark_body(unsigned int lsf)
{
    for (uint32_t lsf_cnt = 0; lsf_cnt < lsf; lsf_cnt++) {
        int32_t i, j, nmax = 20, n = 5;
        int32_t /* eps, */ w;

        /* eps = 1.0e-6; */

        /* Init loop */
        for (i = 0; i <= n; i++) {
            w = 0; /* data to fill in cells */
            for (j = 0; j <= n; j++) {
                a[i][j] = (i + 1) + (j + 1);
                if (i == j) /* only once per loop pass */
                    a[i][j] *= 2;
                w += a[i][j];
            }
            b[i] = w;
        }

        /*  chkerr = ludcmp(nmax, n, eps); */
        chkerr = ludcmp(nmax, n);
    }

    // bpf_printf("benchmark_body return: %d\n", chkerr);
    return chkerr;
}

static inline int ludcmp(int32_t nmax, int32_t n)
{
    int32_t i, j, k;
    int32_t w, y[100];

    /* if(n > 99 || eps <= 0.0) return(999); */
    for (i = 0; i < n; i++) {
        /* if(fabs(a[i][i]) <= eps) return(1); */
        for (j = i + 1; j <= n; j++) /* triangular loop vs. i */
        {
            w = a[j][i];
            if (i != 0) /* sub-loop is conditional, done
                                   all iterations except first of the
                                   OUTER loop */
                for (k = 0; k < i; k++)
                    w -= a[j][k] * a[k][i];
            a[j][i] = w / a[i][i];
        }
        for (j = i + 1; j <= n; j++) /* triangular loop vs. i */
        {
            w = a[i + 1][j];
            for (k = 0; k <= i; k++) /* triangular loop vs. i */
                w -= a[i + 1][k] * a[k][j];
            a[i + 1][j] = w;
        }
    }
    y[0] = b[0];
    for (i = 1; i <= n; i++) /* iterates n times */
    {
        w = b[i];
        for (j = 0; j < i; j++) /* triangular sub loop */
            w -= a[i][j] * y[j];
        y[i] = w;
    }
    x[n] = y[n] / a[n][n];
    for (i = n - 1; i >= 0; i--) /* iterates n times */
    {
        w = y[i];
        for (j = i + 1; j <= n; j++) /* triangular sub loop */
            w -= a[i][j] * x[j];
        x[i] = w / a[i][i];
    }
    return (0);
}

/*
   Local Variables:
   mode: C
   c-file-style: "gnu"
   End:
*/


