from abc import ABC, abstractmethod

class Manusia(ABC):
  @abstractmethod
  def berbicara(self):
    pass

  @abstractmethod
  def bekerja(self):
    pass

  @abstractmethod
  def makan(self):
    pass

class Joko(Manusia):
  def berbicara(self):
    print("Halo, saya Joko. Senang bertemu dengan Anda!")

  def bekerja(self):
    print("Joko bekerja keras menyusun laporan akhir proyek.")

  def makan(self):
    print("Joko menikmati sepiring nasi goreng hangat.")

class Beni(Manusia):
  def berbicara(self):
    print("Yo bro, apa kabar?" )

  def bekerja(self):
    print("Beni sibuk mengembangkan kode Python yang keren.")

  def makan(self):
    print("Beni memilih burger besar dengan kentang goreng.")

class Fani(Manusia):
  def berbicara(self):
    print("Selamat pagi, semoga harimu menyenangkan.")

  def bekerja(self):
    print("Fani fokus merancang presentasi yang informatif.")

  def makan(self):
    print("Fani menikmati sate ayam yang lezat.")

class Jani(Manusia):
  def berbicara(self):
    print("Ayo kita mulai petualangan baru!")

  def bekerja(self):
    print("Jani menata jadwal kegiatan dengan penuh semangat.")

  def makan(self):
    print("Jani memesan Ichiraku ramen.")

def main():
  manusia = {
    "joko": Joko(),
    "beni": Beni(),
    "fani": Fani(),
    "jani": Jani(),
  }

  print("=== Manusia & Aktivitas ===")
  while True:
    nama = input("Pilih nama Joko/Beni/Fani/Jani: ").strip().lower()
    if nama == "exit":
      print("Terima kasih. Sampai jumpa!")
      break
    if nama not in manusia:
      print(f"Maaf, '{nama}' tidak ditemukan. Harap masukkan Joko/Beni/Fani/Jani!")
      continue
    orang = manusia[nama]

    while True:
      print(f"\nPilih aktivitas yang ingin dilakukan {nama.capitalize()}")
      print("1. Berbicara")
      print("2. Bekerja")
      print("3. Makan")
      print("4. Semua aktivitas")
      print("5. Pilih nama lagi")
      print("6. Keluar")
      pilihan = input("Masukkan angka (1-6): ").strip()

      if pilihan == "1":
        orang.berbicara()
      elif pilihan == "2":
        orang.bekerja()
      elif pilihan == "3":
        orang.makan()
      elif pilihan == "4":
        orang.berbicara()
        orang.bekerja()
        orang.makan()
      elif pilihan =="5":
        break
      elif pilihan == "6":
        print("Terima kasih. sampai jumpa!")
        return
      else:
        print(f"Pilihan tidak valid! Mohon isi 1-6.")

main()