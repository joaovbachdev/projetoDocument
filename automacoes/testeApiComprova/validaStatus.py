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

TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJvNnAzNFZTZURNMnVoWTNueXg4dFFxNGJQN1EtQzBBcUxfelV1WFF6Q0xjIn0.eyJleHAiOjE3MDg4ODI5OTMsImlhdCI6MTcwODAxODk5MywianRpIjoiOTM1NGZiZjYtZjJmYy00ZTFiLWFiZmItMmY4MDlhOTljMTNjIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWhvbW9sLm1hdHJpeGNhcmdvLmNvbS5ici9yZWFsbXMvbWF0cml4Y2FyZ28iLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiNjg4MjUwYjMtZGM2NS00ZDI0LWI1YzEtY2ZmZmMyYzBhZmY2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXRyaXhjYXJnbyIsIkZGX0ZST05UX1NPUlQiLCJvZmZsaW5lX2FjY2VzcyIsImFkbWluIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbInZpZXctZXZlbnRzIiwicXVlcnktY2xpZW50cyJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWFwcGxpY2F0aW9ucyIsInZpZXctY29uc2VudCIsInZpZXctZ3JvdXBzIiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJtYW5hZ2UtY29uc2VudCIsImRlbGV0ZS1hY2NvdW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCB0ZW5hbnQgcHJvZmlsZSByb2xlcyIsImNsaWVudElkIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImNsaWVudEhvc3QiOiIxNzcuOTIuNDguOSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtY29tcHJvdmEtbWF0cml4LWFwaSIsImdpdmVuX25hbWUiOiIiLCJmYW1pbHlfbmFtZSI6IiIsImNsaWVudEFkZHJlc3MiOiIxNzcuOTIuNDguOSJ9.gqaxp7I1msuKKDxYyS7-aLsbIK5hADJ1gTUqB4DS4Gwu-GxVcDCBt0GDB1uVbzIYcCKRlnXOZGSDxiUPtQ9rYk3Puv-STvm5VyCMOGDQgWJqnhzevd88tsf6VtRnIAdXzudYPWvORBidUi3BMpOfQ1VE_njxLuge26rxpRij7Fmtu2lD062tlxx2uLbPLM5Yn7lQSe9vi8N9DWcU5_xdg5kMpG_iMLl2A_08BvxwodeigL58QAwDgsvclxKSwrfNI4n6VfOgOmWQNwIG_VlqLwzVDyogl_aEn9xS3uQBM5mCSgiYV07kBYjLXq3JjsuT8SlClm1zP1NYBy2x7S5OVw"
TOKEN_STATUS = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJvNnAzNFZTZURNMnVoWTNueXg4dFFxNGJQN1EtQzBBcUxfelV1WFF6Q0xjIn0.eyJleHAiOjE3MDkzMTM1NDYsImlhdCI6MTcwODQ0OTU0NiwianRpIjoiODNkOWY1YTEtYjNkNS00MTY2LTliYzUtYWQwOTJjY2IxN2EyIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWhvbW9sLm1hdHJpeGNhcmdvLmNvbS5ici9yZWFsbXMvbWF0cml4Y2FyZ28iLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiNjg4MjUwYjMtZGM2NS00ZDI0LWI1YzEtY2ZmZmMyYzBhZmY2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXRyaXhjYXJnbyIsIkZGX0ZST05UX1NPUlQiLCJvZmZsaW5lX2FjY2VzcyIsImFkbWluIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbInZpZXctZXZlbnRzIiwicXVlcnktY2xpZW50cyJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWFwcGxpY2F0aW9ucyIsInZpZXctY29uc2VudCIsInZpZXctZ3JvdXBzIiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJtYW5hZ2UtY29uc2VudCIsImRlbGV0ZS1hY2NvdW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCB0ZW5hbnQgcHJvZmlsZSByb2xlcyIsImNsaWVudElkIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImNsaWVudEhvc3QiOiIxNzcuMjIwLjE4MS4xMzciLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWNvbXByb3ZhLW1hdHJpeC1hcGkiLCJnaXZlbl9uYW1lIjoiIiwiZmFtaWx5X25hbWUiOiIiLCJjbGllbnRBZGRyZXNzIjoiMTc3LjIyMC4xODEuMTM3In0.YXiTUhZPvhGw5lPZ5lRhtxvAZnH-d3Nv0PSYFnPSRXADkZ4GvaTjRxghThpbNI9DJTlhTvhrZ3DsdJFjNMfnDKCPX-OYqYhH3MXVXzhW8Nn9i5wfJk_C2x79us_k-GU6DUSqFRwLNLQqMM6Ur1hpwKiUWHSBEvibaBvLgrkmaD0LEo6xfK5yQE4Y7-sN89icB2R2Exvjv7gzC6gTHbeXWry3SJCb2ixBbeGyNTupbsr8fsvsJJN_AcJ2b7G0p0DhING7yf92_nBUFkFc83Cufp_h6hJ6Aosp17Af2Wcl_yvGdch4kPQ2QF0BXMGXHbUWS9dVYGyKKJq8xFqmJWSTNg" 
HEADERS = {"Authorization":f"Bearer {TOKEN}",'Content-Type': 'application/json'}
HEADERS_STATUS = {"Authorization":f"Bearer: {TOKEN_STATUS}",'Content-Type': 'application/json'}
ultimoId = 0

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
        
    
def enviaComprovante():
    with open("automacoes/testeApiComprova/payloads/comprovante.json","r+") as f:
        data = json.loads(f.read())
        response = requests.post(URL_mandaComprovante.format(getExternalId()), json=data, headers=HEADERS)
        





def executaCenario(dadosViagens, dadosComprovantes):
        criaViagem(dadosViagens[0], dadosViagens[1])
        for i in dadosComprovantes:
                setComprovante(i[0],i[1])
                enviaComprovante()
        time.sleep(6)
        print(getExternalId(),f"deve estar arquivado e esta {requests.get(URL_status.format(ultimoId),headers=HEADERS).json()['status']}")
        updateExternalId()





#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","cte"]]) #VIAGEM ESPERANDO 1 CTE, RECEBE 1 CTE QUE APROVA AUTOMATICO

##executaCenario([["nf"],["35240202481644000174550020002309151511528521"]],[["nf_aprova.jpeg","nf"]])      #VIAGEM ESPERANDO 1 NF, RECEBE 1 NF QUE APROVA

#executaCenario([["ric"],["TCLU5927621"]],[["ric_aprova.jpeg","ric"]])                                    #VIAGEM ESPERANDO 1 RIC, RECEBE 1 RIC QUE APROVA

#executaCenario([["cte"],["123513123"]],[["cte_completo.jpeg","cte"]])                                    #VIAGEM ESPERA 1 CTE, RECEBE 1 CTE QUE REJEITA

#executaCenario([["nf"],["33733"]],[["cte_completo.jpeg","nf"]])                                          #VIAGEM ESPERA 1 NF, RECEBE 1 NF QUE REJEITA

#executaCenario([["ric"],["8774"]],[["cte_completo.jpeg","ric"]])                                         #VIAGEM ESPERA 1 RIC, RECEBE 1 RIC QUE REJEIT#A

#executaCenario([["cte"],["37368736"]],[["cte_completo.jpeg","cte"],["cte_completo","ric"]])              #VIAGEM ESPERA 1 CTE, RECEBE 1 CTE E 1 RIC QUE REJEITA, DEVE ESTAR REJEITADA

#executaCenario([["ric"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","ric"],["cte_completo.jpeg","cte"]]) #ESPERA 1 RIC E RECEBE CTE E RIC QUE REJEITA, DEVE SER REJEITADO

#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","cte"],["nf_aprova.jpeg","cte"]])  #VIAGEM ESPERA 1 CTE, RECEBE 1 QUE  APROVA E 1 QUE REJEITA, DEVE ESTAR REJEITADA

#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","cte"],["cte_completo.jpeg","ric"]])  #ESPERA CTE, RECEBE 1 CTTE QUE APROVA E 1 RIC QUE REJEITA, ARQUIVADA E DELETAR O RIC

#executaCenario([["nf"],["35240212475660000108550010001298291412507339"]],[["nf_aprova.jpeg","nf"],["cte_completo.jpeg","nf"]]) #ESPERA NF, RECEBE 1 QUE APROVA E UMA QUE REJEITA, DEVE APROVAR E APAGAR A REJEITADA

#executaCenario([["ric"],["TCLU5927621"]],[["ric_aprova.jpeg","ric"],["cte_completo.jpeg","ric"]]) #ESPERA RIC, RECEBE 1 RIIC QUE APROVA E 1 RIC QUE REJEITA, DEVE ARQUIVAR E DELETAR OO REJEITADO

#executaCenario([["ric"],["TCLU5927621"]],[["ric_aprova.jpeg","ric"],["cte_completo.jpeg","cte"]])  #ESPERA RIIC, RECEBE 1 RIC QUE APROVA E 1 CTE QUE REJEITA, DEVE IR PARA ARQUIVADA E DELETAR O CTE

#executaCenario([["cte"],["35220882270711002194570000000707921426247610"]],[["cte_completo.jpeg","documento_acessorio"],["cte_completo.jpeg","cte"]]) #DEVE FICAR EM ANALISE

#executaCenario([["ric","cte"],["TCLU5927621","35220882270711002194570000000707921426247610"]],[["ric_aprova.jpeg","ric"],["cte_completo.jpeg","cte"]])  #ESPERA RIC E CTE, RECEBE RIC E CTE QUE APROVA

#executaCenario([["documento_acessorio"],[""]],[["ric_aprova.jpeg","documento_acessorio"]])


#ENVIAR UM DOC ACESSORIO EM UMA VIAGEM QUE NAO POSSUI NADA

#ENVIAR UM DOC ACESSORIO EM UMA VIAGEM QUE POSSUI UM CTE REJEITADO

#ENVIAR UM DOC ACESSORIOI EM UMA VIAGEM QUE POSSUI 1 CTE REJEITADO E 1 CTE APROVADO