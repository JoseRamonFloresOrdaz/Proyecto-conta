from infrestructura.porarchivo.archivodiariorepo import repodiarios
from casosdeuso.listardiarios import ListaDiarios
from flask import jsonify
class ControladorListaDiarios:
    def __init__(self,ucc):
        self.__ucc = ucc

    def manejar(self,req):
        diarios = []
        if 'id' in req.args:
            d = self.__ucc.execute('id',req.args.get('id'))
            if d != None:
                return jsonify({'id':d.id,'nombre':d.nombre}),200
            else:
                return jsonify({'error':'diario no encontrado'}),404
            
        else:
            lista_diarios = self.__ucc.execute('todas')
            for d in lista_diarios:
                diarios.append({'id':d.id,'nombre':d.nombre})
            return jsonify(diarios),200
    
uc = ListaDiarios(repodiarios)
controladorlistardiarios = ControladorListaDiarios(uc)