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
        saldo = 0
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        for asiento in self.__repac.obtenerPorRangoDeFecha(fecha_inicio,fecha_fin):
            for movimiento in self.__repomov.obtenerPorAsiento(asiento.id):
                if movimiento.cuenta_id == cuenta_id:
                    if movimiento.tipo == TipoMovimiento.DEBE:
                        debe += movimiento.monto
                    else:
                        haber += movimiento.monto
        cuenta = self.__repocu.ObtenerPorId(cuenta_id)
        if (debe > 0 or haber > 0):
            if cuenta.tipo == NaturalezaCuenta.DEUDORA:
                if haber > debe:
                    raise ErrorCuenta(f'Error al obtener saldo de la cuenta {cuenta.nombre}, revisa los asientos del periodo')
                saldo = debe - haber
            elif cuenta.tipo == NaturalezaCuenta.ACREDORA:
                if debe > haber:
                    raise ErrorCuenta(f'Error al obtener saldo de la cuenta {cuenta.nombre}, revisa los asientos del periodo')
                saldo = haber - debe
        return saldo
        