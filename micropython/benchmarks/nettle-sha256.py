# import micropython

SCALE_FACTOR = 1

MASK32 = 0xFFFFFFFF
MASK64 = 0xFFFFFFFFFFFFFFFF

SHA256_DIGEST_SIZE = 32
SHA256_BLOCK_SIZE = 64
_SHA256_DIGEST_LENGTH = 8
SHA256_DATA_LENGTH = 16

K = (
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
    0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
    0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
    0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
    0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
)

H0 = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c,
      0x1f83d9ab, 0x5be0cd19]

msg = b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"

hash_ = bytes([
   0x24, 0x8d, 0x6a, 0x61, 0xd2, 0x06, 0x38, 0xb8, 0xe5, 0xc0, 0x26, 0x93,
   0x0c, 0x3e, 0x60, 0x39, 0xa3, 0x3c, 0xe4, 0x59, 0x64, 0xff, 0x21, 0x67,
   0xf6, 0xec, 0xed, 0xd4, 0x19, 0xdb, 0x06, 0xc1
])

buffer = bytearray(SHA256_DIGEST_SIZE)


def rotl32(n, x):
    return ((x << n) | (x >> ((-n) & 31))) & MASK32


def choice(x, y, z):
    return (z ^ (x & (y ^ z))) & MASK32


def majority(x, y, z):
    return ((x & y) ^ (z & (x ^ y))) & MASK32


def big_s0(x):
    return (rotl32(30, x) ^ rotl32(19, x) ^ rotl32(10, x)) & MASK32


def big_s1(x):
    return (rotl32(26, x) ^ rotl32(21, x) ^ rotl32(7, x)) & MASK32


def small_s0(x):
    return (rotl32(25, x) ^ rotl32(14, x) ^ ((x >> 3) & MASK32)) & MASK32


def small_s1(x):
    return (rotl32(15, x) ^ rotl32(13, x) ^ ((x >> 10) & MASK32)) & MASK32


def expand(W, i):
    W[i & 15] = (
            W[i & 15] + small_s1(W[(i - 2) & 15]) + W[(i - 7) & 15]
            + small_s0(W[(i - 15) & 15])
            ) & MASK32
    return W[i & 15]


def sha256_round(a, b, c, d, e, f, g, h, k, data):
    h = (h + big_s1(e) + choice(e, f, g) + k + data) & MASK32
    d = (d + h) & MASK32
    h = (h + big_s0(a) + majority(a, b, c)) & MASK32
    return a, b, c, d, e, f, g, h


def write_uint64(dst, offset, src):
    src &= MASK64
    dst[offset] = (src >> 56) & 0xFF
    dst[offset + 1] = (src >> 48) & 0xFF
    dst[offset + 2] = (src >> 40) & 0xFF
    dst[offset + 3] = (src >> 32) & 0xFF
    dst[offset + 4] = (src >> 24) & 0xFF
    dst[offset + 5] = (src >> 16) & 0xFF
    dst[offset + 6] = (src >> 8) & 0xFF
    dst[offset + 7] = src & 0xFF


def write_uint32(dst, offset, src):
    src &= MASK32
    dst[offset] = (src >> 24) & 0xFF
    dst[offset + 1] = (src >> 16) & 0xFF
    dst[offset + 2] = (src >> 8) & 0xFF
    dst[offset + 3] = src & 0xFF


def read_uint32(src, offset):
    return ((src[offset] << 24) | (src[offset + 1] << 16) |
            (src[offset + 2] << 8) | src[offset + 3]) & MASK32


def nettle_write_be32(length, dst, src):
    words = length // 4
    leftover = length % 4
    di = 0
    for i in range(words):
        write_uint32(dst, di, src[i])
        di += 4
    if leftover:
        word = src[words]
        j = leftover
        if leftover >= 3:
            j -= 1
            dst[di + j] = (word >> 8) & 0xFF
        if leftover >= 2:
            j -= 1
            dst[di + j] = (word >> 16) & 0xFF
        if leftover >= 1:
            j -= 1
            dst[di + j] = (word >> 24) & 0xFF


def nettle_sha256_compress(state, input_data, input_offset):
    data = [0] * SHA256_DATA_LENGTH
    off = input_offset
    for i in range(SHA256_DATA_LENGTH):
        data[i] = read_uint32(input_data, off)
        off += 4

    A = state[0]
    B = state[1]
    C = state[2]
    D = state[3]
    E = state[4]
    F = state[5]
    G = state[6]
    H = state[7]

    ki = 0
    for i in range(0, 16, 8):
        A, B, C, D, E, F, G, H = sha256_round(
                A, B, C, D, E, F, G, H, K[ki + 0], data[i + 0])
        H, A, B, C, D, E, F, G = sha256_round(
                H, A, B, C, D, E, F, G, K[ki + 1], data[i + 1])
        G, H, A, B, C, D, E, F = sha256_round(
                G, H, A, B, C, D, E, F, K[ki + 2], data[i + 2])
        F, G, H, A, B, C, D, E = sha256_round(
                F, G, H, A, B, C, D, E, K[ki + 3], data[i + 3])
        E, F, G, H, A, B, C, D = sha256_round(
                E, F, G, H, A, B, C, D, K[ki + 4], data[i + 4])
        D, E, F, G, H, A, B, C = sha256_round(
                D, E, F, G, H, A, B, C, K[ki + 5], data[i + 5])
        C, D, E, F, G, H, A, B = sha256_round(
                C, D, E, F, G, H, A, B, K[ki + 6], data[i + 6])
        B, C, D, E, F, G, H, A = sha256_round(
                B, C, D, E, F, G, H, A, K[ki + 7], data[i + 7])
        ki += 8

    for _ in range(16, 64, 16):
        A, B, C, D, E, F, G, H = sha256_round(
                A, B, C, D, E, F, G, H, K[ki + 0], expand(data, 0))
        H, A, B, C, D, E, F, G = sha256_round(
                H, A, B, C, D, E, F, G, K[ki + 1], expand(data, 1))
        G, H, A, B, C, D, E, F = sha256_round(
                G, H, A, B, C, D, E, F, K[ki + 2], expand(data, 2))
        F, G, H, A, B, C, D, E = sha256_round(
                F, G, H, A, B, C, D, E, K[ki + 3], expand(data, 3))
        E, F, G, H, A, B, C, D = sha256_round(
                E, F, G, H, A, B, C, D, K[ki + 4], expand(data, 4))
        D, E, F, G, H, A, B, C = sha256_round(
                D, E, F, G, H, A, B, C, K[ki + 5], expand(data, 5))
        C, D, E, F, G, H, A, B = sha256_round(
                C, D, E, F, G, H, A, B, K[ki + 6], expand(data, 6))
        B, C, D, E, F, G, H, A = sha256_round(
                B, C, D, E, F, G, H, A, K[ki + 7], expand(data, 7))
        A, B, C, D, E, F, G, H = sha256_round(
                A, B, C, D, E, F, G, H, K[ki + 8], expand(data, 8))
        H, A, B, C, D, E, F, G = sha256_round(
                H, A, B, C, D, E, F, G, K[ki + 9], expand(data, 9))
        G, H, A, B, C, D, E, F = sha256_round(
                G, H, A, B, C, D, E, F, K[ki + 10], expand(data, 10))
        F, G, H, A, B, C, D, E = sha256_round(
                F, G, H, A, B, C, D, E, K[ki + 11], expand(data, 11))
        E, F, G, H, A, B, C, D = sha256_round(
                E, F, G, H, A, B, C, D, K[ki + 12], expand(data, 12))
        D, E, F, G, H, A, B, C = sha256_round(
                D, E, F, G, H, A, B, C, K[ki + 13], expand(data, 13))
        C, D, E, F, G, H, A, B = sha256_round(
                C, D, E, F, G, H, A, B, K[ki + 14], expand(data, 14))
        B, C, D, E, F, G, H, A = sha256_round(
                B, C, D, E, F, G, H, A, K[ki + 15], expand(data, 15))
        ki += 16

    state[0] = (state[0] + A) & MASK32
    state[1] = (state[1] + B) & MASK32
    state[2] = (state[2] + C) & MASK32
    state[3] = (state[3] + D) & MASK32
    state[4] = (state[4] + E) & MASK32
    state[5] = (state[5] + F) & MASK32
    state[6] = (state[6] + G) & MASK32
    state[7] = (state[7] + H) & MASK32


def sha256_init(ctx):
    ctx["state"] = list(H0)
    ctx["count"] = 0
    ctx["block"] = bytearray(SHA256_BLOCK_SIZE)
    ctx["index"] = 0


def sha256_update(ctx, data):
    length = len(data)
    data_offset = 0
    index = ctx["index"]

    if index:
        left = SHA256_BLOCK_SIZE - index
        if length < left:
            for j in range(length):
                ctx["block"][index + j] = data[data_offset + j]
            ctx["index"] = index + length
            return
        else:
            for j in range(left):
                ctx["block"][index + j] = data[data_offset + j]
            nettle_sha256_compress(ctx["state"], ctx["block"], 0)
            ctx["count"] = (ctx["count"] + 1) & MASK64
            data_offset += left
            length -= left

    while length >= SHA256_BLOCK_SIZE:
        nettle_sha256_compress(ctx["state"], data, data_offset)
        ctx["count"] = (ctx["count"] + 1) & MASK64
        data_offset += SHA256_BLOCK_SIZE
        length -= SHA256_BLOCK_SIZE

    for j in range(length):
        ctx["block"][j] = data[data_offset + j]
    ctx["index"] = length


def sha256_write_digest(ctx, length, digest):
    i = ctx["index"]
    ctx["block"][i] = 0x80
    i += 1

    if i > (SHA256_BLOCK_SIZE - 8):
        for j in range(i, SHA256_BLOCK_SIZE):
            ctx["block"][j] = 0
        nettle_sha256_compress(ctx["state"], ctx["block"], 0)
        i = 0

    for j in range(i, SHA256_BLOCK_SIZE - 8):
        ctx["block"][j] = 0

    bit_count = ((ctx["count"] << 9) | (ctx["index"] << 3)) & MASK64
    write_uint64(ctx["block"], SHA256_BLOCK_SIZE - 8, bit_count)
    nettle_sha256_compress(ctx["state"], ctx["block"], 0)

    nettle_write_be32(length, digest, ctx["state"])


def sha256_digest(ctx, length, digest):
    sha256_write_digest(ctx, length, digest)
    sha256_init(ctx)


def initialise_benchmark():
    pass


def benchmark_body(lsf):
    global buffer
    for _ in range(lsf):
        for i in range(len(buffer)):
            buffer[i] = 0
        ctx = {}
        sha256_init(ctx)
        sha256_update(ctx, msg)
        sha256_digest(ctx, SHA256_DIGEST_SIZE, buffer)
    return 0


def verify_benchmark(res):
    for i in range(_SHA256_DIGEST_LENGTH):
        if hash_[i] != buffer[i]:
            return False
    return True


def benchmark():
    initialise_benchmark()
    result = benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(result)
