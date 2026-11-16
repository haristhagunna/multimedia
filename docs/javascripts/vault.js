/* Sign-in and in-browser decryption for protected pages.
   Copyright (c) 2026 Er. Harish Thagunna. All rights reserved. */
(function () {
  "use strict";
  var T = new TextEncoder(), D = new TextDecoder(), SK = "mm:vk", BASE = null, MAN = null, MANDATA = null;

  function b64d(s) { var x = atob(s), a = new Uint8Array(x.length); for (var i = 0; i < x.length; i++) a[i] = x.charCodeAt(i); return a; }
  function b64e(u) { var s = ""; for (var i = 0; i < u.length; i++) s += String.fromCharCode(u[i]); return btoa(s); }
  function base() {
    if (BASE) return BASE;
    var s = [].slice.call(document.scripts).filter(function (x) { return /javascripts\/vault\.js/.test(x.src); })[0];
    BASE = s ? s.src.replace(/javascripts\/vault\.js.*$/, "") : location.origin + "/";
    return BASE;
  }
  function manifest() {
    if (!MAN) MAN = fetch(base() + "vault.json", { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (m) { MANDATA = m; window.MM_VAULT = m; return m; });
    return MAN;
  }
  function stored() { try { var r = sessionStorage.getItem(SK) || localStorage.getItem(SK); return r ? JSON.parse(r) : null; } catch (e) { return null; } }
  function save(o, remember) {
    try { sessionStorage.setItem(SK, JSON.stringify(o)); if (remember) localStorage.setItem(SK, JSON.stringify(o)); else localStorage.removeItem(SK); } catch (e) {}
  }
  function clear() { try { sessionStorage.removeItem(SK); localStorage.removeItem(SK); } catch (e) {} }

  async function dec(key, o) { return new Uint8Array(await crypto.subtle.decrypt({ name: "AES-GCM", iv: b64d(o.iv) }, key, b64d(o.ct))); }
  async function aes(raw) { return crypto.subtle.importKey("raw", raw, "AES-GCM", false, ["decrypt"]); }
  async function derive(pw, salt, iter) {
    var k = await crypto.subtle.importKey("raw", T.encode(pw), "PBKDF2", false, ["deriveBits"]);
    return new Uint8Array(await crypto.subtle.deriveBits({ name: "PBKDF2", hash: "SHA-256", salt: b64d(salt), iterations: iter }, k, 256));
  }
  async function ok(raw, chk) { try { return D.decode(await dec(await aes(raw), chk)) === "mm-vault-ok"; } catch (e) { return false; } }

  async function login(pw, remember) {
    var m = await manifest();
    var a = await derive(pw, m.saltA, m.iter);
    if (await ok(a, m.checkA)) { save({ role: "a", key: b64e(a) }, remember); return "a"; }
    var s = await derive(pw, m.saltS, m.iter);
    if (await ok(s, m.checkS)) { save({ role: "s", key: b64e(s) }, remember); return "s"; }
    return null;
  }
  async function openPkg(pkg) {
    var k = stored(); if (!k) return { state: "nokey" };
    var w = k.role === "a" ? pkg.wa : pkg.ws; if (!w) return { state: "locked" };
    try {
      var kek = await aes(b64d(k.key)), dek = await aes(await dec(kek, w));
      return { state: "ok", data: await dec(dek, pkg) };
    } catch (e) { return { state: "badkey" }; }
  }

  /* ---------- UI ---------- */
  function formHtml() {
    return '<form class="vault-form" autocomplete="on"><label>Password<input type="password" name="pw" autocomplete="current-password" required></label>' +
      '<label class="vault-remember"><input type="checkbox" name="rem"> Remember me on this device</label>' +
      '<button class="md-button md-button--primary" type="submit">Unlock</button><p class="vault-err" role="alert"></p></form>';
  }
  function bindForm(form, done) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      var btn = form.querySelector("button"), err = form.querySelector(".vault-err");
      btn.disabled = true; btn.textContent = "Checking..."; err.textContent = "";
      var role = null;
      try { role = await login(form.pw.value, form.rem.checked); } catch (x) { err.textContent = "Could not check the password. Please try again."; }
      btn.disabled = false; btn.textContent = "Unlock";
      if (role) { done(role); } else if (!err.textContent) { err.textContent = "Incorrect password."; form.pw.value = ""; form.pw.focus(); }
    });
  }
  function lockedView(g) {
    var admin = g.dataset.key === "admin";
    var h1 = g.querySelector("h1").outerHTML;
    g.innerHTML = h1 + '<div class="lock-panel"><div class="lock-panel__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 1a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2h-1V6a5 5 0 0 0-5-5m-3 5a3 3 0 1 1 6 0v3H9V6Z"/></svg></div><h2>' +
      (admin ? "Administrator only" : "This material is locked") + "</h2><p>" +
      (admin ? "This page is only available to the course administrator." : "It will be unlocked after it has been taught in class. Please check again after your next lecture.") + "</p></div>";
  }
  function gateForm(g, bad) {
    var m = g.querySelector(".vault-msg");
    if (m) m.textContent = bad ? "Your saved sign-in no longer works. Please sign in again." : "This page is protected. Enter the class password to read it.";
    if (g.querySelector("form")) return;
    g.insertAdjacentHTML("beforeend", formHtml());
    bindForm(g.querySelector("form"), function () { run(); });
  }
  function header() {
    var inner = document.querySelector(".md-header__inner"); if (!inner) return;
    var k = stored(), b = document.querySelector(".vault-btn");
    if (!b) {
      b = document.createElement("button"); b.type = "button"; b.className = "vault-btn"; inner.appendChild(b);
      b.addEventListener("click", function () { if (stored()) { clear(); location.reload(); } else modal(); });
    }
    b.textContent = k ? (k.role === "a" ? "Admin" : "Student") + " · Sign out" : "Sign in";
    b.classList.toggle("is-in", !!k);
    document.querySelectorAll('a[href$="admin/"]').forEach(function (a) {
      var li = a.closest("li") || a; li.style.display = k && k.role === "a" ? "" : "none";
    });
  }
  function modal() {
    if (document.querySelector(".vault-modal")) return;
    var d = document.createElement("div"); d.className = "vault-modal";
    d.innerHTML = '<div class="vault-card"><button class="vault-x" aria-label="Close">&times;</button><h2>Sign in</h2><p>Enter the class password. Your instructor gives it to you.</p>' + formHtml() + "</div>";
    document.body.appendChild(d);
    d.querySelector(".vault-x").onclick = function () { d.remove(); };
    d.addEventListener("click", function (e) { if (e.target === d) d.remove(); });
    bindForm(d.querySelector("form"), function () { d.remove(); header(); run(); });
    d.querySelector("input").focus();
  }

  /* ---------- content ---------- */
  function relPath(href) {
    try {
      var u = new URL(href, location.href); if (u.origin !== location.origin) return null;
      var bp = new URL(base()).pathname; return u.pathname.indexOf(bp) === 0 ? decodeURIComponent(u.pathname.slice(bp.length)) : null;
    } catch (e) { return null; }
  }
  async function fileBlob(rel) {
    var r = await fetch(base() + rel + ".enc"); if (!r.ok) throw new Error("missing");
    var pkg = await r.json(), o = await openPkg(pkg);
    if (o.state !== "ok") throw new Error(o.state);
    return { blob: new Blob([o.data], { type: pkg.type }), type: pkg.type };
  }
  async function resolveFiles(root) {
    var m = await manifest(); if (!m.files.length) return;
    root.querySelectorAll("img[src]").forEach(async function (img) {
      var rel = relPath(img.getAttribute("src")); if (!rel || m.files.indexOf(rel) < 0) return;
      try { img.src = URL.createObjectURL((await fileBlob(rel)).blob); } catch (e) {}
    });
  }
  function toc(art) {
    var nav = document.querySelector(".md-sidebar--secondary .md-nav--secondary"); if (!nav) return;
    var hs = [].slice.call(art.querySelectorAll("h2[id], h3[id]")); if (!hs.length) { nav.innerHTML = ""; return; }
    nav.innerHTML = '<label class="md-nav__title" for="__toc"><span class="md-nav__icon md-icon"></span>Table of contents</label><ul class="md-nav__list" data-md-component="toc" data-md-scrollfork>' +
      hs.map(function (h) {
        var t = h.textContent.replace(/¶/g, "").trim();
        return '<li class="md-nav__item"' + (h.tagName === "H3" ? ' style="margin-left:.7rem"' : "") + '><a href="#' + h.id + '" class="md-nav__link"><span class="md-ellipsis">' + t.replace(/</g, "&lt;") + "</span></a></li>";
      }).join("") + "</ul>";
  }
  async function run() {
    header();
    var g = document.querySelector(".vault-gate"); if (!g) return;
    var pkg = JSON.parse(g.dataset.vault), r = await openPkg(pkg);
    if (r.state === "ok") {
      var art = g.closest("article"); art.innerHTML = D.decode(r.data);
      toc(art); resolveFiles(art);
      if (window.document$ && window.document$.next) window.document$.next(document);
      if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
    } else if (r.state === "locked") lockedView(g);
    else gateForm(g, r.state === "badkey");
  }

  document.addEventListener("click", async function (e) {
    var a = e.target.closest && e.target.closest("a[href]"); if (!a || !MANDATA) return;
    var rel = relPath(a.href); if (!rel || MANDATA.files.indexOf(rel) < 0) return;
    e.preventDefault(); e.stopPropagation();
    try {
      var f = await fileBlob(rel), url = URL.createObjectURL(f.blob);
      if (/^image\//.test(f.type)) window.open(url, "_blank");
      else { var d = document.createElement("a"); d.href = url; d.download = rel.split("/").pop(); document.body.appendChild(d); d.click(); d.remove(); }
    } catch (x) { alert("Please sign in with a password that allows this file."); }
  }, true);

  window.MM_Vault = { stored: stored, manifest: manifest, base: base };
  function start() { manifest(); run(); }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(function () { start(); });
  else document.addEventListener("DOMContentLoaded", start);
})();
