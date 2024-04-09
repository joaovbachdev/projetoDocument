import json


cenario = []

def getData():
    with open('dados.json','r+') as f:
        return json.load(f)
    
def monta(area, index):
   
    if getData()[area][index]['prerequisito']['area']!="":
        pre = getData()[area][index]['prerequisito']
        cenario.append(getData()[pre['area']][pre['index']]['automacao'])
        monta(pre['area'],pre['index'])
    else:
        cenario.append(getData()[area][index]['automacao'])
