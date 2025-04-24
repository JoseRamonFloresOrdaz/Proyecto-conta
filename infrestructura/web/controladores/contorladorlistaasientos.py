from infrestructura.porarchivo.archivoasientorepo import repoasiento
from infrestructura.porarchivo.archivocuentarepo import repocuenta
from infrestructura.porarchivo.archivomovimientorepo import repomovimiento
from casosdeuso.listarasientos import ListarAsientos
from casosdeuso.listarcuentas import ListaCuentas
from flask import jsonify

class ControladorListarAsientos:
    def __init__(self,uca,ucc):
        self.__uca = uca
        self.__ucc = ucc

    def manejar(self,req):
        acs =[]
        asientos,lista_movimientos = self.__uca.execute()
        for pos in range(len(asientos)):
            ac = {'id':asientos[pos].id,'nombre':asientos[pos].nombre,'fecha':asientos[pos].fecha}
            print(ac)
            l = []
            for movimiento in lista_movimientos[pos]:
                cuenta = self.__ucc.execute('id',movimiento.cuenta_id)[0]
                l.append({'asiento_id':movimiento.asiento_id,'cuenta':{'id':cuenta.id,'nombre':cuenta.nombre},'monto':movimiento.monto,'tipo':movimiento.tipo.value})
            ac['movimientos'] = l
            acs.append(ac)
        return jsonify(acs),200

            

uca = ListarAsientos(repoasiento,repomovimiento)
ucc = ListaCuentas(repocuenta)

controladorlistarasientos = ControladorListarAsientos(uca,ucc)