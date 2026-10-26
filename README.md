
# Pertemuan 13 - Debugging dan Testing

Nama: Mauliana Mutiara  
NIM: 2225250078  
Kelas: 3A

## Kasus

Pada pertemuan ini saya belajar mencari dan memperbaiki kesalahan pada program Python. Program yang diuji adalah program untuk menghitung rata-rata, menentukan status kelulusan, dan mencari nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report

### B01 - Kesalahan rata-rata
Gejala: Hasil rata-rata tidak sesuai dengan data.
Penyebab: Program selalu membagi jumlah nilai dengan 5.
Perbaikan: Pembagi diganti menjadi jumlah data menggunakan len(nilai).

### B02 - Kesalahan status kelulusan
Gejala: Nilai 60 dinyatakan tidak lulus.
Penyebab: Program menggunakan operator >.
Perbaikan: Operator diganti menjadi >=.

### B03 - Kesalahan nilai tertinggi
Gejala: Program menghasilkan nilai tertinggi 0.
Penyebab: Nilai dibandingkan menggunakan operator < dan nilai awal 0.
Perbaikan: Nilai awal diambil dari data pertama, lalu dibandingkan dengan operator >.

## Retest

Setelah program diperbaiki, seluruh test case dijalankan kembali. Hasil yang diharapkan adalah semua test berstatus PASS.

## Cara Menjalankan

Jalankan perintah berikut pada terminal dari folder utama:

python praktik/praktik_4_debugging.py

## Refleksi

Saya belajar bahwa program yang dapat dijalankan belum tentu menghasilkan jawaban yang benar. Karena itu, saya perlu membuat test case, memeriksa penyebab kesalahan, memperbaiki kode, dan melakukan pengujian ulang.
