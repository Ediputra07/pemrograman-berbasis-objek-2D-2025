from abc import ABC, abstractmethod

class Peminjaman(ABC):
  @abstractmethod
  def pinjam(self, nama, durasi):
    pass