from nucleo.entidades import TipoMovimiento,NaturalezaCuenta
from nucleo.excepciones import ErrorCuenta
from datetime import datetime
class ObtenerSaldoCuenta:
    def __init__(self,repac,repcu,repmov):
        self.__repac = repac
        self.__repocu = repcu
        self.__repomov = repmov
    def execute(self,cuenta_id,fecha_inicio,fecha_fin):
        debe = 0
        haber = 0
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        for asiento in self.__repac.obtenerPorRangoDeFecha(fecha_inicio,fecha_fin):
            for movimiento in self.__repomov.obtenerPorAsiento(asiento.id):
                if movimiento.cuenta_id == cuenta_id:
                    print(movimiento.cuenta_id)
                    print(cuenta_id)
                    if movimiento.tipo == TipoMovimiento.DEBE:
                        debe += movimiento.monto
                    else:
                        haber += movimiento.monto
        cuenta = self.__repocu.ObtenerPorId(cuenta_id)
        print(debe)
        print(haber)
        if cuenta.tipo == NaturalezaCuenta.DEUDORA and not debe > haber:
            raise ErrorCuenta('Error al obtener saldo de la cuenta ')
        else:
            saldo = debe - haber
        if cuenta.tipo == NaturalezaCuenta.ACREDORA and not haber > debe:
            raise ErrorCuenta('Error al obtener saldo de la cuenta ')
        else:
            saldo = haber - debe
        return saldo
        