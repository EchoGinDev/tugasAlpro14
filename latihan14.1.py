import re
import time
import datetime

teks = """Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02)."""

tanggal_sekarang = datetime.datetime.now()

tanggal_list = re.findall(r'\d{4}-\d{2}-\d{2}', teks)

for tanggal_str in tanggal_list:
    tahun, bulan, hari = map(int, tanggal_str.split('-'))
    tanggal_obj = datetime.datetime(tahun, bulan, hari)
    selisih_hari = (tanggal_sekarang - tanggal_obj).days
    tanggal_baru_str = tanggal_obj.strftime('%d-%m-%Y')
    print(f"{tanggal_str} {tanggal_baru_str} selisih {selisih_hari} hari")
