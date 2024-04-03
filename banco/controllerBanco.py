import json
from os import stat
import requests

class ControllerBanco:
    def __init__(self) -> None:
        pass

    def getElementosPositions(self):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            return data
            #return {'positions':[data[i]['position'] for i in data.keys()],'names':[i for i in data.keys()],'interactions':[data[i]['interageCom'] for i in data.keys()]}
        
    def getInformatios(self, name):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            return data[name]

    def getLines(self):
        with open("banco/lines.json","r+") as f:
            data = json.load(f)
            return data

    def getLineInformation(self,name):
        with open("banco/lines.json", "r+") as f:
            data = json.load(f)
            return data[name]
         
    def createElement(self, name):
        with open('elementos.json','r+') as f:
            data = json.load(f)
            data[name] = {
                "position":[],
                "description":"descricao aqui",
                "name":name
            }
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def createLines(self):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            for i in data.keys():
                if data[i]['interageCom']!="":
                    newLine = i+"/"+data[i]['interageCom']
                    newData = {
                        'positions': [j for i in [data[i]['position'],data[data[i]['interageCom']]['position']] for j in i],
                        'description':"sua descricao aqui",
                        'name':newLine,
                        'tags':[],
                        'testes':[]
                    }
                    with open('banco/lines.json','r+') as b:
                        data2 = json.load(b)
                        data2[newLine] = newData
                        b.seek(0)
                        json.dump(data2,b,indent=4)
                        b.truncate()

    def deletaTag(self,name,father,elementType):
        with open(f"banco/{elementType}.json","r+") as f:
            data = json.load(f)
            if name in data[father]['tags']:
                data[father]['tags'].remove(name)
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()
        
    def addNewTag(self,tagName,fatherName, elementType):
        with open(f"banco/{elementType}.json","r+") as f:
            data = json.load(f)
            data[fatherName]['tags'].append(tagName)
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def saveHistorico(self, name, resultado):

        
        with open("banco/historico.json","r+") as f:
            data = json.load(f)

            if name not in data.keys():
                data[name] = []

            data[name].append({
                "resultado":resultado
            })
            f.seek(0)
            json.dump(data,f, indent=4)
            f.truncate()

    def getAllTags(self):
        with open("banco/elementos.json","r+") as f:
            data = json.load(f)
            tags = []
            for i in data.keys():
                for j in data[i]['tags']:
                    if j not in tags:
                        tags.append(j)
        return tags

    def validateElementTagFilter(self,tagName):
        values = {"circles":[], "lines":[]}
        with open("banco/elementos.json","r+") as f:
            data = json.load(f)
            for i in data.keys():
                if len(data[i]["tags"])<=0:
                    values["circles"].append([data[i]["name"],"False"])
                else:
                    if tagName in data[i]["tags"]:
                        values["circles"].append([data[i]["name"],"True"])
                    else:
                        values["circles"].append([data[i]["name"],"False"])


        with open("banco/lines.json","r+") as f:
            data = json.load(f)
            for i in data.keys():
                if len(data[i]["tags"])<=0:
                    values["lines"].append([data[i]["name"],"False"])
                else:
                    if tagName in data[i]["tags"]:
                        values["lines"].append([data[i]["name"],"True"])
                    else:
                        values["lines"].append([data[i]["name"],"False"])
       
        return values

    def updateTodo(self, elementName, index, status):
        print(elementName, index, status, "DADHASHDASHIASHD")
        with open("banco/elementos.json","r+") as f:
            data = json.load(f)
            if status == "none":
                if data[elementName]["testes"][index]["status"] == "realizado":
                    data[elementName]["testes"][index]["status"] = "naoRealizado"
                else:
                    data[elementName]["testes"][index]["status"] = "realizado"
            else:
                data[elementName]["testes"][index]["status"] = status
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def getTestsNames(self, name,type):
         with open(f"banco/{type}.json","r+") as f:
            data = json.load(f)
            return [i["teste"] for i in data[name]["testes"]]

    def getElementTests(self, name,type):
        with open(f"banco/{type}.json","r+") as f:
            data = json.load(f)
        return [i["automacao"] for i in data[name]["testes"]]

    def setTodo(self,elementName,elementType,index,status):
        print(elementName,elementType,index,status)
        with open(f"banco/{elementType}.json","r+") as f:
            data = json.load(f)
            data[elementName]["testes"][index]["status"] = status
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def getAllElementstestStatus(self):
        values = {}
        with open("banco/elementos.json","r+") as f:
            data = json.load(f)
            for i in data.keys():
                if len(data[i]["testes"])<=0:
                    values[i] = "none"
                else:
                    values[i] = "realizado"
                    for j in data[i]["testes"]:
                        if j["status"] == "naoRealizado":
                            values[i] = "naoRealizado"
                            break
        return values

    def addNewAutomationBd(self,elementName,elementType, newData):
        with open(f'banco/{elementType}.json','r+') as f:
            data = json.load(f)
            data[elementName]["testes"].append(newData)
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()                    

    def getAutomatedTests(self, elementName,elementType):
        with open(f"banco/{elementType}.json","r+") as f:
            data = json.load(f)
            return data[elementName]["testes"]
    
    def deleteTest(self,elementName, elementType, test):
        with open(f"banco/{elementType}.json", "r+") as f:
            data = json.load(f)
            del data[elementName]["testes"][test]
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def createNewBug(self, elementName, elementType, bug):
        with open(f'banco/{elementType}.json','r+') as f:
            data = json.load(f)
            data[elementName]['bugs'].append(bug)
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def getBugs(self, name, _type):
        with open(f'banco/{_type}.json') as f:
            data = json.load(f)
            return data[name]['bugs']

    def deleteBug(self, element, elementType, bugName):
        print(bugName)
        with open(f'banco/{elementType}.json', 'r+') as f:
            data = json.load(f) 
        
            data[element]['bugs'].remove(bugName)
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

            return data[element]['bugs']
    
    def getAllTests(self):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            automacoes = {f'{i}-{index}':j['automacao'] for i in data.keys() for index,j in enumerate(data[i]["testes"]) if j['automacao']!=['']}

        return automacoes

    def limpaTestes(self):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            for i in data.keys():
                data[i]['testes'] = []

            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def extraiRelatorio(self):
        data = {}
        with open('banco/elementos.json','r+') as f:
            dadosElementos = json.load(f)
            data['quantidadeElementos'] = len(list(dadosElementos.keys()))
            data['testesAprovados'] = len([dadosElementos[i] for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if j['status'] == 'realizado'])
            data['testesPendentes/reprovados'] = len([dadosElementos[i] for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if j['status'] == 'naoRealizado'])
            data['elementosSemTeste'] = len([1 for i in dadosElementos.keys() if len(dadosElementos[i]['testes']) == 0])
            data['elementosComTestes'] = len([1 for i in dadosElementos.keys() if len(dadosElementos[i]['testes']) > 0])
            data['testesEscritos'] = data['testesAprovados'] + data['testesPendentes/reprovados'] 
            data['interacoes'] = len([1 for i in dadosElementos.keys() if dadosElementos[i]['interageCom'] != ""])
            data['testesComAutomacao'] = len([1 for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if len(j['automacao'])>0])
            data['testeSemAutomacao'] = len([1 for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if len(j['automacao'])==0])
            
        with open('banco/historico.json','r+') as d:
            dadosHistorico = json.load(d)
            data['testesAutomaticosRealizados'] = sum([len(dadosHistorico[i]) for i in dadosHistorico.keys()])
            data['testesAutomaticosComSucesso'] = len([1 for i in dadosHistorico.keys() for j in dadosHistorico[i] if j['resultado']=='sucesso'])
            data['testesAutomaticosComErro'] = len([1 for i in dadosHistorico.keys() for j in dadosHistorico[i] if j['resultado']=='erro'])
        return data

    def getMobileTestsAreas(self):
        with open('automacoes/testesYaml/dicionario.json','r+') as f:
            return [i for i in json.load(f).keys()]
    def getMobileAreaComands(self, area):
        print("AREAAAAAAAAAAAAAAAAAA",area)
        with open('automacoes/testesYaml/dicionario.json','r+') as f:
            return json.load(f)[area]

    def verifica_weakup_record_criado(self):
        url = "https://back-homologacao.matrixcargo.com.br/graphql"
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJkODM3N2Q3NS1lYTlkLTQ3YmUtYmFiMS00MWQyYjY2MmY2NjYiLCJkYXRhIjp7ImNvbXBhbnkiOiJjYXJnb2xpZnQifSwiaWF0IjoxNzEwMjY4NzExfQ.MGEr3tSuMfQ5LTEztk6cHQ0BUct2aZmfw0FeBHWl0FI"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        query_variables = {
            "select": {
                "pagination": {
                    "page": 1,
                    "limit": 20,
                    "orderBy": "recommended_rest_datetime,asc"
                },
                "filters": {
                    "situation": "em_analise",
                    "driver_type": "todos"
                }
            }
        }

        graphql_query = '''
        query getAllDriverWakeupRecords($select: GetAllRecordsParams) {
        getAllDriverWakeupRecords(select: $select) {
            itens {
            id
            motorista
            data_hora_do_registro
            data_hora_despertou
            data_hora_recomendada_descanso
            tempo_decorrido
            vinculo
            status
            analisado_em
            }
            pagination {
            totalItens
            totalPages
            page
            limit
            }
        }
        }
        '''
        query = {
            "operationName": "getAllDriverWakeupRecords",
            "variables": query_variables,
            "query": graphql_query
        }
        response = requests.post(url, headers=headers, json=json.loads(json.dumps(query)))

        formated = json.dumps(response.json(), indent=2)
        print(formated)
#ControllerBanco().limpaTestes()
#print(ControllerBanco().getAllTests())

#ControllerBanco().getAllElementstestStatus()


#ControllerBanco().getAllTags()

#ControllerBanco().createLines()
#print(ControllerBanco().extraiRelatorio())  

#ControllerBanco().verifica_weakup_record_criado()


#ControllerBanco().getMobileTestsAreas()
#print(ControllerBanco().getMobileAreaComands('checklist'))


'''
with open("banco/elementos.json","r+") as f:
    data = json.load(f)
    for i in data.keys():
        data[i]["bugs"] = []
    f.seek(0)
    json.dump(data,f,indent=4)
    f.truncate
'''

#ControllerBanco().validateElementTagFilter("geral")
#ControllerBanco().getElementTests("inputUsuario","elementos")
