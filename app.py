from unicodedata import name
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
    return render_template('index.html', tags=bd.getAllTags())

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
 
@app.route("/executar", methods=["POST"])
def executa():

    for index,i in enumerate(bd.getElementTests(request.json["name"],request.json["type"])):
        try:
            main.start('\n'.join(i))
            bd.setTodo(request.json["name"],request.json["type"],index,"realizado")
            bd.saveHistorico(request.json["name"], "sucesso")
            print("deu certo")
        except:
            bd.setTodo(request.json["name"],request.json["type"],index,"naoRealizado")
            bd.saveHistorico(request.json["name"], "erro")
            print("deu erro")

    return "executado"



@app.route("/auxCriaElemento", methods=["POST"])
def auxCriaElemento():
    with open("banco/elementos.json", "r+") as f:
        data = json.load(f)
        data[request.json['name']] = {
            'position': request.json['pos'],
            'description':'cria via  auxiliar',
            'name':request.json['name'],
            'interageCom':""
        }
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()
    return "a"

@app.route("/deletaTag", methods=["POST"])
def deletaTag():
    name = request.json['name']
    father = request.json['father']
    elementType = request.json['elementType']
    bd.deletaTag(name,father, elementType)

    return "tag deletada com sucesso"


@app.route("/addNewTag",methods=["POST"])
def addNewTag():    
    tagName = request.json["tagName"]
    fatherName = request.json["fatherName"]
    elementType = request.json["elementType"]
    bd.addNewTag(tagName, fatherName, elementType)
    return "tag adicionada com sucesso"



@app.route("/checkTagExists")
def checkTagExists():
    return bd.validateElementTagFilter(request.args.get("tagName"))


@app.route("/checkTodo",methods=["POST"])
def checkTodo():
    print(request.json)
    elementName = request.json["elementName"]
    index = request.json["index"]
    bd.updateTodo(elementName,int(index))
    return "todo atualizado"
app.run(debug=True)