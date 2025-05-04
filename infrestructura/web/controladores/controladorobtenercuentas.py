from infrestructura.porarchivo.archivocuentarepo import repocuenta
from casosdeuso.listarcuentas import ListaCuentas
from flask import jsonify
class ObtenerCuentas:
    def __init__(self,ucc):
        self.__ucc = ucc

    def manejar(self,req):
        cuentas = []
        for d in self.__ucc.execute('todas'):
            cuentas.append({'id':d.id,'nombre':d.nombre,'tipo':d.tipo.value})

        return jsonify(cuentas),200
    

ucc = ListaCuentas(repocuenta)
controladorobtenercuenta = ObtenerCuentas(ucc)
               
               


            
