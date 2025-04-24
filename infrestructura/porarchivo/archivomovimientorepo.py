from infrestructura.porarchivo.archivo import Archivo
from interfaces.abstractmovimiento import AbstractMovimiento
from nucleo.entidades import Movimiento,TipoMovimiento


class ArchivoMovimientoRepo(Archivo,AbstractMovimiento):
    def __init__(self,ruta):
        super().__init__(ruta)

    def __obtenerSiguienteId(self):
        datos = self.leer()
        return int(datos[len(datos)-1].split(',')[0])+1 if datos else 1
    
    def nuevo(self,m:Movimiento):
        id = self.__obtenerSiguienteId()
        linea = f"{id},{m.asiento_id},{m.cuenta_id},{m.monto},{m.tipo.value}\n"
        self.guardar(linea)
        m.id = id
        return m
    
    def obtenerPorAsiento(self,aid):
        movimientos = []
        datos = self.leer()
        if datos:
            for d in datos:
                id,asiento_id,cuenta_id,monto,tipo = d[:d.find('\n')].split(',')
                if int(asiento_id) == aid:
                    movimientos.append(Movimiento(id,asiento_id,cuenta_id,float(monto),TipoMovimiento.__members__.get(tipo.upper())))
        return movimientos

    def obtenerPorId(self,id):
        datos = self.leer()
        if datos:
            for d in datos:
                id_c,asiento_id,cuenta_id,monto,tipo = d[:d.find('\n')].split(',')
                if id == int(id_c):
                    return Movimiento(id,asiento_id,cuenta_id,float(monto),TipoMovimiento.__members__.get(tipo))
                
                
    def obtenerPorCuenta(self,cid):
        movimientos = []
        datos = self.leer()
        if datos:
            for d in datos:
                id,asiento_id,cuenta_id,monto,tipo = d[:d.find('\n')].split(',')
                if int(cuenta_id) == cid:
                    movimientos.append(Movimiento(id,asiento_id,cuenta_id,float(monto),TipoMovimiento.__members__.get(tipo)))
        return movimientos

    def obtenerPorTipo(self, tipo):
        pass

    def actualizar(self,m:Movimiento):
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



repomovimiento = ArchivoMovimientoRepo('infrestructura/porarchivo/src/movimientos.csv')