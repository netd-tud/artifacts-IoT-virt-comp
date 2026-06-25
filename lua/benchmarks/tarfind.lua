local SCALE_FACTOR = 1
local ARCHIVE_FILES = 35
local N_SEARCHES = 5

local seed = 0

local function rand_beebs()
    seed = (seed * 1103515245 + 12345) & ((1 << 31) - 1)
    return seed >> 16
end

local function initialise_benchmark()
    seed = 0
end

local function benchmark_body(lsf)
    local found = 0
    for _ = 1, lsf do
        local hdr = {}
        for i = 1, ARCHIVE_FILES do
          local c = {
              filename = {},
              mode = {},
              uID = {},
              gID = {},
              size = {0},
              mtime = {},
              checksum = {},
              isLink = 0,
              linkedFile = {}
          }
            local flen = 5 + ((i - 1) % 94)
            for p = 1, flen do
                c.filename[p] = (rand_beebs() % 26) + 65
            end
            c.filename[flen + 1] = 0
            hdr[i] = c
        end

        found = 0
        for p = 1, N_SEARCHES do
            local idx = ((p - 1 + ARCHIVE_FILES // 2) % ARCHIVE_FILES) + 1
            local search = hdr[idx].filename
            for i = 1, ARCHIVE_FILES do
                local c1, c2 = 1, 1
                while hdr[i].filename[c1] ~= nil and search[c2] ~= nil and hdr[i].filename[c1] ~= 0 and search[c2] ~= 0 and hdr[i].filename[c1] == search[c2] do
                    c1 = c1 + 1
                    c2 = c2 + 1
                end
                local v1 = hdr[i].filename[c1] or 0
                local v2 = search[c2] or 0
                if v1 == 0 and v2 == 0 then
                    found = found + 1
                    break
                end
            end
        end
    end
    return (found == N_SEARCHES) and 1 or 0
end

local function verify_benchmark(r)
    return r == 1
end

local function benchmark()
    initialise_benchmark()
    local result = benchmark_body(SCALE_FACTOR)
    return verify_benchmark(result)
end

return benchmark()
