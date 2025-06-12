from interface import MetodePembayaran

class DompetDigital(MetodePembayaran):
  def __init__(self):
    self.__potongan = 2000

  def get_potongan(self):
    return self.__potongan

  def set_potongan(self, bayar):
    if bayar >= 100000:
      self.__potongan = 5000
    elif bayar >= 50000:
      self.__potongan = 3000

  def proses_pembayaran(self, jumlah):
    self.set_potongan(jumlah)
    total = jumlah - self.__potongan
    print(f"Pembayaran dompet digital: {jumlah:,} - {self.__potongan:,} = Rp{total:,}")
