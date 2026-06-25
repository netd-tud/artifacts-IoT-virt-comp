# import micropython

SCALE_FACTOR = 1

TEST_SIZE = 500

orig_data = bytearray(
    b'J2OZF50FYLD5UTVYYRMT0VXO01VC5FNIB1CG12MTIPT2CIV00BOUWFDRAYTA3AI42KFXHRKP'
    b'A3LCGA3ABLUYQXJRQ2RN2ZMYERPLC00CXFE3GB3HMS53JIOZE5HBYTZ2EJHGDBI0HMYNOVU0'
    b'HUXR2FKBERC3E1ZIEBOHCWCJD0WRPLLX5DI1IS2NE4KI0DR4E5GHWIQZCHKRSVIRYQMBDJOH'
    b'HYPB1AAAAGHWOXPQ4ZBQOKBH0OI3XWE4OUAJUAJUGQKUIZEGSFXBPYIKGQH3GM2UA23U2HJC'
    b'XTW5N0G553APVIZ2YAZ4MVSMRQBNXKPO3FOK5UK5RKOGTHCLH2KUR2ADMBQDLASJFATFU3EF'
    b'ISL1ZOGAKQU1NV4ZWP3CPPLUP4ZD23IEPT5IBFJLW3HDSF2JUZLDIWYXUR0QPCU4WTHXZQDP'
    b'NKSAPOJEIUHQK5I4RCPAFD41XFSQVV5D5RDP5MTHA0YK0AILCXLH1JCSPVCEKBHKSKZR'
)

test_data = bytearray()


def heap_adjust(freq, heap, n, k):
    v = heap[k - 1]

    while k <= (n // 2):
        j = k + k

        if (j < n) and (freq[heap[j - 1]] > freq[heap[j]]):
            j += 1

        if freq[v] < freq[heap[j - 1]]:
            break

        heap[k - 1] = heap[j - 1]
        k = j

    heap[k - 1] = v


def compdecomp(data, data_len):
    dptr = 0

    freq = [0] * 512
    heap = [0] * 256
    link = [0] * 512
    code = [0] * 256
    clen = [0] * 256

    comp = bytearray(data_len + 1)

    for i in range(data_len):
        freq[data[dptr]] += 1
        dptr += 1

    n = 0
    for i in range(256):
        if freq[i]:
            heap[n] = i
            n += 1

    for i in range(n, 0, -1):
        heap_adjust(freq, heap, n, i)

    while n > 1:
        n -= 1
        temp = heap[0]
        heap[0] = heap[n]

        heap_adjust(freq, heap, n, 1)

        freq[256 + n] = freq[heap[0]] + freq[temp]
        link[temp] = 256 + n
        link[heap[0]] = -256 - n
        heap[0] = 256 + n

        heap_adjust(freq, heap, n, 1)

    link[256 + n] = 0

    maxx = 0
    maxi = 0

    for m in range(256):
        if not freq[m]:
            code[m] = 0
            clen[m] = 0
        else:
            i = 0
            j = 1
            x = 0
            l1 = link[m]

            while l1:
                if l1 < 0:
                    x += j
                    l1 = -l1

                l1 = link[l1]
                j <<= 1
                i += 1

            code[m] = x
            clen[m] = i

            if x > maxx:
                maxx = x

            if i > maxi:
                maxi = i

    if maxi > 32:
        return

    comp_len = 0
    bout = 0
    bit = -1
    dptr = 0

    if maxx == 0:
        return

    for j in range(data_len):
        mask = 1 << (clen[data[dptr]] - 1)

        for i in range(clen[data[dptr]]):
            if bit == 7:
                comp[comp_len] = bout
                comp_len += 1

                if comp_len == data_len:
                    return

                bit = 0
                bout = 0
            else:
                bit += 1
                bout = (bout << 1) & 0xFF

            if code[data[dptr]] & mask:
                bout |= 1

            mask >>= 1

        dptr += 1

    bout = (bout << (7 - bit)) & 0xFF
    comp[comp_len] = bout
    comp_len += 1

    heap2 = [0] * 256
    outc = bytearray(256)

    optr = 0
    for j in range(256):
        outc[optr] = j
        optr += 1

        if code[j] | clen[j]:
            k = 0
            mask = 1 << (clen[j] - 1)

            for i in range(clen[j]):
                k = k * 2 + 1

                if code[j] & mask:
                    k += 1

                mask >>= 1

            heap2[j] = k

    for i in range(1, 256):
        t = heap2[i]
        c = outc[i]
        j = i

        while j and (heap2[j - 1] > t):
            heap2[j] = heap2[j - 1]
            outc[j] = outc[j - 1]
            j -= 1

        heap2[j] = t
        outc[j] = c

    j = 0
    while heap2[j] == 0:
        j += 1

    k = 0
    i = j
    mask = 0x80
    n = 0
    cptr = 0
    dptr = 0

    while n < data_len:
        k = k * 2 + 1

        if comp[cptr] & mask:
            k += 1

        while heap2[i] < k:
            i += 1

        if k == heap2[i]:
            data[dptr] = outc[i]
            dptr += 1
            n += 1
            k = 0
            i = j

        if mask > 1:
            mask >>= 1
        else:
            mask = 0x80
            cptr += 1


def verify_benchmark(res):
    return test_data == orig_data


def initialise_benchmark():
    global test_data
    test_data = bytearray(orig_data)


def benchmark():
    initialise_benchmark()
    benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(0)


def benchmark_body(lsf):
    global test_data
    for _ in range(lsf):
        test_data = bytearray(orig_data)
        compdecomp(test_data, TEST_SIZE)
    return 0
