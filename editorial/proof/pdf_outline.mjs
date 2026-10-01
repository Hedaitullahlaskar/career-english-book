// Dump the PDF's bookmarks (outline) with the page each one opens, for the consistency audit.
//   node editorial/proof/pdf_outline.mjs <pdf> <out.json>
// Needs pdfjs-dist (see editorial/HOSTINGER-UPDATE.md for the npm install line).
import fs from "fs";
import { createRequire } from "module";
import { pathToFileURL } from "url";
const require = createRequire(import.meta.url);
const pdfjs = await import(pathToFileURL(require.resolve("pdfjs-dist/legacy/build/pdf.mjs")).href);

const [file, out] = process.argv.slice(2);
const doc = await pdfjs.getDocument({ data: new Uint8Array(fs.readFileSync(file)) }).promise;
const rows = [];
async function walk(items, depth) {
  for (const it of items || []) {
    let page = null;
    let dest = it.dest;
    if (typeof dest === "string") dest = await doc.getDestination(dest);
    if (Array.isArray(dest) && dest[0]) page = (await doc.getPageIndex(dest[0])) + 1;
    rows.push({ depth, title: it.title, page });
    await walk(it.items, depth + 1);
  }
}
await walk(await doc.getOutline(), 0);
fs.writeFileSync(out, JSON.stringify({ pages: doc.numPages, bookmarks: rows }, null, 1));
console.log(`${rows.length} bookmarks, ${doc.numPages} pages -> ${out}`);
