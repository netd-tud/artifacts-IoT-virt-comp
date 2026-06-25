local SCALE_FACTOR = 1
local TEST_SIZE = 500
local compression_buff = {}
for i = 1, TEST_SIZE + 1 do
    compression_buff[i] = 0
end

local orig_data = {74,50,79,90,70,53,48,70,89,76,68,53,85,84,86,89,89,82,77,84,48,86,88,79,48,49,86,67,53,70,78,73,66,49,67,71,49,50,77,84,73,80,84,50,67,73,86,48,48,66,79,85,87,70,68,82,65,89,84,65,51,65,73,52,50,75,70,88,72,82,75,80,65,51,76,67,71,65,51,65,66,76,85,89,81,88,74,82,81,50,82,78,50,90,77,89,69,82,80,76,67,48,48,67,88,70,69,51,71,66,51,72,77,83,53,51,74,73,79,90,69,53,72,66,89,84,90,50,69,74,72,71,68,66,73,48,72,77,89,78,79,86,85,48,72,85,88,82,50,70,75,66,69,82,67,51,69,49,90,73,69,66,79,72,67,87,67,74,68,48,87,82,80,76,76,88,53,68,73,49,73,83,50,78,69,52,75,73,48,68,82,52,69,53,71,72,87,73,81,90,67,72,75,82,83,86,73,82,89,81,77,66,68,74,79,72,72,89,80,66,49,65,65,65,65,71,72,87,79,88,80,81,52,90,66,81,79,75,66,72,48,79,73,51,88,87,69,52,79,85,65,74,85,65,74,85,71,81,75,85,73,90,69,71,83,70,88,66,80,89,73,75,71,81,72,51,71,77,50,85,65,50,51,85,50,72,74,67,88,84,87,53,78,48,71,53,53,51,65,80,86,73,90,50,89,65,90,52,77,86,83,77,82,81,66,78,88,75,80,79,51,70,79,75,53,85,75,53,82,75,79,71,84,72,67,76,72,50,75,85,82,50,65,68,77,66,81,68,76,65,83,74,70,65,84,70,85,51,69,70,73,83,76,49,90,79,71,65,75,81,85,49,78,86,52,90,87,80,51,67,80,80,76,85,80,52,90,68,50,51,73,69,80,84,53,73,66,70,74,76,87,51,72,68,83,70,50,74,85,90,76,68,73,87,89,88,85,82,48,81,80,67,85,52,87,84,72,88,90,81,68,80,78,75,83,65,80,79,74,69,73,85,72,81,75,53,73,52,82,67,80,65,70,68,52,49,88,70,83,81,86,86,53,68,53,82,68,80,53,77,84,72,65,48,89,75,48,65,73,76,67,88,76,72,49,74,67,83,80,86,67,69,75,66,72,75,83,75,90,82}

local test_data = {}
for i = 1, TEST_SIZE do
    test_data[i] = 0
end

local function heap_adjust(freq, heap, n, k)
    local v = heap[k]
    while k <= n // 2 do
        local j = k + k
        if j < n and freq[heap[j] + 1] > freq[heap[j + 1] + 1] then
            j = j + 1
        end
        if freq[v + 1] < freq[heap[j] + 1] then
            break
        end
        heap[k] = heap[j]
        k = j
    end
    heap[k] = v
end

local function compdecomp(data, data_len)
    local freq = {}
    local heap = {}
    local link = {}
    local code = {}
    local clen = {}
    local comp = compression_buff

    for i = 1, data_len + 1 do
        comp[i] = 0
    end
    for i = 1, 512 do
        freq[i] = 0
        link[i] = 0
    end
    for i = 1, 256 do
        heap[i] = 0
        code[i] = 0
        clen[i] = 0
    end

    local dptr = 1
    for _ = 1, data_len do
        local v = data[dptr]
        freq[v + 1] = freq[v + 1] + 1
        dptr = dptr + 1
    end

    local n = 0
    for i = 0, 255 do
        if freq[i + 1] ~= 0 then
            n = n + 1
            heap[n] = i
        end
    end

    for i = n, 1, -1 do
        heap_adjust(freq, heap, n, i)
    end

    while n > 1 do
        n = n - 1
        local temp = heap[1]
        heap[1] = heap[n + 1]
        heap_adjust(freq, heap, n, 1)

        freq[256 + n + 1] = freq[heap[1] + 1] + freq[temp + 1]
        link[temp + 1] = 256 + n
        link[heap[1] + 1] = -256 - n
        heap[1] = 256 + n

        heap_adjust(freq, heap, n, 1)
    end

    link[256 + n + 1] = 0

    local maxx = 0
    local maxi = 0

    for m = 0, 255 do
        if freq[m + 1] == 0 then
            code[m + 1] = 0
            clen[m + 1] = 0
        else
            local i = 0
            local j = 1
            local x = 0
            local l = link[m + 1]

            while l ~= 0 do
                if l < 0 then
                    x = x + j
                    l = -l
                end

                l = link[l + 1]
                j = j << 1
                i = i + 1
            end

            code[m + 1] = x
            clen[m + 1] = i

            if x > maxx then
                maxx = x
            end
            if i > maxi then
                maxi = i
            end
        end
    end

    if maxi > 64 then
        return
    end

    local comp_len = 0
    local bout = 0
    local bit = -1
    dptr = 1

    if maxx == 0 then
        return
    end

    for _ = 1, data_len do
        local d = data[dptr]
        local mask = 1 << (clen[d + 1] - 1)

        for _ = 1, clen[d + 1] do
            if bit == 7 then
                comp[comp_len + 1] = bout
                comp_len = comp_len + 1
                if comp_len == data_len then
                    return
                end
                bit = 0
                bout = 0
            else
                bit = bit + 1
                bout = (bout << 1) & 0xff
            end

            if (code[d + 1] & mask) ~= 0 then
                bout = bout | 1
            end
            mask = mask >> 1
        end

        dptr = dptr + 1
    end

    bout = (bout << (7 - bit)) & 0xff
    comp[comp_len + 1] = bout
    comp_len = comp_len + 1

    local heap2 = {}
    local outc = {}

    for j = 0, 255 do
        outc[j + 1] = j
        heap2[j + 1] = 0
        if (code[j + 1] | clen[j + 1]) ~= 0 then
            local k = 0
            local mask = 1 << (clen[j + 1] - 1)
            for _ = 1, clen[j + 1] do
                k = k * 2 + 1
                if (code[j + 1] & mask) ~= 0 then
                    k = k + 1
                end
                mask = mask >> 1
            end
            heap2[j + 1] = k
        end
    end

    for i = 2, 256 do
        local t = heap2[i]
        local c = outc[i]
        local j = i
        while j > 1 and heap2[j - 1] > t do
            heap2[j] = heap2[j - 1]
            outc[j] = outc[j - 1]
            j = j - 1
        end
        heap2[j] = t
        outc[j] = c
    end

    local j = 1
    while heap2[j] == 0 do
        j = j + 1
    end

    local k = 0
    local i = j
    local mask = 0x80
    n = 0
    local cptr = 1
    dptr = 1

    while n < data_len do
        k = k * 2 + 1
        if (comp[cptr] & mask) ~= 0 then
            k = k + 1
        end

        while heap2[i] < k do
            i = i + 1
        end

        if k == heap2[i] then
            data[dptr] = outc[i]
            dptr = dptr + 1
            n = n + 1
            k = 0
            i = j
        end

        if mask > 1 then
            mask = mask >> 1
        else
            mask = 0x80
            cptr = cptr + 1
        end
    end
end

local function initialise_benchmark()
end

local function benchmark_body(lsf)
    for _ = 1, lsf do
        for i = 1, TEST_SIZE do
            test_data[i] = orig_data[i]
        end
        compdecomp(test_data, TEST_SIZE)
    end
    return 0
end

local function verify_benchmark(_)
    for i = 1, TEST_SIZE do
        if test_data[i] ~= orig_data[i] then
            return false
        end
    end
    return true
end

local function benchmark()
    initialise_benchmark()
    local result = benchmark_body(SCALE_FACTOR)
    return verify_benchmark(result)
end

return benchmark()
