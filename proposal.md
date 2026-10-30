# Proposal Proyek: Generator Soal Latihan Aritmetika Dasar

## 1. Judul Proyek
Generator Soal Latihan Aritmetika Dasar Berbasis Python

## 2. Latar Belakang
Guru matematika sering kali memerlukan waktu yang cukup banyak untuk menyusun variasi soal latihan hitung dasar secara manual bagi siswa. Selain itu, proses koreksi jawaban satu per satu kurang efisien. Oleh karena itu, dibutuhkan program sederhana yang dapat membangkitkan soal acak, mengoreksi, serta merekap nilai secara otomatis.

## 3. Pengguna dan Tujuan
- **Pengguna Utama:** Guru matematika sekolah dasar/menengah atau siswa untuk latihan mandiri.
- **Tujuan:** Menyediakan latihan soal aritmetika yang dinamis dengan penilaian dan laporan otomatis.

## 4. Ruang Lingkup dan Fitur Wajib
- Memilih tingkat kesulitan (Mudah, Sedang, Sulit).
- Membangkitkan soal operasi dasar secara acak (penjumlahan, pengurangan, perkalian).
- Memvalidasi input jawaban dari pengguna agar tidak *crash* jika salah format.
- Menghitung skor akhir dan persentase keberhasilan.
- Menyimpan hasil rekap latihan ke dalam file laporan eksternal.

## 5. Kebutuhan Fungsional (Requirements)
- **F01:** Program dapat meminta input tingkat kesulitan dari pengguna.
- **F02:** Program dapat menghasilkan angka dan operator secara acak.
- **F03:** Program memvalidasi bahwa input jawaban siswa berupa angka bulat.
- **F04:** Program menghitung jumlah jawaban benar dan salah.
- **F05:** Program menyimpan laporan hasil latihan ke folder `output/`.

## 6. Spesifikasi Input, Proses, Output (IPO)

| Input | Proses | Output |
|---|---|---|
| Pilihan menu, jumlah soal, dan jawaban numerik siswa. | Membangkitkan angka acak, validasi tipe data, evaluasi kesamaan jawaban, hitung total skor. | Tampilan soal, umpan balik benar/salah per soal, dan file ringkasan nilai. |

## 7. Pseudocode Alur Utama
```text
MULAI
tampilkan_menu_utama()
pilih tingkat kesulitan dan jumlah soal
UNTUK setiap soal dari 1 sampai jumlah_soal:
	buat_soal_acak(tingkat)
	tampilkan pertanyaan kepada pengguna
	ULANGI:
		terima input jawaban_siswa
		JIKA jawaban_siswa valid:
			bandingkan dengan jawaban_benar
			tampilkan status (Benar/Salah)
			keluar dari pengulangan validasi
		JIKA TIDAK:
			tampilkan pesan error validasi dan minta input ulang
HITUNG total skor dan persentase
SIMPAN laporan ke file output
SELESAI
```

## 8. Struktur Program & Modularisasi
- `main.py`: Mengatur alur utama menu dan perulangan kuis.
- `data_io.py`: Menangani pembacaan konfigurasi/referensi dan penyimpanan laporan ke file.
- `analisis.py`: Mengandung fungsi logika matematika, pembuatan soal acak, dan perhitungan skor.
- `utilitas.py`: Berisi fungsi validasi input angka dan pembersih layar/pesan bantu.

## 9. Struktur Data
- **List:** Digunakan untuk menampung daftar riwayat skor atau daftar soal yang telah di-generate.
- **Dictionary:** Digunakan untuk menyimpan konfigurasi tingkat kesulitan (misalnya rentang angka minimum dan maksimum).
- **String:** Digunakan untuk memformat teks laporan hasil latihan.

## 10. Test Case Awal
Lihat [tests/test_case.md](tests/test_case.md) untuk daftar test case awal.

## 11. Pembagian Tugas Tim
- **Anggota 1:** Koordinator & `main.py`
- **Anggota 2:** `data_io.py`
- **Anggota 3:** `analisis.py`
- **Anggota 4:** `utilitas.py` & penyusunan `test_case.md`
