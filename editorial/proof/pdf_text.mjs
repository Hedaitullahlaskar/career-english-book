// Extract the text of the rendered PDF page by page (lines rebuilt from text positions),
// plus simple layout measurements used by the automated proof checks.
//   node editorial/proof/pdf_text.mjs <pdf> <out.json>
// Needs pdfjs-dist (see editorial/HOSTINGER-UPDATE.md for the npm install line).
import fs from "fs";
import { createRequire } from "module";
import { pathToFileURL } from "url";
const require = createRequire(import.meta.url);
const pdfjs = await import(pathToFileURL(require.resolve("pdfjs-dist/legacy/build/pdf.mjs")).href);

const [file, out] = process.argv.slice(2);
const doc = await pdfjs.getDocument({ data: new Uint8Array(fs.readFileSync(file)) }).promise;
const pages = [];
for (let n = 1; n <= doc.numPages; n++) {
  const page = await doc.getPage(n);
  const { width, height } = page.getViewport({ scale: 1 });
  const tc = await page.getTextContent();
  const items = tc.items.filter(i => i.str && i.str.trim() !== "" || i.hasEOL);
  // group into lines by baseline
  const rows = [];
  for (const it of tc.items) {
    if (!it.str) continue;
    const x = it.transform[4], y = it.transform[5], size = Math.hypot(it.transform[2], it.transform[3]);
    let row = rows.find(r => Math.abs(r.y - y) < Math.max(2, size * 0.4));
    if (!row) { row = { y, parts: [], size: 0 }; rows.push(row); }
    row.parts.push({ x, str: it.str, w: it.width, font: it.fontName, size });
    row.size = Math.max(row.size, size);
  }
  rows.sort((a, b) => b.y - a.y);
  const lines = rows.map(r => {
    r.parts.sort((a, b) => a.x - b.x);
    let s = "", end = null;
    for (const p of r.parts) {
      if (end !== null && p.x - end > p.size * 0.15 && !s.endsWith(" ") && !p.str.startsWith(" ")) s += " ";
      s += p.str; end = p.x + p.w;
    }
    const minX = Math.min(...r.parts.map(p => p.x)), maxX = Math.max(...r.parts.map(p => p.x + p.w));
    return { y: Math.round(r.y), size: Math.round(r.size * 10) / 10, minX: Math.round(minX), maxX: Math.round(maxX), text: s.replace(/\s+/g, " ").trim() };
  }).filter(l => l.text);
  pages.push({ page: n, width: Math.round(width), height: Math.round(height), lines });
}
fs.writeFileSync(out, JSON.stringify(pages));
console.log(`${doc.numPages} pages -> ${out}`);
