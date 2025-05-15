class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo

    def get_info(self):
        return f"No Rek: {self.__no_rek}, Nama: {self.__nama}, Saldo: {self.__saldo:,}"

    def get_no_rek(self):
        return self.__no_rek

    def set_saldo(self, angka):
        if angka == 0:
            print("Jumlah tidak boleh 0.")
        elif angka > 0:
            self.__saldo += angka
            print(f"Setoran berhasil: +{angka:,}")
        elif angka < 0:
            if -angka <= self.__saldo:
                self.__saldo += angka
                print(f"Penarikan berhasil: {angka:,}")
            else:
                print("Saldo tidak cukup.")
        else:
            print("Input tidak valid.")

class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rek):
        self.rekening_list.append(rek)

    def cari_rekening(self, no_rek):
        for i in self.rekening_list:
            if i.get_no_rek() == no_rek:
                return i
        return None

    def tampilkan_rekening(self):
        print("\nData Rekening Nasabah")
        for i in self.rekening_list:
            print(i.get_info())

def main():
    bank = Bank()
    jumlah = int(input("Masukkan jumlah rekening: "))
    for i in range(jumlah):
        print(f"\nRekening ke-{i + 1}")
        while True:
            no_rek = input("No Rekening (maks 10 digit, hanya angka): ")
            if no_rek.isdigit() and len(no_rek) == 10:
                break
            else:
                print("No rekening harus berupa angka maksimal 10 digit.")

        while True:
            nama = input("Nama Pemilik (Hanya Huruf): ")
            if nama.replace(" ", "").isalpha():
                break
            else:
                print("Nama tidak boleh mengandung angka")

        while True:
            saldo_awal = input("Saldo Awal (Harus angka): ")
            if saldo_awal.isdigit() and int(saldo_awal) > 0:
                saldo = int(saldo_awal)
                break
            else:
                print("Saldo harus angka dan tidak negatif.")

        bank.tambah_rekening(RekeningBank(no_rek, nama, saldo))

    while True:
        print("\n=== Menu ===")
        print("1. Setor")
        print("2. Tarik")
        print("3. Tampilkan Semua")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            no = input("\nMasukkan No Rekening: ")
            rek = bank.cari_rekening(no)
            if rek:
                while True:
                    angka = input("Jumlah Setor: ")
                    if angka.isdigit():
                        rek.set_saldo(int(angka))
                        break
                    else:
                        print("Jumlah harus angka")
            else:
                print("Rekening tidak ditemukan.")

        elif pilihan == "2":
            no = input("\nMasukkan No Rekening: ")
            rek = bank.cari_rekening(no)
            if rek:
                while True:
                    angka = input("Jumlah Tarik: ")
                    if angka.isdigit():
                        rek.set_saldo(-int(angka))
                        break
                    else:
                        print("Jumlah harus angka")
            else:
                print("Rekening tidak ditemukan.")

        elif pilihan == "3":
            bank.tampilkan_rekening()

        elif pilihan == "4":
            print("Terima kasih banyak.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1–4.")

main()