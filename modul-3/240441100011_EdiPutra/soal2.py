class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan
    
    def estimasi_waktu(self):
        return 5

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
    
    def estimasi_waktu(self):
        if self.jenis_kendaraan == "mobil":
            return 3
        elif self.jenis_kendaraan == "truk":
            return 7
        else:
            return super().estimasi_waktu()

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
    
    def estimasi_waktu(self):
        if self.maskapai == "garuda indonesia":
            return 1
        elif self.maskapai == "lion air":
            return 2
        else:
            return super().estimasi_waktu()

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    kota_dlm_negri = [
        "jakarta", "surabaya", "bandung", "medan", "semarang", "makassar", "palembang", "yogyakarta", "depok", "tangerang",
        "bekasi", "bogor", "malang", "padang", "madura", "denpasar", "balikpapan", "banjarmasin", "serang", "batam", "pekanbaru",
        "pontianak", "madura"
    ]

    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

        if self.tujuan not in self.kota_dlm_negri:
            self.status = "Luar Negeri"
        else:
            self.status = "Dalam Negeri"
    
    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        waktu_awal = waktu_darat + waktu_udara 

        if self.status == "Luar Negeri":
            return waktu_awal + 3
        return waktu_awal

p1 = PengirimanInternasional("jakarta", "tokyo", "mobil", "garuda indonesia")
p2 = PengirimanInternasional("surabaya", "tangerang", "truk", "lion air")
p3 = PengirimanInternasional("bandung", "yogyakarta", "motor", "citylink")

print(f"Pengiriman dari {p1.asal} ke {p1.tujuan}")
print(f"- Kendaraan: {p1.jenis_kendaraan}, Maskapai: {p1.maskapai}")
print(f"- Status: {p1.status}, Estimasi waktu: {p1.estimasi_waktu()} hari")

print(f"\nPengiriman dari {p2.asal} ke {p2.tujuan}")
print(f"- Kendaraan: {p2.jenis_kendaraan}, Maskapai: {p2.maskapai}")
print(f"- Status: {p2.status}, waktu: {p2.estimasi_waktu()} hari")

print(f"\nPengiriman dari {p3.asal} ke {p3.tujuan}")
print(f"- Kendaraan: {p3.jenis_kendaraan}, Maskapai: {p3.maskapai}")
print(f"- Status: {p3.status}, Estimasi waktu: {p3.estimasi_waktu()} hari") 