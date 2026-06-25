#include <stdio.h>
#include <stdint.h>

int benchmark(void) {
    int64_t val = 0x0123456789ABCDEFLL;
    printf("Test: %lld\n", (long long)val);
    printf("Hex:  %llx\n", (long long)val);
    return 0;
}
