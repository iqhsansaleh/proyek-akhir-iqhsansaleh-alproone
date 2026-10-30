from pathlib import Path
import sys

from src.input_data import baca_data_nilai
from src.output import simpan_laporan_file, tampilkan_layar
from src.proses import hitung_statistik, tentukan_status_kelas


ROOT_DIR = Path(__file__).resolve().parent
FILE_DATA = ROOT_DIR / "data" / "contoh_data.txt"
FILE_LAPORAN = ROOT_DIR / "output" / "laporan_ringkas.txt"


def main() -> int:
    try:
        data_siswa = baca_data_nilai(FILE_DATA)
        statistik = hitung_statistik(data_siswa)
        hasil_status = tentukan_status_kelas(data_siswa)
    except (OSError, ValueError) as error:
        print(f"Gagal menganalisis nilai: {error}", file=sys.stderr)
        return 1

    tampilkan_layar(statistik, hasil_status)
    if simpan_laporan_file(statistik, hasil_status, FILE_LAPORAN) is None:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
