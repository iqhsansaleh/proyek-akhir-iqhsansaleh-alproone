"""
Modul Input Data (Data I/O)
Bertanggung jawab membaca file teks dan memvalidasi rentang nilai (0-100).
"""


def baca_data_nilai(path):
	data_siswa = []
	try:
		with open(path, "r", encoding="utf-8") as file:
			for baris in file:
				baris = baris.strip()
				if not baris:
					continue
				parts = baris.split(",")
				if len(parts) == 2:
					nama = parts[0].strip()
					try:
						nilai = float(parts[1].strip())
						# Validasi batas nilai 0 - 100
						if 0 <= nilai <= 100:
							data_siswa.append({"nama": nama, "nilai": nilai})
						else:
							print(f"[WARNING] Nilai di luar batas (0-100) diabaikan: {nama} ({nilai})")
					except ValueError:
						print(f"[WARNING] Format angka salah pada baris: {baris}")
		print(f"[INFO] Berhasil membaca {len(data_siswa)} data valid dari file.")
		return data_siswa
	except FileNotFoundError:
		print(f"[ERROR] File pada path '{path}' tidak ditemukan.")
		return []
