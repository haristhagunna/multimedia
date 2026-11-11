/* Multimedia and Application - interactive simulators
   Copyright (c) 2026 Er. Harish Thagunna. All rights reserved. */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  function el(tag, attrs, html) { var e = document.createElement(tag); for (var k in (attrs || {})) e.setAttribute(k, attrs[k]); if (html != null) e.innerHTML = html; return e; }
  function sv(tag, attrs) { var e = document.createElementNS(NS, tag); for (var k in (attrs || {})) e.setAttribute(k, attrs[k]); return e; }
  function slider(parent, label, min, max, val, step, fmt, cb) {
    var w = el("label", { "class": "sim-ctl" }), out = el("b"), inp = el("input", { type: "range", min: min, max: max, value: val, step: step || 1 });
    function upd() { out.textContent = fmt ? fmt(+inp.value) : inp.value; }
    inp.oninput = function () { upd(); cb(+inp.value); }; upd();
    w.appendChild(el("span", null, label)); w.appendChild(inp); w.appendChild(out); parent.appendChild(w); return inp;
  }
  function svgBox(w, h) { var s = sv("svg", { viewBox: "0 0 " + w + " " + h, "class": "sim-svg", role: "img" }); return s; }
  function line(s, x1, y1, x2, y2, c, w, dash) { var l = sv("line", { x1: x1, y1: y1, x2: x2, y2: y2, stroke: c, "stroke-width": w || 1 }); if (dash) l.setAttribute("stroke-dasharray", dash); s.appendChild(l); return l; }
  function text(s, x, y, t, c, size, anchor) { var e = sv("text", { x: x, y: y, fill: c || "currentColor", "font-size": size || 12, "text-anchor": anchor || "start", "font-family": "inherit" }); e.textContent = t; s.appendChild(e); return e; }
  function rect(s, x, y, w, h, fill, stroke) { var r = sv("rect", { x: x, y: y, width: w, height: h, fill: fill, stroke: stroke || "none" }); s.appendChild(r); return r; }
  function fmtBytes(b) { if (b >= 1e9) return (b / 1e9).toFixed(2) + " GB"; if (b >= 1e6) return (b / 1e6).toFixed(2) + " MB"; if (b >= 1e3) return (b / 1e3).toFixed(1) + " KB"; return Math.round(b) + " B"; }
  var COL = ["#818cf8", "#f472b6", "#34d399", "#fbbf24", "#22d3ee"];

  /* ---------- 1. sampling & quantization ---------- */
  function sampling(root) {
    var st = { f: 3, fs: 16, bits: 3 }, ctl = el("div", { "class": "sim-controls" }), out = el("div", { "class": "sim-out" }), box = el("div");
    function draw() {
      var W = 640, H = 260, s = svgBox(W, H), levels = Math.pow(2, st.bits);
      line(s, 0, H / 2, W, H / 2, "#4b5190", 1);
      var pts = []; for (var i = 0; i <= 600; i++) { var t = i / 600; pts.push((t * W).toFixed(1) + "," + (H / 2 - Math.sin(2 * Math.PI * st.f * t) * 100).toFixed(1)); }
      s.appendChild(sv("polyline", { points: pts.join(" "), fill: "none", stroke: "#818cf8", "stroke-width": 2 }));
      var n = Math.floor(st.fs), q = [];
      var hold = "";
      for (var k = 0; k < n; k++) {
        var tk = k / st.fs, v = Math.sin(2 * Math.PI * st.f * tk), qv = Math.round((v + 1) / 2 * (levels - 1)) / (levels - 1) * 2 - 1;
        var x = tk * W, y = H / 2 - v * 100, yq = H / 2 - qv * 100;
        line(s, x, H / 2, x, y, "#f472b6", 1.2); var c = sv("circle", { cx: x, cy: y, r: 4, fill: "#f472b6" }); s.appendChild(c);
        hold += (hold ? " " : "") + x.toFixed(1) + "," + yq.toFixed(1) + " " + Math.min(W, (tk + 1 / st.fs) * W).toFixed(1) + "," + yq.toFixed(1);
      }
      s.appendChild(sv("polyline", { points: hold, fill: "none", stroke: "#fbbf24", "stroke-width": 2 }));
      box.innerHTML = ""; box.appendChild(s);
      var ok = st.fs >= 2 * st.f, alias = Math.abs(st.f - Math.round(st.f / st.fs) * st.fs);
      out.innerHTML = "<p><b>Nyquist check:</b> fs = " + st.fs + " Hz, 2·f = " + 2 * st.f + " Hz → " + (ok ? "<span class='ok'>fs ≥ 2f: the tone can be reconstructed.</span>" : "<span class='bad'>fs &lt; 2f: aliasing! It will look like a " + alias + " Hz tone.</span>") +
        "</p><p><b>Quantization:</b> " + st.bits + " bits → " + levels + " levels (yellow staircase). Step size = 2/" + (levels - 1) + " ≈ " + (2 / (levels - 1)).toFixed(3) + " of full scale.</p><p><b>Data rate:</b> " + st.fs + " × " + st.bits + " = " + st.fs * st.bits + " bit/s per channel.</p>";
    }
    slider(ctl, "Signal frequency f (Hz)", 1, 10, st.f, 1, null, function (v) { st.f = v; draw(); });
    slider(ctl, "Sampling rate fs (Hz)", 2, 40, st.fs, 1, null, function (v) { st.fs = v; draw(); });
    slider(ctl, "Bits per sample", 1, 8, st.bits, 1, null, function (v) { st.bits = v; draw(); });
    root.appendChild(ctl); root.appendChild(box); root.appendChild(out); draw();
  }

  /* ---------- 2. Huffman builder ---------- */
  function huffman(root) {
    var inp = el("input", { type: "text", value: "AAAAABCCCCCCDDD", "class": "sim-text", "aria-label": "Text to encode", maxlength: 60 });
    var ctl = el("div", { "class": "sim-controls" }); ctl.appendChild(el("span", null, "Text (up to 60 characters)")); ctl.appendChild(inp);
    var out = el("div", { "class": "sim-out" }), box = el("div");
    function build() {
      var txt = inp.value, freq = {}; for (var i = 0; i < txt.length; i++) freq[txt[i]] = (freq[txt[i]] || 0) + 1;
      var nodes = Object.keys(freq).map(function (c) { return { c: c, f: freq[c], l: null, r: null }; });
      if (!nodes.length) { out.innerHTML = "<p>Type some text.</p>"; box.innerHTML = ""; return; }
      var steps = [];
      while (nodes.length > 1) { nodes.sort(function (a, b) { return a.f - b.f || (a.c || "~").localeCompare(b.c || "~"); }); var a = nodes.shift(), b = nodes.shift(); steps.push(label(a) + "(" + a.f + ") + " + label(b) + "(" + b.f + ") → " + (a.f + b.f)); nodes.push({ c: null, f: a.f + b.f, l: a, r: b }); }
      var root0 = nodes[0], codes = {};
      (function walk(n, p) { if (!n.l) { codes[n.c] = p || "0"; return; } walk(n.l, p + "0"); walk(n.r, p + "1"); })(root0, "");
      var bits = 0; Object.keys(freq).forEach(function (c) { bits += freq[c] * codes[c].length; });
      var raw = txt.length * 8;
      var rows = Object.keys(freq).sort(function (a, b) { return freq[b] - freq[a]; }).map(function (c) { return "<tr><td>" + (c === " " ? "␣" : c) + "</td><td>" + freq[c] + "</td><td><code>" + codes[c] + "</code></td><td>" + freq[c] * codes[c].length + "</td></tr>"; }).join("");
      out.innerHTML = "<table><tr><th>Symbol</th><th>Freq</th><th>Code</th><th>Bits</th></tr>" + rows + "</table><p><b>Merge steps:</b> " + steps.join("; ") + "</p><p><b>Total:</b> " + bits + " bits vs " + raw + " bits at 8 bits/char → ratio <b>" + (raw / bits).toFixed(2) + " : 1</b> (tree itself not counted).</p>";
      // layout
      var leaves = 0; (function cnt(n) { if (!n.l) { n.x = leaves++; } else { cnt(n.l); cnt(n.r); n.x = (n.l.x + n.r.x) / 2; } })(root0);
      var depth = 0; (function dep(n, d) { n.d = d; depth = Math.max(depth, d); if (n.l) { dep(n.l, d + 1); dep(n.r, d + 1); } })(root0, 0);
      var W = Math.max(320, leaves * 80), H = 70 + depth * 70, s = svgBox(W, H);
      (function drawN(n) {
        var x = 40 + n.x * ((W - 80) / Math.max(1, leaves - 1 || 1)), y = 30 + n.d * 65; n.px = x; n.py = y;
        if (n.l) { drawN(n.l); drawN(n.r); [n.l, n.r].forEach(function (ch, k) { line(s, x, y, ch.px, ch.py, "#9aa0cc", 1.4); text(s, (x + ch.px) / 2 + (k ? 6 : -6), (y + ch.py) / 2, String(k), "#fbbf24", 12, k ? "start" : "end"); }); }
      })(root0);
      (function drawBoxes(n) { var g = sv("g"); var r = sv("rect", { x: n.px - 24, y: n.py - 15, width: 48, height: 30, rx: 8, fill: n.l ? "#27306b" : "#14364a", stroke: n.l ? "#818cf8" : "#22d3ee" }); g.appendChild(r); s.appendChild(g); text(s, n.px, n.py + 4, (n.l ? "" : (n.c === " " ? "␣" : n.c) + ":") + n.f, "#fff", 12, "middle"); if (n.l) { drawBoxes(n.l); drawBoxes(n.r); } })(root0);
      box.innerHTML = ""; box.appendChild(s);
    }
    function label(n) { return n.c || "node"; }
    inp.oninput = build; root.appendChild(ctl); root.appendChild(box); root.appendChild(out); build();
  }

  /* ---------- 3. EDF / RM scheduler ---------- */
  function scheduler(root) {
    var tasks = [{ c: 2, p: 5 }, { c: 4, p: 7 }], pol = "RM", ctl = el("div", { "class": "sim-controls" }), tbl = el("div", { "class": "sim-tasks" }), out = el("div", { "class": "sim-out" }), box = el("div");
    function gcd(a, b) { return b ? gcd(b, a % b) : a; }
    function run() {
      var T = tasks.filter(function (t) { return t.c > 0 && t.p > 0; }); if (!T.length) { out.innerHTML = "<p>Add at least one task.</p>"; box.innerHTML = ""; return; }
      var L = T.reduce(function (a, t) { return a * t.p / gcd(a, t.p); }, 1), H = Math.min(L, 60), rem = T.map(function () { return 0; }), dl = T.map(function () { return 0; }), slots = [], miss = [];
      for (var t = 0; t < H; t++) {
        T.forEach(function (tk, i) { if (t % tk.p === 0) { if (rem[i] > 0) miss.push([i, t]); rem[i] = tk.c; dl[i] = t + tk.p; } });
        var best = -1; T.forEach(function (tk, i) { if (rem[i] > 0) { if (best < 0) best = i; else if (pol === "EDF" ? dl[i] < dl[best] : tk.p < T[best].p) best = i; } });
        slots.push(best); if (best >= 0) rem[best]--;
        T.forEach(function (tk, i) { if (rem[i] > 0 && dl[i] === t + 1) { miss.push([i, t + 1]); rem[i] = 0; } });
      }
      var cw = Math.max(10, Math.min(28, 700 / H)), W = 70 + H * cw, h = 40 + T.length * 34, s = svgBox(W, h);
      T.forEach(function (tk, i) {
        text(s, 4, 28 + i * 34, "T" + (i + 1), COL[i % 5], 13);
        for (var r = 0; r <= H; r += tk.p) line(s, 60 + r * cw, 10 + i * 34, 60 + r * cw, 36 + i * 34, COL[i % 5], 1, "2 3");
      });
      slots.forEach(function (i, t) { if (i >= 0) rect(s, 60 + t * cw, 14 + i * 34, cw - 1, 18, COL[i % 5], "#0b0d1c"); });
      miss.forEach(function (m) { var x = 60 + m[1] * cw; line(s, x, 6 + m[0] * 34, x, 40 + m[0] * 34, "#f87171", 2); text(s, x, 8 + m[0] * 34, "✕", "#f87171", 12, "middle"); });
      for (var k = 0; k <= H; k += (H > 30 ? 5 : 1)) text(s, 60 + k * cw, h - 4, String(k), "#9aa0cc", 10, "middle");
      box.innerHTML = ""; box.appendChild(s);
      var U = T.reduce(function (a, tk) { return a + tk.c / tk.p; }, 0), n = T.length, rm = n * (Math.pow(2, 1 / n) - 1);
      out.innerHTML = "<p><b>Utilisation U</b> = " + T.map(function (tk) { return tk.c + "/" + tk.p; }).join(" + ") + " = <b>" + U.toFixed(3) + "</b></p><p><b>EDF:</b> " + (U <= 1 ? "schedulable (U ≤ 1)" : "<span class='bad'>not schedulable (U > 1)</span>") + " &nbsp; <b>RM bound</b> n(2<sup>1/n</sup>−1) = " + rm.toFixed(3) + " → " + (U <= rm ? "<span class='ok'>guaranteed by the bound</span>" : "bound not met (a set may still pass an exact test)") + "</p><p><b>Simulation (" + pol + ", " + H + " time units):</b> " + (miss.length ? "<span class='bad'>" + miss.length + " deadline miss(es) marked ✕</span>" : "<span class='ok'>no deadline missed</span>") + "</p>";
    }
    function renderTasks() {
      tbl.innerHTML = "";
      tasks.forEach(function (tk, i) {
        var row = el("div", { "class": "sim-row" }); row.appendChild(el("b", { style: "color:" + COL[i % 5] }, "T" + (i + 1)));
        ["c", "p"].forEach(function (k) { var l = el("label", null, k === "c" ? "C " : "P "), inp = el("input", { type: "number", min: 1, max: 30, value: tk[k] }); inp.oninput = function () { tk[k] = Math.max(1, Math.min(30, +inp.value || 1)); run(); }; l.appendChild(inp); row.appendChild(l); });
        var rm = el("button", { "class": "btn-s", type: "button" }, "×"); rm.onclick = function () { tasks.splice(i, 1); renderTasks(); run(); }; row.appendChild(rm); tbl.appendChild(row);
      });
    }
    var sel = el("select", { "class": "sim-text" }, "<option value='RM'>Rate Monotonic (RM)</option><option value='EDF'>Earliest Deadline First (EDF)</option>"); sel.onchange = function () { pol = sel.value; run(); };
    var add = el("button", { "class": "btn-s primary", type: "button" }, "+ Add task"); add.onclick = function () { if (tasks.length < 5) { tasks.push({ c: 1, p: 6 }); renderTasks(); run(); } };
    var ex = el("button", { "class": "btn-s", type: "button" }, "Load example (RM misses, EDF meets)"); ex.onclick = function () { tasks = [{ c: 2, p: 5 }, { c: 4, p: 7 }]; renderTasks(); run(); };
    ctl.appendChild(sel); ctl.appendChild(add); ctl.appendChild(ex); root.appendChild(ctl); root.appendChild(tbl); root.appendChild(box); root.appendChild(out); renderTasks(); run();
  }

  /* ---------- 4. token bucket ---------- */
  function bucket(root) {
    var st = { b: 4, r: 1.2, seed: 7 }, ctl = el("div", { "class": "sim-controls" }), out = el("div", { "class": "sim-out" }), box = el("div");
    function rnd() { st.seed = (st.seed * 16807) % 2147483647; return st.seed / 2147483647; }
    var ev = [];
    function gen() { ev = []; var t = 0; for (var i = 0; i < 8; i++) { t += rnd() * 2.2; ev.push([t, 1 + Math.floor(rnd() * 4)]); } }
    function draw() {
      var W = 640, H = 280, s = svgBox(W, H), T = 12, mx = 24, X = function (t) { return 40 + t / T * (W - 60); }, Y = function (v) { return H - 30 - v / mx * (H - 50); };
      line(s, 40, H - 30, W - 20, H - 30, "#9aa0cc", 1); line(s, 40, 10, 40, H - 30, "#9aa0cc", 1);
      line(s, X(0), Y(st.b), X(T), Y(st.b + st.r * T), "#34d399", 2.4); text(s, X(T) - 4, Y(st.b + st.r * T) - 6, "b + r·t", "#34d399", 12, "end");
      var cum = 0, pts = "0," + Y(0), viol = 0, px = X(0), py = Y(0), pts2 = [[X(0), Y(0)]];
      ev.forEach(function (e) { pts2.push([X(e[0]), Y(cum)]); cum += e[1]; pts2.push([X(e[0]), Y(cum)]); if (cum > st.b + st.r * e[0] + 1e-9) viol++; });
      pts2.push([X(T), Y(cum)]); s.appendChild(sv("polyline", { points: pts2.map(function (p) { return p.join(","); }).join(" "), fill: "none", stroke: "#f472b6", "stroke-width": 2.4 }));
      text(s, 46, 24, "cumulative data sent (pink) vs allowed (green)", "#9aa0cc", 11); text(s, W - 20, H - 12, "time", "#9aa0cc", 11, "end");
      box.innerHTML = ""; box.appendChild(s);
      out.innerHTML = "<p>The flow is <b>conforming</b> if the pink line never rises above the green line. Here: " + (viol ? "<span class='bad'>" + viol + " burst(s) exceed the profile and would be delayed or dropped.</span>" : "<span class='ok'>all bursts conform.</span>") + "</p><p>Bucket depth <b>b = " + st.b + "</b> allows a burst; token rate <b>r = " + st.r.toFixed(1) + "</b> limits the long-term average.</p>";
    }
    slider(ctl, "Bucket depth b", 1, 12, st.b, 1, null, function (v) { st.b = v; draw(); });
    slider(ctl, "Token rate r", .2, 3, st.r, .1, function (v) { return v.toFixed(1); }, function (v) { st.r = v; draw(); });
    var nb = el("button", { "class": "btn-s primary", type: "button" }, "New random traffic"); nb.onclick = function () { st.seed = Math.floor(Math.random() * 1e6) + 1; gen(); draw(); };
    ctl.appendChild(nb); root.appendChild(ctl); root.appendChild(box); root.appendChild(out); gen(); draw();
  }

  /* ---------- 5. DCT + quantization ---------- */
  function dct(root) {
    var Q = [[16, 11, 10, 16, 24, 40, 51, 61], [12, 12, 14, 19, 26, 58, 60, 55], [14, 13, 16, 24, 40, 57, 69, 56], [14, 17, 22, 29, 51, 87, 80, 62], [18, 22, 37, 56, 68, 109, 103, 77], [24, 35, 55, 64, 81, 104, 113, 92], [49, 64, 78, 87, 103, 121, 120, 101], [72, 92, 95, 98, 112, 100, 103, 99]];
    var blk = []; for (var y = 0; y < 8; y++) { blk[y] = []; for (var x = 0; x < 8; x++) blk[y][x] = Math.max(0, Math.min(255, Math.round(128 + 50 * Math.sin(x / 7 * 1.6) + 30 * (y / 7) + 6 * ((x + y) % 2) + (x > 4 && y < 3 ? 40 : 0)))); }
    var C = []; for (var k = 0; k < 8; k++) { C[k] = []; for (var n = 0; n < 8; n++) C[k][n] = (k ? Math.sqrt(2 / 8) : Math.sqrt(1 / 8)) * Math.cos((2 * n + 1) * k * Math.PI / 16); }
    function mul(A, B) { var R = []; for (var i = 0; i < 8; i++) { R[i] = []; for (var j = 0; j < 8; j++) { var s = 0; for (var k = 0; k < 8; k++) s += A[i][k] * B[k][j]; R[i][j] = s; } } return R; }
    function tr(A) { var R = []; for (var i = 0; i < 8; i++) { R[i] = []; for (var j = 0; j < 8; j++) R[i][j] = A[j][i]; } return R; }
    var shifted = blk.map(function (r) { return r.map(function (v) { return v - 128; }); }), D = mul(mul(C, shifted), tr(C));
    var ctl = el("div", { "class": "sim-controls" }), box = el("div", { "class": "sim-grid3" }), out = el("div", { "class": "sim-out" });
    function canv(data, scale, lab) { var w = el("figure", { "class": "sim-fig" }), c = el("canvas", { width: 8, height: 8, style: "width:" + 8 * scale + "px;height:" + 8 * scale + "px;image-rendering:pixelated" }), g = c.getContext("2d"), im = g.createImageData(8, 8); for (var i = 0; i < 8; i++) for (var j = 0; j < 8; j++) { var v = Math.max(0, Math.min(255, data[i][j])); var p = (i * 8 + j) * 4; im.data[p] = im.data[p + 1] = im.data[p + 2] = v; im.data[p + 3] = 255; } g.putImageData(im, 0, 0); w.appendChild(c); w.appendChild(el("figcaption", null, lab)); return w; }
    function run(q) {
      var scale = q < 50 ? 5000 / q : 200 - 2 * q; scale = Math.max(1, scale) / 100;
      var Qs = Q.map(function (r) { return r.map(function (v) { return Math.max(1, Math.round(v * scale)); }); });
      var qd = D.map(function (r, i) { return r.map(function (v, j) { return Math.round(v / Qs[i][j]); }); }), nz = 0; qd.forEach(function (r) { r.forEach(function (v) { if (v) nz++; }); });
      var deq = qd.map(function (r, i) { return r.map(function (v, j) { return v * Qs[i][j]; }); }), rec = mul(mul(tr(C), deq), C).map(function (r) { return r.map(function (v) { return Math.round(v + 128); }); });
      var err = 0; for (var i = 0; i < 8; i++) for (var j = 0; j < 8; j++) err += Math.pow(rec[i][j] - blk[i][j], 2); var mse = err / 64, psnr = mse ? 10 * Math.log10(255 * 255 / mse) : 99;
      box.innerHTML = ""; box.appendChild(canv(blk, 14, "Original 8×8 block")); box.appendChild(canv(D.map(function (r) { return r.map(function (v) { return Math.abs(v) * 2; }); }), 14, "DCT magnitudes (bright = large)")); box.appendChild(canv(rec, 14, "Reconstructed after quantization"));
      out.innerHTML = "<p><b>Quality " + q + ":</b> " + nz + " of 64 coefficients are non-zero. Mean squared error = " + mse.toFixed(1) + ", PSNR ≈ " + psnr.toFixed(1) + " dB.</p><p>Lower quality → larger quantization steps → more zeros (smaller file) but a worse reconstruction.</p>";
    }
    slider(ctl, "JPEG quality", 5, 95, 50, 1, null, run); root.appendChild(ctl); root.appendChild(box); root.appendChild(out); run(50);
  }

  /* ---------- 6. size calculator ---------- */
  function calc(root) {
    var tabs = el("div", { "class": "sim-controls" }), form = el("div", { "class": "sim-controls" }), out = el("div", { "class": "sim-out" }), mode = "audio";
    var defs = { audio: [["Sampling rate (Hz)", 44100], ["Bits per sample", 16], ["Channels", 2], ["Duration (s)", 60]], image: [["Width (px)", 640], ["Height (px)", 480], ["Bits per pixel", 24]], video: [["Width (px)", 640], ["Height (px)", 480], ["Bits per pixel", 24], ["Frames per second", 25], ["Duration (s)", 60]] };
    function paint() {
      form.innerHTML = ""; var inputs = [];
      defs[mode].forEach(function (d, i) { var l = el("label", { "class": "sim-ctl" }), inp = el("input", { type: "number", min: 1, value: d[1], "class": "sim-text" }); inp.oninput = calc2; l.appendChild(el("span", null, d[0])); l.appendChild(inp); form.appendChild(l); inputs.push(inp); });
      function calc2() {
        var v = inputs.map(function (i) { return Math.max(0, +i.value || 0); }), bytes, rate, f;
        if (mode === "audio") { bytes = v[0] * v[1] / 8 * v[2] * v[3]; rate = v[0] * v[1] * v[2]; f = "S = R × (b/8) × C × D = " + v[0] + " × " + v[1] + "/8 × " + v[2] + " × " + v[3]; }
        else if (mode === "image") { bytes = v[0] * v[1] * v[2] / 8; f = "size = width × height × bpp / 8 = " + v[0] + " × " + v[1] + " × " + v[2] + " / 8"; }
        else { var fr = v[0] * v[1] * v[2] / 8; bytes = fr * v[3] * v[4]; rate = fr * v[3] * 8; f = "frame = " + fmtBytes(fr) + "; size = frame × fps × duration"; }
        out.innerHTML = "<p><code>" + f + "</code></p><p><b>Size:</b> " + bytes.toLocaleString() + " bytes = <b>" + fmtBytes(bytes) + "</b></p>" + (rate ? "<p><b>Data rate:</b> " + (rate / 1e6).toLocaleString(undefined, { maximumFractionDigits: 3 }) + " Mbit/s</p>" : "") + "<p>Time to send at 1 Mbit/s: " + (bytes * 8 / 1e6).toFixed(1) + " s (no overhead).</p>";
      }
      calc2();
    }
    ["audio", "image", "video"].forEach(function (m) { var b = el("button", { "class": "btn-s" + (m === mode ? " primary" : ""), type: "button" }, m[0].toUpperCase() + m.slice(1)); b.onclick = function () { mode = m; [].forEach.call(tabs.children, function (c) { c.classList.remove("primary"); }); b.classList.add("primary"); paint(); }; tabs.appendChild(b); });
    root.appendChild(tabs); root.appendChild(form); root.appendChild(out); paint();
  }

  var REG = { sampling: sampling, huffman: huffman, scheduler: scheduler, bucket: bucket, dct: dct, calc: calc };
  function init() { document.querySelectorAll(".sim[data-sim]").forEach(function (r) { if (r.dataset.ready) return; r.dataset.ready = 1; try { REG[r.dataset.sim](r); } catch (e) { r.textContent = "Simulator failed to load: " + e.message; } }); }
  if (window.document$) window.document$.subscribe(init); else document.addEventListener("DOMContentLoaded", init);
})();
