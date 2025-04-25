from infrestructura.porarchivo.archivodiariorepo import repodiarios
from infrestructura.porarchivo.archivoasientorepo import repoasiento
from infrestructura.porarchivo.archivocuentarepo import repocuenta
from infrestructura.porarchivo.archivomovimientorepo import repomovimiento
from casosdeuso.generarasiento import GenerarAsiento
from casosdeuso.generarmovimiento import GenerarMovimiento
from nucleo.excepciones import ErrorAsiento,ErrorMovimiento,AdvertenciaMovimiento
from flask import jsonify,request

class ControladorAsiento:
    def __init__(self,ucm,uca):
        self.__ucm = ucm
        self.__uca = uca
    def __movimientos(self,id,movimientos):
        if movimientos:
            for m in movimientos:
                try:
                    print(m)
                    self.__ucm.execute(id,m['cuenta_id'],m['monto'],m['tipo'])
                    return jsonify({'text': 'Asiento generado exitosamente'})
                except ErrorMovimiento as e:
                    return jsonify({'error': str(e)}),400
                except AdvertenciaMovimiento as e:
                    return jsonify({'text': 'Asiento generado exitosamente','warn':str(e)})

    def manejar(self,req):
        data = request.get_json()
        print(data)
        try:
            if not 'movimientos' in data:
                raise ErrorAsiento('El asiento debe contar con por lo menos un movimiento')
            ac = self.__uca.execute(data['nombre'],data['diario_id'],data['fecha'])
            return self.__movimientos(ac.id,data['movimientos'])
        except ErrorAsiento as e:
            return jsonify({'error': str(e)}),400
        

ucm = GenerarMovimiento(repomovimiento,repoasiento,repocuenta)
uca = GenerarAsiento(repoasiento,repodiarios)
controladorasiento = ControladorAsiento(ucm,uca)
