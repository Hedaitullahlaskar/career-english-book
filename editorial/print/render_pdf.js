// Render the print edition to PDF with headless Chrome, then stamp running heads and page numbers.
//
//   node editorial/print/render_pdf.js [chrome.exe]
//
// Needs: npm install puppeteer-core@23 pdf-lib@1.17.1 pdfjs-dist@4.10.38   (in editorial/print, or on NODE_PATH)
// Writes editorial/print/Career-English-Master.pdf and editorial/print/pages.json
// (the page on which each level, module, lesson and assessment starts). Run build_print.py,
// then this script, then build_print.py and this script again so the contents pages show real numbers.
const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");
const puppeteer = require("puppeteer-core");
const { PDFDocument, StandardFonts, rgb } = require("pdf-lib");

const DIR = __dirname;
const HTML = path.join(DIR, "career-english-print.html");
const RAW = path.join(DIR, "render-raw.pdf");
const OUT = path.join(DIR, "Career-English-Master.pdf");
const CHROME = process.argv[2] || "C:/Program Files/Google/Chrome/Application/chrome.exe";

// Chrome drops the space where a heading wraps, so compare without whitespace.
const norm = s => String(s).replace(/\s+/g, "").replace(/[’‘]/g, "'").replace(/[“”]/g, '"').toLowerCase();

async function outlinePages(file) {
  const pdfjs = await import(pathToFileURL(require.resolve("pdfjs-dist/legacy/build/pdf.mjs")).href);
  const doc = await pdfjs.getDocument({ data: new Uint8Array(fs.readFileSync(file)) }).promise;
  const flat = [];
  async function walk(items) {
    for (const it of items || []) {
      let dest = it.dest;
      if (typeof dest === "string") dest = await doc.getDestination(dest);
      let page = null;
      if (dest && dest[0]) page = (await doc.getPageIndex(dest[0])) + 1;
      flat.push({ title: it.title, page });
      await walk(it.items);
    }
  }
  await walk(await doc.getOutline());
  return { flat, numPages: doc.numPages };
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new" });
  const page = await browser.newPage();
  await page.goto(pathToFileURL(HTML).href, { waitUntil: "networkidle0", timeout: 0 });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: RAW, format: "A4", printBackground: true, preferCSSPageSize: true, outline: true, tagged: true, timeout: 0 });
  await browser.close();

  // Map bookmarks to keys (document order; content headings in between are skipped).
  const heads = JSON.parse(fs.readFileSync(path.join(DIR, "headings.json"), "utf8"));
  const { flat, numPages } = await outlinePages(RAW);
  const pages = {};
  let i = 0;
  for (const o of flat) {
    if (i < heads.length && norm(o.title) === norm(heads[i].title)) { pages[heads[i].key] = o.page; i++; }
  }
  if (i < heads.length) console.warn(`only ${i} of ${heads.length} headings found in the outline; next expected: ${heads[i].title}`);
  fs.writeFileSync(path.join(DIR, "pages.json"), JSON.stringify(pages, null, 1));

  // Running head: which level each page belongs to.
  const starts = heads.filter(h => pages[h.key]).map(h => ({ page: pages[h.key], level: h.level, key: h.key }));
  const levelTitles = {};
  heads.filter(h => h.key.startsWith("level-")).forEach(h => { levelTitles[h.level] = h.title; });
  function headFor(p) {
    let cur = null;
    for (const s of starts) { if (s.page <= p) cur = s; else break; }
    if (!cur) return "Career English";
    if (cur.key === "index") return "Career English · Reference Index";
    if (cur.key === "how-to-use") return "Career English · How to Use This Book";
    return "Career English · " + (levelTitles[cur.level] || "");
  }

  const pdf = await PDFDocument.load(fs.readFileSync(RAW));
  const font = await pdf.embedFont(StandardFonts.Helvetica);
  const grey = rgb(0.38, 0.42, 0.47);
  const all = pdf.getPages();
  all.forEach((pg, idx) => {
    const n = idx + 1;
    if (n === 1 || n === all.length) return; // covers
    const { width } = pg.getSize();
    const num = String(n);
    pg.drawText(num, { x: width / 2 - font.widthOfTextAtSize(num, 9) / 2, y: 28, size: 9, font, color: grey });
    if (n > 3) {
      const head = headFor(n);
      pg.drawText(head, { x: 48, y: 812, size: 7.5, font, color: grey });
    }
  });
  pdf.setTitle("Career English: Professional English for the Real Workplace");
  pdf.setAuthor("Hidayet English Academy");
  pdf.setSubject("Five-level workplace English course: 40 modules, 186 lessons");
  pdf.setLanguage("en");
  fs.writeFileSync(OUT, await pdf.save());
  fs.unlinkSync(RAW);
  console.log(JSON.stringify({ pages: numPages, bookmarksMatched: i, of: heads.length, out: path.basename(OUT) }));
})().catch(e => { console.error(e); process.exit(1); });
