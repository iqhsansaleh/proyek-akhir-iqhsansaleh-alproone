# Dokumen Pengujian (Test Case) Proyek Aritmetika

Dokumen ini mencatat skenario pengujian awal sebelum program diimplementasikan penuh pada Pertemuan 15.

| ID Test Case | Kategori | Skenario / Kondisi Input | Expected Result (Hasil yang Diharapkan) | Status |
|--------------|----------|---------------------------|------------------------------------------|--------|
| TC01         | Normal   | Pilih menu 1 (Mudah), input jumlah soal: 3, lalu jawab seluruh soal dengan benar. | Program menghitung skor 3/3 (100%), menampilkan pesan sukses, dan mencatat hasil ke file laporan. | 🟢 Ready |
| TC02         | Batas    | Input jumlah soal bernilai 1 (batas minimum). | Program mengeksekusi tepat 1 soal kuis, lalu masuk ke rekap akhir. | 🟢 Ready |
| TC03         | Invalid  | Masukkan teks huruf (misalnya, "lima") saat diminta memasukkan jawaban angka. | Program menampilkan pesan validasi, tidak *crash*, dan meminta input ulang tanpa keluar dari aplikasi. | 🟢 Ready |
| TC04         | Normal   | Jawab salah pada beberapa soal. | Persentase skor dihitung secara akurat berdasarkan proporsi jawaban benar. | 🟢 Ready |
| TC05         | Normal   | Periksa pembuatan file laporan di folder `output/`. | File `laporan_nilai.txt` dibuat otomatis setelah hasil sesi kuis disimpan. | 🟢 Ready |
