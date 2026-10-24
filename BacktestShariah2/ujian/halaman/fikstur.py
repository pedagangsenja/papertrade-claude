# fikstur.py — data tetap kecil bagi ujian halaman dashboard (uji_halaman.js, Playwright) dan ujian kira_semula.py
# (test_kira_semula.py). Satu sumber: baris CSV Papertrade C, watchlist, stor harga, kalendar earnings, AUTOTUNE dan Papan
# Penganalisis kecil; dokumen db dibina dengan format jana_db.py (baris_db, ringkas_pt, bahagi) supaya halaman membaca bentuk
# yang sama dengan pengeluaran. Angka dijangka (dikira dengan tangan) dalam jangka.json.
#
#   python3 BacktestShariah2/ujian/halaman/fikstur.py      -> tulis semula fikstur_db.json (selepas mengubah data di bawah)
#
# Sesi data S = 2026-10-23 (Jumaat); hari dagangan berikut 2026-10-26.
import csv, json, os, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
BS2 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(BS2, 'standard'))

S = '2026-10-23'
DIBINA = '2026-10-24 06:30 MYT'

_ASAS = dict(unit='1', sumber='harian_c', keluar='False', keluar_henti='False', tutup_semua='False', sektor='Technology',
             industri='Software')
LORONG2_PEGANG = 'Pegang (paras keluar {p}; puncak {q}; 3 hari)'


def _p(**k):
    return dict(_ASAS, **k)


# Papertrade C (claude.csv). Komen = peranan dalam jangka.json.
POSISI = [
    # dipegang lorong kaedah (6): AAA x2, BBB, CCC, FFF, III
    _p(tarikh_beli='2026-10-20', saham='AAA', kaedah='M03', id_kaedah='M03', harga_beli='100', harga_terkini='110',
       untung_pct='10.0', hari='3', henti='95', isyarat_keluar='Pegang (henti 95)', tarikh_isyarat='2026-10-17',
       status_henti=LORONG2_PEGANG.format(p=98, q=110)),
    _p(tarikh_beli='2026-10-21', saham='AAA', kaedah='M07', id_kaedah='M07', harga_beli='104', harga_terkini='110',
       untung_pct='5.77', hari='2', henti='98', isyarat_keluar='Pegang (henti 98)', tarikh_isyarat='2026-10-20',
       status_henti=LORONG2_PEGANG.format(p=99, q=110)),
    # BBB: isyarat keluar lorong kaedah menunggu buka esok -> Esok "Dijual pada buka"
    _p(tarikh_beli='2026-10-21', saham='BBB', kaedah='M03', id_kaedah='M03', harga_beli='50', harga_terkini='45',
       untung_pct='-10.0', hari='2', henti='46', isyarat_keluar='Isyarat keluar: tutup bawah henti 46 (menunggu)',
       tarikh_isyarat='2026-10-20', status_henti=LORONG2_PEGANG.format(p=44, q=50)),
    # CCC: lorong 2 tercetus, jual pada buka esok (menunggu) -> Esok "Dijual pada buka"
    _p(tarikh_beli='2026-10-22', saham='CCC', kaedah='M12', id_kaedah='M12', harga_beli='20', harga_terkini='21',
       untung_pct='5.0', hari='1', henti='18', isyarat_keluar='Pegang (henti 18)', tarikh_isyarat='2026-10-21',
       status_henti='Tutup 21 bawah paras keluar 21.5 — jual pada buka esok (menunggu)', sektor='Energy', industri='Oil & Gas'),
    # DDD: lorong kaedah keluar, lorong 2 masih dipegang -> "Lorong 2 sahaja"
    _p(tarikh_beli='2026-10-16', saham='DDD', kaedah='M07', id_kaedah='M07', harga_beli='30', harga_terkini='33',
       untung_pct='10.0', hari='3', henti='27', isyarat_keluar='Keluar: sasaran (2026-10-21 @ 33)', keluar='True',
       tarikh_keluar='2026-10-21', harga_keluar='33', untung_akhir_pct='10.0', tarikh_isyarat='2026-10-15',
       status_henti=LORONG2_PEGANG.format(p=31, q=34)),
    # EEE: kedua-dua lorong keluar -> "Tutup kedua-dua lorong"; keluar lorong kaedah terkini (2026-10-23)
    _p(tarikh_beli='2026-10-15', saham='EEE', kaedah='M12', id_kaedah='M12', harga_beli='40', harga_terkini='38',
       untung_pct='-5.0', hari='6', henti='37', isyarat_keluar='Keluar: had masa (2026-10-23 @ 38)', keluar='True',
       tarikh_keluar='2026-10-23', harga_keluar='38', untung_akhir_pct='-5.0', tarikh_isyarat='2026-10-14',
       keluar_henti='True', tarikh_keluar_henti='2026-10-22', harga_keluar_henti='39', untung_henti_pct='-2.5',
       status_henti='Keluar: tutup 39.2 bawah paras keluar 39.5 pada 2026-10-21 (2026-10-22 @ 39)', tutup_semua='True'),
    # FFF: dibeli pada sesi terakhir
    _p(tarikh_beli='2026-10-23', saham='FFF', kaedah='M03', id_kaedah='M03', harga_beli='10', harga_terkini='10.5',
       untung_pct='5.0', hari='0', henti='9', isyarat_keluar='Pegang (henti 9)', tarikh_isyarat='2026-10-22'),
    # GGG: tidak sah (tidak cair) -> dikecualikan daripada purata; segmen "Tidak sah"
    _p(tarikh_beli='2026-10-23', saham='GGG', kaedah='M12', id_kaedah='M12', harga_beli='25', harga_terkini='24',
       untung_pct='-4.0', hari='0', henti='22', isyarat_keluar='Pegang (henti 22)', tarikh_isyarat='2026-10-22',
       tidak_sah='True', sebab_tidak_sah='isyarat palsu: saham tidak cair (3 bar tanpa julat) pada 2026-10-22'),
    # HHH: tidak dibeli pada sesi terakhir -> BUKAN "dibeli". Konvensyen data sebenar (24 Okt 2026: 64/64 baris): tidak_dibeli
    # juga ditanda tidak_sah; halaman bergantung padanya (prSrc/sahSahaja hanya menapis tidak_sah)
    _p(tarikh_beli='2026-10-23', saham='HHH', kaedah='M07', id_kaedah='M07', harga_beli='', harga_terkini='', untung_pct='',
       hari='', henti='12', isyarat_keluar='TIDAK DIBELI', tarikh_isyarat='2026-10-22', tidak_dibeli='True', tidak_sah='True',
       sebab_tidak_sah='sedia() sig=False pada 2026-10-22 (disemak dengan bar hingga 2026-10-23)',
       harga_buka_rujukan='11.8', tarikh_beli_dirancang='2026-10-23', keluar_henti='', tutup_semua=''),
    # III: tiada bar sesi terakhir dalam stor (harga skrin Moomoo) -> kira_semula nilai.harga.tanpa_bar_sesi
    _p(tarikh_beli='2026-10-22', saham='III', kaedah='M12', id_kaedah='M12', harga_beli='60', harga_terkini='61',
       untung_pct='1.67', hari='1', henti='55', isyarat_keluar='Pegang (henti 55)', tarikh_isyarat='2026-10-21'),
]

# earnings (medan db sahaja earn_kini/earn_kini_h; kalendar ujian kira_semula)
KALENDAR = {'AAA': [date(2026, 10, 28)], 'CCC': [date(2026, 11, 20)], 'DDD': [date(2026, 3, 1)]}
EARN_KINI = {'AAA': ('2026-10-28', 3), 'CCC': ('2026-11-20', 20)}

WATCH = [
    # isyarat lengkap, tiada posisi C -> Esok "Isyarat lengkap dalam watchlist" (menunggu belian 2026-10-26)
    {'Saham': 'JJJ', 'Nama': 'Jjj Corp', 'Kaedah': 'M03', 'Sektor': 'Technology', 'Industri': 'Software', 'Harga': '15.0',
     '% hampir': '100.0', 'Pencetus': 'Tutup > SMA20', 'Keadaan semasa': 'Isyarat lengkap', 'Syarat belum cukup': 'Tiada (isyarat sah)',
     'Syarat dipenuhi': '3/3', 'Paras pencetus': '14.9', 'Jarak %': '0.0', 'Tarikh masuk watchlist': '2026-10-22',
     'Hari dalam watchlist': '2', 'Skor': '0.8', 'Set': '431', 'tarikh_data': S, 'dibina': DIBINA},
    # isyarat lengkap tetapi posisi AAA M03 masih dipegang -> dilangkau (bukan menunggu)
    {'Saham': 'AAA', 'Nama': 'Aaa Inc', 'Kaedah': 'M03', 'Sektor': 'Technology', 'Industri': 'Software', 'Harga': '110.0',
     '% hampir': '100.0', 'Pencetus': 'Tutup > SMA20', 'Keadaan semasa': 'Isyarat lengkap', 'Syarat belum cukup': 'Tiada (isyarat sah)',
     'Syarat dipenuhi': '3/3', 'Paras pencetus': '108', 'Jarak %': '0.0', 'Tarikh masuk watchlist': '2026-10-23',
     'Hari dalam watchlist': '1', 'Skor': '0.7', 'Set': '431', 'tarikh_data': S, 'dibina': DIBINA},
    # paras disentuh, isyarat belum lengkap: % hampir 100 dalam CSV -> 99.9 dalam db
    {'Saham': 'KKK', 'Nama': 'Kkk Ltd', 'Kaedah': 'M07', 'Sektor': 'Energy', 'Industri': 'Oil & Gas', 'Harga': '20.0',
     '% hampir': '100.0', 'Pencetus': 'Tutup esok > 20', 'Keadaan semasa': 'Paras disentuh', 'Syarat belum cukup': 'Tutup esok > 20',
     'Syarat dipenuhi': '2/3', 'Paras pencetus': '20', 'Jarak %': '0.0', 'Tarikh masuk watchlist': '2026-10-23',
     'Hari dalam watchlist': '1', 'Skor': '0.6', 'Set': '431', 'tarikh_data': S, 'dibina': DIBINA},
    {'Saham': 'LLL', 'Nama': 'Lll Co', 'Kaedah': 'M12', 'Sektor': 'Energy', 'Industri': 'Oil & Gas', 'Harga': '28.65',
     '% hampir': '95.5', 'Pencetus': 'Tutup > 30', 'Keadaan semasa': 'Hampir', 'Syarat belum cukup': 'Tutup esok > 30',
     'Syarat dipenuhi': '2/3', 'Paras pencetus': '30', 'Jarak %': '4.5', 'Tarikh masuk watchlist': '2026-10-21',
     'Hari dalam watchlist': '3', 'Skor': '0.5', 'Set': '431', 'tarikh_data': S, 'dibina': DIBINA},
    # di bawah 90%: tidak dipapar halaman
    {'Saham': 'MMM', 'Nama': 'Mmm Plc', 'Kaedah': 'M03', 'Sektor': 'Technology', 'Industri': 'Software', 'Harga': '8.5',
     '% hampir': '85.0', 'Pencetus': 'Tutup > 10', 'Keadaan semasa': 'Jauh', 'Syarat belum cukup': 'Tutup esok > 10',
     'Syarat dipenuhi': '1/3', 'Paras pencetus': '10', 'Jarak %': '15.0', 'Tarikh masuk watchlist': '2026-10-20',
     'Hari dalam watchlist': '4', 'Skor': '0.2', 'Set': '431', 'tarikh_data': S, 'dibina': DIBINA},
]

# stor harga (ticker, date, open, high, low, close, volume); III tiada bar S
_TUTUP = (('AAA', 108, 110), ('BBB', 47, 45), ('CCC', 21.6, 21), ('DDD', 33, 33.5), ('EEE', 38.5, 38.2), ('FFF', 10, 10.5),
          ('GGG', 25, 24), ('JJJ', 14.9, 15), ('KKK', 19.8, 20), ('LLL', 28, 28.65))
STOR = ([(t, 20261022, a, a, a, a, 1000) for t, a, _ in _TUTUP] + [(t, 20261023, b, b, b, b, 1000) for t, _, b in _TUTUP]
        + [('III', 20261022, 60, 60, 60, 60, 1000)])

SPY_BERSIH = 0.1204
AUTOTUNE = {'dijana': '2026-10-18T05:10Z', 'kaedah': [
    dict(id='M03', nama='Kaedah tiga', label='TINGGI', cagr_a=0.2, spy_a=0.1463, cagr_b=0.18, spy_b=0.1463, cagr_kunci=0.21,
         spy_kunci=0.1629, cagr_bersih=0.15, spy_bersih=SPY_BERSIH, dsr=0.97, pbo=0.2),
    dict(id='M07', nama='Kaedah tujuh', label='SEDERHANA', cagr_a=0.16, spy_a=0.1463, cagr_b=0.15, spy_b=0.1463, cagr_kunci=0.1,
         spy_kunci=0.1629, cagr_bersih=0.1, spy_bersih=SPY_BERSIH, dsr=0.9, pbo=0.3),
    dict(id='M12', nama='Kaedah dua belas', label='RENDAH', cagr_a=0.1, spy_a=0.1463, cagr_b=0.2, spy_b=0.1463, cagr_kunci=0.05,
         spy_kunci=0.1629, cagr_bersih=0.05, spy_bersih=SPY_BERSIH, dsr=0.5, pbo=0.6)]}


def _anl(id_, nama, swing, kedudukan, ditolak, status, h_posisi, h_matang, p1, p5, pk, lulus_subset, lulus_wfo):
    a = next((x for x in AUTOTUNE['kaedah'] if x['id'] == id_), None)
    lulus_at = (a['cagr_a'] > a['spy_a'] and a['cagr_b'] > a['spy_b']) if a else None
    return dict(id=id_, nama=nama, varian='V1', swing=swing, hari=8.0 if swing else 45.0, bt_keputusan='DITOLAK' if ditolak else 'GUNA',
                bt_cagr=0.2, bt_mdd=-0.2, bt_menang=0.5, bt_purata=1.5, bt_n=400, bt_setahun=60.0, subset='3/4' if lulus_subset else '1/4',
                lulus_subset=lulus_subset, wfo_cagr=0.3, wfo_ew=0.326, lulus_wfo=lulus_wfo,
                at_label=a and a['label'], at_cagr_a=a and a['cagr_a'], at_cagr_b=a and a['cagr_b'], at_spy=a and a['spy_a'],
                at_cagr_kunci=a and a['cagr_kunci'], at_cagr_bersih=a and round(a['cagr_bersih'], 3), at_dsr=a and a['dsr'],
                at_pbo=a and a['pbo'], lulus_at=lulus_at, lulus=sum(bool(x) for x in (lulus_subset, lulus_wfo, lulus_at)),
                kekal=0.5, jangkaan=0.75, h_posisi=h_posisi, h_tutup=h_matang, h_matang=h_matang, h_purata=None, h_umur=14,
                h_hari_beli=h_matang, c_posisi=h_posisi, skor=0.8, skor_bawah=-0.5, skor_atas=2.1, skor_bulan=2.0,
                skor_bulan_bawah=-1.0, skor_bulan_atas=5.0, lb_bulan=-1.0, g_matang=h_matang, g_perlu=10, nb=float(h_matang),
                nb_perlu=100, ditolak=ditolak, lejar_n=h_posisi, status=status, pantau='BELUM CUKUP', p_sebab='', sampel_kecil=kedudukan is None and swing,
                kedudukan=kedudukan, p_top1=p1, p_top5=p5, pangkat_p5=pk and pk[0], pangkat_p95=pk and pk[1], kelompok=None,
                kelompok_wakil=None, kedudukan_sebelum=kedudukan)


# Pintu: aktif 5 -> swing 4 -> berkedudukan 3 -> tidak DITOLAK 2 -> AUTOTUNE SEDERHANA/TINGGI 2 -> bersih > SPY 1 -> KUAT 1
PAPAN = dict(
    dibina=DIBINA, kini='2026-10-22', harga_pada='2026-10-22', mula_lejar='2026-10-16', lejar_posisi=10, lejar_tindih=2, c_posisi=9,
    c_pra_lejar=4, lejar_sesi='2026-10-22',
    fasa=dict(matang_hadapan=6, jumlah_hadapan=12, kaedah_bukti=1, tarikh_sebenar_pertama=None, tarikh_top5=[None, None],
              teks='Fasa 1 — fikstur ujian.'),
    parameter={}, penemuan=['Penemuan satu (fikstur).', 'Penemuan dua (fikstur).', 'Penemuan tiga (fikstur).'],
    rujukan=dict(is_tempoh='1 Nov 2019 – 2 Okt 2026', is_ew=0.2191, is_spy=0.1586, wfo_tempoh='1 Jan 2023 – 2 Okt 2026',
                 wfo_ew=0.326, wfo_spy=0.221, at_tempoh='2013 – Sep 2024 (2000 saham AS)', at_spy=0.1463, slot=None,
                 at_kunci_tempoh='Okt 2024 – Okt 2026', at_spy_kunci=0.1629, at_bersih_tempoh='2013–2018 (parameter asal)',
                 at_spy_bersih=SPY_BERSIH),
    rows=[_anl('M03', 'Kaedah tiga', True, 1, False, 'KUAT', 5, 3, 0.6, 1.0, (1, 2), True, True),
          _anl('M07', 'Kaedah tujuh', True, 2, False, 'PERHATI', 4, 2, 0.3, 1.0, (1, 3), False, True),
          _anl('M12', 'Kaedah dua belas', True, 3, True, 'BELUM CUKUP', 2, 1, 0.1, 1.0, (2, 3), False, False),
          _anl('M20', 'Kaedah dua puluh', True, None, False, 'BELUM CUKUP', 1, 0, None, None, None, False, False),
          _anl('M99', 'Kaedah bukan swing', False, None, False, 'BELUM CUKUP', 0, 0, None, None, None, False, False)],
    nota='Fikstur ujian (bukan data sebenar).')

LANGKAU = [dict(tarikh=S, saham='NNN', kaedah='M03', sebab='buka > buka_maks', sumber='ujian')]


def tulis_csv(path, rows):
    lajur = []
    for r in rows:
        lajur += [k for k in r if k not in lajur]
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=lajur)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in lajur})


def tulis_stor(folder):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, 'harga_A.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ticker', 'date', 'open', 'high', 'low', 'close', 'volume'])
        w.writerows(STOR)


def harian_kaedah():
    """prestasi/harian_kaedah akaun C (np, j) — dikira dengan tangan (jangka.json)."""
    rows = [dict(a='C', k='Semua', np=8, j=2.8), dict(a='C', k='M03', np=3, j=1.67), dict(a='C', k='M07', np=2, j=7.88),
            dict(a='C', k='M12', np=3, j=0.56)]
    for r in rows:
        r.update(d=[0.5, -0.2], n=[r['np'], r['np']], ev=[])
    return dict(tarikh=[20261022, 20261023], spy=[0.3, -0.1], rows=rows, dibina=DIBINA, harga_hingga=f'{S} tutup')


def dokumen(had_ringkas=1500, had_bahagi=1200):
    """{path: dokumen} db dashboard daripada data di atas (format jana_db: ringkas_pt dan bahagi dengan had kecil supaya
    penyahkod bahagian/kamus diuji)."""
    import jana_db as J
    from bahagi_db import bahagi
    from harian_c import normal_watch
    C = []
    for r in POSISI:
        d = J.baris_db({k: v for k, v in r.items()})
        e = EARN_KINI.get(r['saham'])
        if e:
            d.update(earn_kini=e[0], earn_kini_h=e[1])
        if r.get('tidak_sah') == 'True':
            d['jenis_tidak_sah'] = J.jenis_tidak_sah(r.get('sebab_tidak_sah'))
        C.append(d)
    D = {}
    for doc_id, d in J.ringkas_pt(C, 'ringkas_c', dict(dibina=DIBINA, harga_pada=f'{S} tutup (fikstur ujian)', nota='Fikstur ujian.'),
                                  had=had_ringkas):
        D[f'papertrade/{doc_id}'] = d
    W = []
    for r in WATCH:
        x = dict(r)
        normal_watch(x)
        W.append(J.baris_db(x, J.PETA_WATCH))
    wd = dict(definisi='Fikstur ujian.', dibina=DIBINA, gred_pada='', pemangkin_pada='', tarikh_data=S, rows=W)
    for doc_id, d in bahagi(wd, 'watchlist', had_bahagi):
        D[f'papertrade/{doc_id}'] = d
    D['papertrade/langkau'] = dict(rows=LANGKAU, liputan={S: dict(bil_log=1, bil=1)}, mula='2026-10-14', sumber=['ujian'], dibina=DIBINA)
    D['prestasi/harian_kaedah'] = harian_kaedah()
    D['analisis/papan'] = PAPAN
    D['harian/status'] = dict(dikemaskini=DIBINA, sumber='fikstur ujian', harga_tutup_pada=S, tarikh_data_pagi=S, tarikh_data=S,
                              kemaskini_pagi='', scan_malam='', ralat=[], mod='rasmi', sumber_harga='fikstur ujian',
                              saluran=dict(ringkas_c=DIBINA, watchlist=S, langkau=S), beli_langkau=1,
                              beli_ringkas=dict(direkod=2, dilangkau=1), beli_pada='')
    return D


def tulis_sumber(folder):
    """CSV papertrade (claude.csv, watchlist.csv) bagi kira_semula.py."""
    os.makedirs(folder, exist_ok=True)
    tulis_csv(os.path.join(folder, 'claude.csv'), POSISI)
    tulis_csv(os.path.join(folder, 'watchlist.csv'), WATCH)


def tulis_db(folder, D=None):
    for p, d in (D or dokumen()).items():
        q = os.path.join(folder, p + '.json')
        os.makedirs(os.path.dirname(q), exist_ok=True)
        with open(q, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, separators=(',', ':'))


if __name__ == '__main__':
    out = os.path.join(HERE, 'fikstur_db.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(dokumen(), f, ensure_ascii=False, indent=0, sort_keys=True)
        f.write('\n')
    print(out)
