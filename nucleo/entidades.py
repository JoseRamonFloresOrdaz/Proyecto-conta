from dataclasses import dataclass
@dataclass
class Diario:
    id: int
    nombre: str

@dataclass
class Asiento:
    id: int
    nombre: str
    fecha: str

@dataclass
class Cuenta:
    id: int
    nombre: str
    tipo: str

@dataclass
class  Movimiento:
    id: int
    asiento_id: int
    cuenta_id: int
    monto: float
    tipo: str