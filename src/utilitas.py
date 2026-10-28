def validasi_nilai(teks_nilai):
    """Memeriksa apakah input berupa angka dan berada dalam rentang 0-100."""
    try:
        nilai = float(teks_nilai)
        if 0 <= nilai <= 100:
            return True, nilai
        return False, "Nilai di luar rentang 0-100"
    except ValueError:
        return False, "Nilai harus berupa angka"