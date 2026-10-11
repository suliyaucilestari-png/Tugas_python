# ini komentar, tidak di jalankan
print("Hallo, Dunia")

nama = "python"

if nama == "python":
    print("indentasi = blok kode")
    print("Gunakan 4 spasi")

nama = "Budi" 
umur = 20
tinggi = 170.5
aktif = True

#nilai bisa diganti kapan saja
umur = umur + 1

#multiple assigment
x, y, z = 1, 2, 3
print(nama, umur, x + y + z)  

angka = int("25")
print(angka + 5)
harga = float("12500.75")
print(type(harga))

umur = 20
print("Umur: " + str(umur))
print(bool(0), bool("hai"))

nama = "Python Dasar"
print(len(nama))
print(nama.upper())
print(nama[0:6])
print(nama.split(" "))

bab = 2
print(f"Belajar {nama} bab {bab}")

print("hallo", "Dunia")
print("A", "B", "C", sep="-")
print("Loading", end="...")
print("selesai")

harga = 15000 / 7
print(f"Harga: Rp{harga:.2f}")
print(f"Total: {1500000:,}")

nama = input("Siapa namamu? ")
umur = int(input("Berapa umurmu? "))

tahun_depan = umur + 1
print(f"Hallo {nama}!")
print(f"Tahun depan kamu {tahun_depan} tahun")

umur = 20
punya_ktp = True

print(umur >= 17 and punya_ktp)
print(umur < 13 or umur > 60)
print(not punya_ktp)

skor = 10
skor += 5
skor *= 2
print(skor)

buah = ["apel", "jeruk", "mangga"]
print("apel" in buah)
print("anggur" not in buah)
print("th" in "Python")

nilai = 80

if nilai >= 75:
    print("Selamat, kamu lulus!")
else:
    print("Ayo remedial dulu")

print("Program selesai")

nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

print(f"Nilai {nilai} → grade {grade}")

hari = "sabtu"

match hari:
      case "sabtu"  | "minggu":
          print("Libur!")
      case "senin":
          print("Semangat!")
      case _:
          print("Hari kerja")

umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("Boleh memilih")
    else:
        print("Buat KTP dulu")

umur = 16
s = "dewasa" if umur >= 17 else "anak"
print(s)     # anak

for i in range(1, 4):
    print(f"Putar ke-{i}")

buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print(b.upper())

hitung = 3

while hitung > 0:
    print(f"Hitung mundur: {hitung}")
    hitung -= 1

print("Meluncur!")

for n in range(1, 10):
    if n == 3:
        continue
    if n == 6:
        break
    print(n)

for i in range (3):
    pass   

nilai = [80, 65, 90]
nilai.append(75)
nilai.remove(65)
nilai[0] = 85

print(nilai)
print(nilai[-1], len(nilai))
print(sorted(nilai))

titik = (3, 7)
warna = (255, 128, 0)

x, y = titik
print(f"x={x}, y={y}")
print(warna[0], len(warna))

# titik[0] = 10

angka = {1, 2, 3, 3, 3}
print(angka)
 
ipa = {"Ani", "Budi", "Citra"}
ips = {"Budi",  "Doni"}

print(ipa | ips)
print(ipa & ips)
print(ipa - ips)

siswa = {"nama": "Sari", "umur": 19}
siswa["kota"] = "Bandung"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(f"{k}: {v}")

def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    luas = panjang * lebar
    return luas

hasil = hitung_luas(5, 3)
print(hasil)
print(hitung_luas(10, 2))

def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))

def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))

kuadrat = lambda x: x ** 2
print(kuadrat(4))

siswa = [("Ani", 80), ("Budi", 95)]
print(max(siswa, key=lambda s: s[1]))

x = "global"
def tes():
    x = "lokal"
    print(x)
tes()
print(x)

try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
else:
    print(f"Hasil: {hasil}")
finally:
    print("Selesai.")

def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak valid")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"Error: {e}")

import math
from random import randint
import datetime as dt

print(math.sqrt(16))
print(math.pi)
print(randint(1, 6))
print(dt.date.today().year)

def rata_rata(data):
    return sum(data) / len(data)

nilai = [80, 90, 70]
print(rata_rata(nilai))

import csv

data = []
with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")
print(data[0])

nilai = [d["nilai"] for d in data]

rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data
         if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")

import pandas as pd

df = pd.read_csv("nilai.csv")
print(df.groupby("kelas")["nilai"].mean())
print(df[df["nilai"] >= 75]["nama"].tolist())
print(df.sort_values("nilai").tail(1))