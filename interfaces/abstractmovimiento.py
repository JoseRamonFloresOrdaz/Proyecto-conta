from abc import ABC,abstractmethod
from nucleo.entidades import Movimiento
class AbstractMovimiento(ABC):
    @abstractmethod
    def nuevo(self,m:Movimiento):
        pass
    @abstractmethod
    def obtenerPorAsiento(self,aid):
        pass
    @abstractmethod
    def obtenerPorId(self,id):
        pass
    @abstractmethod
    def obtenerPorCuenta(self,cid):
        pass
    @abstractmethod
    def obtenerPorTipo(self,tipo):
        pass
    @abstractmethod
    def actualizar(self,m:Movimiento):
        pass
    @abstractmethod
    def eliminar(self,id):
        pass
    
