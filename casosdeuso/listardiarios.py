class ListaDiarios:
    def __init__(self,rep):
        self.__rep = rep
    
    def execute(self,filtro=None,value=None):
            match filtro:
                case 'id':
                    print("por id")
                    return self.__rep.ObtenerPorId(int(value))
                case 'nombre':
                    return self.__rep.ObtenerPorNombre(value)
                case _: 
                      return self.__rep.ObtenerDiarios()


