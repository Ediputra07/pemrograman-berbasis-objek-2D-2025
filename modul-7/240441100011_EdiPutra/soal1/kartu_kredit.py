from interface import MetodePembayaran

class KartuKredit(MetodePembayaran):
  def __init__(self):
    self.__biaya = 2000

  def get_biaya(self):
    return self.__biaya

  def set_biaya(self, bayar):
    if bayar >= 100000:
      self.__biaya = 5000

  def proses_pembayaran(self, jumlah):
    self.set_biaya(jumlah)
    total = jumlah + self.__biaya
    print(f"Pembayaran kartu kredit: {jumlah:,} + {self.__biaya:,} = Rp{total:,}")