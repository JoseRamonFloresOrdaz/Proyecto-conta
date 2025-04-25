class ListaDiarios:
    def __init__(self,rep):
        self.__rep = rep
    
    def execute(self,filtro=None,value=None):
            filtros = ['id','nombre','todas']
            match filtro := filtros:
                case 'id':
                    return self.__rep.ObtenerPorId(value)
                case 'nombre':
                    return self.__rep.ObtenerPorNombre(value)
                case _: 
                      return self.__rep.ObtenerDiarios()


