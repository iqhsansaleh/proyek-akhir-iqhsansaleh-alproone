# Test Case

1. Data valid dengan nilai 0, 60, dan 100 diterima.
2. Nilai kurang dari 0 atau lebih dari 100 dilewati dengan peringatan.
3. Nilai 60 berstatus tuntas; nilai di bawah 60 belum tuntas.
4. Rata-rata, minimum, maksimum, dan jumlah status sesuai data siswa.
5. Laporan tersimpan dan folder output dibuat otomatis.

Pengujian otomatis untuk skenario ini dijalankan dengan
`python -m unittest discover -s tests -v`.
