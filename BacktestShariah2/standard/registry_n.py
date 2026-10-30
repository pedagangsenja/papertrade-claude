"""Registry Nxx — kombinasi daripada pakar, forum dan platform sosial.

Keluarga KEDUA selari dengan Mxx (keputusan pengguna 30 Okt 2026):
  Mxx = kaedah lengkap daripada pedagang bernama, sudah dikodkan dalam `kod/kaedah/`
  Nxx = kombinasi indikator yang dikumpul daripada sumber awam, didaftar dahulu, diuji kemudian

Ini SATU sumber kebenaran. Ia menulis dua keluaran:
  `data/registry_N.csv`        — boleh dibaca mesin, untuk skrip ujian
  `spec/SPEC_SEMUA_N.md`       — boleh dibaca manusia, selari dengan SPEC_SEMUA_KAEDAH.md

Status: DIUJI (ada hasil), SEDIA (indikator sudah ada), PERLU:<x> (indikator baharu diperlukan).

Guna: python3 BacktestShariah2/standard/registry_n.py
"""
import csv
import os
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV = os.path.join(AKAR, 'BacktestShariah2', 'data', 'registry_N.csv')
SPEC = os.path.join(AKAR, 'BacktestShariah2', 'spec', 'SPEC_SEMUA_N.md')

LAJUR = ['id', 'keluarga', 'nama', 'masuk', 'sumber', 'platform', 'status', 'nota']

# (id, keluarga, nama, peraturan masuk, sumber, platform, status, nota)
MASUK = [
 ('N01', 'MA', 'MA10 silang MA20 + volum', 'ma10 silang naik ma20 DAN vol_n50 >= 1.2',
  'permintaan pengguna', 'pengguna', 'DIUJI',
  'lift +0.123 latih / +0.392 tahan; TERBAIK daripada 40 (KOMBINASI.md)'),
 ('N02', 'MA', 'MA20 silang MA50', 'ma20 silang naik ma50', 'klasik', 'umum', 'DIUJI',
  'lift negatif pada kedua-dua tingkap'),
 ('N03', 'MA', 'MA20 silang MA200', 'ma20 silang naik ma200', 'skrip MA+ATR', 'TradingView',
  'DIUJI', 'lift -0.342 latih / +0.209 tahan — tidak konsisten'),
 ('N04', 'MA', 'EMA20>EMA50 + RSI 50-70', 'ema20 > ema50 DAN 50 <= rsi14 <= 70',
  'skrip awam', 'TradingView', 'DIUJI', 'lift negatif'),
 ('N05', 'MA', 'tutup>EMA20>SMA100 + volum',
  'tutup > ema20 DAN ema20 > sma100 DAN vol_n50 >= 1.2', 'pedagang forum', 'babypips', 'DIUJI',
  'lift negatif'),
 ('N06', 'MA', 'Golden cross MA50/MA200', 'ma50 silang naik ma200', 'klasik', 'umum', 'SEDIA',
  'hari_gc sudah ada'),
 ('N07', 'MA', 'Tiga MA tersusun', 'hari pertama ma10 > ma20 > ma50', 'triple-MA klasik',
  'umum', 'SEDIA', ''),
 ('N08', 'MA', 'tutup>EMA20 tidak terlalu jauh',
  'tutup > ema20 DAN (tutup - ema20) <= 1.5 x atr14', 'pedagang forum', 'babypips', 'SEDIA',
  'sumber menegaskan LANGKAU jika terlalu jauh dari EMA20'),
 ('N09', 'MA', 'Undur EMA10 + penapis EMA50',
  'tutup > ema10 DAN tutup[-1] < ema10[-1] DAN tutup > ema50', 'skrip 10ema', 'TradingView',
  'SEDIA', ''),
 ('N10', 'RSI', 'RSI14 silang SMA14(RSI)', 'rsi14 silang naik SMA14(rsi14)', 'skrip sumber terbuka',
  'TradingView', 'DIUJI', 'lift +0.016 / +0.006 — hampir sifar'),
 ('N11', 'RSI', 'RSI 40-50 + tutup>MA50', '40 <= rsi14 <= 50 DAN tutup > ma50',
  'pedagang forum', 'forum', 'DIUJI', 'lift negatif'),
 ('N12', 'RSI', 'RSI 40-60 + EMA20 + MA50 naik',
  'tutup > ema20 DAN cerun_ma50 > 0 DAN 40 <= rsi14 <= 60', 'konsensus blog', 'blog', 'DIUJI',
  'lift negatif'),
 ('N13', 'RSI', 'RSI<=30 + EMA + MACD + volum',
  'ema20 > ema50 DAN rsi14 <= 30 DAN macd > 0 DAN vol_n50 >= 1.5', 'skrip awam', 'TradingView',
  'DIUJI', 'lift negatif'),
 ('N14', 'RSI', 'Connors RSI2<5 + SMA200', 'rsi2 < 5 DAN tutup > ma200',
  'Connors (varian 200-hari)', 'buku/blog', 'PERLU:ma5',
  'keluar asal: tutup > SMA5 ATAU tutup < SMA200'),
 ('N15', 'RSI', 'Connors RSI2<10 + SMA200', 'rsi2 < 10 DAN tutup > ma200', 'EA MQL5', 'MQL5',
  'SEDIA', 'keluar asal rsi2 > 65'),
 ('N16', 'RSI', 'RSI2<10 tanpa penapis', 'rsi2 < 10', 'Quantified Strategies', 'YouTube/Substack',
  'SEDIA', 'keluar asal rsi2 > 60; pegang 1-10 hari'),
 ('N17', 'RSI', 'RSI14 silang naik 30', 'rsi14 silang naik 30', 'klasik terlebih jual', 'umum',
  'SEDIA', ''),
 ('N18', 'RSI', 'RSI 30-50 pullback', '30 <= rsi14 <= 50 DAN tutup > ma200',
  'Quantified Strategies', 'YouTube/Substack', 'SEDIA',
  'sumber lapor CAGR 5.3%, 196 dagangan, menang 81% pada S&P 500'),
 ('N19', 'BB', 'Bawah jalur BB + RSI<30', 'bb_pctb < 0 DAN rsi14 < 30', 'LuxAlgo', 'LuxAlgo',
  'SEDIA', 'keluar asal rsi14 > 70'),
 ('N20', 'BB', 'Kembali masuk jalur + RSI silang 30',
  'bb_pctb[-1] < 0 DAN bb_pctb > 0 DAN rsi14 silang naik 30', 'therighttrader', 'blog', 'SEDIA',
  'henti pada ekstrem luar; keluar jalur tengah'),
 ('N21', 'BB', 'BB + RSI 40/60', 'bb_pctb < 20 DAN rsi14 > 40', 'Fmz', 'Fmz', 'SEDIA',
  'sasaran untung 2% tetap'),
 ('N22', 'BB', 'BB pecah atas + RSI', 'bb_pctb > 100 DAN rsi14 > 50', 'StockSharp', 'StockSharp',
  'SEDIA', 'keluar jalur tengah'),
 ('N23', 'BB', 'BB squeeze kemudian pecah', 'bb_squeeze[-1] DAN tutup > ema20', 'klasik', 'umum',
  'SEDIA', ''),
 ('N24', 'TREND', 'Supertrend(10,3) + ADX>20', 'supertrend > 0 DAN adx14 > 20',
  'therighttrader', 'blog', 'SEDIA', 'sumber: ATR 10, pengganda 3, ADX Wilder 14, ambang 20'),
 ('N25', 'TREND', 'Supertrend + EMA + ADX>23', 'supertrend > 0 DAN tutup > ema20 DAN adx14 > 23',
  'skrip awam', 'TradingView', 'SEDIA', ''),
 ('N26', 'TREND', 'Tiga Supertrend + EMA + ADX',
  'ketiga supertrend > 0 DAN tutup > ema20 DAN adx14 > ambang', 'LuxAlgo', 'LuxAlgo',
  'PERLU:supertrend3', 'tiga pengganda ATR berbeza'),
 ('N27', 'TREND', 'Ichimoku atas awan', 'atas_awan DAN tenkan_atas', 'klasik', 'umum', 'SEDIA',
  ''),
 ('N28', 'TREND', 'ADX>25 + DI+ > DI-', 'adx14 > 25 DAN mdi < adx14', 'Wilder', 'buku', 'SEDIA',
  'proksi DI daripada lajur sedia ada'),
 ('N29', 'TREND', 'PSAR naik + tutup>MA50', 'psar_arah > 0 DAN tutup > ma50', 'klasik', 'umum',
  'SEDIA', ''),
 ('N30', 'PECAH', 'Turtle sistem 1', 'donchian20 pecah', 'Dennis/Eckhardt', 'buku',
  'PERLU:donchian10', 'henti 2xATR20; keluar Donchian10 bertentangan'),
 ('N31', 'PECAH', 'Turtle sistem 2', 'donchian55 pecah', 'Dennis/Eckhardt', 'buku', 'SEDIA', ''),
 ('N32', 'PECAH', 'Donchian50 (Darvas ringkas)', 'donchian50 pecah', 'EA Darvas', 'MQL5',
  'PERLU:donchian50', ''),
 ('N33', 'PECAH', 'Donchian20 + penapis MA200', 'donchian20 pecah DAN j_ma200 > 0',
  'skrip awam', 'TradingView', 'SEDIA', 'henti pada jalur bertentangan'),
 ('N34', 'PECAH', 'Darvas Box', 'pecah atas kotak Darvas', 'Darvas', 'buku', 'PERLU:darvas',
  'tiada peraturan berangka standard; henti bawah kotak'),
 ('N35', 'PECAH', 'Pecah 52 minggu tinggi', 'breakout_52w', 'klasik', 'umum', 'SEDIA', ''),
 ('N36', 'PECAH', 'Pocket pivot', 'pocket_pivot', 'Morales/Kacher', 'buku', 'SEDIA',
  'juga M35 dalam keluarga Mxx'),
 ('N37', 'PECAH', 'Gap and go', 'gap_and_go', 'klasik intraday', 'umum', 'SEDIA', ''),
 ('N38', 'PECAH', 'VCP pecah', 'vcp', 'Minervini', 'buku', 'SEDIA', 'juga M06'),
 ('N39', 'PECAH', 'NR7 kemudian pecah', 'nr7[-1] DAN donchian20', 'Crabel', 'buku', 'SEDIA', ''),
 ('N40', 'VOLUM', 'OBV tinggi baharu + MA50', 'obv_tinggi_baru DAN tutup > ma50', 'klasik',
  'umum', 'SEDIA', ''),
 ('N41', 'VOLUM', 'CMF20>0 + tutup>EMA20', 'cmf20 > 0 DAN tutup > ema20', 'Chaikin', 'buku',
  'SEDIA', ''),
 ('N42', 'VOLUM', 'Lonjakan volum 2x', 'vol_n50 >= 2.0 DAN tutup > tutup[-1]', 'umum', 'umum',
  'SEDIA', ''),
 ('N43', 'UNDUR', 'Undur EMA8 + penapis MA50',
  'tutup[-1] < ema9[-1] DAN tutup > ema9 DAN tutup > ma50', 'Morpheus Trading (Deel)', 'blog',
  'SEDIA', 'sumber guna EMA8; repo ada ema9 — proksi terdekat'),
 ('N44', 'UNDUR', 'Undur EMA21 + EMA21>MA50',
  'tutup > ema21 DAN tutup[-1] < ema21[-1] DAN ema21 > ma50', 'panduan 8/21 EMA', 'blog',
  'SEDIA', 'sumber: 21 EMA atas 50 EMA dan harga atas kedua-duanya'),
 ('N45', 'UNDUR', 'Undur EMA21 cerun positif',
  'tutup > ema21 DAN cerun_ema21 > 0 DAN julat10 < julat20', 'panduan 8/21 EMA', 'blog',
  'SEDIA', 'sumber syarat "EMA 45 darjah" — proksi cerun; elak EMA rata'),
 ('N46', 'UNDUR', 'Pecah tinggi bar penolakan',
  'rendah[-1] <= ema21[-1] DAN tutup > tinggi[-1]', 'journalplus/kotakneo', 'blog', 'SEDIA',
  'sumber TEGAS: masuk pada pecah tinggi lilin penolakan, BUKAN pada undur itu sendiri'),
 ('N47', 'KETAT', 'NR7 + EMA9>EMA21', 'nr7 DAN ema9 > ema21 DAN tutup > ema21', 'Stockezee',
  'screener', 'SEDIA', 'sumber asal 10EMA>20EMA pasaran India; ema9/ema21 proksi'),
 ('N48', 'KETAT', 'Inside day pecah', 'inside_day[-1] DAN tutup > tinggi[-1]', 'Crabel', 'buku',
  'SEDIA', 'order henti atas tinggi inside day — tidak meramal arah'),
 ('N49', 'KETAT', 'NR7 + inside day serentak', 'nr7 DAN inside_day', 'Crabel', 'buku', 'SEDIA',
  'Crabel: gabungan dua ini paling mampat'),
 ('N50', 'KETAT', 'Mampat + pecah volum 1.5x',
  'julat10 < 0.5 x julat20 DAN vol_n50 >= 1.5 DAN tutup > tinggi[-1]', 'Stockezee', 'screener',
  'SEDIA', 'sumber tolak pecah bervolum lemah (< 1.5x) dan langkau 5 hari sebelum earnings'),
 ('N51', 'KETAT', 'BB squeeze + Supertrend', 'bb_squeeze DAN supertrend > 0',
  'Squeeze Momentum (LazyBear)', 'YouTube', 'SEDIA', ''),
 ('N52', 'KETAT', 'Squeeze lepas + atas MA200',
  'bb_squeeze[-1] DAN bb_lebar > bb_lebar[-1] DAN j_ma200 > 0', 'Squeeze + EMA200', 'YouTube',
  'SEDIA', 'video guna EMA200 sebagai penapis trend'),
 ('N53', 'ADX', 'Supertrend + ADX>25', 'supertrend > 0 DAN adx14 > 25', 'StockSharp',
  'StockSharp', 'SEDIA', 'keluar asal: supertrend berbalik (dipakai sebagai henti ekor)'),
 ('N54', 'ADX', 'Supertrend + RSI>50', 'supertrend > 0 DAN rsi14 > 50', 'skrip posisional',
  'TradingView', 'SEDIA', 'ADX pilihan dalam sumber'),
 ('N55', 'ADX', 'BB + RSI + ADX>20', 'bb_pctb < 20 DAN rsi14 > 40 DAN adx14 > 20',
  '"Super Swing Strategy"', 'TradingView', 'SEDIA', ''),
 ('N56', 'ADX', 'RSI>50 + ADX>20', 'rsi14 > 50 DAN adx14 > 20', 'MTF RSI-ADX-ATR',
  'TradingView', 'SEDIA', 'henti ATR dalam sumber'),
 ('N57', 'ADX', 'ADX bangkit daripada <20', 'adx14 > 20 DAN adx14[-1] <= 20 DAN tutup > ma50',
  'Wilder', 'buku', 'SEDIA', ''),
 ('N58', 'ADX', 'DI+ silang DI- + ADX>20', 'pdi silang naik mdi DAN adx14 > 20', 'Wilder',
  'buku', 'SEDIA', ''),
 ('N59', 'VWAP', 'tutup>VWAP + ADX>25', 'tutup > vwap20 DAN adx14 > 25', 'StockSharp',
  'StockSharp', 'PERLU:vwap20',
  'sumber lapor ~157%/tahun tetapi pada KRIPTO, bukan saham; keluar bila adx14 < 20'),
 ('N60', 'VWAP', 'VWAP + ADX + nisbah volum',
  'tutup > vwap20 DAN adx14 > 20 DAN vol_n50 >= 1.5', 'SwingTrade ADX v6', 'TradingView',
  'PERLU:vwap20', ''),
 ('N61', 'VWAP', 'VWAP berankor', 'tutup > vwap_ankor sejak pecah terakhir', 'pedagang X',
  'X/Twitter', 'PERLU:vwap_ankor', 'tiada definisi standard bagi titik ankor'),
 ('N62', 'POLA', 'Flat base pecah', 'julat20 <= 0.08 x tutup DAN tutup > tinggi20[-1]',
  'Tradezella/O’Neil', 'blog', 'SEDIA', 'sumber: MA mengetat dan julat harian mengecil'),
 ('N63', 'POLA', 'High tight flag', 'gap >= 3% DAN vol_n50 >= 2.0 pada hari gap DAN '
  'sisi 3-8 hari DAN tutup > tinggi bendera', 'skrip gaya Minervini', 'TradingView',
  'PERLU:htf', ''),
 ('N64', 'POLA', 'Episodic pivot', 'gap_and_go DAN vol_n50 >= 2.0', 'Qullamaggie/Tradezella',
  'blog/YouTube', 'SEDIA', 'sumber tawar "high-volume close" sebagai masuk kedua'),
 ('N65', 'POLA', 'Gap 4% + volum + hampir 52w',
  'gap_and_go DAN vol_n50 >= 1.5 DAN j_52w_tinggi >= -0.05', 'pemeriksa pramasa', 'blog',
  'SEDIA', 'sumber: gap 4%, volum pramasa > 100k, pemangkin dalam 24 jam'),
 ('N66', 'POLA', '52w tinggi + pengesahan 1%', 'tutup > 1.01 x tinggi_52w[-1]',
  'panduan amaran pecah', 'blog', 'SEDIA',
  'sumber: cetus 1-2% ATAS paras untuk tapis pecah palsu; elak saham tipis'),
 ('N67', 'POLA', 'Hammer di MA50', 'hammer DAN rendah <= ma50 DAN tutup > ma50', 'klasik lilin',
  'umum', 'SEDIA', ''),
 ('N68', 'POLA', 'Bullish engulfing + EMA21', 'bullish_engulfing DAN tutup > ema21',
  'klasik lilin', 'umum', 'SEDIA', ''),
 ('N69', 'KEKUATAN', 'RS kuintil 5 + sektor atas MA50',
  'rs_spy_6b dalam kuintil teratas DAN sektor_atas_ma50', 'O’Neil/Minervini', 'buku',
  'SEDIA', 'dua daripada tiga tiang yang DITINGGALKAN daripada grid 672 setup'),
 ('N70', 'KEKUATAN', 'Garis RS tinggi baharu', 'garis_rs_tinggi', 'Minervini', 'buku', 'SEDIA',
  ''),
 ('N71', 'KEKUATAN', 'RS + pecah + rejim SPY',
  'rs_spy_6b kuintil teratas DAN sektor_atas_ma50 DAN donchian20 DAN '
  'spy > ma50 DAN spy > ma200', 'pakej Sistem A', 'buku', 'DIUJI',
  'Sistem A penuh: CAGR -1.03%, MDD -40.65%, sebaran benih 4.01 (SISTEM.md)'),
 ('N72', 'KEKUATAN', 'Momentum Clenow 90 hari',
  'skor = (exp(cerun regresi log 90 hari x 252) - 1) x R^2; ambil 20 teratas, imbang bulanan',
  'Clenow', 'buku', 'DIUJI',
  'Sistem B: CAGR +6.38%, MDD -11.59%, sebaran benih 0.00; pendedahan hanya 35.4%'),
]

# (id, peraturan keluar, sumber, platform, status, nota)
KELUAR = [
 ('X01', 'henti 1.5 x ATR14, sasaran 1 x ATR14', 'pedagang forum', 'babypips', 'DIUJI',
  'asas tahan -0.281% — MENUKAR ASAS JADI NEGATIF; kadar menang 61.1%'),
 ('X02', 'henti 2 x ATR14, sasaran 4 x ATR14', 'pelbagai', 'umum', 'DIUJI', 'asas tahan +0.953%'),
 ('X03', 'henti 2 x ATR14, pegang 63 sesi', 'asas kajian', 'repo', 'DIUJI',
  'asas tahan +2.595% — TERBAIK; kadar menang 30.2%'),
 ('X04', 'ekori 2 x ATR14', 'pelbagai', 'umum', 'DIUJI', 'asas tahan +1.156%'),
 ('X05', 'keluar pada jalur tengah BB(20)', 'therighttrader/StockSharp', 'blog', 'SEDIA', ''),
 ('X06', 'keluar bila tutup < SMA5', 'Connors', 'buku', 'PERLU:ma5', ''),
 ('X07', 'keluar bila rsi2 > 60', 'Quantified Strategies', 'YouTube/Substack', 'SEDIA', ''),
 ('X08', 'keluar bila rsi2 > 80', 'Connors', 'buku', 'SEDIA',
  'sumber lapor CAGR 9% pada SPY 1993+, melabur hanya ~28% masa'),
 ('X09', 'keluar bila rsi2 > 65', 'EA MQL5', 'MQL5', 'SEDIA', ''),
 ('X10', 'sasaran untung 2% tetap', 'Fmz', 'Fmz', 'SEDIA', ''),
 ('X11', 'keluar Donchian10 bertentangan', 'Turtle', 'buku', 'PERLU:donchian10', ''),
 ('X12', 'henti pada ekstrem luar jalur BB', 'therighttrader', 'blog', 'SEDIA', ''),
 ('X13', 'keluar bila rsi14 > 70', 'LuxAlgo', 'LuxAlgo', 'SEDIA', ''),
 ('X14', 'keluar bila rsi14 silang naik 50', 'skrip awam', 'TradingView', 'SEDIA', ''),
 ('X15', 'ekori Chandelier 4 x ATR14', 'lorong 2 repo', 'repo', 'SEDIA',
  'sudah dipakai Papertrade C'),
 ('X16', 'keluar bila supertrend berbalik (henti ekor)', 'StockSharp', 'StockSharp', 'SEDIA',
  ''),
 ('X17', 'keluar bila adx14 < 20', 'StockSharp VWAP+ADX', 'StockSharp', 'SEDIA', ''),
 ('X18', 'keluar Donchian20 bertentangan', 'Turtle sistem 2', 'buku', 'SEDIA', ''),
 ('X19', 'ekori EMA21 (jual bila tutup < ema21)', 'panduan 8/21 EMA', 'blog', 'SEDIA', ''),
 ('X20', 'separa 1/3 pada 2R, ekori baki dengan EMA20', 'panduan 8/21 EMA', 'blog', 'SEDIA',
  'sumber: ambil separa pada 2R atau tinggi swing terdahulu'),
 ('X21', 'jual 1/3 pada +10% atau hari-5, ekori MA20', 'Minervini/Qullamaggie', 'buku', 'DIUJI',
  'komponen Sistem A (SISTEM.md)'),
 ('X22', 'henti keras -8% daripada harga masuk', 'O’Neil', 'buku', 'DIUJI',
  'komponen Sistem A'),
 ('X23', 'keluar bila jatuh keluar 20 teratas pangkat momentum; imbang bulanan', 'Clenow',
  'buku', 'DIUJI', 'komponen Sistem B; sebaran benih 0.00'),
 ('X24', 'keluar pada tinggi swing terdahulu', 'umum', 'blog', 'PERLU:tinggi_swing', ''),
 ('X25', 'henti 1% bawah EMA21 atau bawah rendah undur, mana lebih ketat',
  'panduan 8/21 EMA', 'blog', 'SEDIA', ''),
]


def semak():
    """Pulangkan senarai masalah; kosong bermakna registry konsisten."""
    masalah = []
    for nama, baris, awalan, n_medan in (('MASUK', MASUK, 'N', 8), ('KELUAR', KELUAR, 'X', 6)):
        ids = [b[0] for b in baris]
        if len(set(ids)) != len(ids):
            masalah.append(f'{nama}: id berulang')
        for i, b in enumerate(baris, start=1):
            if len(b) != n_medan:
                masalah.append(f'{nama} {b[0]}: {len(b)} medan, sepatutnya {n_medan}')
            jangka = f'{awalan}{i:02d}'
            if b[0] != jangka:
                masalah.append(f'{nama}: {b[0]} tidak berturutan, sepatutnya {jangka}')
            st = b[6] if awalan == 'N' else b[4]
            if st not in ('DIUJI', 'SEDIA') and not st.startswith('PERLU:'):
                masalah.append(f'{nama} {b[0]}: status "{st}" tidak dikenali')
    return masalah


def tulis_csv():
    os.makedirs(os.path.dirname(CSV), exist_ok=True)
    with open(CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(LAJUR)
        for b in MASUK:
            w.writerow(list(b))
        for b in KELUAR:
            # keluar: id, keluarga KELUAR, nama = peraturan, masuk kosong
            w.writerow([b[0], 'KELUAR', b[1], '', b[2], b[3], b[4], b[5]])
    return len(MASUK) + len(KELUAR)


def _kira(baris, idx_status):
    d = {'DIUJI': 0, 'SEDIA': 0, 'PERLU': 0}
    for b in baris:
        st = b[idx_status]
        d['PERLU' if st.startswith('PERLU:') else st] += 1
    return d


def tulis_spec():
    km = _kira(MASUK, 6)
    kk = _kira(KELUAR, 4)
    perlu = sorted({b[6].split(':', 1)[1] for b in MASUK if b[6].startswith('PERLU:')} |
                   {b[4].split(':', 1)[1] for b in KELUAR if b[4].startswith('PERLU:')})
    L = []
    A = L.append
    A('# SPEC SEMUA N — kombinasi daripada pakar, forum dan platform sosial')
    A('')
    A('**Dijana oleh `BacktestShariah2/standard/registry_n.py`. Jangan sunting fail ini '
      'secara manual** — sunting senarai dalam skrip itu, kemudian jalankan semula.')
    A('')
    A('## Mengapa dua keluarga')
    A('')
    A('`Mxx` = kaedah lengkap daripada pedagang bernama, sudah dikodkan dalam '
      '`BacktestShariah2/kod/kaedah/`. Spec: `SPEC_SEMUA_KAEDAH.md`.')
    A('')
    A('`Nxx` = **kombinasi indikator** yang dikumpul daripada sumber awam (TradingView, '
      'babypips, MQL5, LuxAlgo, StockSharp, Fmz, Stockezee, Tradezella, Quantified Strategies, '
      'YouTube, X/Twitter, blog pedagang, buku). Didaftar DAHULU, diuji KEMUDIAN. '
      'Pendaftaran dahulu ialah disiplin pradaftar yang sama seperti REVERSE: senarai penuh '
      'dikomit sebelum keputusan dilihat, supaya bilangan ujian diketahui dan FDR boleh '
      'dikira.')
    A('')
    A('**Dapatan carian web yang penting:** peraturan pedagang **TIDAK diseragamkan**. '
      'Setiap sumber memberi versi berbeza bagi setup yang sama (ambang gap 3%-5%, '
      'pengganda volum 1.5x-2x, ADX 20-25, henti bawah rendah undur lawan bawah EMA). '
      'Jadi setiap baris di bawah ialah **satu versi tertentu daripada satu sumber '
      'tertentu**, bukan "peraturan rasmi" setup itu.')
    A('')
    A('## Status')
    A('')
    A('- `DIUJI` — sudah ada hasil terukur; nota memberi angkanya dan fail laporan.')
    A('- `SEDIA` — semua indikator yang diperlukan sudah dikira oleh kod repo '
      '(`REVERSE/teras/ind.py` atau `REVERSE/step15_setup.py` / `step17_kombinasi.py`); '
      'boleh diuji tanpa kod indikator baharu.')
    A('- `PERLU:<x>` — perlu indikator baharu `<x>` dahulu.')
    A('')
    A(f'Masuk: {len(MASUK)} ({km["DIUJI"]} DIUJI, {km["SEDIA"]} SEDIA, {km["PERLU"]} PERLU). '
      f'Keluar: {len(KELUAR)} ({kk["DIUJI"]} DIUJI, {kk["SEDIA"]} SEDIA, {kk["PERLU"]} PERLU).')
    A('')
    A('Indikator baharu yang diperlukan: ' + (', '.join(f'`{p}`' for p in perlu) or 'tiada') +
      '.')
    A('')
    A('## Peraturan masuk')
    A('')
    for kel in dict.fromkeys(b[1] for b in MASUK):
        A(f'### {kel}')
        A('')
        for b in MASUK:
            if b[1] != kel:
                continue
            _id, _, nama, masuk, sumber, plat, status, nota = b
            A(f'**{_id} {nama}** — `{masuk}` · {sumber} ({plat}) · {status}' +
              (f' · {nota}' if nota else ''))
            A('')
    A('## Peraturan keluar')
    A('')
    A('Keluar diuji **bersilang** dengan masuk, kerana `KOMBINASI.md` menunjukkan keluar '
      'mengubah tanda jangkaan: asas tanpa sasaran +2.595% lawan sasaran 1xATR **-0.281%** '
      'pada tingkap tahan yang sama. Lift mesti dikira lawan asas **keluar yang sama**.')
    A('')
    for b in KELUAR:
        _id, peraturan, sumber, plat, status, nota = b
        A(f'**{_id}** — `{peraturan}` · {sumber} ({plat}) · {status}' +
          (f' · {nota}' if nota else ''))
        A('')
    A('## Cara menguji')
    A('')
    A('1. Pradaftar: tulis `REVERSE/SPEC_<nama>.md` dengan senarai id yang akan diuji, '
      'pecahan LATIH/TAHAN, dan jangkaan priori. Komit sebelum larian.')
    A('2. Kira lift lawan asas keluar yang sama (bukan jangkaan mutlak — kesilapan '
      '`SPEC_SETUP.md` §4).')
    A('3. Syarat lulus: lift positif pada KEDUA-DUA tingkap, BH-FDR q <= 0.05 merentas '
      'bilangan ujian yang dipradaftar, dan jangkaan selepas buang 5% teratas kekal positif.')
    A('4. Setakat ini hanya `N01` (MA10 silang MA20 + volum >= 1.2x) mencapai syarat 1 dan 2; '
      'tiada satu pun mencapai syarat 3.')
    A('')
    os.makedirs(os.path.dirname(SPEC), exist_ok=True)
    with open(SPEC, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    return len(L)


def main():
    masalah = semak()
    if masalah:
        for m in masalah:
            print('MASALAH:', m)
        return 1
    n = tulis_csv()
    tulis_spec()
    km = _kira(MASUK, 6)
    kk = _kira(KELUAR, 4)
    print(f'registry N: {len(MASUK)} masuk + {len(KELUAR)} keluar = {n} baris')
    print(f'  masuk  : {km["DIUJI"]} DIUJI, {km["SEDIA"]} SEDIA, {km["PERLU"]} PERLU')
    print(f'  keluar : {kk["DIUJI"]} DIUJI, {kk["SEDIA"]} SEDIA, {kk["PERLU"]} PERLU')
    print(f'  -> {os.path.relpath(CSV, AKAR)}')
    print(f'  -> {os.path.relpath(SPEC, AKAR)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
