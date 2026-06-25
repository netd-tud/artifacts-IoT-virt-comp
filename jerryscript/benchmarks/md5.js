var SCALE_FACTOR = 1;
var MSG_SIZE = 1000;
var MSG_SIZE_PADDED = (((Math.floor((MSG_SIZE + 8) / 64) + 1) * 64) - 8);
var RESULT = 0x33f673b4;

var starting_message = new Array(MSG_SIZE);
var msg_buff = new Array(MSG_SIZE_PADDED + 64);

var r = [
  7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
  5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
];

var k = [
  0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
  0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
  0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
  0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
  0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
  0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
  0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
  0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
  0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
  0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
  0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
  0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
  0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
  0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
  0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
  0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
];

var h0 = 0;
var h1 = 0;
var h2 = 0;
var h3 = 0;

function leftrotate(x, c) {
  return ((x << c) | (x >>> (32 - c))) >>> 0;
}

function md5(initial_msg) {
  h0 = 0x67452301;
  h1 = 0xefcdab89;
  h2 = 0x98badcfe;
  h3 = 0x10325476;

  for (var i = 0; i < msg_buff.length; i++) {
    msg_buff[i] = 0;
  }
  for (var i = 0; i < MSG_SIZE; i++) {
    msg_buff[i] = initial_msg[i];
  }
  msg_buff[MSG_SIZE] = 128;

  var bits_len = (8 * MSG_SIZE) >>> 0;
  msg_buff[MSG_SIZE_PADDED] = bits_len & 0xff;
  msg_buff[MSG_SIZE_PADDED + 1] = (bits_len >>> 8) & 0xff;
  msg_buff[MSG_SIZE_PADDED + 2] = (bits_len >>> 16) & 0xff;
  msg_buff[MSG_SIZE_PADDED + 3] = (bits_len >>> 24) & 0xff;

  for (var offset = 0; offset < MSG_SIZE_PADDED; offset += 64) {
    var w = new Array(16);
    for (var j = 0; j < 16; j++) {
      var base = offset + j * 4;
      w[j] = (
        msg_buff[base] |
        (msg_buff[base + 1] << 8) |
        (msg_buff[base + 2] << 16) |
        (msg_buff[base + 3] << 24)
      ) >>> 0;
    }

    var a = h0;
    var b = h1;
    var c = h2;
    var d = h3;

    for (var i = 0; i < 64; i++) {
      var f;
      var g;
      if (i < 16) {
        f = ((b & c) | ((~b) & d)) >>> 0;
        g = i;
      } else if (i < 32) {
        f = ((d & b) | ((~d) & c)) >>> 0;
        g = (5 * i + 1) % 16;
      } else if (i < 48) {
        f = (b ^ c ^ d) >>> 0;
        g = (3 * i + 5) % 16;
      } else {
        f = (c ^ (b | (~d))) >>> 0;
        g = (7 * i) % 16;
      }

      var temp = d;
      d = c;
      c = b;
      b = (b + leftrotate((a + f + k[i] + w[g]) >>> 0, r[i])) >>> 0;
      a = temp;
    }

    h0 = (h0 + a) >>> 0;
    h1 = (h1 + b) >>> 0;
    h2 = (h2 + c) >>> 0;
    h3 = (h3 + d) >>> 0;
  }
}

function initialise_benchmark() {
}

function benchmark_body(lsf) {
  for (var lsf_cnt = 0; lsf_cnt < lsf; lsf_cnt++) {
    for (var i = 0; i < MSG_SIZE; i++) {
      starting_message[i] = i & 0xff;
    }
    md5(starting_message);
  }
  return (h0 ^ h1 ^ h2 ^ h3) >>> 0;
}

function verify_benchmark(r) {
  return r === RESULT;
}

function benchmark() {
  initialise_benchmark();
  var result = benchmark_body(SCALE_FACTOR);
  return verify_benchmark(result);
}

benchmark();
