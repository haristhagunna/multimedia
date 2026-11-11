/* Multimedia and Application - interactive features
   Copyright (c) 2026 Er. Harish Thagunna. All rights reserved. */
(function () {
  "use strict";
  var KEY = "mm:done", LAST = "mm:last", EXAM = "mm:exam", KNOWN = "mm:known";
  function get(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  var CHECK = '<svg viewBox="0 0 24 24"><path d="M21 7 9 19l-5.5-5.5 1.41-1.41L9 16.17 19.59 5.59 21 7Z"/></svg>';
  function done() { return get(KEY, []); }
  function unitDone(n) { return done().filter(function (k) { return k.split("/")[0] === String(n); }).length; }

  /* reading progress */
  function bar() {
    var b = document.getElementById("read-progress");
    if (!b) { b = document.createElement("div"); b.id = "read-progress"; document.body.appendChild(b); }
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    b.style.width = (max > 0 ? Math.min(100, h.scrollTop / max * 100) : 0) + "%";
  }
  window.addEventListener("scroll", bar, { passive: true });

  /* track button */
  function track() {
    document.querySelectorAll(".track-slot").forEach(function (slot) {
      if (slot.dataset.ready) return; slot.dataset.ready = 1;
      var key = slot.dataset.unit + "/" + slot.dataset.page;
      set(LAST, { url: location.pathname, title: document.title.replace(/ - .*$/, "") });
      var btn = document.createElement("button");
      btn.className = "track-btn";
      function paint() { var d = done().indexOf(key) > -1; btn.classList.toggle("done", d); btn.innerHTML = CHECK + (d ? "Completed" : "Mark page as complete"); }
      btn.onclick = function () {
        var a = done(), i = a.indexOf(key);
        if (i > -1) a.splice(i, 1); else a.push(key);
        set(KEY, a); paint(); nav(); unitBars();
      };
      paint(); slot.appendChild(btn);
    });
  }
  function nav() {
    var a = done();
    document.querySelectorAll(".md-nav__link").forEach(function (l) {
      var m = (l.getAttribute("href") || "").match(/unit-(\d+)\/([^\/#]+)\/?$/);
      if (!m) return;
      l.classList.toggle("is-done", a.indexOf(parseInt(m[1], 10) + "/" + m[2]) > -1);
    });
  }
  function unitBars() {
    document.querySelectorAll(".unit-progress").forEach(function (el) {
      var n = el.dataset.unit, total = parseInt(el.dataset.total || (window.__units && window.__units[n]) || 0, 10);
      var d = unitDone(n);
      var pct = total ? Math.min(100, Math.round(d / total * 100)) : 0;
      el.innerHTML = '<strong>Your progress: ' + d + (total ? ' / ' + total : '') + ' pages</strong><div class="bar"><span class="bar__fill" style="width:' + pct + '%"></span></div>';
    });
    document.querySelectorAll(".unit-card").forEach(function (c) {
      var n = c.dataset.unit, t = parseInt(c.dataset.pages, 10) || 1, p = Math.min(100, Math.round(unitDone(n) / t * 100));
      var f = c.querySelector(".bar__fill"); if (f) f.style.width = p + "%";
      var pc = c.querySelector(".unit-card__pct"); if (pc) pc.textContent = p + "%";
    });
    var ring = document.getElementById("overall-ring");
    if (ring) {
      var tot = 0; document.querySelectorAll(".unit-card").forEach(function (c) { tot += parseInt(c.dataset.pages, 10) || 0; });
      var d = done().length, p = tot ? Math.min(100, Math.round(d / tot * 100)) : 0;
      ring.querySelector(".ring__fg").style.strokeDashoffset = 327 - 327 * p / 100;
      document.getElementById("overall-pct").textContent = p + "%";
      document.getElementById("overall-text").textContent = d + " of " + tot + " pages completed.";
      var last = get(LAST, null), w = document.getElementById("resume-wrap");
      if (last && w) { var base = document.querySelector('link[rel="canonical"]'); w.hidden = false; var a = document.getElementById("resume-link"); a.href = last.url; a.textContent = "Continue: " + last.title; }
    }
  }

  /* count-up */
  function counters() {
    document.querySelectorAll(".stat__num[data-count]").forEach(function (el) {
      if (el.dataset.run) return; el.dataset.run = 1;
      var end = parseInt(el.dataset.count, 10) || 0, t0 = performance.now();
      (function step(t) { var k = Math.min(1, (t - t0) / 1100); el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3))).toLocaleString(); if (k < 1) requestAnimationFrame(step); })(t0);
    });
  }

  /* countdown */
  function countdown() {
    var inp = document.getElementById("exam-date"); if (!inp) return;
    var v = get(EXAM, ""); if (v) inp.value = v;
    function paint() {
      var d = document.getElementById("cd-days"), l = document.getElementById("cd-label");
      if (!inp.value) { d.textContent = "–"; l.textContent = "set your exam date"; return; }
      var n = Math.ceil((new Date(inp.value + "T00:00:00") - new Date()) / 864e5);
      if (n > 0) { d.textContent = n; l.textContent = n === 1 ? "day to go" : "days to go"; }
      else if (n === 0) { d.textContent = "0"; l.textContent = "exam is today - good luck!"; }
      else { d.textContent = "–"; l.textContent = "exam date has passed"; }
    }
    inp.onchange = function () { set(EXAM, inp.value); paint(); }; paint();
  }

  /* interactive MCQs + tools on practice pages */
  function practice() {
    var h1 = document.querySelector(".md-content h1");
    if (!h1 || !/Practice Questions/i.test(h1.textContent) || document.querySelector(".practice-tools")) return;
    var qs = Array.prototype.slice.call(document.querySelectorAll("details.question"));
    var mcqs = [], score = { r: 0, w: 0 };
    var tools = document.createElement("div"); tools.className = "practice-tools";
    tools.innerHTML = '<button class="btn-s" data-a="open">Expand all</button><button class="btn-s" data-a="close">Collapse all</button><button class="btn-s primary" data-a="fc">Flashcards</button><span class="score" hidden></span>';
    h1.parentNode.insertBefore(tools, h1.nextElementSibling && h1.nextElementSibling.classList.contains("page-meta") ? h1.nextElementSibling.nextSibling : h1.nextSibling);
    var sc = tools.querySelector(".score");
    function paintScore() { sc.hidden = false; sc.textContent = "MCQ score: " + score.r + " / " + (score.r + score.w); }
    qs.forEach(function (d) {
      var ul = d.querySelector("ul"); var ans = d.querySelector("p strong");
      if (!ul || !ans || !/^Answer:/i.test(ans.textContent)) return;
      var lis = ul.querySelectorAll(":scope > li");
      if (lis.length < 2 || !Array.prototype.every.call(lis, function (li) { return /^[A-E]\.\s/.test(li.textContent.trim()); })) return;
      var right = (ans.textContent.match(/Answer:\s*([A-E])/i) || [])[1];
      if (!right) return;
      mcqs.push(d);
      var expl = ans.parentNode; expl.hidden = true; expl.classList.add("mcq-explain");
      ul.classList.add("mcq-opts");
      var answered = false;
      lis.forEach(function (li) {
        var letter = li.textContent.trim().charAt(0), txt = li.innerHTML;
        li.innerHTML = ""; var b = document.createElement("button"); b.className = "mcq-opt"; b.type = "button"; b.innerHTML = txt; li.appendChild(b);
        b.onclick = function () {
          if (answered) return; answered = true;
          ul.querySelectorAll(".mcq-opt").forEach(function (x) { x.disabled = true; if (x.textContent.trim().charAt(0) === right) x.classList.add("correct"); });
          if (letter === right) score.r++; else { b.classList.add("wrong"); score.w++; }
          expl.hidden = false; paintScore();
        };
      });
    });
    tools.onclick = function (e) {
      var a = e.target.dataset && e.target.dataset.a; if (!a) return;
      if (a === "open" || a === "close") qs.forEach(function (d) { d.open = a === "open"; });
      if (a === "fc") flash(qs);
    };
  }

  /* flashcards */
  function flash(qs) {
    var cards = qs.map(function (d, i) {
      var s = d.querySelector("summary"), body = d.cloneNode(true); body.querySelector("summary").remove();
      body.querySelectorAll("[hidden]").forEach(function (x) { x.hidden = false; });
      body.querySelectorAll(".mcq-opt").forEach(function (x) { var p = x.parentNode; p.innerHTML = x.innerHTML; });
      return { id: location.pathname + "#" + i, q: s.innerHTML, a: body.innerHTML };
    });
    var known = get(KNOWN, []), order = cards.slice(), idx = 0, onlyUnknown = false;
    var ov = document.createElement("div"); ov.className = "fc-overlay open";
    ov.innerHTML = '<div class="fc-shell"><div class="fc-top"><span class="fc-count"></span><button class="btn-s" data-f="x">Close (Esc)</button></div><div class="fc-card"><div class="fc-inner"><div class="fc-face front"><span class="tag">Question</span><div class="q"></div></div><div class="fc-face back"><span class="tag">Answer</span><div class="a"></div></div></div></div><div class="fc-controls"><button class="btn-s" data-f="prev">&larr; Prev</button><button class="btn-s" data-f="shuf">Shuffle</button><button class="btn-s" data-f="unk">Only unknown: off</button><button class="btn-s primary" data-f="know">I know this &check;</button><button class="btn-s" data-f="next">Next &rarr;</button></div><div class="fc-hint">Space = flip &middot; &larr; &rarr; = navigate &middot; K = known</div></div>';
    document.body.appendChild(ov);
    var card = ov.querySelector(".fc-card");
    function list() { return onlyUnknown ? order.filter(function (c) { return known.indexOf(c.id) < 0; }) : order; }
    function show() {
      var L = list(); card.classList.remove("flip");
      if (!L.length) { ov.querySelector(".q").textContent = "All cards known - great work!"; ov.querySelector(".a").textContent = ""; ov.querySelector(".fc-count").textContent = "0 cards"; return; }
      idx = (idx + L.length) % L.length; var c = L[idx];
      ov.querySelector(".q").innerHTML = c.q; ov.querySelector(".a").innerHTML = c.a;
      ov.querySelector(".fc-count").textContent = "Card " + (idx + 1) + " / " + L.length + " · known " + known.filter(function (k) { return cards.some(function (c) { return c.id === k; }); }).length;
      if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([ov]).catch(function () {});
    }
    function close() { document.removeEventListener("keydown", key); ov.remove(); }
    function key(e) {
      if (e.key === "Escape") close(); else if (e.key === " ") { e.preventDefault(); card.classList.toggle("flip"); }
      else if (e.key === "ArrowRight") { idx++; show(); } else if (e.key === "ArrowLeft") { idx--; show(); }
      else if (e.key.toLowerCase() === "k") ov.querySelector('[data-f="know"]').click();
    }
    document.addEventListener("keydown", key);
    card.onclick = function () { card.classList.toggle("flip"); };
    ov.onclick = function (e) {
      if (e.target === ov) return close();
      var f = e.target.dataset && e.target.dataset.f; if (!f) return;
      if (f === "x") close();
      if (f === "next") { idx++; show(); }
      if (f === "prev") { idx--; show(); }
      if (f === "shuf") { order.sort(function () { return Math.random() - .5; }); idx = 0; show(); }
      if (f === "unk") { onlyUnknown = !onlyUnknown; e.target.textContent = "Only unknown: " + (onlyUnknown ? "on" : "off"); idx = 0; show(); }
      if (f === "know") { var c = list()[idx]; if (c && known.indexOf(c.id) < 0) { known.push(c.id); set(KNOWN, known); } show(); }
    };
    show();
  }

  /* revision planner */
  function planner() {
    var root = document.getElementById("planner"); if (!root || root.dataset.ready) return; root.dataset.ready = 1;
    var H = [4, 4, 5, 4, 5, 5, 5, 3, 3, 4, 3, 4]; // units 1..12 weights (hours)
    var names = ["Introduction", "Sound & Audio", "Image & Graphics", "Video & Animation", "Data Compression", "Optical Storage / CD", "Operating System & Scheduling", "Networking & QoS", "Multimedia Databases / Documents", "Synchronization", "Abstractions for Programming", "Applications"];
    root.innerHTML = '<div class="planner-form"><label>Exam date<input type="date" id="pl-date"></label><label>Study hours per day<input type="number" id="pl-h" min="1" max="12" value="3"></label><button class="btn-s primary" id="pl-go">Build my plan</button></div><div id="pl-out"></div>';
    var di = root.querySelector("#pl-date"); di.value = get(EXAM, "");
    function build() {
      var out = root.querySelector("#pl-out"), ex = di.value;
      if (!ex) { out.innerHTML = "<p>Pick your exam date to generate a day-by-day plan.</p>"; return; }
      set(EXAM, ex);
      var perDay = Math.max(1, parseFloat(root.querySelector("#pl-h").value) || 3);
      var today = new Date(); today.setHours(0, 0, 0, 0);
      var days = Math.ceil((new Date(ex + "T00:00:00") - today) / 864e5);
      if (days < 1) { out.innerHTML = "<p>The exam date is today or already past.</p>"; return; }
      var revDays = days >= 4 ? Math.max(1, Math.round(days * .2)) : 0, study = days - revDays;
      var tasks = []; names.forEach(function (n, i) { var h = H[i]; for (var k = 0; k < h; k++) tasks.push("Unit " + (i + 1) + ": " + n); });
      var slots = Math.max(1, Math.round(perDay)), html = "", ti = 0, per = Math.ceil(tasks.length / study);
      per = Math.max(1, Math.min(per, slots * 1));
      for (var d = 0; d < days; d++) {
        var dt = new Date(today.getTime() + d * 864e5), lab = dt.toDateString().slice(0, 10), rev = d >= study;
        var items = [];
        if (rev) items = ["Full revision: formula sheet, glossary, flashcards on all units", "Attempt practice MCQs; redo the ones you missed"];
        else { var take = Math.ceil((tasks.length - ti) / (study - d)); var seen = {}; tasks.slice(ti, ti + take).forEach(function (t) { seen[t] = 1; }); ti += take; items = Object.keys(seen).map(function (t) { return "Read notes and practise: " + t; }); }
        if (!items.length) items = ["Buffer day: revisit weak topics"];
        html += '<div class="plan-day' + (rev ? " rev" : "") + '"><div><b>Day ' + (d + 1) + '</b><small>' + lab + (d === days - 1 ? " · exam day" : "") + '</small></div><div>' + items.join("<br>") + '</div></div>';
      }
      out.innerHTML = html;
    }
    root.querySelector("#pl-go").onclick = build; if (di.value) build();
  }

  function init() {
    if (document.querySelector(".md-content")) { bar(); track(); nav(); unitBars(); practice(); planner(); counters(); countdown(); }
    document.querySelectorAll(".md-nav__link").length && nav();
  }
  window.addEventListener("beforeprint", function () { document.querySelectorAll("details").forEach(function (d) { d.open = true; }); });
  if (window.document$) window.document$.subscribe(init); else document.addEventListener("DOMContentLoaded", init);
})();
