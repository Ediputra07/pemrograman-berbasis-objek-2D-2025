class ayam:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def suara(self):
        print(f"Ayam namanya {self.nama} berwarna {self.warna} mengeluarkan suara 'cukurukuk'")

class sapi:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat

    def suara(self):
        print(f"Sapi bernama {self.nama} beratnya {self.berat}kg mengeluarkan suara 'moooo'")

class kambing:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat

    def suara(self):
        print(f"Kambing bernama {self.nama} memiliki berat {self.berat}kg dan mengeluarkan suara 'mbek'")

daftar_hewan = [
    ayam("Rambo", "coklat"),
    sapi("Lembu", "100"),
    kambing("Son", "50")
]

for hewan in daftar_hewan:
    hewan.suara()