class ErrorDiario(Exception):
    def __init__(self,msj='Error al crear diario'):
        super().__init__(msj)

class ErrorAsiento(Exception):
    def __init__(self,msj='Error al crear asiento'):
        super().__init__(msj)

class ErrorCuenta(Exception):
    def __init__(self,msj='Error al crear cuenta'):
        super().__init__(msj)

class ErrorMovimiento(Exception):
    def __init__(self,msj='Error al crear movimiento'):
        super().__init__(msj)

class AdvertenciaMovimiento(Exception):
    def __init__(self,msj='Existe un problema con el movimiento'):
        super().__init__(msj)