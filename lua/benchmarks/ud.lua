local SCALE_FACTOR = 1

local a, b, x = {}, {}, {}
for i = 1, 20 do
    a[i] = {}
    b[i] = 0
    x[i] = 0
    for j = 1, 20 do
        a[i][j] = 0
    end
end

local chkerr = 0

local function ludcmp(nmax, n)
    local y = {}
    for i = 1, 100 do y[i] = 0 end

    for i = 0, n - 1 do
        local ii = i + 1
        for j = i + 1, n do
            local jj = j + 1
            local w = a[jj][ii]
            if i ~= 0 then
                for k = 0, i - 1 do
                    local kk = k + 1
                    w = w - a[jj][kk] * a[kk][ii]
                end
            end
            a[jj][ii] = w // a[ii][ii]
        end
        for j = i + 1, n do
            local jj = j + 1
            local w = a[ii + 1][jj]
            for k = 0, i do
                local kk = k + 1
                w = w - a[ii + 1][kk] * a[kk][jj]
            end
            a[ii + 1][jj] = w
        end
    end

    y[1] = b[1]
    for i = 1, n do
        local ii = i + 1
        local w = b[ii]
        for j = 0, i - 1 do
            local jj = j + 1
            w = w - a[ii][jj] * y[jj]
        end
        y[ii] = w
    end

    x[n + 1] = y[n + 1] // a[n + 1][n + 1]
    for i = n - 1, 0, -1 do
        local ii = i + 1
        local w = y[ii]
        for j = i + 1, n do
            local jj = j + 1
            w = w - a[ii][jj] * x[jj]
        end
        x[ii] = w // a[ii][ii]
    end

    return 0
end

local function initialise_benchmark()
end

local function benchmark_body(lsf)
    for _ = 1, lsf do
        local nmax, n = 20, 5
        for i = 0, n do
            local ii = i + 1
            local w = 0
            for j = 0, n do
                local jj = j + 1
                a[ii][jj] = (i + 1) + (j + 1)
                if i == j then
                    a[ii][jj] = a[ii][jj] * 2
                end
                w = w + a[ii][jj]
            end
            b[ii] = w
        end
        chkerr = ludcmp(nmax, n)
    end
    return chkerr
end

local function verify_benchmark(res)
    local x_ref = {0,0,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
    if res ~= 0 then
        return false
    end
    for i = 1, 20 do
        if x[i] ~= x_ref[i] then
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
