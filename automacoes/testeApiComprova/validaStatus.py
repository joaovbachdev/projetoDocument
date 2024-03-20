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

TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJvNnAzNFZTZURNMnVoWTNueXg4dFFxNGJQN1EtQzBBcUxfelV1WFF6Q0xjIn0.eyJleHAiOjE3MTE4MTc4NDksImlhdCI6MTcxMDk1Mzg0OSwianRpIjoiMDhlNWQzYzMtMGJmMS00NWU5LWJhZTEtMTExODU3ZmU2NjdkIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWhvbW9sLm1hdHJpeGNhcmdvLmNvbS5ici9yZWFsbXMvbWF0cml4Y2FyZ28iLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiNjg4MjUwYjMtZGM2NS00ZDI0LWI1YzEtY2ZmZmMyYzBhZmY2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1tYXRyaXhjYXJnbyIsIkZGX0ZST05UX1NPUlQiLCJvZmZsaW5lX2FjY2VzcyIsImFkbWluIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbInZpZXctZXZlbnRzIiwicXVlcnktY2xpZW50cyJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWFwcGxpY2F0aW9ucyIsInZpZXctY29uc2VudCIsInZpZXctZ3JvdXBzIiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJtYW5hZ2UtY29uc2VudCIsImRlbGV0ZS1hY2NvdW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCB0ZW5hbnQgcHJvZmlsZSByb2xlcyIsImNsaWVudElkIjoiY29tcHJvdmEtbWF0cml4LWFwaSIsImNsaWVudEhvc3QiOiIxOC4yMTMuMjMwLjIzIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC1jb21wcm92YS1tYXRyaXgtYXBpIiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIiwiY2xpZW50QWRkcmVzcyI6IjE4LjIxMy4yMzAuMjMifQ.NwD_qNK-7sQ7KL573Qb9uO9QO_BF53v3v8QuYFdbMkX7KAYMqmMb4DZQJy14qSLZFiC7Be9zOod8agDhXTjzo-RRc_PuExmVtZPj_pdjs9ffcb4gBdrP6_uqm089299D_84PCQ66Awk3RZqiiV9ACHGSR_OinmusCScE0eEOAR8qVWg2Gf5LFPXVM3DtBY8ByliMEfCs1rqPekm22s4BBoGMtebWwXv4CkL4IeLMidmRrv9zEVKF7rwdH6E8hTH-04m3bg8VgnKX5pk5gcmH15xx1oRsFQFQx3AvNnkzxC8F4OO06qOek96Okt8lrlJo0789tat5T53r9zApEKoMiQ"
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

cte_code_analise = ["41240282270711000817570000002431121066906369","35240282270711002003570000003579841540070091",
                    "35240282270711002003570000003579861218403511","35240282270711002003570000003579821047920313",
                    "35240282270711002003570000003579851632249427","41240282270711000817570000002430751522096403",
                    "41240282270711000817570000002430741516732754","41240282270711000817570000002430731561250766",
                    "35240282270711002003570000003577291888780059","35240282270711002003570000003579561015147090"]

nf_codes = ["31240201998585002006550010000309981449332492","35240260857349002110550010000382172140127254",
"35240260857349002110550010000382242283620404","35240202481644000174550020002310701935901391",
"35231059275792000150550040031451371401756276","35240260857349001571550010003647871913884255",
"35231261381323000248550010004940561362246001","35231261381323000248550010004940701966766360",
"35231261381323000248550010004940601151707834","35240202481644000174550020002310051708549435",
"35240202481644000174550020002309421456401860","35240210795959000114550010000192861000192876",
"35240210795959000114550010000192871000192881","35240259275792000150550040032226731905072470",
"35240259275792000826550080014723211934609923"]

nf_analise = ["43240259275792009610550080011556321038981514","35240260857349001571550010003657951275705102",
              "35240259275792000826550080014724421109150581","35240259275792000826550080014724431116107952",
              "35240259275792000150550040032237521951607070","35240259275792000150550040032241481305100625",
              "35240259275792003680550080008537461441619875","35240260857349002381550010000028801984355153",
              "35240260857349002381550010000028791285329853","35240260857349002039550010000152731450557449",
              "35240260857349002039550010000152731450557449","35240260857349002039550010000153071716177375",
              "35240260857349002039550010000152701762813627","35240261064838008975550010003964401637706660"]

ric_code = ["MRKU1006305","MRKU1006305","MSDU2890536","HLXU8074573","MRKU4028524","FBIU5262167",
            "MEAS2023080","CAIU6894167","DFSU2887710","MEAS2023080","MRKU6189662"]

cte_rejeitado = ["35240282270711002003570000003582961082199180","35240282270711002003570000003580251589558165",
                "35240282270711002003570000003578221201432812","43240282270711000736570000001109821469581312",
                "35240282270711002003570000003580251589558165","43240282270711000736570000001109821469581312"]

ric_rejeitado = ["TCNU9854520","TCNU9854520","TCLU2510296","DRYU4212818"]

nf_rejeitada = ["43240202591818000585550010003130571313393512","35240259160069000125550040002684131217736644",
"35240260857349002110550010000389251923799386","35240260857349001571550010003657581454001149",
"35240259275792000826550080014726301763952969","35240200384369000145550020001396881499601369",
"35240260857349002110550010000389191659227266"]

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
        #print(getExternalId())
        
    
def enviaComprovante():
    with open("automacoes/testeApiComprova/payloads/comprovante.json","r+") as f:
        data = json.loads(f.read())
        #response = requests.post(URL_mandaComprovante.format(getExternalId()), json=data, headers=HEADERS)
    




def executaCenario(dadosViagens, dadosComprovantes,esperado,tipo,contador):
        criaViagem(dadosViagens[0], dadosViagens[1])
        for i in dadosComprovantes:
                setComprovante(i[0],i[1])
                enviaComprovante()
        time.sleep(8)
        #print(requests.get(URL_status.format(ultimoId),headers=HEADERS).json())
        print(str(contador)+"-  "+getExternalId(),f"{tipo} deve estar {esperado} e esta {requests.get(URL_status.format(ultimoId),headers=HEADERS).json()['status']}")
        updateExternalId()


#print(requests.get("https://comprova-matrix-homol.matrixcargo.com.br/viagens/237919",headers=HEADERS).json())
'''
for i in [i["id"] for i in requests.get("https://comprova-matrix-homol.matrixcargo.com.br/viagens?status=todos&limit=5000",headers=HEADERS).json()["itens"]]:
     r = requests.get(f"https://comprova-matrix-homol.matrixcargo.com.br/viagens/{i}",headers=HEADERS).json()
     print(r["rejeitada_em"] is not None and r["aprovada_em"] is not None, r["id_externo"])
'''





#executaCenario([["nf"],["35240208279845000170550030000277131211396842"]],[['testeVictor/nf0.jpeg','nf']],'rejeitado','nf',0)
#time.sleep(50)
#-----------------------------------------------------------------------------VALIDACAO DE STATUS------------------------------------------------------------------------------------
contador = 0
#print(len(cte_code_analise)+len(cte_codes)+len(nf_codes)+len(ric_code))

for index,i in enumerate(cte_codes):
    executaCenario([["cte"],[i]],[[f'cteAprovados/cte{index}.jpeg','cte']],'aprovado','cte',contador)#CTE QUE DEVEM APROVAR
    contador+=1

for index,i in enumerate(cte_code_analise):
    executaCenario([["cte"],[i]],[[f'cteAnalise/cte{index}.jpeg','cte']],'em analise','cte',contador)#CTE QUE DEVEM FICAR EM ANALISE
    contador+=1

for index,i in enumerate(nf_codes):
    executaCenario([["nf"],[i]],[[f'nf_aprova/nf{index}.jpeg','nf']],'aprovada','nf',contador)#NF QUE DEVEM APROVAR
    contador+=1

for index,i in enumerate(ric_code):
    executaCenario([["ric"],[i]],[[f'ricAprova/ric{index}.jpeg','ric']],'aprovado','ric',contador)#RIC QUE DEVEM APROVAR
    contador+=1

for index,i in enumerate(nf_analise):
    executaCenario([["nf"],[i]],[[f'nfAnalise/nf{index}.jpeg','nf']],'em analise','nf',contador)#NF QUE DEVEM FICAR EM ANALISE
    contador+=1

for index,i in enumerate(cte_rejeitado):
    executaCenario([["cte"],[i]],[[f'cteRejeitado/cte{index}.jpeg','cte']],'rejeitado','cte',contador)#CTE DEVEM ESTAR REJEITADOS
    contador+=1

for index,i in enumerate(nf_rejeitada):
    executaCenario([["nf"],[i]],[[f'nfRejeitada/nf{index}.jpeg','nf']],'rejeitada','nf',contador)#NF QUE DEVEM FICAR REJEITADAS
    contador+=1

for index,i in enumerate(ric_rejeitado):
    executaCenario([["ric"],[i]],[[f'ricRejeitado/ric{index}.jpeg','ric']],'rejeitado','ric',contador)#RIC DEVE ESTAR REJEITADOS
    contador+=1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






#---------------------------------------------------------------TESTES DE EXCLUSAO DE COMPROVANTES SOBRANDO---------------------------------------------------------------------------
executaCenario([["nf"],["42191157475747770000000000005747711457550477"]],[["nf_cardTeste.png","nf"]],'aprovada','n',contador) 

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
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------