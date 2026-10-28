def baca_data(path_file):
    """Membaca file masukan teks baris demi baris."""
    hasil = []
    try:
        with open(path_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if baris:
                    hasil.append((nomor, baris))
    except FileNotFoundError:
        print(f"[ERROR] File tidak ditemukan: {path_file}")
    return hasil

def simpan_laporan(path_file, statistik):
    """Menuliskan ringkasan hasil rekapitulasi ke file teks output."""
    with open(path_file, "w", encoding="utf-8") as file:
        file.write("=== LAPORAN REKAP NILAI MATEMATIKA ===\n")
        file.write(f"Jumlah Data Valid : {statistik['jumlah_data']}\n")
        file.write(f"Rata-Rata Kelas   : {statistik['rata_rata']:.2f}\n")
        file.write(f"Nilai Minimum     : {statistik['minimum']:.2f}\n")
        file.write(f"Nilai Maksimum    : {statistik['maksimum']:.2f}\n")
        file.write(f"Jumlah Tuntas     : {statistik['jumlah_tuntas']}\n")
        file.write(f"Jumlah Belum Tuntas: {statistik['jumlah_belum_tuntas']}\n")
    print(f"[INFO] Laporan berhasil disimpan ke {path_file}")