from src.utilitas import validasi_nilai

def proses_data_siswa(data_mentah):
    """Memproses data mentah menjadi list of dictionary berisi record siswa valid."""
    data_valid = []
    for nomor, baris in data_mentah:
        bagian = baris.split(",")
        if len(bagian) != 3:
            print(f"Baris {nomor} dilewati (format tidak sesuai): {baris}")
            continue
        
        nim, nama, teks_nilai = bagian
        is_valid, hasil = validasi_nilai(teks_nilai.strip())
        
        if is_valid:
            nilai = hasil
            status = "Tuntas" if nilai >= 60 else "Belum Tuntas"
            data_valid.append({
                "nim": nim.strip(),
                "nama": nama.strip(),
                "nilai": nilai,
                "status": status
            })
        else:
            print(f"Baris {nomor} dilewati ({hasil}): {baris}")
            
    return data_valid

def hitung_statistik(data_valid):
    """Menghitung ringkasan statistik dari list data siswa yang valid."""
    if not data_valid:
        return None
    
    daftar_nilai = [item["nilai"] for item in data_valid]
    tuntas = sum(1 for item in data_valid if item["status"] == "Tuntas")
    
    return {
        "jumlah_data": len(daftar_nilai),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "jumlah_tuntas": tuntas,
        "jumlah_belum_tuntas": len(daftar_nilai) - tuntas
    }