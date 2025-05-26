import math

class BangunDatar:
    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun):
    print(f"Bangun Datar: {bangun.__class__.__name__}")
    print(f"Luas: {bangun.luas():.2f}\n")

def main():
    while True:
        print("Pilih bangun datar")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            while True:
                sisi = input("Masukkan panjang sisi: ")
                if sisi.isdigit():
                    sisi = int(sisi)
                    obj = Persegi(sisi)
                    cetak_luas(obj)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
        elif pilihan == "2":
            while True:
                r = input("Masukkan jari-jari: ")
                if r.isdigit():
                    r = int(r)
                    obj = Lingkaran(r)
                    cetak_luas(obj)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
        elif pilihan == "3":
            while True:
                alas = input("Masukkan alas: ")
                if alas.isdigit():
                    alas = int(alas)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
            while True:
                tinggi = (input("Masukkan tinggi: "))
                if tinggi.isdigit():
                    tinggi = int(tinggi)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
            obj = Segitiga(alas, tinggi)
            cetak_luas(obj)
        elif pilihan == "4":
            print("Terima kasih menggunakan program.")
            break
        else:
            print("Pilihan tidak valid.\n")

main()