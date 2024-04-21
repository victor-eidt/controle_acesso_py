import json
import os

def carregar_permissoes():

    with open("permissoes.json", "r") as arquivo:
        return json.load(arquivo)
        
permissoes = carregar_permissoes()

print(permissoes["enio"])
print(permissoes)

if 'ler' in permissoes["enio"]:
    print("enio tem permissão pra escrever")

elif 'ler' not in permissoes["enio"]:
    print("enio não tem permissão")
    
else:
    print("não caiu nos ifs, erro")
    
diretorio_atual = os.getcwd()

arquivos = os.listdir(diretorio_atual)
print(arquivos)