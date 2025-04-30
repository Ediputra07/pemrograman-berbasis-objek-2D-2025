class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}, Gaji: Rp{self.gaji:,}, Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan:,}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam/hari")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

m = ManajemenKaryawan()
m.tambah_karyawan(KaryawanTetap("Armin", 8000000, "Keuangan", 50000))
m.tambah_karyawan(KaryawanTetap("Inqu", 6000000, "IT", 1000000))
m.tambah_karyawan(KaryawanHarian("Loptus", 100000, "Produksi", 8))
m.tambah_karyawan(KaryawanHarian("Budi", 100000, "Manajemen", 6))
m.tampilkan_semua_karyawan()