import yaml

class MontaYaml:
    def __init__(self) -> None:
        pass

    def monta(self, data):
        conteudo_yaml = """\
appId: com.example.app
---
"""
        for  i in data:
            conteudo_yaml += i+"\n"

        arquivo = 'automacoes/testesYaml/arquivo.yaml'
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo_yaml)

        return conteudo_yaml


#MontaYaml().monta(['a','b'])
