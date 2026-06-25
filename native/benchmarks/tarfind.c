/*
 * This benchmark simulates the search in a TAR archive
 * for a set of filenames
 *
 * Created by Julian Kunkel for Embench-iot
 * Licensed under MIT
 */
// SPDX-License-Identifier: MIT

/* ==========================================
   [Modification Summary]
   ==========================================
   Purpose: Adjustments to be used with RIOT.
   Date: April 21th 2026
   Author: Leonard Herbst <leonard.herbst@tu-dresden.de>
   Details:
      - formated according to the RIOT formating convention
      - used stdint types when appropriate
      - inlined functions
      - used an static array instead of allocating memory using the beebs heap
      - removed warm_caches
      - moved the beebs random function into the benchmark
    ========================================== */

#include <stdint.h>
#include <string.h>

#ifndef SCALE_FACTOR
#  define SCALE_FACTOR 1
#endif

#define HEADER_BUFFER_SIZE sizeof(tar_header_t) * ARCHIVE_FILES

// number of files in the archive
#define ARCHIVE_FILES 35

#define N_SEARCHES    5

// this is the basic TAR header format which is in ASCII
typedef struct {
    uint8_t filename[100];
    uint8_t mode[8];     // file mode
    uint8_t uID[8];      // user id
    uint8_t gID[8];      // group id
    uint8_t size[12];    // in bytes octal base
    uint8_t mtime[12];   // numeric Unix time format (octal)
    uint8_t checksum[8]; // for the header, ignored herew2
    uint8_t isLink;
    uint8_t linkedFile[100];
} tar_header_t;

static uint8_t header_buff[HEADER_BUFFER_SIZE];
static uint32_t seed = 0;

static inline int benchmark_body(unsigned int lsf);
static inline int verify_benchmark(int r);
static inline void initialise_benchmark(void);

static inline uint32_t rand_beebs(void)
{
  seed = (seed * 1103515245UL + 12345UL) & ((1UL << 31) - 1UL);
  return (int) (seed >> 16);
}

int benchmark(void)
{
    initialise_benchmark();
    int result = benchmark_body(SCALE_FACTOR);
    return verify_benchmark(result);
}

static inline void initialise_benchmark(void)
{
  seed = 0;
}

static inline int benchmark_body(unsigned int lsf)
{
    int i, p;
    tar_header_t *hdr;
    int found;

    for (unsigned int lsf_cnt = 0; lsf_cnt < lsf; lsf_cnt++) {

            // always create ARCHIVE_FILES files in the archive
            int files = ARCHIVE_FILES;
            hdr = (tar_header_t *) header_buff;
            for (i = 0; i < files; i++) {
                // create record
                tar_header_t *c = &hdr[i];
                // initialize here for cache efficiency reasons
                memset(c, 0, sizeof(tar_header_t));
                int flen = 5 + i % 94; // vary file lengths
                c->isLink = '0';
                for (p = 0; p < flen; p++) {
                    c->filename[p] = rand_beebs() % 26 + 65;
                }
                c->size[0] = '0';
            }

            found = 0; // number of times a file was found
            // actual benchmark, strcmp with a set of N_SEARCHES files
            // the memory access here is chosen inefficiently on purpose
            for (p = 0; p < N_SEARCHES; p++) {
                // chose the position of the file to search for from the mid of the list
                uint8_t *search = hdr[(p + ARCHIVE_FILES / 2) % ARCHIVE_FILES].filename;

                // for each filename iterate through all files until found
                for (i = 0; i < files; i++) {
                    tar_header_t *cur = &hdr[i];
                    // implementation of strcmp
                    uint8_t *c1;
                    uint8_t  *c2;
                    for (c1 = hdr[i].filename, c2 = search; (*c1 != '\0' && *c2 != '\0' && *c1 == *c2); c1++, c2++)
                        ;
                    // complete match?
                    if (*c1 == '\0' && *c2 == '\0') {
                        found++;
                        break;
                    }
                }
            }
        }

    return found == N_SEARCHES;
}

int verify_benchmark(int r)
{
    return r == 1;
}
