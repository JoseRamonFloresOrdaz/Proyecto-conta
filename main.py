from infrestructura.archivodiariorepo import repodiarios
from casosdeuso.generarDiario import GenerarDiario


uc = GenerarDiario(repodiarios)
uc.execute('Diario 2')