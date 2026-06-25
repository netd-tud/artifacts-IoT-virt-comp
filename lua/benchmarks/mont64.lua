local SCALE_FACTOR = 1
local MASK = -1
local SIGNBIT = 0x8000000000000000

local in_a = 0
local in_b = 0
local in_m = 0

local function u64(x)
    return x & MASK
end

local function u_lt(a, b)
    return ((a ~ SIGNBIT) < (b ~ SIGNBIT))
end

local function u_ge(a, b)
    return not u_lt(a, b)
end

local function mulul64(u, v)
    local u1 = u >> 32
    local u0 = u & 0xFFFFFFFF
    local v1 = v >> 32
    local v0 = v & 0xFFFFFFFF

    local t = u64(u0 * v0)
    local w0 = t & 0xFFFFFFFF
    local k = t >> 32

    t = u64(u1 * v0 + k)
    local w1 = t & 0xFFFFFFFF
    local w2 = t >> 32

    t = u64(u0 * v1 + w1)
    k = t >> 32

    local wlo = u64((t << 32) + w0)
    local whi = u64(u1 * v1 + w2 + k)
    return whi, wlo
end

local function modul64(x, y, z)
    for _ = 1, 64 do
        local t = x >> 63
        x = u64((x << 1) | (y >> 63))
        y = u64(y << 1)

        local xt = x
        if t ~= 0 then
            xt = x | MASK
        end

        if u_ge(xt, z) then
            x = u64(x - z)
            y = u64(y + 1)
        end
    end
    return x
end

local function montmul(abar, bbar, m, mprime)
    local thi, tlo = mulul64(abar, bbar)
    local tm = u64(tlo * mprime)
    local tmmhi, tmmlo = mulul64(tm, m)

    local ulo = u64(tlo + tmmlo)
    local uhi = u64(thi + tmmhi)
    if u_lt(ulo, tlo) then
        uhi = u64(uhi + 1)
    end

    local ov = 0
    if u_lt(uhi, thi) or (uhi == thi and u_lt(ulo, tlo)) then
        ov = 1
    end

    ulo = uhi
    local cond = ov ~= 0 or u_ge(ulo, m)
    local sub = m & (cond and MASK or 0)
    ulo = u64(ulo - sub)

    return ulo
end

local function xbinGCD(a, b)
    local u = 1
    local v = 0
    local alpha = a
    local beta = b

    while a ~= 0 do
        a = a >> 1
        if (u & 1) == 0 then
            u = u >> 1
            v = v >> 1
        else
            u = u64(((u ~ beta) >> 1) + (u & beta))
            v = u64((v >> 1) + alpha)
        end
    end

    return u64(u), u64(v)
end

local function initialise_benchmark()
    in_m = 0xfae849273928f89f
    in_b = 0x14736defb9330573
    in_a = 0x0549372187237fef
end

local function benchmark_body(lsf)
    local errors = 0

    for _ = 1, lsf do
        local m = in_m
        local b = in_b
        local a = in_a
        local p1hi, p1lo, p1, p, phi, plo
        local rinv, mprime

        errors = 0

        p1hi, p1lo = mulul64(a, b)
        p1 = modul64(p1hi, p1lo, m)
        p1hi, p1lo = mulul64(p1, p1)
        p1 = modul64(p1hi, p1lo, m)
        p1hi, p1lo = mulul64(p1, p1)
        p1 = modul64(p1hi, p1lo, m)

        local hr = 0x8000000000000000
        rinv, mprime = xbinGCD(hr, m)

        if u64(2 * hr * rinv - m * mprime) ~= 1 then
            errors = 1
        end

        local abar = modul64(a, 0, m)
        local bbar = modul64(b, 0, m)

        p = montmul(abar, bbar, m, mprime)
        p = montmul(p, p, m, mprime)
        p = montmul(p, p, m, mprime)

        phi, plo = mulul64(p, rinv)
        p = modul64(phi, plo, m)
        if p ~= p1 then
            errors = 1
        end
    end

    return errors
end

local function verify_benchmark(r)
    return r == 0
end

local function benchmark()
    initialise_benchmark()
    local result = benchmark_body(SCALE_FACTOR)
    return verify_benchmark(result)
end

return benchmark()
