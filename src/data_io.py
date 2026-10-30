"""
Modul Data I/O (data_io.py)
Menangani penyimpanan laporan hasil kuis ke dalam file teks di folder output/.
"""

import os


def simpan_laporan_ke_file(nama_siswa, tingkat, benar, total, persentase):
	direktori_proyek = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	direktori_output = os.path.join(direktori_proyek, "output")
	nama_file = os.path.join(direktori_output, "laporan_nilai.txt")

	try:
		os.makedirs(direktori_output, exist_ok=True)
		with open(nama_file, "a", encoding="utf-8") as file:
			file.write("========================================\n")
			file.write("LAPORAN LATIHAN ARITMETIKA\n")
			file.write(f"Nama Siswa   : {nama_siswa}\n")
			file.write(f"Tingkat      : {tingkat}\n")
			file.write(f"Skor         : {benar} / {total}\n")
			file.write(f"Persentase   : {persentase:.2f}%\n")
			file.write("========================================\n\n")
		print(f"\n[Info] Laporan berhasil disimpan ke {nama_file}")
	except OSError:
		print("\n[Error] Gagal menyimpan file laporan ke sistem.")
