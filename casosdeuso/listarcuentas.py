class ListaCuentas:
    def __init__(self,rep):
        self.__rep = rep
    
    def execute(self,filtro=None,value=None):
            filtros = ['id','nombre','tipo','todas']
            match filtro := filtros:
                case 'id':
                    return self.__rep.ObtenerPorId(value)
                case 'nombre':
                    return self.__rep.ObtenerPorNombre(value)
                case 'tipo':
                    return self.__rep.ObtenerPorTipo(value)
                case _: 
                      return self.__rep.ObtenerCuentas()


