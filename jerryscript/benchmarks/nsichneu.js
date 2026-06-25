var SCALE_FACTOR = 1;

var P1_IS_MARKED = 3;
var P1_MARKING_MEMBER_0 = [0, 0, 0];
var P2_IS_MARKED = 5;
var P2_MARKING_MEMBER_0 = [0, 0, 0, 0, 0];
var P3_IS_MARKED = 0;
var P3_MARKING_MEMBER_0 = [0, 0, 0, 0, 0, 0];

function initialize_benchmark() {

}

function benchmark() {
  initialize_benchmark();
  benchmark_body(SCALE_FACTOR);
  return verify_benchmark(0);
}

function benchmark_body(lsf) {
  for (var lsf_cnt = 0; lsf_cnt < lsf; lsf_cnt++) {
    P1_IS_MARKED = 3;
    P2_IS_MARKED = 5;
    P3_IS_MARKED = 0;

    var x, y, z, a, b, c;

    if ((P1_IS_MARKED >= 3) && (P3_IS_MARKED + 3 <= 6) && (P1_MARKING_MEMBER_0[2] == P1_MARKING_MEMBER_0[3])) {

      x = P1_MARKING_MEMBER_0[1];
      y = P1_MARKING_MEMBER_0[2];

      if ((x < y)) {

        P1_IS_MARKED = P1_IS_MARKED - 3;

        z = x - y;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P1_IS_MARKED >= 3) && (P3_IS_MARKED + 3 <= 6) && (P1_MARKING_MEMBER_0[3] == P1_MARKING_MEMBER_0[2])) {

      x = P1_MARKING_MEMBER_0[1];
      y = P1_MARKING_MEMBER_0[3];

      if ((x < y)) {

        P1_IS_MARKED = P1_IS_MARKED - 3;

        z = x - y;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P1_IS_MARKED >= 3) && (P3_IS_MARKED + 3 <= 6) && (P1_MARKING_MEMBER_0[1] == P1_MARKING_MEMBER_0[3])) {

      x = P1_MARKING_MEMBER_0[2];
      y = P1_MARKING_MEMBER_0[1];

      if ((x < y)) {

        P1_IS_MARKED = P1_IS_MARKED - 3;

        z = x - y;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P1_IS_MARKED >= 3) && (P3_IS_MARKED + 3 <= 6) && (P1_MARKING_MEMBER_0[3] == P1_MARKING_MEMBER_0[1])) {

      x = P1_MARKING_MEMBER_0[2];
      y = P1_MARKING_MEMBER_0[3];

      if ((x < y)) {

        P1_IS_MARKED = P1_IS_MARKED - 3;

        z = x - y;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P1_IS_MARKED >= 3) && (P3_IS_MARKED + 3 <= 6) && (P1_MARKING_MEMBER_0[1] == P1_MARKING_MEMBER_0[2])) {

      x = P1_MARKING_MEMBER_0[3];
      y = P1_MARKING_MEMBER_0[1];

      if ((x < y)) {

        P1_IS_MARKED = P1_IS_MARKED - 3;

        z = x - y;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P1_IS_MARKED >= 3) && (P3_IS_MARKED + 3 <= 6) && (P1_MARKING_MEMBER_0[2] == P1_MARKING_MEMBER_0[1])) {

      x = P1_MARKING_MEMBER_0[3];
      y = P1_MARKING_MEMBER_0[2];

      if ((x < y)) {

        P1_IS_MARKED = P1_IS_MARKED - 3;

        z = x - y;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = x;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = y;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = z;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && (((P3_IS_MARKED + 3) <= 6)) && (((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3])) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4])))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && (((P3_IS_MARKED + 3) <= 6)) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 4) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[1];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[2];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[3];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[5]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[5] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[4];
      b = P2_MARKING_MEMBER_0[5];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[1] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[1];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[2] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[2];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[4];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[4]) && (P2_MARKING_MEMBER_0[3] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[3];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[3];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[1]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_MARKING_MEMBER_0[1] = P2_MARKING_MEMBER_0[2];
        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }

    if ((P2_IS_MARKED >= 5) && ((P3_IS_MARKED + 3) <= 6) && ((P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[3]) && (P2_MARKING_MEMBER_0[4] == P2_MARKING_MEMBER_0[2]))) {

      a = P2_MARKING_MEMBER_0[5];
      b = P2_MARKING_MEMBER_0[4];

      if ((b > a)) {

        P2_IS_MARKED = P2_IS_MARKED - 4;

        c = a + b;

        P3_MARKING_MEMBER_0[P3_IS_MARKED + 1] = a;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 2] = b;
        P3_MARKING_MEMBER_0[P3_IS_MARKED + 3] = c;
        P3_IS_MARKED = P3_IS_MARKED + 3;

      }
    }
  }

  return 0;
}

function verify_benchmark(unused) {
  var expP1_is_marked = 3;
  var expP1_marking_member_0 = [0, 0, 0];
  var expP2_is_marked = 5;
  var expP2_marking_member_0 = [0, 0, 0, 0, 0];
  var expP3_is_marked = 0;
  var expP3_marking_member_0 = [0, 0, 0, 0, 0, 0];

  if (expP1_is_marked != P1_IS_MARKED || expP2_is_marked != P2_IS_MARKED || expP3_is_marked != P3_IS_MARKED) {
    return false;
  }
  for (var i = 0; i < 3; i++) {
    if (expP1_marking_member_0[i] != P1_MARKING_MEMBER_0[i] || expP2_marking_member_0[i] != P2_MARKING_MEMBER_0[i] || expP3_marking_member_0[i] != P3_MARKING_MEMBER_0[i]) {
      return false;
    }
  }
  for (var i = 4; i < 5; i++) {
    if (expP2_marking_member_0[i] != P2_MARKING_MEMBER_0[i] || expP3_marking_member_0[i] != P3_MARKING_MEMBER_0[i]) {
      return false;
    }
  }
  for (var i = 5; i < 6; i++) {
    if (expP3_marking_member_0[i] != P3_MARKING_MEMBER_0[i]) {
      return false;
    }
  }

  return true;
}

benchmark()
