from casosdeuso.generardiario import GenerarDiario
from infrestructura.porarchivo.archivodiariorepo import repodiarios
from nucleo.excepciones import ErrorDiario
from flask import jsonify,request
class ControladorCrearDiario:
    def __init__(self,uc):
        self.__uc = uc

    def manejar(self,req):
        if req:
            nombre = req.get_json()['nombre']
            try:
                self.__uc.execute(nombre)
                return jsonify({'text':'Diario generado correctamente'}),200
            except ErrorDiario as e:
                return jsonify({'error':str(e)}),400

uc = GenerarDiario(repodiarios)

controladorDiario = ControladorCrearDiario(uc)