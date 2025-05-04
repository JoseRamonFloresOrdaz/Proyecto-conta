from casosdeuso.obtenersaldocuentas import ObtenerSaldoCuenta
from casosdeuso.listarcuentas import ListaCuentas
class GenerarBalance:
    def __init__(self,repoac,repo_cue,repomov):

        self.__repomov = repomov
        self.__repocue = repo_cue
        self.__lista_cuentas = ListaCuentas(self.__repocue)
        self.__repoac = repoac
        self.__plantilla = {
            "Nombre": 'BLANACE GENERAL',
            "empresa": "Empresa x",
            "periodo": "",
            "activos_circulante": [
                {"cuenta":1,"monto":0 },
                {"cuenta":2,"monto":0 },
                {"cuenta":3,"monto":0 },
                {"cuenta":4,"monto":0 },
                {"cuenta":5,"monto":0 },
                {"cuenta":6,"monto":0 },
                {"cuenta":7,"monto":0 },
                {"cuenta":8,"monto":0 },
                {"cuenta":9,"monto":0 },
                {"cuenta":10,"monto":0 },
                {"cuenta":11,"monto":0 }
            ],
            "activos_no_circulante": [
                {"cuenta":12,"monto":0 },
                {"cuenta":13,"monto":0 },
                {"cuenta":14,"monto":0 },
                {"cuenta":15,"monto":0 },
                {"cuenta":16,"monto":0 },
                {"cuenta":17,"monto":0 },
                {"cuenta":18,"monto":0 },
                {"cuenta":19,"monto":0 },
                {"cuenta":20,"monto":0 },
                {"cuenta":22,"monto":0 },
                {"cuenta":22,"monto":0 },
                {"cuenta":23,"monto":0 },
                {"cuenta":24,"monto":0 },
                {"cuenta":25,"monto":0 }   
            ],
            "pasivo_circulante": [
                {"cuenta":26,"monto":0 },
                {"cuenta":27,"monto":0 },
                {"cuenta":28,"monto":0 },
                {"cuenta":29,"monto":0 },
                {"cuenta":30,"monto":0 },
                {"cuenta":31,"monto":0 },
                {"cuenta":32,"monto":0 },
                {"cuenta":33,"monto":0 },
                {"cuenta":34,"monto":0 },
                {"cuenta":35,"monto":0 }
            ],
            "pasivo_no_circulante": [
                {"cuenta":36,"monto":0 },
                {"cuenta":37,"monto":0 },
                {"cuenta":38,"monto":0 },
                {"cuenta":39,"monto":0 },
                {"cuenta":40,"monto":0 }
            ],
            "capital_contribuido": [
                {"cuenta":41,"monto":0 },
                {"cuenta":42,"monto":0 },
                {"cuenta":43,"monto":0 },
                {"cuenta":44,"monto":0 }
            ],
            "capital_ganado": [
                {"cuenta":45,"monto":0 },
                {"cuenta":46,"monto":0 },
                {"cuenta":47,"monto":0 },
                {"cuenta":48,"monto":0 }
            ],
        }
    def execute(self,inicio,fin):
            balance = self.__plantilla.copy()
            totales = {}
            eliminar = []
            for key, value in balance.items():
                if isinstance(value, list):
                    total = 0
                    nuevos_elementos = []  # Nueva lista para guardar solo los elementos válidos
                    for element in value:
                        nombre = self.__lista_cuentas.execute('id', element['cuenta']).nombre
                        saldo = ObtenerSaldoCuenta(self.__repoac, self.__repocue, self.__repomov).execute(element['cuenta'], inicio, fin)
                        if saldo > 0:
                            nuevos_elementos.append({
                                'cuenta': nombre,
                                'monto': saldo
                            })
                        total += saldo
                    balance[key] = nuevos_elementos  # Actualizar la lista limpia
                    totales[f"total_{key}"] = total
            balance.update(totales)
            return balance






        


