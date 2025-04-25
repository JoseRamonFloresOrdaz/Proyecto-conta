from infrestructura.porarchivo.archivodiariorepo import repodiarios
from casosdeuso.listardiarios import ListaDiarios
from flask import jsonify
class ControladorListaDiarios:
    def __init__(self,ucc):
        self.__ucc = ucc

    def manejar(self,req):
        diarios = []
        for d in self.__ucc.execute('todas'):
            print(d)
            diarios.append({'id':d.id,'nombre':d.nombre})

        return jsonify(diarios),200
    
uc = ListaDiarios(repodiarios)
controladorlistardiarios = ControladorListaDiarios(uc)