# import micropython

SCALE_FACTOR = 1

P1_is_marked = 3
P1_marking_member_0 = [0] * 3
P2_is_marked = 5
P2_marking_member_0 = [0] * 5
P3_is_marked = 0
P3_marking_member_0 = [0] * 6


def benchmark_body(lsf):
    global P1_is_marked, P2_is_marked, P3_is_marked
    global P1_marking_member_0, P2_marking_member_0, P3_marking_member_0

    for lsf_cnt in range(lsf):
        P1_is_marked = 3
        P2_is_marked = 5
        P3_is_marked = 0

        if ((P1_is_marked >= 3) and (P3_is_marked + 3 <= 6)
                and (P1_marking_member_0[1] == P1_marking_member_0[2])):

            x = P1_marking_member_0[0]
            y = P1_marking_member_0[1]

            if x < y:
                P1_is_marked -= 3

                z = x - y

                P3_marking_member_0[P3_is_marked + 0] = x
                P3_marking_member_0[P3_is_marked + 1] = y
                P3_marking_member_0[P3_is_marked + 2] = z
                P3_is_marked += 3

        if ((P1_is_marked >= 3) and (P3_is_marked + 3 <= 6)
                and (P1_marking_member_0[2] == P1_marking_member_0[1])):

            x = P1_marking_member_0[0]
            y = P1_marking_member_0[2]

            if x < y:
                P1_is_marked -= 3

                z = x - y

                P3_marking_member_0[P3_is_marked + 0] = x
                P3_marking_member_0[P3_is_marked + 1] = y
                P3_marking_member_0[P3_is_marked + 2] = z
                P3_is_marked += 3

        if ((P1_is_marked >= 3) and (P3_is_marked + 3 <= 6)
                and (P1_marking_member_0[0] == P1_marking_member_0[2])):

            x = P1_marking_member_0[1]
            y = P1_marking_member_0[0]

            if x < y:
                P1_is_marked -= 3

                z = x - y

                P3_marking_member_0[P3_is_marked + 0] = x
                P3_marking_member_0[P3_is_marked + 1] = y
                P3_marking_member_0[P3_is_marked + 2] = z
                P3_is_marked += 3

        if ((P1_is_marked >= 3) and (P3_is_marked + 3 <= 6)
                and (P1_marking_member_0[2] == P1_marking_member_0[0])):

            x = P1_marking_member_0[1]
            y = P1_marking_member_0[2]

            if x < y:
                P1_is_marked -= 3

                z = x - y

                P3_marking_member_0[P3_is_marked + 0] = x
                P3_marking_member_0[P3_is_marked + 1] = y
                P3_marking_member_0[P3_is_marked + 2] = z
                P3_is_marked += 3

        if ((P1_is_marked >= 3) and (P3_is_marked + 3 <= 6)
                and (P1_marking_member_0[0] == P1_marking_member_0[1])):

            x = P1_marking_member_0[2]
            y = P1_marking_member_0[0]

            if x < y:
                P1_is_marked -= 3

                z = x - y

                P3_marking_member_0[P3_is_marked + 0] = x
                P3_marking_member_0[P3_is_marked + 1] = y
                P3_marking_member_0[P3_is_marked + 2] = z
                P3_is_marked += 3

        if ((P1_is_marked >= 3) and (P3_is_marked + 3 <= 6)
                and (P1_marking_member_0[1] == P1_marking_member_0[0])):

            x = P1_marking_member_0[2]
            y = P1_marking_member_0[1]

            if x < y:
                P1_is_marked -= 3

                z = x - y

                P3_marking_member_0[P3_is_marked + 0] = x
                P3_marking_member_0[P3_is_marked + 1] = y
                P3_marking_member_0[P3_is_marked + 2] = z
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[2]) and (
                (P2_marking_member_0[1] == P2_marking_member_0[3]))):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[3]) and (
                P2_marking_member_0[1] == P2_marking_member_0[2])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[1]) and (
                P2_marking_member_0[2] == P2_marking_member_0[3])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[3]) and (
                P2_marking_member_0[2] == P2_marking_member_0[1])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[1]) and (
                P2_marking_member_0[3] == P2_marking_member_0[2])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[2]) and (
                P2_marking_member_0[3] == P2_marking_member_0[1])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[2]) and (
                P2_marking_member_0[0] == P2_marking_member_0[3])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[0]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[3]) and (
                P2_marking_member_0[0] == P2_marking_member_0[2])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[0]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[0]) and (
                P2_marking_member_0[2] == P2_marking_member_0[3])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[3]) and (
                P2_marking_member_0[2] == P2_marking_member_0[0])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[0]) and (
                P2_marking_member_0[3] == P2_marking_member_0[2])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[2]) and (
                P2_marking_member_0[3] == P2_marking_member_0[0])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[1]) and (
                P2_marking_member_0[0] == P2_marking_member_0[3])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[0]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[3]) and (
                P2_marking_member_0[0] == P2_marking_member_0[1])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[0]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[0]) and (
                P2_marking_member_0[1] == P2_marking_member_0[3])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[3]) and (
                P2_marking_member_0[1] == P2_marking_member_0[0])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[0]) and (
                P2_marking_member_0[3] == P2_marking_member_0[1])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[1]) and (
                P2_marking_member_0[3] == P2_marking_member_0[0])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[1]) and (
                P2_marking_member_0[0] == P2_marking_member_0[2])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[0]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[2]) and (
                P2_marking_member_0[0] == P2_marking_member_0[1])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[0]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[0]) and (
                P2_marking_member_0[1] == P2_marking_member_0[2])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[2]) and (
                P2_marking_member_0[1] == P2_marking_member_0[0])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[0]) and (
                P2_marking_member_0[2] == P2_marking_member_0[1])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 4) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[1]) and (
                P2_marking_member_0[2] == P2_marking_member_0[0])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[2]) and (
                P2_marking_member_0[1] == P2_marking_member_0[4])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[3]) and (
                P2_marking_member_0[1] == P2_marking_member_0[4])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[4]) and (
                P2_marking_member_0[1] == P2_marking_member_0[2])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[4]) and (
                P2_marking_member_0[1] == P2_marking_member_0[3])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[1]) and (
                P2_marking_member_0[2] == P2_marking_member_0[4])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[3]) and (
                P2_marking_member_0[2] == P2_marking_member_0[4])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[4]) and (
                P2_marking_member_0[2] == P2_marking_member_0[1])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[4]) and (
                P2_marking_member_0[2] == P2_marking_member_0[3])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[1]) and (
                P2_marking_member_0[3] == P2_marking_member_0[4])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[2]) and (
                P2_marking_member_0[3] == P2_marking_member_0[4])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[4]) and (
                P2_marking_member_0[3] == P2_marking_member_0[1])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[4]) and (
                P2_marking_member_0[3] == P2_marking_member_0[2])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[1]) and (
                P2_marking_member_0[4] == P2_marking_member_0[2])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[1]) and (
                P2_marking_member_0[4] == P2_marking_member_0[3])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[2]) and (
                P2_marking_member_0[4] == P2_marking_member_0[1])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[2]) and (
                P2_marking_member_0[4] == P2_marking_member_0[3])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[3]) and (
                P2_marking_member_0[4] == P2_marking_member_0[1])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[3]) and (
                P2_marking_member_0[4] == P2_marking_member_0[2])):

            a = P2_marking_member_0[0]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[2]) and (
                P2_marking_member_0[0] == P2_marking_member_0[4])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[3]) and (
                P2_marking_member_0[0] == P2_marking_member_0[4])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[4]) and (
                P2_marking_member_0[0] == P2_marking_member_0[2])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[4]) and (
                P2_marking_member_0[0] == P2_marking_member_0[3])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[0]) and (
                P2_marking_member_0[2] == P2_marking_member_0[4])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[3]) and (
                P2_marking_member_0[2] == P2_marking_member_0[4])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[4]) and (
                P2_marking_member_0[2] == P2_marking_member_0[0])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[4]) and (
                P2_marking_member_0[2] == P2_marking_member_0[3])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[0]) and (
                P2_marking_member_0[3] == P2_marking_member_0[4])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[2]) and (
                P2_marking_member_0[3] == P2_marking_member_0[4])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[4]) and (
                P2_marking_member_0[3] == P2_marking_member_0[0])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[4]) and (
                P2_marking_member_0[3] == P2_marking_member_0[2])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[0]) and (
                P2_marking_member_0[4] == P2_marking_member_0[2])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[0]) and (
                P2_marking_member_0[4] == P2_marking_member_0[3])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[2]) and (
                P2_marking_member_0[4] == P2_marking_member_0[0])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[2]) and (
                P2_marking_member_0[4] == P2_marking_member_0[3])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[4]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[3]) and (
                P2_marking_member_0[4] == P2_marking_member_0[0])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[3]) and (
                P2_marking_member_0[4] == P2_marking_member_0[2])):

            a = P2_marking_member_0[1]
            b = P2_marking_member_0[4]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[1]) and (
                P2_marking_member_0[0] == P2_marking_member_0[4])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[3]) and (
                P2_marking_member_0[0] == P2_marking_member_0[4])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[4]) and (
                P2_marking_member_0[0] == P2_marking_member_0[1])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[4]) and (
                P2_marking_member_0[0] == P2_marking_member_0[3])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[0]) and (
                P2_marking_member_0[1] == P2_marking_member_0[4])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[3]) and (
                P2_marking_member_0[1] == P2_marking_member_0[4])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[4]) and (
                P2_marking_member_0[1] == P2_marking_member_0[0])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[4]) and (
                P2_marking_member_0[1] == P2_marking_member_0[3])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[0]) and (
                P2_marking_member_0[3] == P2_marking_member_0[4])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[1]) and (
                P2_marking_member_0[3] == P2_marking_member_0[4])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[4]) and (
                P2_marking_member_0[3] == P2_marking_member_0[0])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[4]) and (
                P2_marking_member_0[3] == P2_marking_member_0[1])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[0]) and (
                P2_marking_member_0[4] == P2_marking_member_0[1])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[0]) and (
                P2_marking_member_0[4] == P2_marking_member_0[3])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[1]) and (
                P2_marking_member_0[4] == P2_marking_member_0[0])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[1]) and (
                P2_marking_member_0[4] == P2_marking_member_0[3])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[4]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[3]) and (
                P2_marking_member_0[4] == P2_marking_member_0[0])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[3]) and (
                P2_marking_member_0[4] == P2_marking_member_0[1])):

            a = P2_marking_member_0[2]
            b = P2_marking_member_0[4]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[1]) and (
                P2_marking_member_0[0] == P2_marking_member_0[4])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[2]) and (
                P2_marking_member_0[0] == P2_marking_member_0[4])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[4]) and (
                P2_marking_member_0[0] == P2_marking_member_0[1])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[4]) and (
                P2_marking_member_0[0] == P2_marking_member_0[2])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[0]) and (
                P2_marking_member_0[1] == P2_marking_member_0[4])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[2]) and (
                P2_marking_member_0[1] == P2_marking_member_0[4])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[4]) and (
                P2_marking_member_0[1] == P2_marking_member_0[0])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[4]) and (
                P2_marking_member_0[1] == P2_marking_member_0[2])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[0]) and (
                P2_marking_member_0[2] == P2_marking_member_0[4])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[1]) and (
                P2_marking_member_0[2] == P2_marking_member_0[4])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[4]) and (
                P2_marking_member_0[2] == P2_marking_member_0[0])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[4]) and (
                P2_marking_member_0[2] == P2_marking_member_0[1])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[0]) and (
                P2_marking_member_0[4] == P2_marking_member_0[1])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[0]) and (
                P2_marking_member_0[4] == P2_marking_member_0[2])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[1]) and (
                P2_marking_member_0[4] == P2_marking_member_0[0])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[1]) and (
                P2_marking_member_0[4] == P2_marking_member_0[2])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[4]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[2]) and (
                P2_marking_member_0[4] == P2_marking_member_0[0])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[4]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[4] == P2_marking_member_0[2]) and (
                P2_marking_member_0[4] == P2_marking_member_0[1])):

            a = P2_marking_member_0[3]
            b = P2_marking_member_0[4]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[1]) and (
                P2_marking_member_0[0] == P2_marking_member_0[2])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[1]) and (
                P2_marking_member_0[0] == P2_marking_member_0[3])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[2]) and (
                P2_marking_member_0[0] == P2_marking_member_0[1])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[2]) and (
                P2_marking_member_0[0] == P2_marking_member_0[3])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[3]) and (
                P2_marking_member_0[0] == P2_marking_member_0[1])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[0] == P2_marking_member_0[3]) and (
                P2_marking_member_0[0] == P2_marking_member_0[2])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[0]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[0]) and (
                P2_marking_member_0[1] == P2_marking_member_0[2])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[0]) and (
                P2_marking_member_0[1] == P2_marking_member_0[3])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[2]) and (
                P2_marking_member_0[1] == P2_marking_member_0[0])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[2]) and (
                P2_marking_member_0[1] == P2_marking_member_0[3])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[3]) and (
                P2_marking_member_0[1] == P2_marking_member_0[0])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[1]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[1] == P2_marking_member_0[3]) and (
                P2_marking_member_0[1] == P2_marking_member_0[2])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[1]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[0]) and (
                P2_marking_member_0[2] == P2_marking_member_0[1])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[0]) and (
                P2_marking_member_0[2] == P2_marking_member_0[3])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[1]) and (
                P2_marking_member_0[2] == P2_marking_member_0[0])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[3]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[1]) and (
                P2_marking_member_0[2] == P2_marking_member_0[3])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[3]) and (
                P2_marking_member_0[2] == P2_marking_member_0[0])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[2]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[2] == P2_marking_member_0[3]) and (
                P2_marking_member_0[2] == P2_marking_member_0[1])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[2]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[0]) and (
                P2_marking_member_0[3] == P2_marking_member_0[1])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[0]) and (
                P2_marking_member_0[3] == P2_marking_member_0[2])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[1]) and (
                P2_marking_member_0[3] == P2_marking_member_0[0])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[2]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[1]) and (
                P2_marking_member_0[3] == P2_marking_member_0[2])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[2]) and (
                P2_marking_member_0[3] == P2_marking_member_0[0])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[3]

            if b > a:
                P2_marking_member_0[0] = P2_marking_member_0[1]
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3

        if (P2_is_marked >= 5) and ((P3_is_marked + 3) <= 6) and (
                (P2_marking_member_0[3] == P2_marking_member_0[2]) and (
                P2_marking_member_0[3] == P2_marking_member_0[1])):

            a = P2_marking_member_0[4]
            b = P2_marking_member_0[3]

            if b > a:
                P2_is_marked -= 4

                c = a + b

                P3_marking_member_0[P3_is_marked + 0] = a
                P3_marking_member_0[P3_is_marked + 1] = b
                P3_marking_member_0[P3_is_marked + 2] = c
                P3_is_marked += 3
    return 0


def initialize_benchmark():
    pass


def benchmark():
    initialize_benchmark()
    res = benchmark_body(SCALE_FACTOR)
    # print("")
    # micropython.mem_info()
    return verify_benchmark(res)


def verify_benchmark(unused):
    global P1_is_marked, P2_is_marked, P3_is_marked
    global P1_marking_member_0, P2_marking_member_0, P3_marking_member_0
    expP1_is_marked = 3
    expP1_marking_member_0 = [0, 0, 0]
    expP2_is_marked = 5
    expP2_marking_member_0 = [0, 0, 0, 0, 0]
    expP3_is_marked = 0
    expP3_marking_member_0 = [0, 0, 0, 0, 0, 0]
    if (expP1_is_marked != P1_is_marked or expP2_is_marked != P2_is_marked
            or expP3_is_marked != P3_is_marked):
        return False
    for i in range(3):
        if (expP1_marking_member_0[i] != P1_marking_member_0[i]
                or expP2_marking_member_0[i] != P2_marking_member_0[i]
                or expP3_marking_member_0[i] != P3_marking_member_0[i]):
            return False
    for i in range(3, 5):
        if (expP2_marking_member_0[i] != P2_marking_member_0[i]
                or expP3_marking_member_0[i] != P3_marking_member_0[i]):
            return False
    for i in range(5, 6):
        if expP3_marking_member_0[i] != P3_marking_member_0[i]:
            return False

    return True
