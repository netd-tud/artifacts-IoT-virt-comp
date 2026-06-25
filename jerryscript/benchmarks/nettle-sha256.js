var SCALE_FACTOR = 1;
var SHA256_DIGEST_SIZE = 32;
var SHA256_BLOCK_SIZE = 64;
var SHA256_DATA_LENGTH = 16;
var _SHA256_DIGEST_LENGTH = 8;

var K = [
  0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b,
  0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01,
  0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7,
  0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
  0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152,
  0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
  0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
  0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
  0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819,
  0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08,
  0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f,
  0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
  0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
];

var msg = [97,98,99,100,98,99,100,101,99,100,101,102,100,101,102,103,101,102,103,104,102,103,104,105,103,104,105,106,104,105,106,107,105,106,107,108,106,107,108,109,107,108,109,110,108,109,110,111,109,110,111,112,110,111,112,113];

var hash = [
  0x24, 0x8d, 0x6a, 0x61, 0xd2, 0x06, 0x38, 0xb8,
  0xe5, 0xc0, 0x26, 0x93, 0x0c, 0x3e, 0x60, 0x39,
  0xa3, 0x3c, 0xe4, 0x59, 0x64, 0xff, 0x21, 0x67,
  0xf6, 0xec, 0xed, 0xd4, 0x19, 0xdb, 0x06, 0xc1
];

var buffer = new Array(SHA256_DIGEST_SIZE);

function rotl32(n, x) {
  return ((x << n) | (x >>> ((-n) & 31))) >>> 0;
}

function Choice(x, y, z) {
  return (z ^ (x & (y ^ z))) >>> 0;
}

function Majority(x, y, z) {
  return ((x & y) ^ (z & (x ^ y))) >>> 0;
}

function S0(x) {
  return (rotl32(30, x) ^ rotl32(19, x) ^ rotl32(10, x)) >>> 0;
}

function S1(x) {
  return (rotl32(26, x) ^ rotl32(21, x) ^ rotl32(7, x)) >>> 0;
}

function s0(x) {
  return (rotl32(25, x) ^ rotl32(14, x) ^ (x >>> 3)) >>> 0;
}

function s1(x) {
  return (rotl32(15, x) ^ rotl32(13, x) ^ (x >>> 10)) >>> 0;
}

function write_uint64(dst, offset, src) {
  var x = BigInt(src);
  dst[offset] = Number((x >> 56n) & 0xffn);
  dst[offset + 1] = Number((x >> 48n) & 0xffn);
  dst[offset + 2] = Number((x >> 40n) & 0xffn);
  dst[offset + 3] = Number((x >> 32n) & 0xffn);
  dst[offset + 4] = Number((x >> 24n) & 0xffn);
  dst[offset + 5] = Number((x >> 16n) & 0xffn);
  dst[offset + 6] = Number((x >> 8n) & 0xffn);
  dst[offset + 7] = Number(x & 0xffn);
}

function write_uint32(dst, offset, src) {
  dst[offset] = (src >>> 24) & 0xff;
  dst[offset + 1] = (src >>> 16) & 0xff;
  dst[offset + 2] = (src >>> 8) & 0xff;
  dst[offset + 3] = src & 0xff;
}

function read_uint32(src, offset) {
  return (((src[offset] << 24) | (src[offset + 1] << 16) | (src[offset + 2] << 8) | src[offset + 3]) >>> 0);
}

function _nettle_write_be32(length, dst, src) {
  var words = Math.floor(length / 4);
  var leftover = length % 4;
  var i = 0;

  for (i = 0; i < words; i++) {
    write_uint32(dst, i * 4, src[i]);
  }

  if (leftover) {
    var word = src[i];
    var j = leftover;
    if (leftover >= 3) {
      dst[i * 4 + (--j)] = (word >>> 8) & 0xff;
    }
    if (leftover >= 2) {
      dst[i * 4 + (--j)] = (word >>> 16) & 0xff;
    }
    if (leftover >= 1) {
      dst[i * 4 + (--j)] = (word >>> 24) & 0xff;
    }
  }
}

function _nettle_sha256_compress(state, input, inputOffset) {
  var data = new Array(SHA256_DATA_LENGTH);
  for (var i = 0; i < SHA256_DATA_LENGTH; i++) {
    data[i] = read_uint32(input, inputOffset + i * 4);
  }

  var A = state[0];
  var B = state[1];
  var C = state[2];
  var D = state[3];
  var E = state[4];
  var F = state[5];
  var G = state[6];
  var H = state[7];

  for (var i = 0; i < 64; i++) {
    var w;
    if (i < 16) {
      w = data[i];
    } else {
      var idx = i & 15;
      data[idx] = (data[idx] + s1(data[(i - 2) & 15]) + data[(i - 7) & 15] + s0(data[(i - 15) & 15])) >>> 0;
      w = data[idx];
    }

    var temp1 = (H + S1(E) + Choice(E, F, G) + K[i] + w) >>> 0;
    var temp2 = (S0(A) + Majority(A, B, C)) >>> 0;

    H = G;
    G = F;
    F = E;
    E = (D + temp1) >>> 0;
    D = C;
    C = B;
    B = A;
    A = (temp1 + temp2) >>> 0;
  }

  state[0] = (state[0] + A) >>> 0;
  state[1] = (state[1] + B) >>> 0;
  state[2] = (state[2] + C) >>> 0;
  state[3] = (state[3] + D) >>> 0;
  state[4] = (state[4] + E) >>> 0;
  state[5] = (state[5] + F) >>> 0;
  state[6] = (state[6] + G) >>> 0;
  state[7] = (state[7] + H) >>> 0;
}

function sha256_init(ctx) {
  var H0 = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19];
  for (var i = 0; i < 8; i++) {
    ctx.state[i] = H0[i];
  }
  ctx.count = 0;
  ctx.index = 0;
}

function sha256_update(ctx, length, data) {
  var offset = 0;
  if (ctx.index) {
    var left = SHA256_BLOCK_SIZE - ctx.index;
    if (length < left) {
      for (var i = 0; i < length; i++) {
        ctx.block[ctx.index + i] = data[offset + i];
      }
      ctx.index += length;
      return;
    }

    for (var i = 0; i < left; i++) {
      ctx.block[ctx.index + i] = data[offset + i];
    }
    _nettle_sha256_compress(ctx.state, ctx.block, 0);
    ctx.count++;

    offset += left;
    length -= left;
    ctx.index = 0;
  }

  while (length >= SHA256_BLOCK_SIZE) {
    _nettle_sha256_compress(ctx.state, data, offset);
    ctx.count++;
    offset += SHA256_BLOCK_SIZE;
    length -= SHA256_BLOCK_SIZE;
  }

  for (var i = 0; i < length; i++) {
    ctx.block[i] = data[offset + i];
  }
  ctx.index = length;
}

function sha256_write_digest(ctx, length, digest) {
  var i = ctx.index;
  ctx.block[i++] = 0x80;

  if (i > SHA256_BLOCK_SIZE - 8) {
    while (i < SHA256_BLOCK_SIZE) {
      ctx.block[i++] = 0;
    }
    _nettle_sha256_compress(ctx.state, ctx.block, 0);
    i = 0;
  }

  while (i < SHA256_BLOCK_SIZE - 8) {
    ctx.block[i++] = 0;
  }

  var bit_count = (BigInt(ctx.count) << 9n) | (BigInt(ctx.index) << 3n);
  write_uint64(ctx.block, SHA256_BLOCK_SIZE - 8, bit_count);
  _nettle_sha256_compress(ctx.state, ctx.block, 0);

  _nettle_write_be32(length, digest, ctx.state);
}

function sha256_digest(ctx, length, digest) {
  sha256_write_digest(ctx, length, digest);
  sha256_init(ctx);
}

var nettle_sha256 = {
  digest_size: SHA256_DIGEST_SIZE,
  init: sha256_init,
  update: sha256_update,
  digest: sha256_digest
};

function initialise_benchmark() {
}

function verify_benchmark(_) {
  var correct = true;
  for (var i = 0; i < _SHA256_DIGEST_LENGTH; i++) {
    if (hash[i] !== buffer[i]) {
      correct = false;
    }
  }
  return correct;
}

function benchmark_body(lsf) {
  for (var lsf_cnt = 0; lsf_cnt < lsf; lsf_cnt++) {
    buffer.fill(0);
    var ctx = {
      state: new Array(8),
      count: 0,
      block: new Array(SHA256_BLOCK_SIZE),
      index: 0
    };
    nettle_sha256.init(ctx);
    nettle_sha256.update(ctx, msg.length, msg);
    nettle_sha256.digest(ctx, nettle_sha256.digest_size, buffer);
  }
  return 0;
}

function benchmark() {
  initialise_benchmark();
  var result = benchmark_body(SCALE_FACTOR);
  return verify_benchmark(result);
}

benchmark();
