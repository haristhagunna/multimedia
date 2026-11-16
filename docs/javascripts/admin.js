/* Administrator panel: lock and unlock pages by editing release.yml through the GitHub API.
   Copyright (c) 2026 Er. Harish Thagunna. All rights reserved. */
(function () {
  "use strict";
  var TK = "mm:ghtoken";
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function matches(key, entries) { return entries.some(function (e) { return key === e || key.indexOf(e + "/") === 0; }); }
  function isOpen(key, entries) {
    if (matches(key, entries)) return true;
    var m = key.match(/^(unit-\d\d)\/index$/);
    return !!(m && entries.some(function (e) { return e === m[1] || e.indexOf(m[1] + "/") === 0; }));
  }
  function parse(text) {
    var out = [], inList = false;
    text.split("\n").forEach(function (l) {
      if (/^unlocked:\s*$/.test(l)) { inList = true; return; }
      if (inList) { var m = l.match(/^\s*-\s*([^\s#]+)/); if (m) out.push(m[1].replace(/\/$/, "")); else if (/^\S/.test(l) && l.trim() !== "") inList = false; }
    });
    return out;
  }
  function build(text, entries) {
    var lines = text.split("\n"), i = lines.findIndex(function (l) { return /^unlocked:\s*$/.test(l); });
    var head = i < 0 ? lines.concat(["unlocked:"]) : lines.slice(0, i + 1);
    return head.join("\n") + "\n" + entries.map(function (e) { return "  - " + e; }).join("\n") + (entries.length ? "\n" : "  # (nothing unlocked yet)\n");
  }
  function b64u(s) { return decodeURIComponent(escape(atob(s.replace(/\n/g, "")))); }
  function b64e(s) { return btoa(unescape(encodeURIComponent(s))); }

  async function mount() {
    var root = document.getElementById("admin-panel"); if (!root || root.dataset.ready) return; root.dataset.ready = 1;
    var repo = window.MM_REPO || "", branch = window.MM_BRANCH || "main";
    var man = await window.MM_Vault.manifest();
    var pages = man.pages.filter(function (p) { return p.key !== "index" && p.key !== "about" && p.key !== "admin"; });
    var state = { text: "", sha: "", entries: [] };
    root.innerHTML =
      '<div class="admin-card"><h3>1. Connect</h3><p>Paste a GitHub <b>fine-grained token</b> for the repository <code>' + esc(repo) + '</code> with <b>Contents: Read and write</b>. It stays in this browser tab only and is never stored on the site.</p>' +
      '<div class="admin-row"><input id="ad-token" type="password" placeholder="github_pat_..." autocomplete="off"><button class="md-button md-button--primary" id="ad-load">Load</button></div><p id="ad-msg" class="admin-msg"></p></div>' +
      '<div id="ad-list" hidden></div>';
    var tok = root.querySelector("#ad-token"), msg = root.querySelector("#ad-msg");
    try { tok.value = sessionStorage.getItem(TK) || ""; } catch (e) {}
    function say(t, bad) { msg.textContent = t; msg.className = "admin-msg" + (bad ? " is-bad" : ""); }
    async function gh(path, opt) {
      var r = await fetch("https://api.github.com/repos/" + repo + path, Object.assign({ headers: { Authorization: "Bearer " + tok.value.trim(), Accept: "application/vnd.github+json" } }, opt || {}));
      if (!r.ok) throw new Error(r.status + " " + ((await r.json().catch(function () { return {}; })).message || r.statusText));
      return r.json();
    }
    function render() {
      var groups = {}; pages.forEach(function (p) { var g = (p.key.match(/^unit-\d\d/) || [p.key.split("/")[0]])[0]; (groups[g] = groups[g] || []).push(p); });
      var html = '<div class="admin-card"><h3>2. Choose what students can read</h3><div class="admin-row"><button class="btn-s" id="ad-all">Unlock everything</button><button class="btn-s" id="ad-none">Lock everything</button></div>';
      Object.keys(groups).sort().forEach(function (g) {
        html += '<details class="admin-group"' + (/^unit-/.test(g) ? "" : "") + '><summary><label><input type="checkbox" class="ad-grp" data-g="' + g + '"> <b>' + esc(g) + "</b></label></summary><ul>";
        groups[g].forEach(function (p) { html += '<li><label><input type="checkbox" class="ad-pg" data-k="' + esc(p.key) + '" data-g="' + g + '"> ' + esc(p.title) + ' <code>' + esc(p.key) + "</code></label></li>"; });
        html += "</ul></details>";
      });
      html += '<div class="admin-row"><button class="md-button md-button--primary" id="ad-save">Save and publish</button></div><p id="ad-msg2" class="admin-msg"></p></div>';
      var box = root.querySelector("#ad-list"); box.innerHTML = html; box.hidden = false;
      var boxes = box.querySelectorAll(".ad-pg");
      boxes.forEach(function (c) { c.checked = isOpen(c.dataset.k, state.entries); });
      function sync() { box.querySelectorAll(".ad-grp").forEach(function (gc) { var m = [].slice.call(boxes).filter(function (c) { return c.dataset.g === gc.dataset.g; }); var n = m.filter(function (c) { return c.checked; }).length; gc.checked = n === m.length; gc.indeterminate = n > 0 && n < m.length; }); }
      sync();
      box.addEventListener("change", function (e) {
        if (e.target.classList.contains("ad-grp")) boxes.forEach(function (c) { if (c.dataset.g === e.target.dataset.g) c.checked = e.target.checked; });
        sync();
      });
      box.querySelector("#ad-all").onclick = function () { boxes.forEach(function (c) { c.checked = true; }); sync(); };
      box.querySelector("#ad-none").onclick = function () { boxes.forEach(function (c) { c.checked = false; }); sync(); };
      box.querySelector("#ad-save").onclick = async function () {
        var m2 = box.querySelector("#ad-msg2"), entries = [];
        Object.keys(groups).sort().forEach(function (g) {
          var all = groups[g], on = all.filter(function (p) { return box.querySelector('.ad-pg[data-k="' + p.key + '"]').checked; });
          if (!on.length) return;
          if (on.length === all.length) entries.push(g);
          else on.forEach(function (p) { if (!/\/index$/.test(p.key) || /^(labs|revision|instructor)\/index$/.test(p.key)) entries.push(p.key); });
        });
        entries = entries.filter(function (e, i, a) { return a.indexOf(e) === i; });
        m2.textContent = "Saving..."; m2.className = "admin-msg";
        try {
          var cur = await gh("/contents/release.yml?ref=" + branch);
          var res = await gh("/contents/release.yml", { method: "PUT", body: JSON.stringify({ message: "Release update: " + (entries.length ? entries.join(", ") : "lock everything"), content: b64e(build(b64u(cur.content), entries)), sha: cur.sha, branch: branch }) });
          state.entries = entries;
          m2.innerHTML = "Saved. The site is rebuilding and the change appears in about 2 minutes. <a href=\"https://github.com/" + esc(repo) + "/actions\" target=\"_blank\" rel=\"noopener\">Watch progress</a>";
        } catch (e) { m2.textContent = "Could not save: " + e.message; m2.className = "admin-msg is-bad"; }
      };
    }
    root.querySelector("#ad-load").onclick = async function () {
      say("Loading..."); try { sessionStorage.setItem(TK, tok.value.trim()); } catch (e) {}
      try { var cur = await gh("/contents/release.yml?ref=" + branch); state.text = b64u(cur.content); state.entries = parse(state.text); say("Connected. " + state.entries.length + " unlock entries loaded."); render(); }
      catch (e) { say("Could not load: " + e.message, true); }
    };
  }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(function () { setTimeout(mount, 0); });
  else document.addEventListener("DOMContentLoaded", mount);
})();
