# Tugas Pertemuan 1 | Talitha Novelia Salsabila (H1D024122)

import random      # library: menghasilkan nilai & pilihan acak
import statistics  # library: menghitung rata-rata dan median

# struktur data
mata_kuliah = ("Kecerdasan Buatan", "Algoritma", "Basis Data", "Jaringan Komputer", "Pemrograman Web")  
# tuple: data tetap (tidak diubah)
nama_mahasiswa = ["Alvin", "Budi", "Citra", "Dewi", "Eko"]     
# list: menyimpan data mahasiswa
lulus = set()            
tidak_lulus = set()      
# set: menampung data unik tanpa duplikasi
data_nilai = {}          
# dictionary: pasangan nama dan nilai

print("=" * 50)
print("   SISTEM PENILAIAN MAHASISWA")
print("=" * 50)

print("\nDaftar Mata Kuliah:")

# struktur kontrol: for => menampilkan semua mata kuliah
for i, mk in enumerate(mata_kuliah, 1):
    print(f"  {i}. {mk}")

mk_pilih = random.choice(mata_kuliah)  
# random: memilih satu mata kuliah secara acak
print(f"\nMata Kuliah : {mk_pilih}")

print("\nData Nilai Mahasiswa:")
print("-" * 50)
print(f"{'Nama':<12} {'Nilai':>6}  {'Grade':>6}  {'Status'}")
print("-" * 45)

# struktur kontrol: for => mengisi nilai tiap mahasiswa
for nama in nama_mahasiswa:
    data_nilai[nama] = random.randint(40, 100)  
    # random: membuat nilai acak

# struktur kontrol: for + if => menentukan grade & status
for nama, nilai in data_nilai.items():
    if nilai >= 80:          
        grade, status = "A", "LULUS"
    elif nilai >= 70:        
        grade, status = "B", "LULUS"
    elif nilai >= 60:
        grade, status = "C", "LULUS"
    elif nilai >= 50:
        grade, status = "D", "TIDAK LULUS"
    else:
        grade, status = "E", "TIDAK LULUS"

    # if => mengelompokkan ke set lulus/tidak
    if nilai >= 60:
        lulus.add(nama)
    else:
        tidak_lulus.add(nama)

    print(f"{nama:<12} {nilai:>6}  {grade:>6}  {status}")

# statistik nilai
nilai_list = list(data_nilai.values())  
nilai_rata = statistics.mean(nilai_list)  
nilai_median = statistics.median(nilai_list)  
nilai_max = max(nilai_list)
nilai_min = min(nilai_list)

print("\n" + "=" * 50)
print("Statistik Nilai")
print("=" * 50)
print(f"  Rata-rata  : {nilai_rata:.2f}")
print(f"  Median     : {nilai_median:.2f}")
print(f"  Tertinggi  : {nilai_max}")
print(f"  Terendah   : {nilai_min}")

# struktur data: set union => gabung semua data
semua = lulus | tidak_lulus
total = len(nama_mahasiswa)
jml_lulus = len(lulus)
jml_tidak = len(tidak_lulus)

print("\n" + "=" * 50)
print("Rekap Kelulusan")
print("=" * 50)
print(f"  Lulus       : {lulus}")
print(f"  Tidak Lulus : {tidak_lulus}")
print(f"  Total       : {semua}")
print(f"\n  Persentase Lulus       : {jml_lulus/total*100:.1f}%")
print(f"  Persentase Tidak Lulus : {jml_tidak/total*100:.1f}%")

# struktur kontrol: while => mencari nilai tertinggi manual
data = list(data_nilai.items())
i = 0
nama_max = ""
nilai_max2 = 0

while i < len(data):
    nama, nilai = data[i]
    if nilai > nilai_max2:    
        nama_max = nama
        nilai_max2 = nilai
    i += 1
print(f"\n  Nilai tertinggi diraih oleh {nama_max} dengan nilai {nilai_max2}")

# function + if => memberi pesan kelulusan
def pesan(nama, nilai):
    if nilai >= 60:
        print(f"  {nama} -> Selamat, kamu lulus dengan nilai {nilai}.")
    else:
        print(f"  {nama} -> Belum lulus, nilai {nilai}. Tingkatkan lagi!")

print("\n" + "=" * 50)
print("Pesan untuk Mahasiswa")
print("=" * 50)

# struktur kontrol: for => memanggil fungsi
for nama, nilai in data_nilai.items():
    pesan(nama, nilai)
print("=" * 50)