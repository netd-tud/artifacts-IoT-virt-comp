var SCALE_FACTOR = 1;

function fillArray(arr, length, value) {
  for (var i = 0; i < length; i++) {
    arr[i] = value;
  }
  return arr;
}

var a = [];
var b = [];
var x = [];
for (var i = 0; i < 20; i++) {
  b[i] = 0;
  x[i] = 0;
  a[i] = [];
  fillArray(a[i], 20, 0);
}

var chkerr = 0;

function ludcmp(nmax, n) {
  var y = [];
  fillArray(y, 100, 0);

  for (var i = 0; i < n; i++) {
    for (var j = i + 1; j <= n; j++) {
      var w = a[j][i];
      if (i !== 0) {
        for (var k = 0; k < i; k++) {
          w = w - a[j][k] * a[k][i];
        }
      }
      a[j][i] = Math.floor(w / a[i][i]);
    }
    for (var j = i + 1; j <= n; j++) {
      var w = a[i + 1][j];
      for (var k = 0; k <= i; k++) {
        w = w - a[i + 1][k] * a[k][j];
      }
      a[i + 1][j] = w;
    }
  }

  y[0] = b[0];
  for (var i = 1; i <= n; i++) {
    var w = b[i];
    for (var j = 0; j < i; j++) {
      w = w - a[i][j] * y[j];
    }
    y[i] = w;
  }

  x[n] = Math.floor(y[n] / a[n][n]);
  for (var i = n - 1; i >= 0; i--) {
    var w = y[i];
    for (var j = i + 1; j <= n; j++) {
      w = w - a[i][j] * x[j];
    }
    x[i] = Math.floor(w / a[i][i]);
  }

  return 0;
}

function initialise_benchmark() {}

function benchmark_body(lsf) {
  for (var iter = 0; iter < lsf; iter++) {
    var nmax = 20;
    var n = 5;
    for (var i = 0; i <= n; i++) {
      var w = 0;
      for (var j = 0; j <= n; j++) {
        a[i][j] = (i + 1) + (j + 1);
        if (i === j) {
          a[i][j] = a[i][j] * 2;
        }
        w = w + a[i][j];
      }
      b[i] = w;
    }
    chkerr = ludcmp(nmax, n);
  }
  return chkerr;
}

function verify_benchmark(res) {
  var x_ref = [0,0,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
  if (res !== 0) {
    return false;
  }
  for (var i = 0; i < 20; i++) {
    if (x[i] !== x_ref[i]) {
      return false;
    }
  }
  return true;
}

function benchmark() {
  initialise_benchmark();
  var result = benchmark_body(SCALE_FACTOR);
  return verify_benchmark(result);
}

benchmark();
