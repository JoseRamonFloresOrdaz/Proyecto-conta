from nucleo.entidades import Diario
from abc import ABC,abstractmethod

class AbstractDiario(ABC):
    @abstractmethod
    def nuevo(self,d:Diario):
        pass
    @abstractmethod
    def ObtenerPorNombre(self,nombre):
        pass
    @abstractmethod
    def ObtenerPorId(self,id):
        pass
    @abstractmethod
    def actualizar(self,d:Diario):
        pass
    @abstractmethod
    def eliminar(self,id):
        pass
    
