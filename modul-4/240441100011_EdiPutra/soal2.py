class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    def get_info(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Halaman: {self.__halaman}"

    def get_judul(self):
        return self.__judul

    def set_judul(self, judul_baru):
        self.__judul = judul_baru

    def set_penulis(self, penulis_baru):
        self.__penulis = penulis_baru

    def set_halaman(self, halaman_baru):
        self.__halaman = halaman_baru

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan(self):
        print("\nDaftar Buku:")
        if not self.daftar_buku:
            print("Belum ada data.")
        for i in range(len(self.daftar_buku)):
            print(f"{i+1}. {self.daftar_buku[i].get_info()}")

    def update(self, no):
        if no >= 0 and no < len(self.daftar_buku):
            buku = self.daftar_buku[no]
            print("1. Judul")
            print("2. Penulis")
            print("3. Halaman")
            pilih = input("Pilih bagian yang ingin diubah: ")
            if pilih == "1":
                j = input("Judul baru: ")
                buku.set_judul(j)
            elif pilih == "2":
                p = input("Penulis baru: ")
                buku.set_penulis(p)
            elif pilih == "3":
                h = input("Halaman baru: ")
                if h.isdigit():
                    buku.set_halaman(h)
                else:
                    print("Halaman harus angka.")
            else:
                print("Pilihan tidak tersedia.")

    def hapus(self, no):
        if no >= 0 and no < len(self.daftar_buku):
            del self.daftar_buku[no]
            print("Data berhasil dihapus.")

def main():
    perpustakaan = Perpustakaan()
    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            while True:
                judul = input("Judul: ")
                if not judul:
                    print("Judul tidak boleh kosong")
                else:
                    break

            while True:    
                penulis = input("Penulis: ")
                if not penulis:
                    print("Penulis tidak boleh kosong")
                else:
                    break
            
            while True:
                halaman = input("Jumlah Halaman: ")
                if not halaman:
                    print("Jumlah halaman tidak boleh kosong")
                elif not halaman.isdigit():
                    print("Jumlah Halaman dalam bentuk angka")
                else:
                    break
            perpustakaan.tambah(Buku(judul, penulis, halaman))
        
        elif pilihan == "2":
            perpustakaan.tampilkan()
        
        elif pilihan == "3":
            perpustakaan.tampilkan()
            no = input("Nomor buku yang ingin diupdate: ")
            if no.isdigit():
                perpustakaan.update(int(no) - 1)
            else:
                print("Input harus angka.")
        
        elif pilihan == "4":
            perpustakaan.tampilkan()
            no = input("Nomor buku yang ingin dihapus: ")
            if no.isdigit():
                perpustakaan.hapus(int(no) - 1)
            else:
                print("Input harus angka.")
        
        elif pilihan == "5":
            break
        
        else:
            print("Menu tidak tersedia.")

main()