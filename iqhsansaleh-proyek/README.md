# Analisis Nilai Matematika Kelas

## Deskripsi

Program konsol ini membantu guru matematika membaca nilai siswa dari file teks,
memvalidasi nilai, menghitung statistik kelas, menentukan ketuntasan berdasarkan
KKM, dan menyimpan laporan. Sasaran pengguna adalah guru, dosen, anggota tim,
atau pengguna lain yang membutuhkan rekap nilai sederhana.

## Fitur

- Membaca data siswa dari `data/contoh_data.txt` dalam format `nama,nilai`.
- Menerima nilai pada rentang 0 sampai 100 serta memberi peringatan untuk nilai
	di luar rentang atau format angka yang salah.
- Menghitung jumlah siswa, rata-rata, nilai minimum, dan maksimum.
- Menentukan status `Tuntas` atau `Belum Tuntas` dengan KKM default 60.
- Menampilkan hasil di terminal dan menyimpan laporan ke file teks.

## Persyaratan

- Python 3.x
- Visual Studio Code atau terminal

## Cara Menjalankan

Buka terminal pada folder proyek, lalu jalankan:

```bash
python3 main.py
```

Pada Windows, perintah `python main.py` juga dapat digunakan. Hasil laporan
disimpan ke `output/laporan_ringkas.txt`; folder `output` dibuat otomatis.

Format data adalah satu siswa per baris, contohnya `Andi,85`. Baris kosong
diabaikan.

## Struktur Folder

```Iqhsan Saleh - Proyek
.
|-- README.md                 Dokumentasi proyek dan cara menjalankan
|-- .gitignore                Berkas yang tidak disimpan ke Git
|-- main.py                   Titik masuk program konsol
|-- src/
|   |-- __init__.py           Penanda package Python
|   |-- input_data.py         Membaca dan memvalidasi data siswa
|   |-- proses.py             Statistik nilai dan status ketuntasan
|   `-- output.py             Tampilan terminal dan penyimpanan laporan
|-- data/
|   `-- contoh_data.txt       Data nilai contoh
|-- tests/
|   |-- test_analisis_nilai.py Pengujian otomatis
|   `-- test_case.md          Catatan skenario pengujian
|-- docs/screenshot/          Lokasi untuk screenshot dokumentasi
`-- output/                   Laporan yang dibuat saat program berjalan
```

## Test Case

Jalankan pengujian otomatis dengan:

```bash
python3 -m unittest discover -s tests -v
```

| Input / Skenario | Expected | Actual | Status |
|---|---|---|---|
| Nilai 85, 60, 59 | Rata-rata 68; minimum 59; maksimum 85; 60 tuntas dan 59 belum tuntas | Sesuai hasil yang diharapkan | Lulus |
| Data kosong untuk `hitung_rata_rata` | Mengembalikan 0 | Mengembalikan 0 | Lulus |
| Nilai di luar 0-100 | Baris dilewati dan peringatan ditampilkan | Baris dilewati dan peringatan ditampilkan | Lulus |
| Simpan laporan ke subfolder yang belum ada | Folder dan file laporan dibuat | Folder dan file laporan dibuat | Lulus |

Terakhir diverifikasi dengan 7 tes otomatis yang lulus dan menjalankan `main.py`
dengan 5 baris data contoh.

## Dokumentasi Kode

`hitung_rata_rata(data)` di `src/proses.py` mengembalikan rata-rata list
numerik. Fungsi mengembalikan `0` jika list kosong. Fungsi ini digunakan oleh
`hitung_statistik` untuk menghitung rata-rata nilai kelas.

## Known Issues

- Baris dengan jumlah kolom selain dua diabaikan tanpa pesan peringatan.
- Nama siswa kosong belum ditolak oleh pembaca data.
- Jika file input tidak ditemukan, pembaca melaporkan error dan mengembalikan
	list kosong; program kemudian menghasilkan statistik kosong.

## Anggota dan Kontribusi

| Anggota | Kontribusi |
|---|---|
| Belum dicantumkan | Isi nama anggota dan pembagian kerja sebelum penyerahan proyek. |

## Referensi/Bantuan

- Dokumentasi resmi Python: https://docs.python.org/3/
- GitHub Copilot digunakan sebagai bantuan AI untuk implementasi, dokumentasi,
	dan penyusunan tes; hasilnya diverifikasi dengan pengujian lokal.
