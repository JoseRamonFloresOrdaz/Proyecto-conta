from nucleo.entidades import Asiento,TipoAsiento
from nucleo.excepciones import ErrorAsiento
from datetime import datetime

class GenerarAsiento:
    def __init__(self,acrep,drep):
        self.__rep = acrep
        self.__drep = drep

    def execute(self,nombre,tipo,diario_id,fecha):
        if len(nombre) == 0:
            raise ErrorAsiento('El nombre del asiento no puede estar vacio')
        if not self.__drep.ObtenerPorId(diario_id):
            raise ErrorAsiento(f'No existe un diario con el id {diario_id}')
        if self.__rep.ObtenerPorNombre(nombre):
            raise ErrorAsiento('Ya existe un asiento con ese nombre')
        tipo = tipo.upper()
        if not tipo in TipoAsiento.__members__:
            raise  ErrorAsiento('El tipo de cuenta no es valido')
        return self.__rep.nuevo(Asiento(None,nombre,TipoAsiento.__members__.get(tipo),diario_id,fecha))

    