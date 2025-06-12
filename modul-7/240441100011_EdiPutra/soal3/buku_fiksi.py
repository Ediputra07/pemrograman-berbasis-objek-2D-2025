from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def __init__(self):
        self.__maks_pinjam = 7
        self.__hari_reservasi = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

    def pinjam(self, nama, durasi):
        if durasi > self.__maks_pinjam:
            print(f"Maaf {nama}, buku fiksi hanya bisa dipinjam maksimal {self.__maks_pinjam} hari.")
        else:
            print(f"{nama} meminjam buku fiksi selama {durasi} hari.")

    def reservasi(self, nama, hari):
        if hari.capitalize() not in self.__hari_reservasi:
            print(f"Maaf {nama}, buku fiksi hanya bisa direservasi pada hari kerja (Senin–Jumat).")
        else:
            print(f"{nama} berhasil reservasi buku fiksi untuk hari {hari}.")