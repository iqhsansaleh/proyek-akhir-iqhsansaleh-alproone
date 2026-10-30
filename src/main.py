"""
Modul Utama (main.py)
Mengatur alur interaksi terminal untuk program Generator Soal Aritmetika.
"""

from utilitas import validasi_angka_bulat, bersihkan_layar
from analisis import buat_soal, hitung_persentase
from data_io import simpan_laporan_ke_file


def tampilkan_menu():
	print("==========================================")
	print("   GENERATOR SOAL LATIHAN ARITMETIKA     ")
	print("==========================================")
	print("1. Tingkat Mudah   (Angka 1 - 10,  + dan -)")
	print("2. Tingkat Sedang  (Angka 10 - 50, +, -, *)")
	print("3. Tingkat Sulit   (Angka 50 - 100, +, -, *)")
	print("4. Keluar Program")
	print("==========================================")


def main():
	while True:
		tampilkan_menu()
		pilihan = validasi_angka_bulat("Pilih menu (1-4): ")

		if pilihan == 4:
			print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
			break

		if pilihan not in [1, 2, 3]:
			print("\nPilihan tidak valid. Silakan pilih angka 1 sampai 4.\n")
			continue

		mapping_tingkat = {1: "Mudah", 2: "Sedang", 3: "Sulit"}
		tingkat_str = mapping_tingkat[pilihan]

		jumlah_soal = validasi_angka_bulat(
			"Masukkan jumlah soal yang diinginkan (cth: 5): "
		)
		if jumlah_soal <= 0:
			print("\nJumlah soal harus lebih besar dari 0!\n")
			continue

		skor_benar = 0
		riwayat_jawaban = []

		print(
			f"\n--- Memulai Kuis Tingkat: {tingkat_str} "
			f"({jumlah_soal} Soal) ---"
		)

		for nomor_soal in range(1, jumlah_soal + 1):
			soal, jawaban_benar = buat_soal(tingkat_str)
			print(f"\nSoal ke-{nomor_soal}: Berapakah {soal} ?")

			jawaban_siswa = validasi_angka_bulat("Jawaban Anda: ")

			if jawaban_siswa == jawaban_benar:
				print("✅ Benar!")
				skor_benar += 1
				status = "Benar"
			else:
				print(
					f"❌ Kurang tepat. Jawaban yang benar adalah "
					f"{jawaban_benar}"
				)
				status = "Salah"

			riwayat_jawaban.append(
				{
					"no": nomor_soal,
					"soal": soal,
					"jawaban_siswa": jawaban_siswa,
					"jawaban_benar": jawaban_benar,
					"status": status,
				}
			)

		persentase = hitung_persentase(skor_benar, jumlah_soal)
		print("\n==========================================")
		print("               HASIL KUIS                 ")
		print("==========================================")
		print(f"Total Benar  : {skor_benar} dari {jumlah_soal}")
		print(f"Persentase   : {persentase:.2f}%")
		print("==========================================")

		nama_siswa = input("Masukkan nama siswa untuk laporan: ").strip()
		if not nama_siswa:
			nama_siswa = "Siswa_Anonim"

		simpan_laporan_ke_file(
			nama_siswa,
			tingkat_str,
			skor_benar,
			jumlah_soal,
			persentase,
		)

		lanjut = input("\nIngin mencoba lagi? (y/t): ").strip().lower()
		if lanjut != "y":
			print("\nProgram selesai.")
			break
		print("\n" * 2)


if __name__ == "__main__":
	main()
