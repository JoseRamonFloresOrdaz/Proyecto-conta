from infrestructura.porarchivo.archivoasientorepo import repoasiento
from infrestructura.porarchivo.archivocuentarepo import repocuenta
from infrestructura.porarchivo.archivomovimientorepo import repomovimiento
from casosdeuso.estadosdemayor import ObtenerSaldoCuenta

cuenta = ObtenerSaldoCuenta(repoasiento,repocuenta,repomovimiento)
print(cuenta.execute(1,"2025-04-20","2025-04-30"))