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
            conteudo_yaml += "\n"+i

        arquivo = 'automacoes/testesYaml/arquivo.yaml'
        with open(arquivo, 'w') as f:
            f.write(conteudo_yaml)

        return conteudo_yaml


MontaYaml().monta(['a','b'])
