# paparan_awal.py — PAPARAN AWAL dashboard sejurus selepas tutup AS (keputusan pengguna 13 Nov 2026: "selepas pasaran
# usa tutup sepatutnya sama" dengan Moomoo).
#
# Kenapa: harian.yml menunggu data yfinance muktamad (>= 00:20 UTC; lalai 05:07 UTC) sebelum menilai posisi, jadi db
# dashboard ketinggalan satu sesi dari tutup AS (~05:00 MYT) hingga tolakan petang. Skrip ini menilai posisi Papertrade C
# dengan tarikan harga_harian.yml sejurus selepas tutup (data/harga/terkini.csv) dalam SALINAN BacktestShariah2, lalu
# menjana db (jana_db.py --awal) untuk ditolak oleh sesi Claude (jadual/paparan_awal.md).
#
# Batas: repo TIDAK disentuh dan tiada apa dikomit; keputusan rasmi kekal harian.yml dengan data muktamad. Tiada imbasan
# (senarai beli / watchlist kekal sesi sebelumnya).
# Ketepatan tarikan awal (diukur 13 Nov 2026, 8 sesi, tarikan ~22:20 UTC lawan tarikan harian.yml ~06:xx UTC): harga TUTUP
# sama (0 beza > 0.1% dalam 7/8 sesi); harga BUKA ~35 saham berbeza > 0.5% (masih berubah pada 00:57 UTC; muktamad
# pada 03:49 UTC); ~40–48 saham tiada bar sesi itu (33/775 saham posisi terbuka pada 12 Nov). Saham tanpa bar diisi
# daripada carta Yahoo v8 (isi_bar: tutup = regularMarketPrice; buka = lilin 5 minit pertama), dalam salinan sahaja.
#
#   python3 BacktestShariah2/standard/paparan_awal.py --kerja <dir> --keluar <dir> [--versi versi.json] [--tunggu 1200]
#   Keluar 0 + JSON: {"langkau": sebab} (tiada apa untuk ditolak) atau {"sesi", "keluar", "batch", ...}.
import argparse, json, os, shutil, subprocess, sys, time

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(HERE)
ROOT = os.path.dirname(BS2)
STATUS_HARGA = os.path.join('data', 'harga', 'status.json')
STATUS_PT = os.path.join('papertrade', 'status_harian.json')


def baca(p):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def sesi_jangka(masa=None):
    """Sesi NYSE terakhir yang sudah tutup (16:00 NY + 20 minit), 'YYYY-MM-DD'."""
    import exchange_calendars as xc
    c = xc.get_calendar('XNYS')
    ny = (masa or pd.Timestamp.now(tz='UTC')).tz_convert('America/New_York')
    hari = ny.normalize().tz_localize(None)
    ses = [s for s in c.sessions_in_range(hari - pd.Timedelta(days=10), hari)
           if pd.Timestamp(f'{s.date()} 16:20', tz='America/New_York') <= ny]
    return str(ses[-1].date()) if ses else ''


def keadaan(bs2, masa=None):
    """(sebab_langkau atau None, sesi_data, sesi_rasmi, sesi_jangka)."""
    tk = baca(os.path.join(bs2, STATUS_HARGA)).get('terkini', {})
    data = str(tk.get('sesi', ''))
    data = f'{data[:4]}-{data[4:6]}-{data[6:]}' if len(data) == 8 else ''
    rasmi = baca(os.path.join(bs2, STATUS_PT)).get('malam', {}).get('sesi', '')
    jangka = sesi_jangka(masa)
    if not jangka:
        return 'tiada sesi NYSE', data, rasmi, jangka
    if rasmi >= jangka:
        return f'harian.yml sudah memproses {rasmi}: guna tolak_db.md biasa', data, rasmi, jangka
    if data < jangka:
        return f'harga_harian.yml belum menarik sesi {jangka} (terkini.csv = {data or "tiada"})', data, rasmi, jangka
    return None, data, rasmi, jangka


def ke_yahoo(t):
    return t.replace('.', '-')


def bar_carta(t, sesi, sesi_http=None):
    """Bar harian sesi 'YYYY-MM-DD' bagi ticker t daripada carta Yahoo v8 (5 minit + meta), atau None."""
    import requests
    h = sesi_http or requests
    try:
        r = h.get(f'https://query1.finance.yahoo.com/v8/finance/chart/{ke_yahoo(t)}?range=5d&interval=5m',
                  headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
        d = r.json()['chart']['result'][0]
    except Exception:
        return None
    m = d.get('meta', {}); ts = d.get('timestamp') or []; q = (d.get('indicators', {}).get('quote') or [{}])[0]
    if not m.get('regularMarketPrice') or not m.get('regularMarketTime'):
        return None
    hari = pd.Timestamp(m['regularMarketTime'], unit='s', tz='UTC').tz_convert('America/New_York')
    if str(hari.date()) != sesi or hari.hour < 16:   # harga tutup sesi itu sahaja, bukan harga semasa pasaran
        return None
    x = pd.DataFrame(dict(t=pd.to_datetime(ts, unit='s', utc=True).tz_convert('America/New_York'), o=q.get('open'),
                          h=q.get('high'), l=q.get('low'), v=q.get('volume'))).dropna(subset=['o'])
    x = x[(x.t.dt.date.astype(str) == sesi) & (x.t.dt.hour * 60 + x.t.dt.minute >= 570) & (x.t.dt.hour < 16)]
    c = float(m['regularMarketPrice'])
    o = float(x.o.iloc[0]) if len(x) else c
    hi = max([c, o] + [v for v in (m.get('regularMarketDayHigh'), x.h.max() if len(x) else None) if v == v and v])
    lo = min([c, o] + [v for v in (m.get('regularMarketDayLow'), x.l.min() if len(x) else None) if v == v and v])
    vol = int(m.get('regularMarketVolume') or (x.v.sum() if len(x) else 0))
    return dict(ticker=t, date=int(sesi.replace('-', '')), open=round(o, 4), high=round(float(hi), 4), low=round(float(lo), 4),
                close=round(c, 4), volume=vol)


def isi_bar(harga_dir, sesi, semua=False):
    """Tambah bar sesi bagi saham tanpa bar dalam terkini.csv salinan (semua=True: setiap saham universe). Pulang bilangan."""
    import requests
    p = os.path.join(harga_dir, 'terkini.csv')
    tk = pd.read_csv(p) if os.path.exists(p) else pd.DataFrame(columns=['ticker', 'date', 'open', 'high', 'low', 'close', 'volume'])
    ada = set(tk.loc[tk.date == int(sesi.replace('-', '')), 'ticker'])
    st = baca(os.path.join(harga_dir, 'status.json')).get('terkini', {})
    if semua or not ada:
        u = os.path.join(harga_dir, 'univ.txt')
        calon = sorted({x.strip().replace('US.', '') for x in open(u) if x.strip()} if os.path.exists(u) else set(tk.ticker))
    else:
        calon = sorted(set(st.get('tiada_bar_sesi', [])) | set(st.get('tiada_data', [])))
    calon = [t for t in calon if t not in ada]
    h = requests.Session(); baru = []
    for t in calon:
        b = bar_carta(t, sesi, h)
        if b:
            baru.append(b)
        time.sleep(0.15)
    if baru:
        pd.concat([tk, pd.DataFrame(baru)], ignore_index=True).to_csv(p, index=False)
    return dict(dicuba=len(calon), diisi=len(baru))


def jalan(cmd, cwd, log):
    t0 = time.time()
    r = subprocess.run([sys.executable] + cmd, cwd=cwd, capture_output=True, text=True)
    log.append(dict(langkah=os.path.basename(cmd[0]) + (' ' + cmd[1] if len(cmd) > 1 and not cmd[1].startswith('-') else ''),
                    kod=r.returncode, saat=round(time.time() - t0)))
    if r.returncode:
        raise SystemExit(json.dumps(dict(gagal=log[-1], stderr=r.stderr[-1500:]), ensure_ascii=False))
    return r.stdout


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--kerja', required=True, help='folder salinan (dipadam dan dibina semula)')
    ap.add_argument('--keluar', required=True, help='folder db (jana_db.py --keluar)')
    ap.add_argument('--versi', help='daftar meta/versi_db (jana_db.py --versi)')
    ap.add_argument('--tunggu', type=int, default=0, help='saat menunggu terkini.csv sesi baharu (git pull --ff-only setiap 60 s)')
    ap.add_argument('--proses', type=int, default=4)
    a = ap.parse_args(argv)
    sebab, data, rasmi, jangka = keadaan(BS2)
    tamat = time.time() + a.tunggu
    while sebab and sebab.startswith('harga_harian.yml') and time.time() < tamat:
        time.sleep(60)
        subprocess.run(['git', '-C', ROOT, 'pull', '-q', '--ff-only', 'origin', 'main'], capture_output=True)
        sebab, data, rasmi, jangka = keadaan(BS2)
    # harga_harian.yml masih belum menarik sesi itu: bina SEMUA bar sesi daripada carta Yahoo (salinan sahaja)
    semua = bool(sebab and sebab.startswith('harga_harian.yml'))
    if semua:
        sebab = None
    if sebab:
        print(json.dumps(dict(langkau=sebab, sesi_data=data, sesi_rasmi=rasmi, sesi_jangka=jangka), ensure_ascii=False))
        return 0
    log = []
    kerja = os.path.abspath(a.kerja)
    shutil.rmtree(kerja, ignore_errors=True); os.makedirs(kerja)
    t0 = time.time()
    shutil.copytree(BS2, os.path.join(kerja, 'BacktestShariah2'), symlinks=True,
                    ignore=shutil.ignore_patterns('__pycache__', 'kajian', 'bayang'))
    log.append(dict(langkah='salin', kod=0, saat=round(time.time() - t0)))
    S2 = os.path.join(kerja, 'BacktestShariah2'); std = os.path.join(S2, 'standard')
    pt = os.path.join(S2, 'papertrade'); stor = os.path.join(S2, 'data', 'harga', 'stor')
    os.environ.pop('LEJAR_STOR', None)
    t0 = time.time(); isi = isi_bar(os.path.join(S2, 'data', 'harga'), jangka, semua)
    log.append(dict(langkah='isi_bar carta Yahoo' + (' (semua)' if semua else ''), kod=0, saat=round(time.time() - t0), **isi))
    jalan([os.path.join(std, 'lejar.py'), 'stor'], kerja, log)
    jalan([os.path.join(std, 'harian_c.py'), 'malam', '--folder', pt, '--stor', stor, '--isyarat', '', '--tanpa-imbas',
           '--paksa', '--proses', str(a.proses)], kerja, log)
    sesi = baca(os.path.join(S2, STATUS_PT)).get('malam', {}).get('sesi', '')
    if sesi != jangka:
        raise SystemExit(json.dumps(dict(gagal=f'salinan memproses {sesi}, jangka {jangka}', langkah=log), ensure_ascii=False))
    jalan([os.path.join(std, 'pecah_claude.py'), '--pecah', '--folder', pt], kerja, log)
    jalan([os.path.join(std, 'sahkan.py'), '--betulkan', '--folder', pt], kerja, log)
    cmd = [os.path.join(std, 'jana_db.py'), '--awal', '--folder', pt, '--stor', stor, '--keluar', os.path.abspath(a.keluar)]
    if a.versi:
        cmd += ['--versi', os.path.abspath(a.versi)]
    jalan(cmd, kerja, log)
    ring = baca(os.path.join(a.keluar, 'ringkas.json'))
    print(json.dumps(dict(sesi=sesi, sesi_rasmi=rasmi, keluar=os.path.abspath(a.keluar), batch=ring.get('batch', []),
                          dokumen=ring.get('dokumen'), langkah=log), ensure_ascii=False, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
