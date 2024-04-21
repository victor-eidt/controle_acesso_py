import json

def carregar_json():
    with open("teste.json","r") as permissoes:
        
        return json.load(permissoes)

permissoes = carregar_json()