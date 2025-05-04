from dataclasses import dataclass
from enum import Enum
@dataclass
class Diario:
    id: int
    nombre: str

class TipoAsiento(Enum):
    INGRESO = 'Ingreso'
    DIARIO = 'Diario'
    EGRESO = 'Egreso'

@dataclass
class Asiento:
    id: int
    nombre: str
    tipo: TipoAsiento
    diario_id : int
    fecha: str

class NaturalezaCuenta(Enum):
    ACREDORA = 'Acredora'
    DEUDORA = 'Deudora'
    
@dataclass
class Cuenta:
    id: int
    nombre: str
    tipo: NaturalezaCuenta

class TipoMovimiento(Enum):
    DEBE = 'Debe'
    HABER = 'Haber'

@dataclass
class  Movimiento:
    id: int
    asiento_id: int
    cuenta_id: int
    monto: float
    tipo: TipoMovimiento