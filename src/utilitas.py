"""
Modul Utilitas (utilitas.py)
Berisi fungsi validasi input dan bantuan antarmuka terminal.
"""


def validasi_angka_bulat(pesan):
	while True:
		try:
			nilai = int(input(pesan))
			return nilai
		except ValueError:
			print("❌ Input tidak valid! Harap masukkan angka bulat yang benar.")


def bersihkan_layar():
	print("\n" * 2)
