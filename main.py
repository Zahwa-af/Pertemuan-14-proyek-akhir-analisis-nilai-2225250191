from src.data_io import baca_data, simpan_laporan
from src.analisis import proses_data_siswa, hitung_statistik

def main():
    input_path = "data/nilai_mentah.txt"
    output_path = "data/laporan_rekap.txt"
    
    print("--- MEMULAI ANALISIS DATA NILAI MATEMATIKA ---")
    data_mentah = baca_data(input_path)
    
    if not data_mentah:
        print("Proses dihentikan karena file input tidak tersedia.")
        return
        
    data_valid = proses_data_siswa(data_mentah)
    if not data_valid:
        print("Tidak ada data valid yang dapat diproses.")
        return
        
    statistik = hitung_statistik(data_valid)
    
    print("\n=== HASIL REKAPITULASI KELAS ===")
    print(f"Data Valid    : {statistik['jumlah_data']}")
    print(f"Rata-rata     : {statistik['rata_rata']:.2f}")
    print(f"Minimum       : {statistik['minimum']:.2f}")
    print(f"Maksimum      : {statistik['maksimum']:.2f}")
    print(f"Siswa Tuntas  : {statistik['jumlah_tuntas']}")
    print(f"Belum Tuntas  : {statistik['jumlah_belum_tuntas']}")
    
    simpan_laporan(output_path, statistik)

if __name__ == "__main__":
    main()