from infrestructura.porarchivo.archivoasientorepo import repoasiento
from infrestructura.porarchivo.archivocuentarepo import repocuenta
from infrestructura.porarchivo.archivomovimientorepo import repomovimiento
from casosdeuso.generarmovimiento import GenerarMovimiento
from nucleo.excepciones import ErrorMovimiento,AdvertenciaMovimiento
from flask import jsonify

class ControladorMovimiento:
    def __init__(self,ucm):
        self.__ucm = ucm 

    def manejar(self,req):
        data = req.get_json()
        try:
            self.__ucm.execute(data['asiento_id'],data['cuenta_id'],data['monto'],data['tipo'])
            return jsonify({'text':'Movimiento generado exitosamente'})
        except ErrorMovimiento as e:
            return jsonify({'error': str(e)})
        except AdvertenciaMovimiento as e:
            return jsonify({'text':'Movimiento generado exitosamente','warn':str(e)})
        
ucm = GenerarMovimiento(repomovimiento,repoasiento,repocuenta)

controladormovimiento = ControladorMovimiento(ucm)