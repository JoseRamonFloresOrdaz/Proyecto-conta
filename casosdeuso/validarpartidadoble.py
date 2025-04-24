from nucleo.entidades import TipoMovimiento
class ValidarPartidaDoble:
    def __init__(self,repo):
        self.__repo = repo

    def execute(self,asiento_id):
        debe = 0
        haber = 0
        movimientos = self.__repo.obtenerPorAsiento(asiento_id)
        for m in movimientos:
            if m.tipo == TipoMovimiento.DEBE:
                debe += m.monto
            else:
                haber += m.monto
        return True if debe == haber else False

        
