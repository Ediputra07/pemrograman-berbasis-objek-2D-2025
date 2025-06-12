from abc import ABC, abstractmethod

class Kendaraan(ABC):
  @abstractmethod
  def proses_booking(self, usia):
    pass