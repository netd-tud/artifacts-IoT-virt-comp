# import micropython

SCALE_FACTOR = 1

MSG_SIZE = 1000
RESULT = 0x33f673b4

MASK = 0xFFFFFFFF

r = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

k = [
    0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
    0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
    0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
    0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
    0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
    0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
    0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
]

h0 = 0x67452301
h1 = 0xefcdab89
h2 = 0x98badcfe
h3 = 0x10325476


def bytes_to_u32_le(buf, off):
    return (
            buf[off] | (buf[off + 1] << 8) | (buf[off + 2] << 16) | (buf[off + 3] << 24)
            ) & MASK


def leftrotate(x, c):
    return ((x << c) | (x >> (32 - c))) & MASK


def md5(initial_msg):
    global h0, h1, h2, h3

    h0 = 0x67452301
    h1 = 0xefcdab89
    h2 = 0x98badcfe
    h3 = 0x10325476

    new_len = ((((MSG_SIZE + 8) // 64) + 1) * 64) - 8
    msg = bytearray(new_len + 64)
    for i in range(MSG_SIZE):
        msg[i] = initial_msg[i] & 0xff
    msg[MSG_SIZE] = 128

    bits_len = 8 * MSG_SIZE
    msg[new_len + 0] = bits_len & 0xFF
    msg[new_len + 1] = (bits_len >> 8) & 0xFF
    msg[new_len + 2] = (bits_len >> 16) & 0xFF
    msg[new_len + 3] = (bits_len >> 24) & 0xFF

    for offset in range(0, new_len, 64):
        w = [0] * 16
        for i in range(16):
            w[i] = bytes_to_u32_le(msg, offset + i * 4)
        a = h0
        b = h1
        c = h2
        d = h3

        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16

            f &= MASK
            temp = d
            d = c
            c = b
            b = (b + leftrotate((a + f + k[i] + w[g]) & MASK, r[i])) & MASK
            a = temp

        h0 = (h0 + a) & MASK
        h1 = (h1 + b) & MASK
        h2 = (h2 + c) & MASK
        h3 = (h3 + d) & MASK


def initialise_benchmark():
    pass


def benchmark_body(lsf):
    global h0, h1, h2, h3
    for _ in range(lsf):
        starting_message = bytearray(MSG_SIZE)
        for i in range(MSG_SIZE):
            starting_message[i] = i & 0xFF
        md5(starting_message)
    return h0 ^ h1 ^ h2 ^ h3


def verify_benchmark(result):
    return result == RESULT


def benchmark():
    initialise_benchmark()
    result = benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(result)
