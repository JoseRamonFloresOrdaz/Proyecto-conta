from interfaces.abstractdiario import AbstractDiario
from infrestructura.porarchivo.archivo import Archivo
from nucleo.entidades import Diario

class ArchivoDiarioRepo(AbstractDiario,Archivo):
    def __init__(self,ruta):
        super().__init__(ruta)

    def __obtenerSiguienteId(self):
        datos = self.leer()
        return int(datos[len(datos)-1].split(',')[0])+1 if datos else 1
    
    def nuevo(self,d:Diario):
        id = self.__obtenerSiguienteId()
        linea = f"{id},{d.nombre}\n"
        self.guardar(linea)
        d.id = id
        return d
    
    def ObtenerPorNombre(self,nombre):
        datos = self.leer()
        if datos:
            for d in datos:
                id,nom = d[:d.find('\n')].split(',')
                if nombre == nom:
                    return Diario(int(id),nom)
                
    def ObtenerDiarios(self):
        diarios = []
        datos = self.leer()
        if datos:
            for d in datos:
                id,nom = d[:d.find('\n')].split(',')
                diarios.append(Diario(int(id),nom))
        return diarios


    def ObtenerPorId(self,id):
        datos = self.leer()
        if datos:
            for d in datos:
                id_c,nom = d[:d.find('\n')].split(',')
                if id == int(id_c):
                    return Diario(int(id),nom)
                

    def actualizar(self,d:Diario):
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
    

repodiarios = ArchivoDiarioRepo('infrestructura/porarchivo/src/diarios.csv')