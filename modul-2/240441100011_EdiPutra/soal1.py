class Mahasiswa:
    jumlah_mahasiswa = 0                     #nampilin mhs yg dibuat | class atribute

    def __init__(self, nama, nim, prodi):       #nama, nim, prodi, dftr matkul yg diambil
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.daftar_matkul = []                 #list kosong dftr matkul 

        if Mahasiswa.validasi_nim(nim) == "Valid":      #cek validasi nim pake static method
            Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):        #method tambah matkul
        self.daftar_matkul.append(matkul)

    def tampilkan_info(self):               #method biodata
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("Mata Kuliah yang diambil:")
        for matkul in self.daftar_matkul:
            print("-", matkul.nama, f"({matkul.sks} SKS)")
        print()

    @classmethod                                        #nampilin jumlah mahasiswa yang dibuat | class method
    def total_mahasiswa(cls):
        print("Total Mahasiswa ialah:", cls.jumlah_mahasiswa)

    @staticmethod                               #validasi nimnya | static method
    def validasi_nim(nim):
        if len(nim) == 10 and nim[0:2] == "23":
            return "Valid"
        else:
            return "Tidak Valid"


class MataKuliah:
    def __init__(self, kode, nama, sks):                    #atribut kode mk, nama, sks
        self.kode = kode
        self.nama = nama
        if MataKuliah.cek_sks(sks) == "Valid":      #cek sks pake static method
            self.sks = sks
        else:
            self.sks = "SKS tidak valid"

    @staticmethod
    def cek_sks(sks):               #ceksks | static method
        if sks == 2 or sks == 3:
            return "Valid"
        else:
            return "Tidak Valid"


class Kampus:
    jumlah_mahasiswa = 0            #class attribute

    def __init__(self, nama_kampus, alamat):            #attributenya nama kampus dan alamat
        self.nama_kampus = nama_kampus
        self.alamat = alamat
        Kampus.jumlah_mahasiswa = Mahasiswa.jumlah_mahasiswa        #disamakan dengan data jumlah mahasiswa di class mhs

    @classmethod
    def info_kampus(cls, nama, alamat):             #nampilin nama, alamat kampus dan total mhs | class method
        print("Nama Kampus:", nama)
        print("Alamat:", alamat)
        print("Jumlah Mahasiswa:", cls.jumlah_mahasiswa)

    @staticmethod
    def validasi_nama_kampus(nama_kampus):          #validasi nama kampus | static method
        for huruf in nama_kampus:
            if huruf in "0123456789":
                return "Tidak Valid"
        return "Valid"


# Input Mata Kuliah
print("=== Input Data Mata Kuliah (Min 8) ===")
list_matkul = []
urutan_mk = 1
while True:
    print("\nMata Kuliah ke -",urutan_mk)
    kode = input("Kode MK: ")
    nama = input("Nama MK: ")

    while True:
        sks = int(input("SKS (2 atau 3): "))
        if MataKuliah.cek_sks(sks) == "Valid":
            break
        else:
            print("SKS Harus 2 atau 3, isi lagi!")

    mk = MataKuliah(kode, nama, sks)
    list_matkul.append(mk)
    urutan_mk += 1

    if len(list_matkul) >= 8:
        lagi = input("Tambah lagi mata kuliah? (y/n): ")
        if lagi == "n":
            break


# Input Mahasiswa
print("\n=== Input Data Mahasiswa (Min 6) ===")
list_mahasiswa = []
urutan_mhs = 1
while True:
    print("\nMahasiswa ke-",urutan_mhs)
    nama = input("Nama: ")

    while True:
        nim = input("NIM: ")
        if Mahasiswa.validasi_nim(nim) == "Valid":
            break
        else:
            print("NIM Harus diawali 23 dan terdiri 10 digit, isi lagi!.")

    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim, prodi)

    print("\nPilih mata kuliah dari daftar berikut (minimal 4):")
    for matkul in list_matkul:
        print(f"{matkul.kode} - {matkul.nama} ({matkul.sks} SKS)")

    pilihan_matkul = []
    while True:
        kode_input = input("Masukkan kode mata kuliah (pilih minimal 4 matkul): ")
        mk_ditemukan = None
        for mk in list_matkul:
            if mk.kode.lower() == kode_input.lower():
                mk_ditemukan = mk
                break
        if mk_ditemukan:
            if mk_ditemukan in pilihan_matkul:
                print("Mata kuliah sudah dipilih.")
            else:
                pilihan_matkul.append(mk_ditemukan)
                print(f"{mk_ditemukan.nama} ditambahkan.")
        else:
            print("Kode MK tidak ditemukan.")

        if len(pilihan_matkul) >= 4:
            lagi = input("Tambah lagi mata kuliah? (y/n): ")
            if lagi.lower() != "y":
                break

    for mk in pilihan_matkul:
        mhs.tambah_matkul(mk)

    list_mahasiswa.append(mhs)
    urutan_mhs += 1

    if len(list_mahasiswa) >= 6:
        lagi = input("\nTambah lagi mahasiswa? (y/n): ")
        if lagi == "n":
            break


# Input data Kampus
print("\n=== Input Data Kampus ===")
while True:
    nama_kampus = input("Nama kampus: ")
    if Kampus.validasi_nama_kampus(nama_kampus) == "Valid":
        break
    else:
        print("Nama kampus mengandung angka, mohon isi data lagi!.")

alamat_kampus = input("Alamat kampus: ")
kampus = Kampus(nama_kampus, alamat_kampus)


# Output Semua Data
print("\n=== DATA MAHASISWA ===")
for m in list_mahasiswa:
    m.tampilkan_info()

Mahasiswa.total_mahasiswa()

print("\n=== DATA KAMPUS ===")
Kampus.info_kampus(kampus.nama_kampus, kampus.alamat)
print("Validasi Nama Kampus (tidak mengandung angka):", Kampus.validasi_nama_kampus(kampus.nama_kampus))