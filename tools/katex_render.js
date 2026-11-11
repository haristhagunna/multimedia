// reads JSON [{tex, display}] on stdin, writes JSON [html]
const katex = require(process.env.KATEX_PATH || "katex");
let d = ""; process.stdin.on("data", c => d += c).on("end", () => {
  const out = JSON.parse(d).map(x => { try { return katex.renderToString(x.tex, { displayMode: x.display, throwOnError: false, trust: true }); } catch (e) { return x.tex; } });
  process.stdout.write(JSON.stringify(out));
});
