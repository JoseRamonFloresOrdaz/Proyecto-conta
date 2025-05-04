from casosdeuso.generarbalance import GenerarBalance
from flask import jsonify
class controladorGenerarBalance:
    def __init__(self,uc):
        self.__uc = uc
    def manejar(self):
        inicio = req.args.get

        self.__uc.execute(inicio,fin)
        return jsonify({})
        