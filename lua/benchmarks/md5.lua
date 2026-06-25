local SCALE_FACTOR = 1
local MSG_SIZE = 1000
local MSG_SIZE_PADDED = ((((MSG_SIZE + 8) // 64) + 1) * 64) - 8
local RESULT = 0x33f673b4

local starting_message = {}
for i = 1, MSG_SIZE do
    starting_message[i] = 0
end

local msg_buff = {}
for i = 1, MSG_SIZE_PADDED + 64 do
    msg_buff[i] = 0
end

local r = {
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
}

local k = {
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
}

local h0, h1, h2, h3 = 0, 0, 0, 0

local function lrotate(x, c)
	return ((x << c) | (x >> (32 - c))) & 0xffffffff
end

local function md5(initial_msg)
    h0 = 0x67452301
    h1 = 0xefcdab89
    h2 = 0x98badcfe
    h3 = 0x10325476

    for i = 1, #msg_buff do
        msg_buff[i] = 0
    end

    for i = 1, MSG_SIZE do
        msg_buff[i] = initial_msg[i] & 0xff
    end

    msg_buff[MSG_SIZE + 1] = 128

    local bits_len = 8 * MSG_SIZE
    local base = MSG_SIZE_PADDED + 1
    msg_buff[base] = bits_len & 0xff
    msg_buff[base + 1] = bits_len >> 8 & 0xff
    msg_buff[base + 2] = bits_len >> 16 & 0xff
    msg_buff[base + 3] = bits_len >> 24& 0xff

    for offset = 0, MSG_SIZE_PADDED - 1, 64 do
        local w = {}
        for j = 0, 15 do
            local idx = offset + j * 4 + 1
            w[j + 1] = msg_buff[idx] | msg_buff[idx + 1] << 8 | msg_buff[idx + 2] << 16 | msg_buff[idx + 3] << 24
        end

        local a = h0
        local b = h1
        local c = h2
        local d = h3

        for i = 0, 63 do
            local f, g
            if i < 16 then
                f = (b & c) | ((~b) & d);
                g = i
            elseif i < 32 then
                f = (d & b) | ((~d) & c);
                g = (5 * i + 1) % 16
            elseif i < 48 then
                f = b  ~ c  ~ d
                g = (3 * i + 5) % 16
            else
                f = c  ~ (b | (~d));
                g = (7 * i) % 16
            end

            f = f & 0xffffffff

            local temp = d
            d = c
            c = b
            local sum = (a + f + k[i + 1] + w[g + 1]) & 0xffffffff
            b = (b + lrotate(sum, r[i + 1])) & 0xffffffff
            a = temp
        end

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
    end
end

local function initialise_benchmark()
end

local function benchmark_body(lsf)
    for _ = 1, lsf do
        for i = 1, MSG_SIZE do
            starting_message[i] = (i - 1) & 0xff
        end
        md5(starting_message)
    end

    return h0  ~ h1  ~ h2  ~ h3
end

local function verify_benchmark(res)
    return res == RESULT
end

local function benchmark()
    initialise_benchmark()
    local result = benchmark_body(SCALE_FACTOR)
    return verify_benchmark(result)
end

return benchmark()
