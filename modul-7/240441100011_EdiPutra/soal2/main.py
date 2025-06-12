from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def proses_pemesanan(kendaraan, nama, usia):
    berhasil = kendaraan.proses_booking(usia)
    if berhasil:
        print(f"{nama}, Anda berhasil memesan {kendaraan.__class__.__name__}.")
        print(f"Biaya {kendaraan.__class__.__name__}: Rp{kendaraan.get_biaya():,}")

def main():
    print("=== Sistem Pemesanan Kendaraan ===")
    
    while True:
        nama = input("Masukkan nama Anda: ")
        if nama.isalpha():
            break
        print("Nama tidak boleh ada angka")

    while True:
        usia = input("Masukkan usia Anda: ")
        if usia.isdigit():
            usia = int(usia)
            break
        print("Usia harus berupa angka")

    print("--- Pilih Jenis Kendaraan ---")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")
    pilihan = input("Pilih kendaraan (1/2/3): ")

    kendaraan = None
    if pilihan == "1":
        kendaraan = Mobil()
    elif pilihan == "2":
        kendaraan = Motor()
    elif pilihan == "3":
        kendaraan = Sepeda()
    else:
        print("Maaf, pilihan tidak tersedia.")
        return

    proses_pemesanan(kendaraan, nama, usia)

main()