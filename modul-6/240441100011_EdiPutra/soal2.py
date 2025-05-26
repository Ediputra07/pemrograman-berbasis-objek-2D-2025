from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, gaji_pokok, tunjangan, potongan):
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
        self.potongan = potongan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan - self.potongan

class KaryawanKontrak(Karyawan):
    def __init__(self, upah_per_jam, jumlah_jam, lembur_per_jam, jam_lembur):
        self.upah_per_jam = upah_per_jam
        self.jumlah_jam = jumlah_jam
        self.lembur_per_jam = lembur_per_jam
        self.jam_lembur = jam_lembur

    def hitung_gaji(self):
        gaji_pokok = self.upah_per_jam * self.jumlah_jam
        gaji_lembur = self.lembur_per_jam * self.jam_lembur
        return gaji_pokok + gaji_lembur

def cetak_gaji(karyawan):
    print(f"Gaji {karyawan.__class__.__name__}: Rp {karyawan.hitung_gaji():,}\n")

def main():
    while True:
        print("Pilih jenis karyawan:")
        print("1. Karyawan Tetap")
        print("2. Karyawan Kontrak")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            while True:
                gaji_pokok = input("Masukkan gaji pokok: ")
                if gaji_pokok.isdigit():
                    gaji_pokok = int(gaji_pokok)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
            while True:
                tunjangan = input("Masukkan tunjangan: ")
                if tunjangan.isdigit():
                    tunjangan = int(tunjangan)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
            tanya_potongan = input("Apakah ada potongan? (ya/tidak): ").lower()
            if tanya_potongan == "ya":
                while True:
                    potongan = input("Masukkan jumlah potongan: ")
                    if potongan.isdigit():
                        potongan = int(potongan)
                        break
                    else:
                        print("tidak boleh huruf atau angka negatif")
            else:
                potongan = 0
            obj = KaryawanTetap(gaji_pokok, tunjangan, potongan)
            cetak_gaji(obj)

        elif pilihan == "2":
            while True:
                upah_per_jam = input("Masukkan upah per jam: ")
                if upah_per_jam.isdigit():
                    upah_per_jam = int(upah_per_jam)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
            while True:
                jumlah_jam = input("Masukkan jumlah jam kerja: ")
                if jumlah_jam.isdigit():
                    jumlah_jam = int(jumlah_jam)
                    break
                else:
                    print("tidak boleh huruf atau angka negatif")
            tanya_lembur = input("Apakah ada jam lembur? (ya/tidak): ").lower()
            if tanya_lembur == "ya":
                while True:
                    lembur_per_jam = input("Masukkan upah lembur per jam: ")
                    if lembur_per_jam.isdigit():
                        lembur_per_jam = int(lembur_per_jam)
                        break
                    else:
                        print("tidak boleh huruf atau angka negatif")
                while True:
                    jam_lembur = input("Masukkan jumlah jam lembur: ")
                    if jam_lembur.isdigit():
                        jam_lembur = int(jam_lembur)
                        break
                    else:
                        print("tidak boleh huruf atau angka negatif")
            else:
                lembur_per_jam = 0
                jam_lembur = 0
            obj = KaryawanKontrak(upah_per_jam, jumlah_jam, lembur_per_jam, jam_lembur)
            cetak_gaji(obj)

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

main()