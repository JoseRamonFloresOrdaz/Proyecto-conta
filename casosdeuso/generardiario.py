from nucleo.entidades import Diario
from nucleo.excepciones import ErrorDiario

class GenerarDiario:
    def __init__(self,rep):
        self.__rep = rep

    def execute(self,nombre):
        if not isinstance(nombre,str):
            raise ErrorDiario('EL nombre del diario debe de ser una cadena')
        if len(nombre) == 0:
            raise ErrorDiario('El nombre del diario no puede estar vacio')
        if self.__rep.ObtenerPorNombre(nombre):
            raise ErrorDiario('Ya existe un diario con ese nombre')
        
        return self.__rep.nuevo(Diario(None,nombre))
        
