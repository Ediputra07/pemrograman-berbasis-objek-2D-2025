from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def proses_layanan(buku, layanan, nama):
    if layanan == "1":
        durasi = input("Masukkan durasi pinjam (dalam hari): ")
        if durasi.isdigit():
            buku.pinjam(nama, int(durasi))
        else:
            print("Durasi harus angka.")
    elif layanan == "2":
        hari = input("Masukkan hari untuk reservasi: ")
        buku.reservasi(nama, hari)
    else:
        print("Layanan tidak valid.")

def main():
    print("=== Sistem Peminjaman & Reservasi Buku ===")
    
    while True:
        nama = input("Masukkan nama Anda: ")
        if nama.isalpha():
            break
        print("Nama tidak boleh ada angka")

    print("\nPilih jenis buku:")
    print("1. Buku Fiksi")
    print("2. Buku Referensi")
    pilihan = input("Pilihan (1/2): ")

    if pilihan == "1":
        buku = BukuFiksi()
    elif pilihan == "2":
        buku = BukuReferensi()
    else:
        print("Pilihan tidak valid.")
        return

    print("\nPilih layanan:")
    print("1. Pinjam")
    print("2. Reservasi")
    layanan = input("Pilihan (1/2): ")

    proses_layanan(buku, layanan, nama)

main()