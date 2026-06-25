var SCALE_FACTOR = 1;
var ARCHIVE_FILES = 35;
var N_SEARCHES = 5;

var seed = 0;

function rand_beebs() {
  seed = (Math.imul(seed, 1103515245) + 12345) & ((1 << 31) - 1);
  return seed >>> 16;
}

function initialise_benchmark() {
  seed = 0;
}

function benchmark_body(lsf) {
  var found = 0;
  for (var k = 0; k < lsf; k++) {
    var hdr = new Array(ARCHIVE_FILES);
    for (var i = 0; i < ARCHIVE_FILES; i++) {
        var c = {
            filename: [],
            mode: [],
            uID: [],
            gID: [],
            size: [0],
            mtime: [],
            checksum: [],
            isLink: "\0".charCodeAt(0),
            linkedFile: []
          };
      var flen = 5 + (i % 94);
      for (var p = 0; p < flen; p++) {
        c.filename[p] = (rand_beebs() % 26) + 65;
      }
      c.filename[flen] = 0;
      hdr[i] = c;
    }

    found = 0;
    for (var p = 0; p < N_SEARCHES; p++) {
      var idx = (p + Math.floor(ARCHIVE_FILES / 2)) % ARCHIVE_FILES;
      var search = hdr[idx].filename;
      for (var i = 0; i < ARCHIVE_FILES; i++) {
        var c1 = 0;
        var c2 = 0;
        while (
          hdr[i].filename[c1] !== undefined &&
          search[c2] !== undefined &&
          hdr[i].filename[c1] !== 0 &&
          search[c2] !== 0 &&
          hdr[i].filename[c1] === search[c2]
        ) {
          c1++;
          c2++;
        }
        var v1 = hdr[i].filename[c1] === undefined ? 0 : hdr[i].filename[c1];
        var v2 = search[c2] === undefined ? 0 : search[c2];
        if (v1 === 0 && v2 === 0) {
          found++;
          break;
        }
      }
    }
  }
  return found === N_SEARCHES ? 1 : 0;
}

function verify_benchmark(r) {
  return r === 1;
}

function benchmark() {
  initialise_benchmark();
  var result = benchmark_body(SCALE_FACTOR);
  return verify_benchmark(result);
}

benchmark();
