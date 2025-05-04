class Archivo:
    def __init__(self,ruta):
        self.ruta = ruta

    def generar_archivo(self):
        archivo = open(self.ruta,'w')
        archivo.close()

    def leer(self):
        datos = []
        try:
            with open(self.ruta,'r') as f:
                datos = f.readlines()
        except FileNotFoundError:
            self.generar_archivo()
        return datos
        
    def guardar(self,linea):
        with open(self.ruta,'a+') as archivo:
            archivo.write(linea)

    def guardar_lista(self,lista):
        with open(self.ruta,'w') as f:
            f.writelines(lista)

