import json

class ControllerBanco:
    def __init__(self) -> None:
        pass

    def getElementosPositions(self):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            return {'positions':[data[i]['position'] for i in data.keys()],'names':[i for i in data.keys()],'interactions':[data[i]['interageCom'] for i in data.keys()]}
        
    def getInformatios(self, name):
        with open('banco/elementos.json','r+') as f:
            data = json.load(f)
            return data[name]

    def getLines(self):
        with open("banco/lines.json","r+") as f:
            data = json.load(f)
            return {"positions":[data[i]["positions"] for i in data.keys()],"names":[i for i in data.keys()]}

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
                        'name':newLine
                    }
                    with open('banco/lines.json','r+') as b:
                        data2 = json.load(b)
                        data2[newLine] = newData
                        b.seek(0)
                        json.dump(data2,b,indent=4)
                        b.truncate()
                    

#ControllerBanco().createLines()