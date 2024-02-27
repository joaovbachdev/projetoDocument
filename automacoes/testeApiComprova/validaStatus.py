##TIPOS DE COMPROVANTES
#-nf
#-CTe
#-ric
#-documento_acessorio
#-assinatura_digital

##CHAVES DE COMPROVANTES
#-nf -> 35240212475660000108550010001298291412507339, 35240202481644000174550020002309151511528521
#-CTe -> 35220882270711002194570000000707921426247610
#-ric -> TCLU5927621, MAGU5105919
#-documento_acessorio
#-assinatura_digital

from email import header
import enum
from http.client import ResponseNotReady
import json
from urllib import response
from urllib import request
from urllib.request import urlcleanup
import requests
import base64
from urllib.parse import urlencode
import time

URL_criaViagem = "https://comprova-matrix-homol.matrixcargo.com.br/public/viagem"
URL_mandaComprovante = "https://comprova-matrix-homol.matrixcargo.com.br/public/viagem/{}/comprovante"
URL_status = "https://comprova-matrix-homol.matrixcargo.com.br/viagens/{}"

TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJvNnAzNFZTZURNMnVoWTNueXg4dFFxNGJQN1EtQzBBcUxfelV1WFF6Q0xjIn0.eyJleHAiOjE3MDk5MjQ4ODUsImlhdCI6MTcwOTA2MDg4NSwianRpIjoiOTUzMzQ0ZTctYjAzNS00MzFhLWE5M2MtZjhlYWE2MGVmNzlhIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWhvbW9sLm1hdHJpeGNhcmdvLmNvbS5ici9yZWFsbXMvbWF0cml4Y2FyZ28iLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiNjg4MjUwYjMtZGM2NS00ZDI0LWI1YzEtY2ZmZmMyYzBhZmY2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXRyaXhjYXJnbyIsIkZGX0ZST05UX1NPUlQiLCJvZmZsaW5lX2FjY2VzcyIsImFkbWluIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbInZpZXctZXZlbnRzIiwicXVlcnktY2xpZW50cyJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWFwcGxpY2F0aW9ucyIsInZpZXctY29uc2VudCIsInZpZXctZ3JvdXBzIiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJtYW5hZ2UtY29uc2VudCIsImRlbGV0ZS1hY2NvdW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCB0ZW5hbnQgcHJvZmlsZSByb2xlcyIsImNsaWVudElkIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImNsaWVudEhvc3QiOiIxOC4yMTMuMjMwLjIzIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1jb21wcm92YS1tYXRyaXgtYXBpIiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIiwiY2xpZW50QWRkcmVzcyI6IjE4LjIxMy4yMzAuMjMifQ.i7r_REeTb4Cmz-9GdOi1QmsZ-Fgx0pJT6_jv711IWlnPuSJGjxx1Jv1ArHdFueykOevhF0iWLHZ_3EjmdvhSA_bmeJcfhWKdiY9X0A-BKqiaVur1BXja_UTdB-Z4z4JtGbSN_jmWEULBS_-KidppecHQmMqi7VyGPIKeNGTN6pQiC2SEATtAEW0VMmYmCAL0YLZeYTEEAFpiJvf2glpLaVriz7102vzWJAwTzeuKRyFmfewIdZ78IySILkaaI7I2aOBI0Eo7ymcSxiugeu9e-HCn_NJoZ2nf3jVrLCm0OBD_Nsj2tWdiHO_IeJbOxGl2mIgGnCIulFX8w4cRWfjFWg"
TOKEN_STATUS = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJvNnAzNFZTZURNMnVoWTNueXg4dFFxNGJQN1EtQzBBcUxfelV1WFF6Q0xjIn0.eyJleHAiOjE3MDkyMzQ5MjMsImlhdCI6MTcwODM3MDkyMywianRpIjoiODg3NzNmZTItYjk0NC00ZWNjLThhNTAtMzc2NWRkZDM2Yzg5IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWhvbW9sLm1hdHJpeGNhcmdvLmNvbS5ici9yZWFsbXMvbWF0cml4Y2FyZ28iLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiNjg4MjUwYjMtZGM2NS00ZDI0LWI1YzEtY2ZmZmMyYzBhZmY2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXRyaXhjYXJnbyIsIkZGX0ZST05UX1NPUlQiLCJvZmZsaW5lX2FjY2VzcyIsImFkbWluIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbInZpZXctZXZlbnRzIiwicXVlcnktY2xpZW50cyJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWFwcGxpY2F0aW9ucyIsInZpZXctY29uc2VudCIsInZpZXctZ3JvdXBzIiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJtYW5hZ2UtY29uc2VudCIsImRlbGV0ZS1hY2NvdW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCB0ZW5hbnQgcHJvZmlsZSByb2xlcyIsImNsaWVudElkIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImNsaWVudEhvc3QiOiIxODkuMTIzLjIzMC42NCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtY29tcHJvdmEtbWF0cml4LWFwaSIsImdpdmVuX25hbWUiOiIiLCJmYW1pbHlfbmFtZSI6IiIsImNsaWVudEFkZHJlc3MiOiIxODkuMTIzLjIzMC42NCJ9.GjWmQq1fv2JSpYU2w4KhNIhdGJImCtGZcRsBOo1iskEU3XmDWR4MJIyZOQtClpzWSKHGl2EeX4ShFw6tOihNueQKx4TmL9pyyyY8c6BOuH6s3BAvgjUtm2RErHgzD7zPogGPqYE3F6uFeokIF9fdeqBLafG06zRcygwXm69g5kEX9S88ZMnmWJmhg3SmXOzxkoiUh3eqOIxwm4Zk_7lEtU6JUXHtzU0YntI01aAfpFY7unGVwpXdG0e48q2fBp0yi9zwsjC9NDjz_a2dOmM2x8EIZTegflL0SnYhBesHaGFDc3nD3RAOWtWjEsJftk0ij2GRxyvXlSeBva6fVwWTkA" 
HEADERS = {"Authorization":f"Bearer {TOKEN}",'Content-Type': 'application/json'}
ultimoId = 0

cte_codes = ["35230982270711002194570000001026501015786859","35230982270711002194570000001026491015196953","35230982270711002194570000001026471364878117",
"35240282270711002003570000003562621018311627","35240282270711002003570000003562701902662504","35240282270711002003570000003570001125801980",
"35240282270711002003570000003570071114772380","35240182270711002194570000001129831314108368","35240182270711002194570000001129791742491280",
"43240282270711000736570000001108001277589861","35230982270711002194570000001023721866890942",
"41240182270711000140570000002105661199828950","35240282270711002003570000003552531246205755",
"35230782270711002194570000000969371034775358","43240282270711000736570000001107481319614417",
"35230782270711002194570000000976831825585008","35230782270711002194570000000990851198978873",
"35240282270711002003570000003548311996523428","35240282270711002194570000001167321130580260",
"35240282270711002194570000001168601603156584","35240282270711002003570000003554061479382421"]

cte_code_analise = ["35240282270711002003570000003531551352419380","35240282270711002003570000003531541475338888",
"35240282270711002003570000003579841540070091","35240282270711002003570000003579861218403511",
"35240282270711002003570000003579801311297340","35240182270711002003570000003472111435142124"]

nf_codes = ["31240201998585002006550010000309981449332492","35240260857349002110550010000382172140127254",
"35240260857349002110550010000382242283620404","35240202481644000174550020002310701935901391",
"35231059275792000150550040031451371401756276","35240260857349001571550010003647871913884255",
"35231261381323000248550010004940561362246001","35231261381323000248550010004940701966766360",
"35231261381323000248550010004940601151707834","35240202481644000174550020002310051708549435",
"35240202481644000174550020002309421456401860","35240210795959000114550010000192861000192876",
"35240210795959000114550010000192871000192881"]

def getExternalId():
    with open("automacoes/testeApiComprova/payloads/dataController.json","r+") as f:
        return str(json.load(f)["externalId"])

def updateExternalId():
    with open("automacoes/testeApiComprova/payloads/dataController.json","r+") as f:
        data = json.load(f)
        data["externalId"] += 1
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()

def criaViagem(tipos,codigos):
    global ultimoId
    with open("automacoes/testeApiComprova/payloads/viagem.json","r+") as f:
        data = json.load(f)
        data["pontos_de_entrega"][0]["documentos_para_comprovacao"] = []
        data["id_externo"] = getExternalId()
        for index,i in enumerate(tipos):
            data["pontos_de_entrega"][0]["documentos_para_comprovacao"].append({
                "chave":codigos[index],
                "tipo":i
            })
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()

        response = requests.post(URL_criaViagem, json = data, headers={"Authorization":f"Bearer: {TOKEN}"})

        ultimoId = response.json()["id"]
        #print(response.json())
        

def getBase(arq):
    with open(f"automacoes/testeApiComprova/imgs/{arq}","rb") as f:
        return base64.b64encode(f.read()).decode("utf-8").replace('\n','').replace('\r','')


def setComprovante(arq, tipo):
    with open("automacoes/testeApiComprova/payloads/comprovante.json","r+") as f:
        data = json.load(f)
        data["comprovante"]["imagem"] = getBase(arq)
        data["tipo"] = tipo
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()
        response = requests.post(URL_mandaComprovante.format(getExternalId()), json=data, headers=HEADERS)
        print(getExternalId())
        
    
def enviaComprovante():
    with open("automacoes/testeApiComprova/payloads/comprovante.json","r+") as f:
        data = json.loads(f.read())
        #response = requests.post(URL_mandaComprovante.format(getExternalId()), json=data, headers=HEADERS)
    




def executaCenario(dadosViagens, dadosComprovantes):
        criaViagem(dadosViagens[0], dadosViagens[1])
        for i in dadosComprovantes:
                setComprovante(i[0],i[1])
                enviaComprovante()
        time.sleep(8)
        #print(requests.get(URL_status.format(ultimoId),headers=HEADERS).json())
        print(getExternalId(),f"deve estar arquivado e esta {requests.get(URL_status.format(ultimoId),headers=HEADERS).json()['status']}")
        updateExternalId()


#print(requests.get("https://comprova-matrix-homol.matrixcargo.com.br/viagens/237919",headers=HEADERS).json())
'''
for i in [i["id"] for i in requests.get("https://comprova-matrix-homol.matrixcargo.com.br/viagens?status=todos&limit=5000",headers=HEADERS).json()["itens"]]:
     r = requests.get(f"https://comprova-matrix-homol.matrixcargo.com.br/viagens/{i}",headers=HEADERS).json()
     print(r["rejeitada_em"] is not None and r["aprovada_em"] is not None, r["id_externo"])
'''
#for index,i in enumerate(cte_codes):
    #executaCenario([["cte"],[i]],[[f'cteAprovados/cte{index}.jpeg','cte']])

for index,i in enumerate(cte_code_analise):
    executaCenario([["cte"],[i]],[[f'cteAnalise/cte{index}.jpeg','cte']])

#for index,i in enumerate(nf_codes):
    #executaCenario([["nf"],[i]],[[f'nf_aprova/nf{index}.jpeg','nf']])

#executaCenario([["nf"],["42191157475747770000000000005747711457550477"]],[["nf_cardTeste.png","nf"]]) 

#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","cte"]]) #VIAGEM ESPERANDO 1 CTE, RECEBE 1 CTE QUE APROVA AUTOMATICO

##executaCenario([["nf"],["35240202481644000174550020002309151511528521"]],[["nf_aprova.jpeg","nf"]])      #VIAGEM ESPERANDO 1 NF, RECEBE 1 NF QUE APROVA

#executaCenario([["ric"],["TCLU5927621"]],[["ric_aprova.jpeg","ric"]])                                    #VIAGEM ESPERANDO 1 RIC, RECEBE 1 RIC QUE APROVA

#executaCenario([["cte"],["123513123"]],[["cte_completo.jpeg","cte"]])                                    #VIAGEM ESPERA 1 CTE, RECEBE 1 CTE QUE REJEITA

#executaCenario([["nf"],["33733"]],[["cte_completo.jpeg","nf"]])                                          #VIAGEM ESPERA 1 NF, RECEBE 1 NF QUE REJEITA

#executaCenario([["ric"],["8774"]],[["cte_completo.jpeg","ric"]])                                         #VIAGEM ESPERA 1 RIC, RECEBE 1 RIC QUE REJEIT#A

#executaCenario([["cte"],["37368736"]],[["cte_completo.jpeg","cte"],["cte_completo.jpeg","ric"]])              #VIAGEM ESPERA 1 CTE, RECEBE 1 CTE E 1 RIC QUE REJEITA, DEVE ESTAR REJEITADA
#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["nf_aprova.jpeg","cte"]])

#executaCenario([["ric"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","ric"],["cte_completo.jpeg","cte"]]) #ESPERA 1 RIC E RECEBE CTE E RIC QUE REJEITA, DEVE SER REJEITADO

#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","cte"],["nf_aprova.jpeg","cte"]])  #VIAGEM ESPERA 1 CTE, RECEBE 1 QUE  APROVA E 1 QUE REJEITA, DEVE ESTAR REJEITADA

#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","cte"],["cte_completo.jpeg","ric"]])  #ESPERA CTE, RECEBE 1 CTTE QUE APROVA E 1 RIC QUE REJEITA, ARQUIVADA E DELETAR O RIC

#executaCenario([["nf"],["35240212475660000108550010001298291412507339"]],[["nf_aprova.jpeg","nf"],["cte_completo.jpeg","nf"]]) #ESPERA NF, RECEBE 1 QUE APROVA E UMA QUE REJEITA, DEVE APROVAR E APAGAR A REJEITADA
#executaCenario([["nf"],["35240212475660000108550010001298291412507339"]],[["cte_completo.jpeg","nf"],["nf_aprova.jpeg","nf"]])
#executaCenario([["ric"],["TCLU5927621"]],[["ric_aprova.jpeg","ric"],["cte_completo.jpeg","ric"]]) #ESPERA RIC, RECEBE 1 RIIC QUE APROVA E 1 RIC QUE REJEITA, DEVE ARQUIVAR E DELETAR OO REJEITADO

#executaCenario([["ric"],["TCLU5927621"]],[["nf_aprova.jpeg","ric"],["cte_completo.jpeg","cte"],["ric_aprova.jpeg","ric"]])  #ESPERA RIIC, RECEBE 1 RIC QUE APROVA E 1 CTE QUE REJEITA, DEVE IR PARA ARQUIVADA E DELETAR O CTE

#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","documento_acessorio"],["cte_completo.jpeg","cte"]]) #DEVE FICAR EM ANALISE

#executaCenario([["ric","cte"],["TCLU5927621","35220882270711002194570000000707921426247610"]],[["ric_aprova.jpeg","ric"],["cte_completo.jpeg","cte"]])  #ESPERA RIC E CTE, RECEBE RIC E CTE QUE APROVA

#executaCenario([["documento_acessorio"],[""]],[["ric_aprova.jpeg","documento_acessorio"]])


#ENVIAR UM DOC ACESSORIO EM UMA VIAGEM QUE NAO POSSUI NADA

#ENVIAR UM DOC ACESSORIO EM UMA VIAGEM QUE POSSUI UM CTE REJEITADO

#ENVIAR UM DOC ACESSORIOI EM UMA VIAGEM QUE POSSUI 1 CTE REJEITADO E 1 CTE APROVADO