from flask import Flask, render_template, request
import json
from banco.controllerBanco import ControllerBanco
from automacoes.main import Main
from automacoes.cenarios import Cenarios

app = Flask("app")
bd = ControllerBanco()
main = Main(Cenarios())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getElementos',methods=['GET'])
def getElementos():
    return bd.getElementosPositions()

@app.route("/getInformations")
def getInformations():
    return bd.getInformatios(request.args.get('name'))

@app.route("/getLines")
def getLines():
    return bd.getLines()

@app.route("/getLineInformation")
def getLineInformation():
    return bd.getLineInformation(request.args.get('name'))

@app.route("/executar")
def executa():
    main.start()
    return "executado"

app.run(debug=True)