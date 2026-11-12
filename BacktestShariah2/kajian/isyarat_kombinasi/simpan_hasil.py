"""Eksport jadual keputusan kecil daripada fail perantaraan folder kerja ke `hasil/` (dikomit).
Guna (dari folder kerja): python3 simpan_hasil.py"""
import json
import os
import shutil

import pandas as pd

SINI = os.path.dirname(os.path.abspath(__file__))
KE = os.path.join(SINI, 'hasil')
os.makedirs(KE, exist_ok=True)


def tulis(d, nama, **k):
    d.to_csv(os.path.join(KE, nama), float_format='%.4f', **k)
    print(nama, len(d))


if os.path.exists('hasil_isyarat.pkl'):
    tulis(pd.read_pickle('hasil_isyarat.pkl'), 'isyarat_tunggal.csv')
if os.path.exists('matriks.pkl'):
    tulis(pd.read_pickle('matriks.pkl'), 'matriks_masuk_keluar.csv', index=False)
if os.path.exists('kombo_pasangan.pkl'):
    tulis(pd.read_pickle('kombo_pasangan.pkl'), 'kombo_pasangan.csv', index=False)
if os.path.exists('habis_lulus.pkl'):
    L = pd.read_pickle('habis_lulus.pkl')
    L['kunci'] = L.kunci.apply(lambda q: '|'.join(q))
    kol = ['kel', 'nama', 'kunci', 'n', 'jgk', 'mng', 'A', 'B', 'nA', 'nB', 'yp', 'yv', 'nV', 'jgkV', 'lebihV', 'min_lebih']
    tulis(L[kol].sort_values(['kel', 'min_lebih'], ascending=[True, False]), 'pusingan2_lulus_semua.csv', index=False)
if os.path.exists('pradaftar.json'):
    shutil.copy('pradaftar.json', os.path.join(KE, 'pradaftar.json'))
    print('pradaftar.json', len(json.load(open('pradaftar.json'))))
