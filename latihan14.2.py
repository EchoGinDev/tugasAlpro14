import re
import os

texto = """Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""
chara = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def buat_kata_sandi(panjang=8):
    sandi = ''
    for _ in range(panjang):
        indeks = ord(os.urandom(1)) % len(chara)
        sandi = sandi + chara[indeks]
    return sandi

emails = re.findall(r'\S+@\S+', texto)
hasil = []
for email in emails:
    nama_pengguna = email.split('@')[0]
    sandi = buat_kata_sandi()
    hasil.append((email, nama_pengguna, sandi))

for hasil_akhir in hasil:
    print(f"""{hasil_akhir[0]} username: {hasil_akhir[1]}, password: {hasil_akhir[2]}""")
