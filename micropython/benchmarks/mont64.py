# import micropython

SCALE_FACTOR = 1

_MASK64 = 0xFFFFFFFFFFFFFFFF
_MASK32 = 0xFFFFFFFF


def _to_signed64(x):
    x &= _MASK64
    if x >= (1 << 63):
        return x - (1 << 64)
    return x


def mulul64(u, v):
    u1 = u >> 32
    u0 = u & _MASK32
    v1 = v >> 32
    v0 = v & _MASK32

    t = u0 * v0
    w0 = t & _MASK32
    k = t >> 32

    t = (u1 * v0 + k) & _MASK64
    w1 = t & _MASK32
    w2 = t >> 32

    t = (u0 * v1 + w1) & _MASK64
    k = t >> 32

    wlo = ((t << 32) + w0) & _MASK64
    whi = (u1 * v1 + w2 + k) & _MASK64

    return whi, wlo


def modul64(x, y, z):
    x &= _MASK64
    y &= _MASK64
    z &= _MASK64

    for i in range(64):
        t = _to_signed64(x) >> 63
        t &= _MASK64
        x = ((x << 1) | (y >> 63)) & _MASK64
        y = (y << 1) & _MASK64
        if ((x | t) & _MASK64) >= z:
            x = (x - z) & _MASK64
            y = (y + 1) & _MASK64

    return x


def montmul(abar, bbar, m, mprime):

    thi, tlo = mulul64(abar, bbar)

    tm = (tlo * mprime) & _MASK64

    tmmhi, tmmlo = mulul64(tm, m)

    ulo = (tlo + tmmlo) & _MASK64
    uhi = (thi + tmmhi) & _MASK64
    if ulo < tlo:
        uhi = (uhi + 1) & _MASK64

    ov = 1 if (uhi < thi) or (uhi == thi and ulo < tlo) else 0

    ulo = uhi
    uhi = 0

    mask = (-(ov | (1 if ulo >= m else 0))) & _MASK64
    ulo = (ulo - (m & mask)) & _MASK64

    return ulo


def xbinGCD(a, b):
    u = 1
    v = 0
    alpha = a
    beta = b

    iterations = 0
    while a > 0:
        a = a >> 1
        if (u & 1) == 0:
            u = u >> 1
            v = v >> 1
        else:
            u = (((u ^ beta) >> 1) + (u & beta)) & _MASK64
            v = ((v >> 1) + alpha) & _MASK64
        iterations += 1

    return u, v


in_a = 0
in_b = 0
in_m = 0


def initialise_benchmark():
    global in_a, in_b, in_m
    in_m = 0xfae849273928f89f
    in_b = 0x14736defb9330573
    in_a = 0x0549372187237fef


def benchmark_body(lsf):
    global in_a, in_b, in_m
    errors = 0

    for lsf_cnt in range(lsf):
        m = in_m
        b = in_b
        a = in_a
        errors = 0

        p1hi, p1lo = mulul64(a, b)
        p1 = modul64(p1hi, p1lo, m)

        p1hi, p1lo = mulul64(p1, p1)
        p1 = modul64(p1hi, p1lo, m)

        p1hi, p1lo = mulul64(p1, p1)
        p1 = modul64(p1hi, p1lo, m)

        hr = 0x8000000000000000

        rinv, mprime = xbinGCD(hr, m)

        check = (2 * hr * rinv - m * mprime) & _MASK64
        if check != 1:
            errors = 1

        abar = modul64(a, 0, m)
        bbar = modul64(b, 0, m)

        p = montmul(abar, bbar, m, mprime)
        p = montmul(p, p, m, mprime)
        p = montmul(p, p, m, mprime)

        phi, plo = mulul64(p, rinv)
        p = modul64(phi, plo, m)

        if p != p1:
            errors = 1

    return errors


def verify_benchmark(r):
    return r == 0


def benchmark():
    initialise_benchmark()
    result = benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(result)
