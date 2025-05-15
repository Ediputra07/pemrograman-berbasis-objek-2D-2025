class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_info(self):
        return f"Nama: {self.__nama}, Umur: {self.__umur}, Keluhan: {self.__keluhan}"

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def set_umur(self, umur_baru):
        self.__umur = umur_baru

    def set_keluhan(self, keluhan_baru):
        self.__keluhan = keluhan_baru

class Klinik:
    def __init__(self):
        self.pasien_list = []

    def tambah(self, pasien):
        self.pasien_list.append(pasien)

    def tampilkan(self):
        print("\nDaftar Pasien:")
        if not self.pasien_list:
            print("Belum ada data.")
        for i in range(len(self.pasien_list)):
            print(f"{i+1}. {self.pasien_list[i].get_info()}")

    def update(self, no):
        if no >= 0 and no < len(self.pasien_list):
            pasien = self.pasien_list[no]
            print("1. Nama")
            print("2. Umur")
            print("3. Keluhan")
            pilih = input("Pilih bagian yang ingin diubah: ")
            if pilih == "1":
                n = input("Nama baru: ")
                pasien.set_nama(n)

            elif pilih == "2":
                u = input("Umur baru: ")
                if u.isdigit():
                    pasien.set_umur(int(u))
                else:
                    print("Umur harus angka.")
            elif pilih == "3":
                k = input("Keluhan baru: ")
                pasien.set_keluhan(k)
            else:
                print("Pilihan tidak tersedia.")

    def hapus(self, no):
        if no >= 0 and no < len(self.pasien_list):
            del self.pasien_list[no]
            print("Data berhasil dihapus.")

def main():
    klinik = Klinik()
    while True:
        print("\n=== Menu Klinik ===")
        print("\n1. Tambah Pasien")
        print("2. Tampilkan Pasien")
        print("3. Update Pasien")
        print("4. Hapus Pasien")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            while True:
                nama = input("Nama: ")
                if not nama:
                    print("Nama tidak boleh kosong")
                elif nama.isdigit():
                    print("Nama tidak boleh mengandung angka")
                else:
                    break

            while True:    
                umur = input("Umur: ")
                if not umur:
                    print("Umur tidak boleh kosong")
                elif not umur.isdigit():
                    print("Umur harus angka")
                else:
                    break
            
            while True:
                keluhan = input("Keluhan: ")
                if not keluhan:
                    print("Keluhan tidak boleh kosong")
                elif keluhan.isdigit():
                    print("Keluhan tidak boleh mengandung angka")
                else:
                    break
            
            klinik.tambah(Pasien(nama, int(umur), keluhan))

        elif pilihan == "2":
            klinik.tampilkan()
        
        elif pilihan == "3":
            klinik.tampilkan()
            no = input("Nomor pasien yang ingin diupdate: ")
            if no.isdigit():
                klinik.update(int(no) - 1)
            else:
                print("Input harus angka.")
        
        elif pilihan == "4":
            klinik.tampilkan()
            no = input("Nomor pasien yang ingin dihapus: ")
            if no.isdigit():
                klinik.hapus(int(no) - 1)
            else:
                print("Input harus angka.")
        
        elif pilihan == "5":
            break
        
        else:
            print("Menu tidak tersedia.")

main()