<img width="795" height="522" alt="Screenshot 2026-03-17 202914" src="https://github.com/user-attachments/assets/72f4e67b-4277-45e3-a762-fef12eda8e63" /><img width="795" height="522" alt="image" src="https://github.com/user-attachments/assets/57af13d6-4111-424d-96fb-10852c3043ae" /># H1D024122-PraktikumKB-Pertemuan1

Program sederhana penilaian mahasiswa menggunakan Python.
# Fitur yang digunakan:
- Struktur kontrol: if, for, while
- Struktur data: list, set, tuple, dictionary
- Library: random (menghasilkan nilai & pilihan acak) & statistics (menghitung rata-rata dan median)
# Output:
==================================================
   SISTEM PENILAIAN MAHASISWA
==================================================

Daftar Mata Kuliah:
  1. Kecerdasan Buatan
  2. Algoritma
  3. Basis Data
  4. Jaringan Komputer
  5. Pemrograman Web

Mata Kuliah : Basis Data

Data Nilai Mahasiswa:
--------------------------------------------------
Nama          Nilai   Grade  Status
---------------------------------------------
Alvin            43       E  TIDAK LULUS
Budi             88       A  LULUS
Citra            85       A  LULUS
Dewi             41       E  TIDAK LULUS
Eko              75       B  LULUS

==================================================
Statistik Nilai
==================================================
  Rata-rata  : 66.40
  Median     : 75.00
  Tertinggi  : 88
  Terendah   : 41

==================================================
Rekap Kelulusan
==================================================
  Lulus       : {'Eko', 'Citra', 'Budi'}
  Tidak Lulus : {'Alvin', 'Dewi'}
  Total       : {'Citra', 'Dewi', 'Eko', 'Alvin', 'Budi'}

  Persentase Lulus       : 60.0%
  Persentase Tidak Lulus : 40.0%

  Nilai tertinggi diraih oleh Budi dengan nilai 88

==================================================
Pesan untuk Mahasiswa
==================================================
  Alvin -> Belum lulus, nilai 43. Tingkatkan lagi!
  Budi -> Selamat, kamu lulus dengan nilai 88.
  Citra -> Selamat, kamu lulus dengan nilai 85.
  Dewi -> Belum lulus, nilai 41. Tingkatkan lagi!
  Eko -> Selamat, kamu lulus dengan nilai 75.
==================================================
