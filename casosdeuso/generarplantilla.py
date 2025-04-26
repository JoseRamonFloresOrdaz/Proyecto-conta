from casosdeuso.generarcuenta import GenerarCuenta
class GenerarPlantilla:
    def __init__(self,rep,repo_cuentas):
        self.__repo = rep
        self.__uc_cuentas  = GenerarCuenta(repo_cuentas)

    def execute(self,data):
        for cuenta in data['cuentas']:
            self.__uc_cuentas.execute(cuenta.nombre,cuenta.tipo)
        self.__repo.guardar(data)


