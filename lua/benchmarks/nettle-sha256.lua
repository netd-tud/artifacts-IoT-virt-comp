local SCALE_FACTOR = 1
local SHA256_DIGEST_SIZE = 32
local SHA256_BLOCK_SIZE = 64
local SHA256_DATA_LENGTH = 16
local _SHA256_DIGEST_LENGTH = 8

local K = {
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b,
    0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01,
    0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7,
    0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152,
    0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
    0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819,
    0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08,
    0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f,
    0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
}

local msg = {97,98,99,100,98,99,100,101,99,100,101,102,100,101,102,103,101,102,103,104,102,103,104,105,103,104,105,106,104,105,106,107,105,106,107,108,106,107,108,109,107,108,109,110,108,109,110,111,109,110,111,112,110,111,112,113}
local hash = {0x24,0x8d,0x6a,0x61,0xd2,0x06,0x38,0xb8,0xe5,0xc0,0x26,0x93,0x0c,0x3e,0x60,0x39,0xa3,0x3c,0xe4,0x59,0x64,0xff,0x21,0x67,0xf6,0xec,0xed,0xd4,0x19,0xdb,0x06,0xc1}

local buffer = {}
for i = 1, SHA256_DIGEST_SIZE do
    buffer[i] = 0
end

local function rotl32(n, x)
    return (x << n) | (x >>((-n) & 31))
end

local function Choice(x, y, z)
    return z ~ (x & (y ~ z))
end

local function Majority(x, y, z)
    return (x & y) ~ (z & (x ~ y))
end

local function S0(x)
    return rotl32(30, x) ~ rotl32(19, x) ~ rotl32(10, x)
end

local function S1(x)
    return rotl32(26, x) ~ rotl32(21, x) ~ rotl32(7, x)
end

local function s0(x)
    return rotl32(25, x) ~ rotl32(14, x) ~ (x >> 3)
end

local function s1(x)
    return rotl32(15, x) ~ rotl32(13, x) ~ (x >> 10)
end

local function write_uint64(dst, offset, src)
    dst[offset + 1] = (src >> 56) & 0xff
    dst[offset + 2] = (src >> 48) & 0xff
    dst[offset + 3] = (src >> 40) & 0xff
    dst[offset + 4] = (src >> 32) & 0xff
    dst[offset + 5] = (src >> 24) & 0xff
    dst[offset + 6] = (src >> 16) & 0xff
    dst[offset + 7] = (src >> 8) & 0xff
    dst[offset + 8] = src & 0xff
end

local function write_uint32(dst, offset, src)
    dst[offset + 1] = (src >> 24 & 0xff)
    dst[offset + 2] = (src >> 16 & 0xff)
    dst[offset + 3] = (src >> 8 & 0xff)
    dst[offset + 4] = src & 0xff
end

local function read_uint32(src, offset)
    return (src[offset + 1] << 24) | (src[offset + 2] << 16) | (src[offset + 3] << 8) | (src[offset + 4])
end

local function _nettle_write_be32(length, dst, src)
    local words = length // 4
    local leftover = length % 4
    local i = 0

    while i < words do
        write_uint32(dst, i * 4, src[i + 1])
        i = i + 1
    end

    if leftover ~= 0 then
        local word = src[i + 1]
        local j = leftover
        if leftover >= 3 then
            dst[i * 4 + j] = (word >> 8) & 0xff
            j = j - 1
        end
        if leftover >= 2 then
            dst[i * 4 + j] = (word >> 16) & 0xff
            j = j - 1
        end
        if leftover >= 1 then
            dst[i * 4 + j] = (word >> 24) & 0xff
        end
    end
end

local function _nettle_sha256_compress(state, input, input_offset)
    local data = {}
    for i = 0, SHA256_DATA_LENGTH - 1 do
        data[i + 1] = read_uint32(input, input_offset + i * 4)
    end

    local A = state[1]
    local B = state[2]
    local C = state[3]
    local D = state[4]
    local E = state[5]
    local F = state[6]
    local G = state[7]
    local H = state[8]

    for i = 0, 63 do
        local w
        if i < 16 then
            w = data[i + 1]
        else
            local idx = (i & 15) + 1
            data[idx] = (data[idx] + s1(data[((i - 2) & 15) + 1]) + data[((i - 7) & 15) + 1] + s0(data[((i - 15) & 15) + 1])) & 0xffffffff
            w = data[idx]
        end

        local temp1 = (H + S1(E) + Choice(E, F, G) + K[i + 1] + w) & 0xffffffff
        local temp2 = (S0(A) + Majority(A, B, C)) & 0xffffffff

        H = G
        G = F
        F = E
        E = (D + temp1) & 0xffffffff
        D = C
        C = B
        B = A
        A = (temp1 + temp2) & 0xffffffff
    end

    state[1] = (state[1] + A) & 0xffffffff
    state[2] = (state[2] + B) & 0xffffffff
    state[3] = (state[3] + C) & 0xffffffff
    state[4] = (state[4] + D) & 0xffffffff
    state[5] = (state[5] + E) & 0xffffffff
    state[6] = (state[6] + F) & 0xffffffff
    state[7] = (state[7] + G) & 0xffffffff
    state[8] = (state[8] + H) & 0xffffffff
end

local function sha256_init(ctx)
    local H0 = {0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19}
    for i = 1, 8 do
        ctx.state[i] = H0[i]
    end
    ctx.count = 0
    ctx.index = 0
end

local function sha256_update(ctx, length, data)
    local offset = 1

    if ctx.index ~= 0 then
        local left = SHA256_BLOCK_SIZE - ctx.index
        if length < left then
            for i = 0, length - 1 do
                ctx.block[ctx.index + i + 1] = data[offset + i]
            end
            ctx.index = ctx.index + length
            return
        end

        for i = 0, left - 1 do
            ctx.block[ctx.index + i + 1] = data[offset + i]
        end
        _nettle_sha256_compress(ctx.state, ctx.block, 0)
        ctx.count = ctx.count + 1

        offset = offset + left
        length = length - left
        ctx.index = 0
    end

    while length >= SHA256_BLOCK_SIZE do
        _nettle_sha256_compress(ctx.state, data, offset - 1)
        ctx.count = ctx.count + 1
        offset = offset + SHA256_BLOCK_SIZE
        length = length - SHA256_BLOCK_SIZE
    end

    for i = 0, length - 1 do
        ctx.block[i + 1] = data[offset + i]
    end
    ctx.index = length
end

local function sha256_write_digest(ctx, length, digest)
    local i = ctx.index
    ctx.block[i + 1] = 0x80
    i = i + 1

    if i > SHA256_BLOCK_SIZE - 8 then
        while i < SHA256_BLOCK_SIZE do
            ctx.block[i + 1] = 0
            i = i + 1
        end
        _nettle_sha256_compress(ctx.state, ctx.block, 0)
        i = 0
    end

    while i < SHA256_BLOCK_SIZE - 8 do
        ctx.block[i + 1] = 0
        i = i + 1
    end

    local bit_count = (ctx.count << 9) | (ctx.index << 3)
    write_uint64(ctx.block, SHA256_BLOCK_SIZE - 8, bit_count)
    _nettle_sha256_compress(ctx.state, ctx.block, 0)

    _nettle_write_be32(length, digest, ctx.state)
end

local function sha256_digest(ctx, length, digest)
    sha256_write_digest(ctx, length, digest)
    sha256_init(ctx)
end

local nettle_sha256 = {
    digest_size = SHA256_DIGEST_SIZE,
    init = sha256_init,
    update = sha256_update,
    digest = sha256_digest
}

local function initialise_benchmark()
end

local function verify_benchmark(_)
    local correct = true
    for i = 1, _SHA256_DIGEST_LENGTH do
        if hash[i] ~= buffer[i] then
            correct = false
        end
    end
    return correct
end

local function benchmark_body(lsf)
    for _ = 1, lsf do
        for i = 1, SHA256_DIGEST_SIZE do
            buffer[i] = 0
        end

        local ctx = {state = {}, count = 0, block = {}, index = 0}
        for i = 1, SHA256_BLOCK_SIZE do
            ctx.block[i] = 0
        end

        nettle_sha256.init(ctx)
        nettle_sha256.update(ctx, #msg, msg)
        nettle_sha256.digest(ctx, nettle_sha256.digest_size, buffer)
    end

    return 0
end

local function benchmark()
    initialise_benchmark()
    local result = benchmark_body(SCALE_FACTOR)
    return verify_benchmark(result)
end

return benchmark()
