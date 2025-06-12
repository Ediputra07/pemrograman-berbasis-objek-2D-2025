from kendaraan import Kendaraan

class Mobil(Kendaraan):
    def __init__(self):
        self.__biaya = 0
        self.__asuransi = 250000

    def get_biaya(self):
        return self.__biaya

    def set_biaya(self, usia):
        if usia >= 25:
            self.__biaya = 500000
        elif usia >= 17:
            self.__biaya = 250000

    def proses_booking(self, usia):
        if usia < 17:
            print("Maaf, usia minimal untuk memesan mobil adalah 17 tahun.")
            return False

        self.set_biaya(usia)
        total = self.__biaya
        while True:
            print("Apakah Anda ingin menambahkan asuransi?")
            print("1. Ya")
            print("2. Tidak")
            pilihan = input("Pilih (1/2): ")
            if pilihan == "1":
                total += self.__asuransi
                print(f"Asuransi ditambahkan: Rp{self.__asuransi:,}")
                break
            elif pilihan == "2":
                break
            else:
                print("Mohon pilih 1 atau 2")
        print(f"Total dibayar: Rp{total:,}")
        return True