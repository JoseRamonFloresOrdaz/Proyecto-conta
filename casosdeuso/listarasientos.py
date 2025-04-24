class ListarAsientos:
    def __init__(self,repoac,repomov):
        self.__repoac = repoac
        self.__repomov = repomov

    def execute(self):
        asientos = []
        listaMovimientos = []
        for asiento in self.__repoac.ObtenerAsientos():
            asientos.append(asiento)
            movimientos = []
            for movimiento in self.__repomov.obtenerPorAsiento(asiento.id):
                movimientos.append(movimiento)
            listaMovimientos.append(movimientos)

        return asientos,listaMovimientos

            

        