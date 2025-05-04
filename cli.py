from infrestructura.porarchivo.archivoasientorepo import repoasiento
from infrestructura.porarchivo.archivocuentarepo import repocuenta
from infrestructura.porarchivo.archivomovimientorepo import repomovimiento
from casosdeuso.generarbalance import GenerarBalance

balance = GenerarBalance(repoasiento,repocuenta,repomovimiento)
print(balance.execute("2025-04-20","2025-05-30"))