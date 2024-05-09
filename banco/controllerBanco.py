from email import header
import json
from os import stat
import requests
from .notionApi import NotionApi

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
    
    def getTestPlatform(self,name,index):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            return data[name]['testes'][index]['plataforma']

    def getElementTests(self, name,type):
        with open(f"banco/{type}.json","r+") as f:
            data = json.load(f)
        return [i["automacao"] for i in data[name]["testes"]]

    def setTodo(self,elementName,elementType,index,status):
    
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
            automacoes = {f'{i}-{index}':j['automacao'] for i in data.keys() for index,j in enumerate(data[i]["testes"]) if j['automacao']!=[] and j['automacao']!=['']}

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
            data['Quantidade Elementos'] = len(list(dadosElementos.keys()))
            data['Testes Aprovados'] = len([dadosElementos[i] for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if j['status'] == 'realizado'])
            data['Testes Pendentes/Reprovados'] = len([dadosElementos[i] for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if j['status'] == 'naoRealizado'])
            data['Elementos Sem Teste'] = len([1 for i in dadosElementos.keys() if len(dadosElementos[i]['testes']) == 0])
            data['Elementos Com Testes'] = len([1 for i in dadosElementos.keys() if len(dadosElementos[i]['testes']) > 0])
            data['Testes Escritos'] = data['Testes Aprovados'] + data['Testes Pendentes/Reprovados'] 
            data['Interacões'] = len([1 for i in dadosElementos.keys() if dadosElementos[i]['interageCom'] != ""])
            data['Testes Com Automacão'] = len([1 for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if len(j['automacao'])>0])
            data['Teste Sem Automacão'] = len([1 for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if len(j['automacao'])==0])
            data['testeMobile'] = len([dadosElementos[i] for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if j['plataforma'] == 'mobile'])
            data['testesWeb'] = len([dadosElementos[i] for i in dadosElementos.keys() for j in dadosElementos[i]['testes'] if j['plataforma'] == 'web'])
            
        with open('banco/historico.json','r+') as d:
            dadosHistorico = json.load(d)
            data['Testes Automaticos Realizados'] = sum([len(dadosHistorico[i]) for i in dadosHistorico.keys()])
            data['Testes Automaticos Com Sucesso'] = len([1 for i in dadosHistorico.keys() for j in dadosHistorico[i] if j['resultado']=='sucesso'])
            data['Testes Automaticos Com Erro'] = len([1 for i in dadosHistorico.keys() for j in dadosHistorico[i] if j['resultado']=='erro'])

        with open('automacoes/testesYaml/dicionario.json','r+') as f:
            dadosDicionario = json.load(f)
            data['testes mobile cadastrado'] = len([1 for i in dadosDicionario.keys() for j in dadosDicionario[i]])
        return data

    def getMobileTestsAreas(self):
        with open('automacoes/testesYaml/dicionario.json','r+') as f:
            return [i for i in json.load(f).keys()]

    def getMobileAreaComands(self, area):
        with open('automacoes/testesYaml/dicionario.json','r+') as f:
            return [i for i in json.load(f)[area]]
    
    def getMobileTestObject(self, area, teste):
        with open('automacoes/testesYaml/dicionario.json','r+') as f:
            data = json.load(f)
            for i in data[area]:
                if i['automacao'] == teste:
                    return i

    def ultimasDezViagens(self):
        url = "https://back-homologacao.matrixcargo.com.br/api/ranking/get_last_goals"
        headerAcelerador = {'Authorization':f'Bearer {"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxYzI1ODY4MS1mYmUwLTRlNjUtYmJmZi1hNTliMTViODg1YzciLCJkYXRhIjp7ImNvbXBhbnkiOiJjYXJnb2xpZnQifSwiaWF0IjoxNjkyOTY0NDgzfQ.byWzfOhCT_1H2aZgqIXOo4-5dWKUf05Iu1QiR2-JZq4"}',
                       'Content-Type': 'application/json'}
        response = requests.get(url,json={'driver_id':'4b973aa2-1a1e-4e8b-b23b-cb593300620e'},headers=headerAcelerador)
        return [i['internal_id'] for i in response.json()][0]
        

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

    def get_hist_tests(self):
        data = NotionApi().get_pages_info()
        results = {}
        for i in data:
            id = data[i]
            results[data[i]] = []
            with open('banco/elementos.json','r+') as f:
                dados = json.load(f)
                for j in dados:
                    for k in dados[j]['historias']:
                        if k == id:
                            results[data[i]].append(j)
        print(results)

    def get_pages_names(self):
        return [i for i in NotionApi().get_pages_info().values()]

    def getElementPages(self,name):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            return data[name]['historias']
        
    def updatElementHistorys(self, elementName, histName, checked):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            testes = [i['teste'] for i in data[elementName]['testes']]
            if checked == False:
                data[elementName]['historias'].remove(histName)
                for i in data[elementName]['linkedHistoris'][histName]:
                    response = NotionApi().delete_block(i)
                    print(response)
                del data[elementName]['linkedHistoris'][histName]
            else:
                data[elementName]['linkedHistoris'][histName] = []
                data[elementName]['historias'].append(histName)
                for i in testes:
                    response = NotionApi().add_to_do(histName,i)
                    data[elementName]['linkedHistoris'][histName].append(response['results'][0]['id'])
            
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

#ControllerBanco().updatElementHistorys('telaLogin','haha', True)
#ControllerBanco().get_hist_tests()
#ControllerBanco().get_pages_names()    

#print(ControllerBanco().getAllTests())
#print(ControllerBanco().getTestPlatform('inputUsuario',0))
#ControllerBanco().limpaTestes()
#print(ControllerBanco().getAllTests())

#ControllerBanco().getAllElementstestStatus()


#ControllerBanco().getAllTags()

#ControllerBanco().createLines()
#print(ControllerBanco().extraiRelatorio())  

#ControllerBanco().verifica_weakup_record_criado()


#ControllerBanco().getMobileTestsAreas()
#print(ControllerBanco().getMobileAreaComands('checklist'))
#print(ControllerBanco().getInformatios('telaLogin'))

#print(ControllerBanco().getMobileTestObject('telaLogin',0))

#ControllerBanco().ultimasDezViagens()

'''
with open("banco/elementos.json","r+") as f:
    data = json.load(f)
    for i in data.keys():
        data[i]["linkedHistoris"] = {}
    f.seek(0)
    json.dump(data,f,indent=4)
    f.truncate
'''

#print(ControllerBanco().validateElementTagFilter("nada"))
#ControllerBanco().getElementTests("inputUsuario","elementos")
