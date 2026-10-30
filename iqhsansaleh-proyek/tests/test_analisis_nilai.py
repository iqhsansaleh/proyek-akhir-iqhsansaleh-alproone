import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from src.input_data import baca_data_nilai
from src.output import simpan_laporan_file, tampilkan_layar
from src.proses import hitung_rata_rata, hitung_statistik, tentukan_status_kelas


class TestAnalisisNilai(unittest.TestCase):
    def test_baca_data_valid(self):
        with tempfile.TemporaryDirectory() as direktori:
            file_data = Path(direktori) / "nilai.txt"
            file_data.write_text("Andi,85\nBunga,60\n", encoding="utf-8")

            self.assertEqual(
                baca_data_nilai(file_data),
                [{"nama": "Andi", "nilai": 85.0}, {"nama": "Bunga", "nilai": 60.0}],
            )

    def test_baca_data_mengabaikan_nilai_di_luar_rentang(self):
        with tempfile.TemporaryDirectory() as direktori:
            file_data = Path(direktori) / "nilai.txt"
            file_data.write_text("Andi,-1\nBunga,101\nCitra,80\n", encoding="utf-8")
            keluaran = io.StringIO()

            with redirect_stdout(keluaran):
                data = baca_data_nilai(file_data)

            self.assertEqual(data, [{"nama": "Citra", "nilai": 80.0}])
            self.assertIn("di luar batas", keluaran.getvalue())

    def test_baca_data_mengabaikan_format_angka_tidak_valid(self):
        with tempfile.TemporaryDirectory() as direktori:
            file_data = Path(direktori) / "nilai.txt"
            file_data.write_text("Andi,bukan-angka\nBunga,75\n", encoding="utf-8")
            keluaran = io.StringIO()

            with redirect_stdout(keluaran):
                data = baca_data_nilai(file_data)

            self.assertEqual(data, [{"nama": "Bunga", "nilai": 75.0}])
            self.assertIn("Format angka salah", keluaran.getvalue())

    def test_hitung_statistik_dan_status_kelas(self):
        data = [
            {"nama": "Andi", "nilai": 85},
            {"nama": "Bunga", "nilai": 60},
            {"nama": "Citra", "nilai": 59},
        ]

        self.assertEqual(
            hitung_statistik(data),
            {"jumlah": 3, "rata_rata": 68, "minimum": 59, "maksimum": 85},
        )
        self.assertEqual(
            tentukan_status_kelas(data),
            [
                {"nama": "Andi", "nilai": 85, "status": "Tuntas"},
                {"nama": "Bunga", "nilai": 60, "status": "Tuntas"},
                {"nama": "Citra", "nilai": 59, "status": "Belum Tuntas"},
            ],
        )
        self.assertEqual(tentukan_status_kelas(data, kkm=70)[1]["status"], "Belum Tuntas")

    def test_statistik_data_kosong(self):
        self.assertEqual(
            hitung_statistik([]),
            {"jumlah": 0, "rata_rata": 0, "minimum": 0, "maksimum": 0},
        )
        self.assertEqual(hitung_rata_rata([]), 0)
        self.assertEqual(hitung_rata_rata([70, 80, 90]), 80)

    def test_tampilkan_layar_memuat_ringkasan(self):
        statistik = hitung_statistik([{"nama": "Andi", "nilai": 75}])
        hasil_status = tentukan_status_kelas([{"nama": "Andi", "nilai": 75}])
        keluaran = io.StringIO()

        with redirect_stdout(keluaran):
            tampilkan_layar(statistik, hasil_status)

        self.assertIn("Total Siswa Dinilai : 1", keluaran.getvalue())
        self.assertIn("Andi : 75 (Tuntas)", keluaran.getvalue())

    def test_simpan_laporan_membuat_folder_output(self):
        data = [{"nama": "Andi", "nilai": 75}]
        statistik = hitung_statistik(data)
        hasil_status = tentukan_status_kelas(data)

        with tempfile.TemporaryDirectory() as direktori:
            file_laporan = Path(direktori) / "output" / "laporan.txt"
            keluaran = io.StringIO()
            with redirect_stdout(keluaran):
                hasil = simpan_laporan_file(statistik, hasil_status, file_laporan)

            self.assertEqual(hasil, file_laporan)
            isi_laporan = file_laporan.read_text(encoding="utf-8")
            self.assertIn("Total Siswa : 1", isi_laporan)
            self.assertIn("Andi | 75 | Tuntas", isi_laporan)


if __name__ == "__main__":
    unittest.main()