SCALE_FACTOR = 1

P1_IS_MARKED = 3
P1_MARKING_MEMBER_0 = {0, 0, 0}
P2_IS_MARKED = 5
P2_MARKING_MEMBER_0 = {0, 0, 0, 0, 0}
P3_IS_MARKED = 0
P3_MARKING_MEMBER_0 = {0, 0, 0, 0, 0, 0}

local function initialize_benchmark()
end

local function benchmark_body (lsf)

  for _ = 0,lsf do
    P1_IS_MARKED = 3
    P2_IS_MARKED = 5
    P3_IS_MARKED = 0

    local a, b, c, x, y, z
    if (P1_IS_MARKED >= 3) and (P3_IS_MARKED + 3 <= 6) and (P1_MARKING_MEMBER_0[2] == P1_MARKING_MEMBER_0[3]) then

      x = P1_MARKING_MEMBER_0[1]
      y = P1_MARKING_MEMBER_0[2]

      if x < y then

        P1_IS_MARKED = P1_IS_MARKED - 3

        z = x - y

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P1_IS_MARKED >= 3) and (P3_IS_MARKED + 3 <= 6) and (P1_MARKING_MEMBER_0[3] == P1_MARKING_MEMBER_0[2]) then

      x = P1_MARKING_MEMBER_0[1]
      y = P1_MARKING_MEMBER_0[3]

      if (x < y) then

        P1_IS_MARKED = P1_IS_MARKED - 3

        z = x - y

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P1_IS_MARKED >= 3) and (P3_IS_MARKED + 3 <= 6) and (P1_MARKING_MEMBER_0[1] == P1_MARKING_MEMBER_0[3]) then

      x = P1_MARKING_MEMBER_0[2]
      y = P1_MARKING_MEMBER_0[1]

      if x < y then

        P1_IS_MARKED = P1_IS_MARKED - 3

        z = x - y

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P1_IS_MARKED >= 3) and (P3_IS_MARKED + 3 <= 6) and (P1_MARKING_MEMBER_0[3] == P1_MARKING_MEMBER_0[1]) then

      x = P1_MARKING_MEMBER_0[2]
      y = P1_MARKING_MEMBER_0[3]

      if (x < y) then

        P1_IS_MARKED = P1_IS_MARKED - 3

        z = x - y

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P1_IS_MARKED >= 3) and (P3_IS_MARKED + 3 <= 6) and (P1_MARKING_MEMBER_0[1] == P1_MARKING_MEMBER_0[2]) then

      x = P1_MARKING_MEMBER_0[3]
      y = P1_MARKING_MEMBER_0[1]

      if (x < y) then

        P1_IS_MARKED = P1_IS_MARKED - 3

        z = x - y

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P1_IS_MARKED >= 3) and (P3_IS_MARKED + 3 <= 6) and (P1_MARKING_MEMBER_0[2] == P1_MARKING_MEMBER_0[1]) then

      x = P1_MARKING_MEMBER_0[3]
      y = P1_MARKING_MEMBER_0[2]

      if (x < y) then

        P1_IS_MARKED = P1_IS_MARKED - 3

        z = x - y

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and (((P3_IS_MARKED + 3) <= 6)) and (((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]))) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and (((P3_IS_MARKED + 3) <= 6)) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 4) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[1]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[2]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[3]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[4]
      b = P2_MARKING_MEMBER_0[5]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[1]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[2]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) and (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[3]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2]
        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end

    if (P2_IS_MARKED >= 5) and ((P3_IS_MARKED + 3) <= 6) and ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) and (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2])) then

      a = P2_MARKING_MEMBER_0[5]
      b = P2_MARKING_MEMBER_0[4]

      if (b > a) then

        P2_IS_MARKED = P2_IS_MARKED - 4

        c = a + b

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c
        P3_IS_MARKED = P3_IS_MARKED + 3

      end
    end
  end

  return 0
end

local function verify_benchmark (unused)
  local expP1_is_marked = 3
  local expP1_marking_member_0 = {0, 0, 0}
  local expP2_is_marked = 5
  local expP2_marking_member_0 = {0, 0, 0, 0, 0}
  local expP3_is_marked = 0
  local expP3_marking_member_0 = {0, 0, 0, 0, 0, 0}

  if expP1_is_marked ~= P1_IS_MARKED or expP2_is_marked ~= P2_IS_MARKED or expP3_is_marked ~= P3_IS_MARKED then
    return false
  end
  for i=1,4 do
    if expP1_marking_member_0[i] ~= P1_MARKING_MEMBER_0[i] or expP2_marking_member_0[i] ~= P2_MARKING_MEMBER_0[i] or expP3_marking_member_0[i] ~= P3_MARKING_MEMBER_0[i] then
      return false
    end
  end
  for i=4,6 do
    if expP2_marking_member_0[i] ~= P2_MARKING_MEMBER_0[i] or expP3_marking_member_0[i] ~= P3_MARKING_MEMBER_0[i] then
      return false
    end
  end
  for i=6,7 do
    if expP3_marking_member_0[i] ~= P3_MARKING_MEMBER_0[i] then
      return false
    end
  end

  return true
end

local function benchmark ()
  initialize_benchmark();
  benchmark_body(SCALE_FACTOR)
  return verify_benchmark(0)
end


return benchmark()
