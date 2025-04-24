from nucleo.entidades import Cuenta
from abc import ABC,abstractmethod

class AbstractCuenta(ABC):
    @abstractmethod
    def nuevo(self,c:Cuenta):
        pass
    @abstractmethod
    def ObtenerPorId(self,id):
        pass
    @abstractmethod
    def ObtenerPorNombre(self,nombre):
        pass
    def ObtenerPorTipo(self,tipo):
        pass
    @abstractmethod
    def actualizar(self,c:Cuenta):
        pass
    @abstractmethod
    def eliminar(self,id):
        pass
    
