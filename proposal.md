# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python Console.

## 2. Latar Belakang Masalah
Guru matematika membutuhkan program sederhana yang dapat membaca data nilai siswa dari file teks, memvalidasi format dan rentang nilai, menghitung ringkasan statistik kelas, menentukan status ketuntasan berdasarkan KKM, serta menyimpan laporan ke file eksternal secara otomatis dan konsisten[cite: 62, 67].

## 3. Pengguna dan Tujuan
- **Pengguna:** Guru Matematika Sekolah / Pengajar[cite: 62].
- **Tujuan:** Mempercepat proses rekapitulasi nilai dan analisis ketuntasan belajar siswa serta mencegah kesalahan perhitungan manual[cite: 62].

## 4. Ruang Lingkup (Scope)
- Berjalan pada antarmuka konsol/terminal VS Code[cite: 61].
- Membaca file data masukan teks (`data/nilai_mentah.txt`)[cite: 67].
- Memvalidasi nilai dalam rentang valid 0–100[cite: 67].
- Menghitung statistik (rata-rata, minimum, maksimum, jumlah tuntas/belum tuntas)[cite: 67].
- Menyimpan hasil rekap ke file keluaran (`data/laporan_rekap.txt`)[cite: 67].

## 5. Kebutuhan Sistem
### Kebutuhan Fungsional (Functional Requirements)
- **F01:** Program dapat membaca data dari file teks[cite: 62].
- **F02:** Program memvalidasi rentang nilai (0-100) dan mengabaikan nilai invalid/huruf[cite: 62].
- **F03:** Program menghitung rata-rata, nilai minimum, dan maksimum[cite: 62].
- **F04:** Program mengklasifikasikan siswa tuntas jika nilai >= 60 (KKM)[cite: 62, 67].
- **F05:** Program menyimpan ringkasan ke file keluaran[cite: 62].

### Kebutuhan Non-Fungsional
- Program mudah dijalankan melalui terminal dengan perintah Python 3[cite: 62].
- Penanganan error yang informatif (tidak crash saat file tidak ditemukan)[cite: 62, 65].

## 6. Spesifikasi IPO (Input - Proses - Output)
- **Input:** File `data/nilai_mentah.txt` dengan format `NIM,Nama,Nilai` per baris[cite: 63, 67].
- **Proses:** 
  1. Pembacaan file dan pembersihan string (`strip`, `split`)[cite: 63, 64].
  2. Validasi tipe data float dan rentang `0 <= nilai <= 100`[cite: 62, 67].
  3. Perhitungan statistik dan penentuan status kelulusan[cite: 63, 67].
- **Output:** Tampilan laporan di terminal dan penulisan file `data/laporan_rekap.txt`[cite: 63, 67].

## 7. Pseudocode Alur Utama
```text
MULAI
    baca data dari "data/nilai_mentah.txt"
    JIKA file tidak ditemukan:
        tampilkan pesan error "File tidak ditemukan"
        SELESAI

    UNTUK setiap baris data:
        pisahkan NIM, Nama, dan Nilai
        JIKA nilai bukan angka ATAU nilai < 0 ATAU nilai > 100:
            catat peringatan dan lewati baris
        LAINNYA:
            simpan ke list data valid

    JIKA data valid kosong:
        tampilkan "Tidak ada data valid"
        SELESAI

    hitung rata-rata, minimum, maksimum
    hitung jumlah tuntas (nilai >= 60) dan belum tuntas
    tampilkan ringkasan di terminal
    tulis ringkasan ke "data/laporan_rekap.txt"
SELESAI
```[cite: 63, 68]

## 8. Struktur Program dan Modularisasi
- `data_io.py`: Berisi fungsi pembacaan file masukan dan penulisan file laporan keluaran.
- `analisis.py`: Berisi fungsi perhitungan statistik (rata-rata, min, max, ketuntasan)[cite: 64].
- `utilitas.py`: Berisi fungsi validasi nilai dan pembersihan data[cite: 64].
- `main.py`: Mengatur alur eksekusi utama program[cite: 64].

## 9. Pemilihan Struktur Data
- **List of Dictionary:** Digunakan untuk menampung record siswa `[{"nim": ..., "nama": ..., "nilai": ..., "status": ...}]` karena fleksibel dan mudah diakses berdasarkan nama atribut.
- **Dictionary:** Digunakan untuk mengemas ringkasan statistik kelas[cite: 64].

## 10. Perencanaan Test Case Awal
- **TC01 (Normal):** Input `85`, `78`, `92` -> Rata-rata valid dan status terhitung[cite: 65].
- **TC02 (Batas):** Input `0` dan `100` -> Diterima sebagai nilai valid[cite: 65].
- **TC03 (Batas KKM):** Input `60` -> Status "Tuntas"[cite: 65, 67].
- **TC04 (Invalid Value):** Input `105` atau `"abc"` -> Ditolak dengan peringatan[cite: 65].
- **TC05 (File Missing):** File tidak ada -> Menampilkan pesan `FileNotFoundError` tanpa crash[cite: 65].

## 11. Pembagian Tugas Tim
- **Koordinator & Main Loop:** [Nama / NIM] - Penanggung jawab proposal & `main.py`[cite: 65].
- **Programmer Data I/O:** [Nama / NIM] - Penanggung jawab `data_io.py`[cite: 65].
- **Programmer Logika & Validasi:** [Nama / NIM] - Penanggung jawab `analisis.py` & `utilitas.py`[cite: 65].
- **Tester & Documentation:** [Nama / NIM] - Penanggung jawab `test_case.md` & `README.md`[cite: 65].

## 12. Repository GitHub
URL Repository: `https://github.com/USERNAME/proyek-akhir-analisis-nilai-NIM.git`[cite: 66, 67]