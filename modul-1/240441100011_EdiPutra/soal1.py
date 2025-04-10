class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} berjalan ke Lab TI")

    def berlari(self):
        print(f"{self.nama} berlari di taman kampus")

manusia1 = Manusia("Edi", 18, "Bangkalan")
manusia2 = Manusia("Fani", 19, "Gresik")
manusia3 = Manusia("Galuh", 20, "Sidoarjo")
manusia4 = Manusia("Irsad", 22, "Lamongan")
manusia5 = Manusia("Andre", 21, "Malang")

manusia1.berjalan()
manusia2.berjalan()
manusia3.berlari()
manusia4.berlari()
manusia5.berjalan()