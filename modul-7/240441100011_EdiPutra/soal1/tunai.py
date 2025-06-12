from interface import MetodePembayaran

class Tunai(MetodePembayaran):
  def __init__(self):
    self.__diskon = 0

  def get_diskon(self):
    return self.__diskon * 100

  def set_diskon(self, bayar):
    if bayar >= 100000:
      self.__diskon = 0.1
    elif bayar >= 10000:
      self.__diskon = 0.05

  def proses_pembayaran(self, jumlah):
    self.set_diskon(jumlah)
    diskon = jumlah * self.__diskon
    total = jumlah - diskon
    print(f"Pembayaran tunai: {jumlah:,} - {diskon:,g} = Rp{total:,g}")