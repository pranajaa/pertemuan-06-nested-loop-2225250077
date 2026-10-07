# Pertemuan 06 Nested Loop Python
Nama: Hitana Rifa Pranaja

NIM: 2225250077

Kelas: 3A

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan

## Cara Menjalankan 
### Latihan
```bash
latihan/01_pasangan_indeks.py

latihan/02_pola_segitiga.py

latihan/03_jumlah_per_baris.py

latihan/04_hitung_pasangan.py
```
### Tugas
```bash
tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas
- Baca nilai n.
- Jika n <= 0, minta input kembali sampai n positif.
- Set total_semua = 0 dan count_genap = 0.
- Ulangi i dari 1 sampai n.
- Set total_baris = 0.
- Ulangi j dari 1 sampai n.
- Hitung hasil = i × j.
- Tampilkan hasil perkalian.
- Tambahkan hasil ke total_baris dan total_semua.
- Jika hasil genap, tambahkan count_genap.
- Setelah loop dalam selesai, tampilkan jumlah baris.
- Setelah semua loop selesai, tampilkan total keseluruhan dan banyak hasil genap.

## Hasil Pengujian

| No. | Input n | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | Status   |
| --- | ------: | --------------: | ----------: | -----------------: | -------- |
| 1   |       1 |               1 |           1 |                  0 | Berhasil |
| 2   |       2 |               4 |           9 |                  3 | Berhasil |
| 3   |       3 |               9 |          36 |                  5 | Berhasil |

## Analisis Efisiensi
Program menggunakan nested loop dengan dua perulangan yang masing-masing berjalan sebanyak n kali. Oleh karena itu, jumlah operasi perkalian yang dilakukan adalah n × n, sehingga kompleksitas waktunya adalah O(n²).

Semakin besar nilai n, semakin banyak perulangan yang dilakukan. Penggunaan nested loop sudah sesuai karena program perlu menghasilkan setiap kombinasi perkalian dari 1 sampai n.

## Refleksi
Dari tugas ini, saya jadi lebih paham cara kerja nested loop dan bagaimana perulangan di dalam perulangan bisa digunakan untuk membuat tabel perkalian. Saya juga belajar menggunakan variabel untuk menghitung total hasil dan mencari hasil yang genap. Awalnya saya masih bingung dengan posisi perulangan dan variabelnya, tetapi setelah dicoba dan diuji dengan beberapa nilai n, saya jadi lebih memahami cara kerjanya.

## Sumber 
- Bahan ajar pertemuan 06 nested loop
- Chatgpt ai
