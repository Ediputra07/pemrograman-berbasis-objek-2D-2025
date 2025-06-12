from abc import ABC, abstractmethod

class Reservasi(ABC):
  @abstractmethod
  def reservasi(self, nama, hari):
    pass