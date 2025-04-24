from interfaces.absctractcuenta import AbstractCuenta
from infrestructura.porarchivo.archivo import Archivo
from nucleo.entidades import Cuenta,NaturalezaCuenta


class ArchivoCuentaRepo(AbstractCuenta,Archivo):
    def __init__(self,ruta):
        super().__init__(ruta)
    def __obtenerSiguienteId(self):
        datos = self.leer()
        return int(datos[len(datos)-1].split(',')[0])+1 if datos else 1

    def nuevo(self,c:Cuenta):
        id = self.__obtenerSiguienteId()
        linea = f"{id},{c.nombre},{c.tipo.value[0]}\n"
        self.guardar(linea)
        c.id = id
        return c
    
    def ObtenerCuentas(self):
        datos = self.leer()
        cuentas = []
        if datos:
            for d in datos:
                id,nom,tip = d[:d.find('\n')].split(',')
                cuentas.append(Cuenta(int(id),nom,NaturalezaCuenta.__members__.get(tip.upper())))

        return cuentas
        
    def ObtenerPorId(self,id):
        datos = self.leer()
        if datos:
            for d in datos:
                id_c,nom,tipo = d[:d.find('\n')].split(',')
                if id == int(id_c):
                    return Cuenta(int(id),nom,NaturalezaCuenta.__members__.get(tipo.upper()))
    def ObtenerPorNombre(self,nombre):
        datos = self.leer()
        if datos:
            for d in datos:
                id,nom,tipo = d[:d.find('\n')].split(',')
                if nombre == nom:
                    return Cuenta(int(id),nom,NaturalezaCuenta.__members__.get(tipo.upper()))
        
    def ObtenerPorTipo(self,tipo):
        datos = self.leer()
        cuentas = []
        if datos:
            for d in datos:
                id,nom,tip = d[:d.find('\n')].split(',')
                if tip == NaturalezaCuenta.__members__.get(tipo):
                    cuentas.append(Cuenta(int(id),nom,NaturalezaCuenta.__members__.get(tip.upper())))
        return cuentas
    def actualizar(self,c:Cuenta):
        
        pass
    def eliminar(self,id):
        pass
    


repocuenta = ArchivoCuentaRepo('infrestructura/porarchivo/src/cuentas.csv')