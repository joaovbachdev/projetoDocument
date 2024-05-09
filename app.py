from crypt import methods
from urllib.robotparser import RequestRate
from wsgiref.util import request_uri
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
import random
import threading
import time
import matplotlib
import matplotlib.pyplot as plt
import os



app = Flask("app")
bd = ControllerBanco()
main = Main(Cenarios(), ControllerBanco)
matplotlib.use('agg')


socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html', tags=bd.getAllTags(), notionPages=bd.get_pages_names())

@app.route('/relatorio')
def relatorio():
    return render_template('testeRelatorio.html', data=bd.extraiRelatorio())

@app.route('/graficos')
def graficos():
    return render_template('historicoBugs.html')

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
    plataforma = request.json['plataforma']
    
    
    for index,i in enumerate(bd.getElementTests(request.json["name"],request.json["type"])):
        try:
            main.start(i, bd.getTestPlatform(request.json['name'],index))
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
    teste = bd.getAutomatedTests(request.json['name'],request.json['type'])[index]
    plataforma = teste['plataforma']
    automacao = teste['automacao']

    #for i in automacao:
        #print(bd.getMobileTestObject(i['area'],i['teste']))
    try:
        main.start(automacao,plataforma)
        bd.setTodo(request.json["name"],request.json["type"],index,"realizado")
        bd.saveHistorico(request.json["name"], "sucesso")
        print("tentei")
        socketio.emit('atualizar',{'name':request.json["name"],'type':request.json["type"],'index':index,'status':"realizado"})
        
    except Exception as e:
        bd.setTodo(request.json["name"],request.json["type"],index,"naoRealizado")
        bd.saveHistorico(request.json["name"], "erro")
        socketio.emit('atualizar',{'name':request.json["name"],'type':request.json["type"],'index':index,'status':"naoRealizado"})
        print(e)

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
    return render_template("addAutomation.html",elementName = request.args.get("name"),elementType=request.args.get("type"))

@app.route("/addNewAutomationDb",methods=["POST"])
def addNewAutomationBd():
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
    
    automacao = bd.getAutomatedTests(request.json['nome'],'elementos')[int(request.json['index'])]['automacao']
    plataforma = bd.getAutomatedTests(request.json['nome'],'elementos')[int(request.json['index'])]['plataforma']

    #autWeb = bd.getAutomatedTests('inputUsuario','elementos')[int(1)]['automacao']
    #print(automacao, plataforma)

    try:
        main.start(automacao, plataforma)
        #bd.setTodo(nome.split('-')[0],'elementos',int(index),"realizado")
        bd.saveHistorico(request.json['nome'], "sucesso")
        #socketio.emit('atualizar',{'name':nome.split('-')[0],'type':'elementos','index':int(index),'status':"realizado"})

    except:
        #bd.setTodo(nome.split('-')[0],'elementos',int(index),"naoRealizado")
        bd.saveHistorico(request.json['nome'], "error")
        #socketio.emit('atualizar',{'name':nome.split('-')[0],'type':'elementos','index':int(index),'status':"naoRealizado"})
     
        
    #socketio.emit("atualizarStatus",bd.getAllElementstestStatus())
    #socketio.emit("desativarSpiner",nome.split('-')[0])
    #socketio.emit("atualizaTesteEsp", {'status':bd.getAutomatedTests(nome.split('-')[0],'elementos')[index]['status'],'index':index})
    return "executado aleatorio com sucesso"


@app.route('/getMobileTestArea')
def getMobileTestArea():
    return bd.getMobileTestsAreas()

@app.route('/getMobileTestes')
def getMobileTestes():
    value = request.args.get('value')

    return bd.getMobileAreaComands(value)

@app.route('/tratamentoErrosMobile',methods=['POST'])
def tratamentoErrosMobile():
    retorno = request.json['retorno']
    print(retorno, "RETORNOoooooooooooooo")
    return "recebido"

@app.route("/atualizaGrafico",methods=['POST'])
def atualizaGrafico():
    labels = []
    sizes = []
    opcao = request.json['opcao']
    index = ''
    #if os.path.exists('static/grafico_de_pizza.png'):
        #os.remove('static/grafico_de_pizza.png')

    if opcao == 'opcao1':
        index = 'grafico_de_pizza.png'
        print("OPCAO1")
        labels = ['suporte', 'customizacao', 'bug']
        sizes = [20, 33, 47]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Garante que o gráfico seja um círculo
        plt.savefig('static/grafico_de_pizza.png')
        plt.clf()
       
    else:
        index = 'grafico_de_pizza2.png'
        print("OPCAO2")
        labels = ['apicativo', 'da', 'acelerador']
        sizes = [15, 33, 52]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Garante que o gráfico seja um círculo
        plt.savefig('static/grafico_de_pizza.png')
        plt.clf()
    
    return index

@app.route('/get_pages_name',methods= ['GET'])
def get_pages_name():
    return bd.get_pages_names()

@app.route('/getElementPages', methods=['POST'])
def getElementPages():
    elementName = request.json['name']
    return bd.getElementPages(elementName)

@app.route('/updatElementHistorys', methods=['POST'])
def updatElementHistorys():
    elementName = request.json['elementName']
    histName = request.json['histName']
    checked = request.json['checked']
    bd.updatElementHistorys(elementName, histName, checked)
    return 'historias atualizadas'





app.run(host='0.0.0.0', port=5000, debug=True)


#socketio.runapp.run(debug=True)
