#!/usr/bin/env bash
# Jana semula tinjauan isyarat kombinasi. Guna: bash jalan_semua.sh <folder_kerja_di_luar_repo>
# Fail perantaraan (*.pkl, sehingga ~1 GB) ditulis ke folder kerja, BUKAN ke repo. Log ke log/.
# habis.py (pusingan 2, ~35 minit, ~1.35 juta gabungan) hanya dijalankan jika HABIS=1.
set -euo pipefail
SINI="$(cd "$(dirname "$0")" && pwd)"; KERJA="${1:?beri folder kerja}"; mkdir -p "$KERJA" "$SINI/log"; cd "$KERJA"
j() { echo "== $1"; python3 -W ignore "$SINI/$1.py" "${@:2}" > "$SINI/log/$1${LOGSUF:-}.txt" 2>&1; }
j panel mentah panel_mentah.pkl; LOGSUF=_stor j panel stor panel_stor.pkl
j analisa; j teguh; j sah; j matriks; j kombo; j turutan
if [ "${HABIS:-0}" = "1" ]; then j habis; fi
if [ -f habis.pkl ]; then j semak2; j semak3; fi
j pradaftar; j moomoo5
j keluar8 0.08; j baca8 keluar8_8.pkl; rm -f keluar8_8.pkl
python3 "$SINI/simpan_hasil.py" > "$SINI/log/simpan_hasil.txt" 2>&1
echo SIAP
