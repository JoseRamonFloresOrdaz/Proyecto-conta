from infrestructura.web.controladores.controladorcreardiario import controladorDiario
from infrestructura.web.controladores.controladorcrearasiento import controladorasiento
from infrestructura.web.controladores.contorladorcrearmovimiento import controladormovimiento
from infrestructura.web.controladores.controladorobtenercuentas import controladorobtenercuenta
from infrestructura.web.controladores.contorladorlistaasientos import controladorlistarasientos
from infrestructura.web.controladores.controladorlistadiarios import controladorlistardiarios
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diario/<int:id>/',methods=['GET'])
def lista_diario(id):
    return render_template("diario.html")

@app.route('/balance/',methods=['GET'])
def balance():
    pass
@app.route('/diario/<int:diario_id>/plantilla/',methods=['GET'])
def plantilla(diario_id):
    return render_template('plantilla.html')

@app.route('/crearDiario/',methods=['POST'])
def crear_diario():
    return controladorDiario.manejar(request)

@app.route('/crearAsiento/',methods=['POST'])
def crear_asiento():
    return controladorasiento.manejar(request)

@app.route('/crearMovimiento/',methods=['POST'])
def crear_movimiento():
    return controladormovimiento.manejar(request)

@app.route('/listaCuentas/',methods=['GET'])
def lista_cuentas():
    return controladorobtenercuenta.manejar(request)

@app.route('/listaDiarios/',methods=['GET'])
def lista_diarios():
    return controladorlistardiarios.manejar(request)


@app.route('/CrearPlantilla/',methods=['GET'])
def crear_platilla():
    pass
@app.route('/listaAsientos/<int:diario_id>/',methods=['GET'])
def lista_asientos(diario_id):
     return controladorlistarasientos.manejar(diario_id)
   
    


def run():
    app.run(port=4000,debug=True)
    