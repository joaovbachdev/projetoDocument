import json
from os import stat

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

#ControllerBanco().limpaTestes()
#print(ControllerBanco().getAllTests())

#ControllerBanco().getAllElementstestStatus()


#ControllerBanco().getAllTags()

#ControllerBanco().createLines()
    
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
