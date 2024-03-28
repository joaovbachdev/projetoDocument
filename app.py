from binascii import rledecode_hqx
from crypt import methods
from operator import methodcaller
from sched import scheduler
from unicodedata import name
from urllib.robotparser import RequestRate
from flask import Flask, render_template, request
import json
from banco.controllerBanco import ControllerBanco
from automacoes.main import Main
from automacoes.cenarios import Cenarios
from flask_socketio import SocketIO
import webbrowser
import http.server
import socketserver
import threading
from apscheduler.schedulers.background import BackgroundScheduler
import random
import threading
import time

app = Flask("app")
bd = ControllerBanco()
main = Main(Cenarios(), ControllerBanco)
scheduler = BackgroundScheduler()



socketio = SocketIO(app)

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
            socketio.emit('atualizar',{'name':request.json["name"],'type':request.json["type"],'index':index,'status':"realizado"})
           
        except:
            bd.setTodo(request.json["name"],request.json["type"],index,"naoRealizado")
            bd.saveHistorico(request.json["name"], "erro")
            socketio.emit('atualizar',{'name':request.json["name"],'type':request.json["type"],'index':index,'status':"naoRealizado"})
        
        

    socketio.emit("atualizarStatus",bd.getAllElementstestStatus())
    socketio.emit("desativarSpiner",request.json["name"])


    return "executado"


@app.route('/executaTesteEsp', methods=['POST'])
def executaTesteEsp():
    

    index = bd.getTestsNames(request.json['name'],request.json['type']).index(request.json['testName'])
    teste = bd.getAutomatedTests(request.json['name'],request.json['type'])[index]['automacao']
    
    try:
        main.start('\n'.join(teste))
        bd.setTodo(request.json["name"],request.json["type"],index,"realizado")
        bd.saveHistorico(request.json["name"], "sucesso")
        socketio.emit('atualizar',{'name':request.json["name"],'type':request.json["type"],'index':index,'status':"realizado"})
        print("deu certo")
    except:
        bd.setTodo(request.json["name"],request.json["type"],index,"naoRealizado")
        bd.saveHistorico(request.json["name"], "erro")
        socketio.emit('atualizar',{'name':request.json["name"],'type':request.json["type"],'index':index,'status':"naoRealizado"})
        print("deu erro")

    socketio.emit("atualizaTesteEsp", {'status':bd.getAutomatedTests(request.json['name'],request.json['type'])[index]['status'],'index':index})
    #socketio.emit("desativarSpiner",request.json["name"])

    return 'executado'
        
@app.route("/auxCriaElemento", methods=["POST"])
def auxCriaElemento():
    with open("banco/elementos.json", "r+") as f:
        data = json.load(f)
        data[request.json['name']] = {
            'position': request.json['pos'],
            'description':'cria via  auxiliar',
            'name':request.json['name'],
            'interageCom':"",
            'tags':[],
            'testes':[],
            'bugs':[]
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
    elementName = request.json["elementName"]
    index = request.json["index"]
    status = request.json["status"]
    bd.updateTodo(elementName,int(index),status)
    socketio.emit("atualizarStatus",bd.getAllElementstestStatus())
    return "todo atualizado"

@app.route("/addNewAutomation")
def addNewAutomation():
    print(request.args.get("name"))
    print(request.args.get("type"))
    return render_template("addAutomation.html",elementName = request.args.get("name"),elementType=request.args.get("type"))

@app.route("/addNewAutomationDb",methods=["POST"])
def addNewAutomationBd():
    print(request.json)
    bd.addNewAutomationBd(request.json['elementName'],request.json['elementType'],request.json['data'])
    return "nova automacao salva"

@app.route("/getAutomatedTests")
def getAutomatedTests():
    name = request.args.get("elementName")
    elementype = request.args.get("elementType")
    return bd.getAutomatedTests(name, elementype)

@app.route("/deleteTest",methods=["POST"])
def deleteTest():
    name = request.json["elementName"]
    elementType = request.json["elementType"]
    test = request.json["test"]
    bd.deleteTest(name, elementType, test)
    return "teste deletado com sucesso no back"

@app.route('/addBug', methods=['POST'])
def addNewBug():
    name = request.json['elementName']
    elementType = request.json['elementType']
    bug = request.json['bug']
    bd.createNewBug(name,elementType, bug)
    return bd.getBugs(name,elementType)

@app.route('/getBugs')
def getBugs():
    elementName = request.args.get("name")
    elementType = request.args.get("type")

    return bd.getBugs(elementName, elementType)

@app.route('/deleteBug', methods=['POST'])
def deleteBug():

    elementName = request.json['name']
    elementType = request.json['type']
    bugName = request.json['bugName']

    return bd.deleteBug(elementName, elementType, bugName)
@socketio.on('atualizar')
def atualizar():
    # Execute a atualização dos dados aqui, se necessário
    socketio.emit('atualizar')


@app.route('/setExecuaoAleatoria',methods=['POST'])
def setExesetExecuaoAleatoria():
    dados = bd.getAllTests()
    nome = random.choice(list(dados.keys()))
    index = nome.split('-')[1]
    testes = '\n'.join(dados[nome])

    #minha_tarefa(nome.split('-')[0],index, testes)
    return {'nome':nome.split('-')[0],'index':index,'testes':testes}

@app.route('/executaTesteAleatorio', methods=['POST'])
def minha_tarefa():

    nome = request.json['nome']
    index = request.json['index']
    testes = request.json['testes']
    #nome = 'apiCriaViagem-0'
    #index = 0
    #testes = '\n'.join(dados[nome])
    #print(dados[nome],"TAAAAAAAAAAAAAA AAAAAAAAAQUI O NOMEEEEEEEE")
    
    try:
        main.start(testes)
        bd.setTodo(nome.split('-')[0],'elementos',int(index),"realizado")
        bd.saveHistorico(nome.split('-')[0], "sucesso")
        socketio.emit('atualizar',{'name':nome.split('-')[0],'type':'elementos','index':int(index),'status':"realizado"})
        print("deu certo automatco", nome.split('-')[0],index,testes) 
    except:
        bd.setTodo(nome.split('-')[0],'elementos',int(index),"naoRealizado")
        bd.saveHistorico(nome.split('-')[0], "erro")
        socketio.emit('atualizar',{'name':nome.split('-')[0],'type':'elementos','index':int(index),'status':"naoRealizado"})
        print("deu errado automatico", nome.split('-')[0],index,testes)
        
    socketio.emit("atualizarStatus",bd.getAllElementstestStatus())
    socketio.emit("desativarSpiner",nome.split('-')[0])
    #socketio.emit("atualizaTesteEsp", {'status':bd.getAutomatedTests(nome.split('-')[0],'elementos')[index]['status'],'index':index})
    return "executado aleatorio com sucesso"


app.run(host='0.0.0.0', port=5000, debug=True)


#socketio.runapp.run(debug=True)
