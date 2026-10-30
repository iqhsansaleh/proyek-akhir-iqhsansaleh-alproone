"""
Modul Output
Menampilkan hasil ringkasan ke layar terminal dan menulis laporan ke file teks.
"""

from pathlib import Path


def tampilkan_layar(statistik, hasil_status):
	print("\n--- HASIL ANALISIS STATISTIK KELAS ---")
	print(f"Total Siswa Dinilai : {statistik['jumlah']}")
	print(f"Nilai Rata-rata     : {statistik['rata_rata']}")
	print(f"Nilai Minimum       : {statistik['minimum']}")
	print(f"Nilai Maksimum      : {statistik['maksimum']}")
	print("-" * 38)
	print("Daftar Status Siswa:")
	for mhs in hasil_status:
		print(f"- {mhs['nama']} : {mhs['nilai']} ({mhs['status']})")


def simpan_laporan_file(statistik, hasil_status, path_output="output/laporan_ringkas.txt"):
	try:
		lokasi_laporan = Path(path_output)
		lokasi_laporan.parent.mkdir(parents=True, exist_ok=True)
		with lokasi_laporan.open("w", encoding="utf-8") as file:
			file.write("LAPORAN REKAP NILAI MATEMATIKA KELAS\n")
			file.write("=" * 35 + "\n")
			file.write(f"Total Siswa : {statistik['jumlah']}\n")
			file.write(f"Rata-rata   : {statistik['rata_rata']}\n")
			file.write(f"Minimum     : {statistik['minimum']}\n")
			file.write(f"Maksimum    : {statistik['maksimum']}\n")
			file.write("-" * 35 + "\n")
			for mhs in hasil_status:
				file.write(f"{mhs['nama']} | {mhs['nilai']} | {mhs['status']}\n")
		print(f"\n[INFO] Laporan berhasil disimpan ke '{lokasi_laporan}'.")
		return lokasi_laporan
	except OSError as error:
		print(f"[ERROR] Gagal menyimpan file laporan: {error}")
		return None
