from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
  def __init__(self):
    self.energi_tersisa = 100

  @abstractmethod
  def nyalakan(self):
    pass

  @abstractmethod
  def matikan(self):
    pass

  @abstractmethod
  def gunakan(self, jam: int):
    pass

  def status(self):
    print(f"Tipe perangkat: {self.__class__.__name__}")
    print(f"Energi tersisa: {self.energi_tersisa}%")

class Laptop(PerangkatElektronik):
  def nyalakan(self):
    print("Laptop dinyalakan.")

  def matikan(self):
    print("Laptop dimatikan.")

  def gunakan(self, jam: int):
    self.energi_tersisa -= 10 * jam
    if self.energi_tersisa <= 0:
      self.energi_tersisa = 0
      print("Baterai habis.")
    else:
      print(f"Laptop digunakan selama {jam} jam.")

class Kulkas(PerangkatElektronik):
  def nyalakan(self):
    print("Kulkas menyala.")

  def matikan(self):
    print("Kulkas dimatikan.")

  def gunakan(self, jam: int):
    self.energi_tersisa -= 5 * jam
    if self.energi_tersisa <= 0:
      self.energi_tersisa = 0
    print(f"Kulkas digunakan selama {jam} jam.")
    if self.energi_tersisa <= 20:
      print("Energi rendah, kulkas butuh daya tambahan!")

def main():
    print("=== Laptop ===")
    laptop = Laptop()
    laptop.nyalakan()
    while True:
      jam_laptop = int(input("Masukkan durasi penggunaan laptop (jam): "))
      if jam_laptop < 0:
        print("Masukkan nilai jangan minus")
      else:
        laptop.gunakan(jam_laptop)
        laptop.status()
        laptop.matikan()
        break

    print("\n=== Kulkas ===")
    kulkas = Kulkas()
    kulkas.nyalakan()
    while True:
      jam_kulkas = int(input("Masukkan durasi penggunaan kulkas (jam): "))
      if jam_kulkas < 0:
        print("Masukkan nilai jangan minus")
      else:
        kulkas.gunakan(jam_kulkas)
        kulkas.status()
        kulkas.matikan()
        break

main()