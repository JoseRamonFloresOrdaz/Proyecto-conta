from nucleo.entidades import Movimiento,TipoMovimiento
from casosdeuso.validarpartidadoble import ValidarPartidaDoble
from nucleo.excepciones import ErrorMovimiento,AdvertenciaMovimiento

class GenerarMovimiento:
    def __init__(self,repomov,repoasc,repocu):
        self.__repomov = repomov
        self.__repoac = repoasc
        self.__repocu = repocu

    def execute(self,asiento_id,cuenta_id,monto,tipo):
        if not self.__repoac.ObtenerPorId(asiento_id):
            raise ErrorMovimiento(f'El asiento con el id {asiento_id} no existe')
        if not self.__repocu.ObtenerPorId(cuenta_id):
            raise ErrorMovimiento(f'La cuenta  con el id {cuenta_id} no existe')
        monto = float(monto)
        if monto < 1:
            raise ErrorMovimiento('El monto de la cuenta no puede ser cero ni negativo')
        tipo = tipo.upper()    
        if not tipo in TipoMovimiento.__members__:
            raise ErrorMovimiento('El tipo de movimiento no es valido')
            
        self.__repomov.nuevo(Movimiento(None,asiento_id,cuenta_id,monto,TipoMovimiento.__members__.get(tipo)))

        if not ValidarPartidaDoble(self.__repomov).execute(asiento_id):
            raise AdvertenciaMovimiento('El asiento no cumple con las reglas de la partida doble')
        
    