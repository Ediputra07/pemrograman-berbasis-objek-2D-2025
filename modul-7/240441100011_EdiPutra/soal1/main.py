from tunai import Tunai
from kartu_kredit import KartuKredit
from dompet_digital import DompetDigital

def proses(i, j):
    i.proses_pembayaran(j)

def main():
    while True:
        jumlah = input("Masukkan total belanja: ")
        if jumlah.isdigit():
            jumlah = int(jumlah)
        else:
            print("Mohon Masukkan angka valid")
            continue

        print("--- Metode Pembayaran ---")
        print("1. Tunai")
        print("2. Kartu Kredit")
        print("3. Dompet Digital")
        pilihan = input("Pilih metode (1/2/3): ")

        if pilihan == "1":
            t = Tunai()
            proses(t, jumlah)
            print(f"Diskon yang didapatkan: {t.get_diskon():g}%")
            break

        elif pilihan == "2":
            k = KartuKredit()
            proses(k, jumlah)
            print(f"Biaya tambahan: Rp{k.get_biaya():,}")
            break

        elif pilihan == "3":
            d = DompetDigital()
            proses(d, jumlah)
            print(f"Potongan yang diberikan: Rp{d.get_potongan():,}")
            break

        else:
            print("Metode tidak ada")

main()