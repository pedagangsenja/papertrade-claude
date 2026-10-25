// uji_halaman.js — ujian regresi halaman dashboard dengan db tiruan (Playwright; CI .github/workflows/semak_data.yml job "halaman").
//   node BacktestShariah2/ujian/halaman/uji_halaman.js [halaman.html]
// Memuat standard/dashboard_v2.html (atau fail yang diberi) dengan fikstur_db.json sebagai window.__DB (sambungan db halaman
// diganti dengan db tiruan) dalam dua varian, tanpa dan dengan harian/hari_ini (fikstur_hari_ini.json = jana_db.hari_ini atas
// fikstur sama; angka Hari Ini mesti sama), pada lebar 1400 px (desktop) dan 390 px (telefon) klik empat tab utama (Hari Ini, Kaedah, Posisi,
// Lagi) dan menyemak: tiada ralat halaman/konsol (termasuk panel "Ralat memapar tab ini." yang ditangkap renderAll),
// dan angka KPI yang dipapar = jangka.json (dikira dengan tangan; sama dengan nilai kira_semula.py atas fikstur yang sama).
// Permintaan rangkaian luar (Google Fonts) dijawab kosong supaya ujian tidak bergantung pada rangkaian.
// Kod keluar 1 jika mana-mana semakan gagal. Fikstur: python3 BacktestShariah2/ujian/halaman/fikstur.py.
'use strict';
const fs = require('fs'), path = require('path'), os = require('os');
const { chromium } = require('playwright');

const DIR = __dirname, BS2 = path.resolve(DIR, '..', '..');
const HALAMAN = process.argv[2] || path.join(BS2, 'standard', 'dashboard_v2.html');
const DB = JSON.parse(fs.readFileSync(path.join(DIR, 'fikstur_db.json'), 'utf8'));
// v105: varian kedua dengan dokumen pra-kira harian/hari_ini (jana_db.hari_ini atas fikstur sama) -> angka Hari Ini mesti sama
const HI = JSON.parse(fs.readFileSync(path.join(DIR, 'fikstur_hari_ini.json'), 'utf8'));
const J = JSON.parse(fs.readFileSync(path.join(DIR, 'jangka.json'), 'utf8')).halaman;
const SAMBUNG = "const db=window.claude?.use?await window.claude.use('db'):null;";
const TIRUAN = "const db=window.__DB?window.__mockDb(window.__DB):(window.claude?.use?await window.claude.use('db'):null);";
const MOCK = D => '<script>window.__DB=' + JSON.stringify(D).replace(/<\//g, '<\\/') + ';window.__diminta=[];\n' +
  "window.__mockDb=function(D){const snap=p=>({exists:p in D,id:p.split('/').pop(),data:()=>D[p]});\n" +
  ' return {doc:p=>({onSnapshot:cb=>{window.__diminta.push(p);setTimeout(()=>cb(snap(p)),0);return ()=>{};}}),\n' +
  "   collection:c=>{const o={limit:()=>o,onSnapshot:cb=>{setTimeout(()=>cb({docs:Object.keys(D).filter(k=>k.startsWith(c+'/')&&k.split('/').length===2).map(snap)}),0);return ()=>{};}};return o;}};};</script>\n";

function bina(D) {
  const t = fs.readFileSync(HALAMAN, 'utf8');
  const i = t.indexOf(SAMBUNG);
  if (i < 0 || t.indexOf(SAMBUNG, i + 1) >= 0) throw new Error('baris sambungan db tidak ditemui tepat sekali dalam ' + HALAMAN);
  const h = t.slice(0, i) + TIRUAN + t.slice(i + SAMBUNG.length);
  return '<!doctype html><html lang="ms"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' +
    MOCK(D) + h + '</body></html>';
}

const gagal = [], lulus = [];
const sama = (nama, dijangka, didapati) => {
  const ok = JSON.stringify(dijangka) === JSON.stringify(didapati);
  (ok ? lulus : gagal).push(ok ? nama : `${nama}: dijangka ${JSON.stringify(dijangka)}, didapati ${JSON.stringify(didapati)}`);
};
const rata = s => String(s == null ? '' : s).replace(/\s+/g, ' ').trim();

async function larian(b, fail, lebar, varian) {
  const L = `[${lebar}px${varian ? ' ' + varian : ''}] `, ralat = [];
  const ok = (nama, d, g) => sama(L + nama, d, g);
  const ctx = await b.newContext({ viewport: { width: lebar, height: lebar < 800 ? 860 : 1000 } });
  try {
    await ctx.route(/^https?:\/\//, r => r.fulfill({ status: 200, contentType: r.request().resourceType() === 'stylesheet' ? 'text/css' : 'text/plain', body: '' }));
    const p = await ctx.newPage();
    p.on('pageerror', e => ralat.push('pageerror: ' + e.message));
    p.on('console', m => { if (m.type() === 'error') ralat.push('console: ' + m.text()); });
    await p.goto('file://' + fail);
    // tunggu data tiruan dimuat (posisi C dinyahkod daripada ringkas_c + bahagian + kamus)
    await p.waitForFunction(() => /Dibeli|Ralat memapar/.test((document.querySelector('#v-hari') || {}).textContent || ''), null, { timeout: 15000 });
    // renderAll halaman menangkap ralat lukisan dan memapar "Ralat memapar tab ini." (bukan pageerror): dikira sebagai ralat
    const tab = async t => {
      await p.click(`#mainTabs [data-tab="${t}"]`);
      await p.waitForTimeout(400);
      const [id, rl] = await p.evaluate(() => {
        const v = [...document.querySelectorAll('section.view')].find(x => !x.hidden), e = v && v.querySelector('.panel.empty b.neg');
        return [v ? v.id : null, e ? v.textContent.replace(/\s+/g, ' ').slice(0, 300) : ''];
      });
      if (rl) ralat.push(`tab ${t}: ${rl}`);
      return id;
    };
    const kpi = (lbl) => p.evaluate(l => {
      const k = [...document.querySelectorAll('section.view:not([hidden]) .kpi')].find(x => ((x.querySelector('.lbl') || {}).textContent || '').replace(/\s+/g, ' ').trim() === l);
      return k ? [(k.querySelector('.v') || {}).textContent, (k.querySelector('.s') || {}).textContent] : null;
    }, lbl);

    // ---- Hari Ini (v105: Buku hari ini, banner fasa dengan bukti hadapan, Esok tiga tahap, Berubah)
    ok('tab hari', 'v-hari', await tab('hari'));
    const bk = await p.evaluate(() => (document.querySelector('#v-hari .fasa .fasa-bukti') || {}).textContent || null);
    ok('Hari: Bukti hadapan', J.hari.bukti_hadapan, bk && rata(bk));
    const buku = await p.$$eval('#v-hari .buku .bkh', L => L.map(x => [(x.querySelector('.bkl') || {}).textContent, (x.querySelector('.bkv') || {}).textContent]));
    for (const [k, v] of Object.entries(J.hari.buku)) {
      const x = buku.find(r => rata(r[0]) === k);
      ok(`Hari: Buku hari ini "${k}"`, v, x ? rata(x[1]) : null);
    }
    const th = (await p.$$eval('#v-hari .tahap .th, #v-hari .tahap > summary', L => L.map(x => x.textContent))).map(rata);
    ok('Hari: tahap Esok', J.hari.tahap, th.map(x => x.split(' item')[0]));
    if (varian === 'hari_ini') {
      // dokumen posisi (~6 MB dalam db sebenar) tidak dimuat untuk Hari Ini apabila harian/hari_ini ada
      const dm = await p.evaluate(() => window.__diminta.slice());
      ok('Hari: tidak memuat papertrade/ringkas_c', false, dm.includes('papertrade/ringkas_c'));
      ok('Hari: tidak memuat analisis/papan (ringkasan dalam harian/hari_ini)', false, dm.includes('analisis/papan'));
    }
    const bbr = (await p.$$eval('#v-hari .bbr', L => L.map(x => [...x.children].map(c => c.textContent)))).map(x => x.map(rata));
    for (const [k, v] of Object.entries(J.hari.berubah)) {
      const x = bbr.find(r => r[0].endsWith(k));
      ok(`Hari: Berubah sejak sesi lalu "${k}"`, v, x ? x[1] : null);
    }
    const esh = (await p.$$eval('#v-hari .esb .esh', L => L.map(x => x.textContent))).map(rata);
    for (const [k, v] of Object.entries(J.hari.esok)) {
      const x = esh.find(s => s.includes(k));   // cth. "◆ Hampir henti kaedah (≤ 1 ATR) 0 posisi · 0 saham"
      ok(`Hari: Esok "${k}"`, v, x ? x.slice(x.indexOf(k) + k.length).trim().replace(/^\(≤[^)]*\)\s*/, '') : null);
    }
    // ---- Kaedah (pintu wang sebenar)
    ok('tab pilih', 'v-pilih', await tab('pilih'));
    const crg = await p.$$eval('#v-pilih .corong .crg .nm b', L => L.map(x => +x.textContent.replace(/,/g, '')));
    ok('Kaedah: corong pintu', J.pilih.corong, crg);
    const sub = await p.evaluate(() => { const h = [...document.querySelectorAll('#v-pilih .panel-h')].find(x => /Pintu wang sebenar/.test(x.textContent)); return h ? h.querySelector('.sub').textContent : null; });
    ok('Kaedah: pintu lulus', J.pilih.lulus, rata(sub));
    // ---- Posisi
    ok('tab posisi', 'v-pos', await tab('posisi'));
    const seg = (await p.$$eval('#posSt button', L => L.map(x => x.textContent))).map(rata);
    ok('Posisi: segmen', J.posisi.segmen, seg);
    for (const [st, kp] of [['pegang', J.posisi.pegang], ['semua', J.posisi.semua]]) {
      await p.click(`#posSt button[data-v="${st}"]`);
      await p.waitForTimeout(300);
      for (const [lbl, v] of Object.entries(kp)) {
        const x = await kpi(lbl);
        ok(`Posisi (${st}): ${lbl}`, v, x && [rata(x[0]), rata(x[1])]);
      }
    }
    await p.click('#posSt button[data-v="tidaksah"]');
    await p.waitForTimeout(300);
    const ts = await p.evaluate(() => (document.querySelector('#v-pos .strip') || {}).textContent || '');
    ok('Posisi (tidak sah): jalur', true, /1 posisi tidak dikira/.test(rata(ts)));
    // ---- Lagi
    ok('tab lagi (Sistem)', 'v-sistem', await tab('lagi'));
    await p.waitForTimeout(300);
  } catch (e) {
    gagal.push(L + 'larian terhenti: ' + String(e && e.message || e).split('\n')[0]);
  } finally {
    await ctx.close();
  }
  ok('tiada ralat halaman/konsol', [], ralat.slice(0, 10));
}

(async () => {
  const fail = path.join(os.tmpdir(), `uji_halaman_${process.pid}.html`), fail2 = path.join(os.tmpdir(), `uji_halaman_${process.pid}_hi.html`);
  fs.writeFileSync(fail, bina(DB));
  fs.writeFileSync(fail2, bina(Object.assign({}, DB, { 'harian/hari_ini': HI })));
  const b = await chromium.launch();
  try {
    for (const lebar of [1400, 390]) await larian(b, fail, lebar);   // desktop dan telefon (TELEFON: <= 760px)
    for (const lebar of [1400, 390]) await larian(b, fail2, lebar, 'hari_ini');
  } finally {
    await b.close();
    fs.unlinkSync(fail);
    fs.unlinkSync(fail2);
  }
  console.log(`uji_halaman: ${lulus.length} lulus, ${gagal.length} gagal (${path.relative(process.cwd(), HALAMAN) || HALAMAN})`);
  gagal.forEach(g => console.log('  GAGAL ' + g));
  process.exit(gagal.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
