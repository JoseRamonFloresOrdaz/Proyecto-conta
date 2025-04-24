from nucleo.entidades import Cuenta,NaturalezaCuenta
from nucleo.excepciones import ErrorCuenta

class GenerarCuenta:
    def __init__(self,repo):
        self.__repo = repo

    def execute(self,nombre,tipo):
        if not isinstance(nombre,str):
            raise ErrorCuenta('El nombre de la cuenta debe de ser una cadena')
        if len(nombre) == 0:
            raise ErrorCuenta('El nombre de la cuenta no puede estar vacio')
        if self.__repo.ObtenerPorNombre(nombre):
            raise ErrorCuenta('Ya existe una cuenta con ese nombre')
        tipo = tipo.upper()
        if not tipo in NaturalezaCuenta.__members__:
            raise ErrorCuenta('El tipo de cuenta no es valido')
 
        return self.__repo.nuevo(Cuenta(None,nombre,NaturalezaCuenta.__members__.get(tipo)))