from infrestructura.porarchivo.archivo import Archivo
from interfaces.abstractasiento import AbstractAsiento
from nucleo.entidades import Asiento


class ArchivoAsientoRepo(Archivo,AbstractAsiento):
    def __init__(self,ruta):
        super().__init__(ruta)

    def __obtenerSiguienteId(self):
        datos = self.leer()
        return int(datos[len(datos)-1].split(',')[0])+1 if datos else 1
    
    def nuevo(self,a:Asiento):
        id = self.__obtenerSiguienteId()
        linea = f"{id},{a.nombre},{a.diario_id},{a.fecha}\n"
        self.guardar(linea)
        a.id = id
        return a
    
    def ObtenerPorNombre(self,nombre):
        datos = self.leer()
        if datos:
            for d in datos:
                id,nom,diario_id,fecha = d[:d.find('\n')].split(',')
                if nombre == nom:
                    return Asiento(int(id),nom,diario_id,fecha)
                
    def ObtenerAsientos(self):
        datos = self.leer()
        asientos = []
        if datos:
            for d in datos:
                id,nom,diario_id,fecha = d[:d.find('\n')].split(',')
                asientos.append(Asiento(int(id),nom,diario_id,fecha))
        return asientos
                
    def ObtenerPorId(self,id):
        datos = self.leer()
        if datos:
            for d in datos:
                id_c,nom,diario_id,fecha = d[:d.find('\n')].split(',')
                if id == int(id_c):
                    return Asiento(int(id_c),nom,diario_id,fecha)
                
    def obtenerPorDiario(self,id):
        datos = self.leer()
        asientos = []
        if datos:
            for d in datos:
                id_c,nom,diario_id,fecha = d[:d.find('\n')].split(',')
                if id == int(diario_id):
                    asientos.append(Asiento(int(id_c),nom,diario_id,fecha))
        return asientos
    
    def obtenerPorFecha(self,fec):
        datos = self.leer()
        if datos:
            for d in datos:
                id_c,nom,diario_id,fecha = d[:d.find('\n')].split(',')
                if fecha == fec:
                    return Asiento(int(id_c),nom,diario_id,fecha)

    def actualizar(self,a:Asiento):
        pass


    def eliminar(self,id):
        datos = self.leer()
        if datos:
            for d in datos:
                id_c,nom = d[:d.find('\n')].split(',')
                if id == int(id_c):
                    datos.remove(d)

        self.generar_archivo()
        for d in datos:
            self.guardar(d)



repoasiento = ArchivoAsientoRepo('infrestructura/porarchivo/src/asientos.csv')