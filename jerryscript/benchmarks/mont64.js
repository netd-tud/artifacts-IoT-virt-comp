var SCALE_FACTOR = 1;
var MASK = (1n << 64n) - 1n;

var in_a = 0n;
var in_b = 0n;
var in_m = 0n;

function u64(x) {
  return x & MASK;
}

function mulul64(u, v) {
  var product = u64(u * v);
  var hi = u64((u * v) >> 64n);
  var lo = u64(product);
  return [hi, lo];
}

function modul64(x, y, z) {
  x = u64(x);
  y = u64(y);
  z = u64(z);
  for (var i = 0; i < 64; i++) {
    var t = ((x >> 63n) & 1n) ? MASK : 0n;
    x = u64((x << 1n) | (y >> 63n));
    y = u64(y << 1n);
    if ((x | t) >= z) {
      x = u64(x - z);
      y = u64(y + 1n);
    }
  }
  return x;
}

function montmul(abar, bbar, m, mprime) {
  var [thi, tlo] = mulul64(abar, bbar);
  var tm = u64(tlo * mprime);
  var [tmmhi, tmmlo] = mulul64(tm, m);

  var ulo = u64(tlo + tmmlo);
  var uhi = u64(thi + tmmhi);
  if (ulo < tlo) {
    uhi = u64(uhi + 1n);
  }

  var ov = (uhi < thi || (uhi === thi && ulo < tlo)) ? 1n : 0n;
  ulo = uhi;

  var condMask = (ov > 0n || ulo >= m) ? MASK : 0n;
  ulo = u64(ulo - (m & condMask));

  return ulo;
}

function xbinGCD(a, b) {
  var u = 1n;
  var v = 0n;
  var alpha = u64(a);
  var beta = u64(b);

  a = u64(a);
  while (a > 0n) {
    a >>= 1n;
    if ((u & 1n) === 0n) {
      u >>= 1n;
      v >>= 1n;
    } else {
      u = u64(((u ^ beta) >> 1n) + (u & beta));
      v = u64((v >> 1n) + alpha);
    }
  }

  return [u64(u), u64(v)];
}

function initialise_benchmark() {
  in_m = 0xfae849273928f89fn;
  in_b = 0x14736defb9330573n;
  in_a = 0x0549372187237fefn;
}

function benchmark_body(lsf) {
  var errors = 0;

  for (var lsf_cnt = 0; lsf_cnt < lsf; lsf_cnt++) {
    var m = in_m;
    var b = in_b;
    var a = in_a;
    var p1hi;
    var p1lo;
    var p1;
    var p;

    errors = 0;

    [p1hi, p1lo] = mulul64(a, b);
    p1 = modul64(p1hi, p1lo, m);
    [p1hi, p1lo] = mulul64(p1, p1);
    p1 = modul64(p1hi, p1lo, m);
    [p1hi, p1lo] = mulul64(p1, p1);
    p1 = modul64(p1hi, p1lo, m);

    var hr = 0x8000000000000000n;
    var [rinv, mprime] = xbinGCD(hr, m);

    if (u64(2n * hr * rinv - m * mprime) !== 1n) {
      errors = 1;
    }

    var abar = modul64(a, 0n, m);
    var bbar = modul64(b, 0n, m);

    p = montmul(abar, bbar, m, mprime);
    p = montmul(p, p, m, mprime);
    p = montmul(p, p, m, mprime);

    var phi;
    var plo;
    [phi, plo] = mulul64(p, rinv);
    p = modul64(phi, plo, m);

    if (p !== p1) {
      errors = 1;
    }
  }

  return errors;
}

function verify_benchmark(r) {
  return r === 0;
}

function benchmark() {
  initialise_benchmark();
  var result = benchmark_body(SCALE_FACTOR);
  return verify_benchmark(result);
}

benchmark();
