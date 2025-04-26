class GenerarPlantilla:
    def __init__(self,rep,repo_cue,repomov,repoac):
        self.__repo = rep
        self.__repomov = repomov
        self.__repocue = repo_cue
        self.__repoac = repoac

    def execute(self,data):
        for cuenta in data['cuentas']:
            self.__uc_cuentas.execute(cuenta['nombre'],cuenta['tipo'])
        self.__repo.guardar(data)


