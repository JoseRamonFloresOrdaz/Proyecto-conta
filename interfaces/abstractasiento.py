from abc import ABC,abstractmethod
from nucleo.entidades import Asiento
class AbstractAsiento(ABC):
    @abstractmethod
    def nuevo(self,a:Asiento):
        pass
    @abstractmethod
    def ObtenerPorNombre(self,nombre):
        pass
    @abstractmethod
    def ObtenerPorId(self,id):
        pass
    @abstractmethod
    def actualizar(self,a:Asiento):
        pass
    @abstractmethod
    def eliminar(self,id):
        pass
    
