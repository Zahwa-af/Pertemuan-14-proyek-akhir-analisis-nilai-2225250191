# Rancangan Test Case Proyek Akhir

| ID | Kategori | Kondisi / Input | Expected Result | Status Plan |
| :--- | :--- | :--- | :--- | :--- |
| **TC01** | Normal | `A001,Andi,85` | Nilai diterima, rata-rata dihitung benar | Planned |
| **TC02** | Batas | `A007,Siti,60` | Dikategorikan sebagai "Tuntas" (>= 60) | Planned |
| **TC03** | Batas Minimum | `A008,Budi,0` | Diterima sebagai nilai valid | Planned |
| **TC04** | Invalid Rentang | `A004,Dewi,105` | Ditolak dengan pesan validasi rentang | Planned |
| **TC05** | Invalid Tipe | `A005,Rian,abc` | Ditolak dengan pesan validasi angka | Planned |
| **TC06** | Error File | File `nilai_mentah.txt` dihapus | Menampilkan pesan error file tidak ditemukan | Planned |