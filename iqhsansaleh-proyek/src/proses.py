"""
Modul Proses / Logika
Berisi fungsi matematika untuk menghitung statistik kelas dan status ketuntasan.
"""


def hitung_rata_rata(data):
	"""Mengembalikan rata-rata list numerik.

	Jika data kosong, fungsi mengembalikan 0.
	"""
	if not data:
		return 0
	return sum(data) / len(data)


def hitung_statistik(data):
	if not data:
		return {"jumlah": 0, "rata_rata": 0, "minimum": 0, "maksimum": 0}

	nilai_list = [item["nilai"] for item in data]
	jumlah = len(nilai_list)
	rata_rata = hitung_rata_rata(nilai_list)
	minimum = min(nilai_list)
	maksimum = max(nilai_list)

	return {
		"jumlah": jumlah,
		"rata_rata": round(rata_rata, 2),
		"minimum": minimum,
		"maksimum": maksimum,
	}


def tentukan_status_kelas(data, kkm=60):
	hasil = []
	for item in data:
		status = "Tuntas" if item["nilai"] >= kkm else "Belum Tuntas"
		hasil.append({
			"nama": item["nama"],
			"nilai": item["nilai"],
			"status": status,
		})
	return hasil
