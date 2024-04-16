import json


cenario = []
indexAtual = 2
areaAtual = "viagem" 

def getData():
    with open('testesDeLogica/requisitosMobile/dados.json','r+') as f:
        return json.load(f)
    
def monta(area,index):
    
    data = getData()[area][index]
    requisito = data['requisito']
    print(area, index, requisito)
    if requisito > -1:
        cenario.append(data)
        monta(area,requisito)
    else:
        cenario.append(data)
        first = cenario.pop(0)
        cenario.append(first)
        print(cenario)


monta("viagem",4)