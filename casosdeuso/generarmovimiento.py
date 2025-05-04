from nucleo.entidades import Movimiento,TipoMovimiento
from casosdeuso.validarpartidadoble import ValidarPartidaDoble
from nucleo.excepciones import ErrorMovimiento,AdvertenciaMovimiento

class GenerarMovimiento:
    def __init__(self,repomov,repoasc,repocu):
        self.__repomov = repomov
        self.__repoac = repoasc
        self.__repocu = repocu

    def execute(self,asiento_id,nom_cuenta,monto,tipo):
        if not self.__repoac.ObtenerPorId(asiento_id):
            raise ErrorMovimiento(f'El asiento con el id {asiento_id} no existe')
        cuenta = self.__repocu.ObtenerPorNombre(nom_cuenta)
        if not cuenta:
            raise ErrorMovimiento(f'La cuenta {cuenta} no existe')
        monto = float(monto)
        if monto < 1:
            raise ErrorMovimiento('El monto de la cuenta no puede ser cero ni negativo')
        tipo = tipo.upper()    
        if not tipo in TipoMovimiento.__members__:
            raise ErrorMovimiento('El tipo de movimiento no es valido')
            
        self.__repomov.nuevo(Movimiento(None,asiento_id,cuenta.id,monto,TipoMovimiento.__members__.get(tipo)))

    