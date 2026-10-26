# Pertemuan 13 — Debugging, Tracing, Testing, dan Test Case

## Identitas

- Nama: Mauliana Mutiara
- NIM: 2225250078
- Kelas: 3A
- Mata Kuliah: Algoritma dan Pemrograman

## Tujuan

Pada pertemuan ini, saya belajar melakukan debugging, menelusuri jalannya program, membuat test case, dan memperbaiki kesalahan pada kode Python.

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

## Laporan Bug Praktik 4

### Bug 1 — Perhitungan Rata-rata

**Kesalahan:** Program membagi jumlah nilai dengan angka 5, padahal jumlah data dapat berbeda.

**Perbaikan:** Mengganti pembagi dengan `len(nilai)` agar sesuai dengan jumlah data.

### Bug 2 — Status Kelulusan

**Kesalahan:** Program menggunakan kondisi `nilai > 60`, sehingga nilai 60 dinyatakan tidak lulus.

**Perbaikan:** Mengubah kondisi menjadi `nilai >= 60`.

### Bug 3 — Nilai Tertinggi

**Kesalahan:** Program menggunakan kondisi perbandingan yang terbalik sehingga tidak mendapatkan nilai tertinggi dengan benar.

**Perbaikan:** Menggunakan nilai pertama sebagai nilai tertinggi awal, kemudian membandingkannya dengan nilai berikutnya menggunakan kondisi `x > tertinggi`.

## Test Case dan Hasil Retest

| ID | Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | 75.0 | PASS |
| T2 | Rata-rata `[100, 80]` | 90.0 | PASS |
| T3 | Status nilai 60 | Lulus | PASS |
| T4 | Status nilai 59 | Tidak lulus | PASS |
| T5 | Nilai tertinggi `[80, 60, 90, 70]` | 90 | PASS |

Seluruh lima test case berhasil setelah perbaikan dilakukan.

## Refleksi

Dari praktik ini, saya belajar bahwa kesalahan kecil dalam kondisi dan perhitungan dapat menyebabkan hasil program tidak sesuai harapan. Dengan melakukan tracing dan testing, kesalahan dapat ditemukan dan diperbaiki. Setelah kode diperbaiki, program perlu diuji kembali untuk memastikan hasilnya sudah benar.