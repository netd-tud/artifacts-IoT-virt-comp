var SCALE_FACTOR = 1;
var TEST_SIZE = 500;
var compression_buff = new Array(TEST_SIZE + 1);

var orig_data = [74,50,79,90,70,53,48,70,89,76,68,53,85,84,86,89,89,82,77,84,48,86,88,79,48,49,86,67,53,70,78,73,66,49,67,71,49,50,77,84,73,80,84,50,67,73,86,48,48,66,79,85,87,70,68,82,65,89,84,65,51,65,73,52,50,75,70,88,72,82,75,80,65,51,76,67,71,65,51,65,66,76,85,89,81,88,74,82,81,50,82,78,50,90,77,89,69,82,80,76,67,48,48,67,88,70,69,51,71,66,51,72,77,83,53,51,74,73,79,90,69,53,72,66,89,84,90,50,69,74,72,71,68,66,73,48,72,77,89,78,79,86,85,48,72,85,88,82,50,70,75,66,69,82,67,51,69,49,90,73,69,66,79,72,67,87,67,74,68,48,87,82,80,76,76,88,53,68,73,49,73,83,50,78,69,52,75,73,48,68,82,52,69,53,71,72,87,73,81,90,67,72,75,82,83,86,73,82,89,81,77,66,68,74,79,72,72,89,80,66,49,65,65,65,65,71,72,87,79,88,80,81,52,90,66,81,79,75,66,72,48,79,73,51,88,87,69,52,79,85,65,74,85,65,74,85,71,81,75,85,73,90,69,71,83,70,88,66,80,89,73,75,71,81,72,51,71,77,50,85,65,50,51,85,50,72,74,67,88,84,87,53,78,48,71,53,53,51,65,80,86,73,90,50,89,65,90,52,77,86,83,77,82,81,66,78,88,75,80,79,51,70,79,75,53,85,75,53,82,75,79,71,84,72,67,76,72,50,75,85,82,50,65,68,77,66,81,68,76,65,83,74,70,65,84,70,85,51,69,70,73,83,76,49,90,79,71,65,75,81,85,49,78,86,52,90,87,80,51,67,80,80,76,85,80,52,90,68,50,51,73,69,80,84,53,73,66,70,74,76,87,51,72,68,83,70,50,74,85,90,76,68,73,87,89,88,85,82,48,81,80,67,85,52,87,84,72,88,90,81,68,80,78,75,83,65,80,79,74,69,73,85,72,81,75,53,73,52,82,67,80,65,70,68,52,49,88,70,83,81,86,86,53,68,53,82,68,80,53,77,84,72,65,48,89,75,48,65,73,76,67,88,76,72,49,74,67,83,80,86,67,69,75,66,72,75,83,75,90,82];

var test_data = new Array(TEST_SIZE);

function fillArray(arr, length, value) {
  for (var i = 0; i < length; i++) {
    arr[i] = value;
  }
  return arr;
}

function heap_adjust(freq, heap, n, k) {
  var v = heap[k - 1];
  while (k <= Math.floor(n / 2)) {
    var j = k + k;
    if (j < n && freq[heap[j - 1]] > freq[heap[j]]) {
      j++;
    }
    if (freq[v] < freq[heap[j - 1]]) {
      break;
    }
    heap[k - 1] = heap[j - 1];
    k = j;
  }
  heap[k - 1] = v;
}

function compdecomp(data, data_len) {
  var freq = new Array(512);
  var heap = new Array(256);
  var link = new Array(512);
  var code = new Array(256);
  var clen = new Array(256);
  var comp = compression_buff;

  fillArray(comp, data_len + 1, 0)
  fillArray(freq, 512, 0)
  fillArray(heap, 256, 0)
  fillArray(link, 512, 0)
  fillArray(code, 256, 0)
  fillArray(clen, 256, 0)

  var dptr = 0;
  for (var i = 0; i < data_len; i++) {
    freq[data[dptr]]++;
    dptr++;
  }

  var n = 0;
  for (var i = 0; i < 256; i++) {
    if (freq[i]) {
      heap[n] = i;
      n++;
    }
  }

  for (var i = n; i > 0; i--) {
    heap_adjust(freq, heap, n, i);
  }

  while (n > 1) {
    n--;
    var temp = heap[0];
    heap[0] = heap[n];
    heap_adjust(freq, heap, n, 1);

    freq[256 + n] = (freq[heap[0]] + freq[temp]) >>> 0;
    link[temp] = 256 + n;
    link[heap[0]] = -256 - n;
    heap[0] = 256 + n;

    heap_adjust(freq, heap, n, 1);
  }

  link[256 + n] = 0;

  var maxx = 0;
  var maxi = 0;
  for (var m = 0; m < 256; m++) {
    if (!freq[m]) {
      code[m] = 0;
      clen[m] = 0;
    } else {
      var i = 0;
      var j = 1;
      var x = 0;
      var l = link[m];

      while (l) {
        if (l < 0) {
          x += j;
          l = -l;
        }
        l = link[l];
        j <<= 1;
        i++;
      }

      code[m] = x >>> 0;
      clen[m] = i;
      if (x > maxx) {
        maxx = x;
      }
      if (i > maxi) {
        maxi = i;
      }
    }
  }

  if (maxi > 64) {
    return;
  }

  var comp_len = 0;
  var bout = 0;
  var bit = -1;
  dptr = 0;

  if (maxx === 0) {
    return;
  }

  for (var j = 0; j < data_len; j++) {
    var mask = 1 << (clen[data[dptr]] - 1);
    for (var i = 0; i < clen[data[dptr]]; i++) {
      if (bit === 7) {
        comp[comp_len] = bout;
        comp_len++;
        if (comp_len === data_len) {
          return;
        }
        bit = 0;
        bout = 0;
      } else {
        bit++;
        bout = (bout << 1) & 0xff;
      }

      if (code[data[dptr]] & mask) {
        bout |= 1;
      }
      mask >>= 1;
    }
    dptr++;
  }

  bout = (bout << (7 - bit)) & 0xff;
  comp[comp_len] = bout;
  comp_len++;

  var heap2 = new Array(256);
  var outc = new Array(256);

  fillArray(heap2, 257, 0)

  for (var j = 0; j < 256; j++) {
    outc[j] = j;
    if ((code[j] | clen[j]) !== 0) {
      var k = 0;
      var mask = 1 << (clen[j] - 1);
      for (var i = 0; i < clen[j]; i++) {
        k = k * 2 + 1;
        if (code[j] & mask) {
          k++;
        }
        mask >>= 1;
      }
      heap2[j] = k >>> 0;
    }
  }

  for (var i = 1; i < 256; i++) {
    var t = heap2[i];
    var c = outc[i];
    var j = i;
    while (j && heap2[j - 1] > t) {
      heap2[j] = heap2[j - 1];
      outc[j] = outc[j - 1];
      j--;
    }
    heap2[j] = t;
    outc[j] = c;
  }

  var j = 0;
  while (heap2[j] === 0) {
    j++;
  }

  var k = 0;
  var i = j;
  var mask = 0x80;
  n = 0;
  var cptr = 0;
  dptr = 0;

  while (n < data_len) {
    k = k * 2 + 1;
    if (comp[cptr] & mask) {
      k++;
    }

    while (heap2[i] < k) {
      i++;
    }

    if (k === heap2[i]) {
      data[dptr] = outc[i];
      dptr++;
      n++;
      k = 0;
      i = j;
    }

    if (mask > 1) {
      mask >>= 1;
    } else {
      mask = 0x80;
      cptr++;
    }
  }
}

function initialise_benchmark() {
}

function benchmark_body(lsf) {
  for (var lsf_cnt = 0; lsf_cnt < lsf; lsf_cnt++) {
    for (var i = 0; i < TEST_SIZE; i++) {
      test_data[i] = orig_data[i];
    }
    compdecomp(test_data, TEST_SIZE);
  }
  return 0;
}

function verify_benchmark(_) {
  for (var i = 0; i < TEST_SIZE; i++) {
    if (test_data[i] !== orig_data[i]) {
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
