"""
Modul Analisis & Logika (analisis.py)
Menyediakan fungsi pembangkit soal acak dan perhitungan statistik skor.
"""

import random


def buat_soal(tingkat):
	if tingkat == "Mudah":
		a = random.randint(1, 10)
		b = random.randint(1, 10)
		op = random.choice(["+", "-"])
		if op == "-" and a < b:
			a, b = b, a

	elif tingkat == "Sedang":
		a = random.randint(10, 50)
		b = random.randint(1, 20)
		op = random.choice(["+", "-", "*"])
		if op == "-" and a < b:
			a, b = b, a

	else:
		a = random.randint(20, 100)
		b = random.randint(10, 50)
		op = random.choice(["+", "-", "*"])
		if op == "-" and a < b:
			a, b = b, a

	expr = f"{a} {op} {b}"
	if op == "+":
		hasil = a + b
	elif op == "-":
		hasil = a - b
	else:
		hasil = a * b

	return expr, hasil


def hitung_persentase(benar, total):
	if total == 0:
		return 0.0
	return (benar / total) * 100.0
