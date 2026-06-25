# import micropython

SCALE_FACTOR = 1
ARCHIVE_FILES = 35
N_SEARCHES = 5

seed = 0


def rand_beebs():
    global seed
    seed = (seed * 1103515245 + 12345) & ((1 << 31) - 1)
    return seed >> 16


def initialise_benchmark():
    global seed
    seed = 0


def benchmark_body(lsf):
    found = 0
    for k in range(lsf):
        hdr = []
        for i in range(ARCHIVE_FILES):
            c = {
                "filename": "",
                "mode": "",
                "uID": "",
                "gID": "",
                "size": "",
                "mtime": "",
                "checksum": "",
                "isLink": "\0",
                "linkedFile": ""
            }
            flen = 5 + (i % 94)
            for p in range(flen):
                c["filename"] += chr((rand_beebs() % 26) + 65)
            c["filename"] += "\0"
            hdr.append(c)

        found = 0
        for p in range(N_SEARCHES):
            idx = (p + ARCHIVE_FILES // 2) % ARCHIVE_FILES
            search = hdr[idx]["filename"]
            for i in range(ARCHIVE_FILES):
                if (search == hdr[i]["filename"]):
                    found += 1
                    break

    return found == N_SEARCHES


def verify_benchmark(r):
    return r is True


def benchmark():
    initialise_benchmark()
    result = benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(result)


benchmark()
