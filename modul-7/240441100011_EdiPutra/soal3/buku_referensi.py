from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def __init__(self):
        self.__maks_pinjam = 3
        self.__maks_reservasi_hari = ["Sabtu", "Minggu"]

    def pinjam(self, nama, durasi):
        if durasi > self.__maks_pinjam:
            print(f"Maaf {nama}, buku referensi hanya bisa dipinjam maksimal {self.__maks_pinjam} hari.")
        else:
            print(f"{nama} meminjam buku referensi selama {durasi} hari.")

    def reservasi(self, nama, hari):
        if hari.capitalize() not in self.__maks_reservasi_hari:
            print(f"Maaf {nama}, buku referensi hanya bisa direservasi untuk weekend saja (Sabtu-Minggu).")
        else:
            print(f"{nama} berhasil reservasi buku referensi untuk hari {hari}.")