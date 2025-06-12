from abc import ABC, abstractmethod

class MetodePembayaran(ABC):
  @abstractmethod
  def proses_pembayaran(self, jumlah):
    pass