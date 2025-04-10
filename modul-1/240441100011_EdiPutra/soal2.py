class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_data(self):
        print(f"\nNama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Alamat   : {self.alamat}")
        print("-" * 30)

daftar_mahasiswa = []
print("Silakan masukkan data mahasiswa (minimal 3 data)")
while True:
    print(f"\nData Mahasiswa ke-{len(daftar_mahasiswa)+1}")
    
    nama = input("Nama     : ")
    if not nama:
        print("Nama tidak boleh kosong! mohon isi dengan benar.")
        continue
    nim = input("NIM      : ")
    if not nim:
        print("NIM tidak boleh kosong! mohon isi dengan benar.")
        continue
    jurusan = input("Jurusan  : ")
    if not jurusan:
        print("Jurusan tidak boleh kosong! mohon isi dengan benar.")
        continue
    alamat = input("Alamat   : ")
    if not alamat:
        print("Alamat tidak boleh kosong! mohon isi dengan benar.")
        continue

    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    daftar_mahasiswa.append(mahasiswa)
    if len(daftar_mahasiswa) < 3:
        print(f"Data mahasiswa masih kurang dari 3. Silakan isi lagi.")
        continue

    while True:
        lanjut = input("Tambah data lagi? (y/n): ")
        if lanjut == 'y':
            break
        elif lanjut == 'n':
            print("daftar mahasiswa yang telah diinput:")
            for mhs in daftar_mahasiswa:
                mhs.tampilkan_data()
            exit()
        else:
            print("Pilihan tidak valid! Mohon pilih 'y' atau 'n'.")