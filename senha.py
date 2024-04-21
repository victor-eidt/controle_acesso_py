### Victor Gabriel Eidt e Giordano Diniz Serafini ###
import json
from getpass import getpass
import os
import time

with open("usuarios.txt", "r") as arquivo:
    linhas = arquivo.readlines()

usuarios = []
for linha in linhas:
    linha = linha.strip()
    campos = linha.split(",")
    usuarios.append((campos[0], campos[1]))
    
def carregar_permissoes():

    with open("permissoes.json", "r") as arquivo:
        return json.load(arquivo)
    
def salvar_permissoes(permissoes):
    
    with open("permissoes.json", "w") as arquivo:
        json.dump(permissoes, arquivo, indent=4)

def ler_tentativas():
    
    try:
        with open("tentativas.txt", "r") as arquivo:
            tentativas = arquivo.readlines()
            
    except FileNotFoundError:
        tentativas = []
        
    tentativas_limpa = []  # Cria uma lista vazia para armazenar os resultados
    for t in tentativas:   # Loop através de cada item na lista 'tentativas'
        tentativa_limpa = t.strip()  # Remove espaços em branco do início e do fim de cada item
        tentativas_limpa.append(tentativa_limpa)  # Adiciona o item processado à lista nova

    return tentativas_limpa

def registrar_tentativa(login):
    
    with open("tentativas.txt", "a") as arquivo:
        
        arquivo.write(f"{login}\n")
        
def menu_inicial():
    
    while True:
        try:
            selecao = int(input("What's the move?\n(1) Cadastrar\n(2) Autenticar\n(3) Sair\nDigite uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        match selecao:

            case 1:
                cadastro(usuarios)
                break
                
            case 2:
                aut(usuarios)
                break
                
            case 3:
                print("We out...")
                break

            
def cadastro(usuarios):
    
    permissoes = carregar_permissoes()
    
    for i in range(3):
        nome_usuario = input("Digite o seu nome de registro: ")
        senha_usuario = getpass("Digite a sua senha: ")
        confirmar_senha = getpass("Confirme sua senha: ")

        usuario_encontrado = False

        for nome, _ in usuarios:
            if nome == nome_usuario:
                usuario_encontrado = True
                break
            
        if senha_usuario == confirmar_senha and usuario_encontrado == False:
            
            with open("usuarios.txt", "a") as arquivo:
        
                arquivo.write(f"\n{nome_usuario},{senha_usuario}")
                
            permissoes[nome_usuario] = ["ler"]

            salvar_permissoes(permissoes)
        
            print("Cadastro realizado com sucesso!")
            
            break
        
        elif senha_usuario != confirmar_senha:
            print("Passwords didn't match! Try again")
                
        elif usuario_encontrado == True:
            print("Usuário já existe.")
            
def aut(usuarios):
    tentativas = ler_tentativas()

    for i in range(5):
        login = input("Digite o seu nome: ")
        senha = getpass("Digite a sua senha: ")

        tentativas_usuario = tentativas.count(login)

        if tentativas_usuario >= 5:
            print("Conta bloqueada temporariamente.")
            break

        if (login, senha) in usuarios:
            print(f"Seja bem vindo, {login}")
            menu_usuario(login)
            break
        
        else:
            print("Usuário Inexistente ou senha incorreta")
            registrar_tentativa(login)

        if i == 4:
            print("Limite de tentativas excedida, conta bloqueada temporariamente")
            
def menu_usuario(nome_usuario):
    
    while True:
        try:
            selecao = int(input("What's the move?\n(1) listar arquivos\n(2) criar arquivo\n(3) ler arquivo\n(4) escrever arquivo\n(5) apagar arquivo\n(6) executar arquivo\n(7) Desbloquear Usuário\n(8) sair\nDigite uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
    
        permissoes = carregar_permissoes()
        
        match selecao:
            
            case 1:
                
                diretorio_atual = os.getcwd()

                arquivos = os.listdir(diretorio_atual)
                print(arquivos)
                
            case 2:
                
                novo_arquivo = input("digite o nome do novo arquivo txt: ")
                
                with open(f"{novo_arquivo}.txt","+a"):
                    
                    print("Novo arquivo criado com sucesso")
                    
                time.sleep(1)
                    
            case 3:
                
                arquivo_selecionado = input("Qual arquivo você deseja ler? ")
                
                if 'ler' in permissoes[nome_usuario]:
                    print("Acesso permitido.....")
                elif 'ler' not in permissoes[nome_usuario]:
                    print("Acesso negado....")
                
                time.sleep(1)
                
            case 4:
                
                arquivo_selecionado = input("Qual arquivo você deseja escrever? ")
                
                if 'escrever' in permissoes[nome_usuario]:
                    print("Acesso permitido.....")
                elif 'escrever' not in permissoes[nome_usuario]:
                    print("Acesso negado....")
                
                time.sleep(1)
                    
            case 5:
                
                arquivo_selecionado = input("Qual arquivo você deseja apagar? ")
                
                if 'apagar' in permissoes[nome_usuario]:
                    print("Acesso permitido....")
                elif 'apagar' not in permissoes[nome_usuario]:
                    print("Acesso negado.....")
                
                time.sleep(1)
            
            case 6:
                
                arquivo_selecionado = input("Qual arquivo você deseja executar? ")
                
                if 'exec' in permissoes[nome_usuario]:
                    print("Acesso permitido.....")
                elif 'exec' not in permissoes[nome_usuario]:
                    print("Acesso negado.....")
                    
                time.sleep(1)
            
            case 7:
                
                if 'admin' in permissoes[nome_usuario]:
                    unblockuser = input("tem certeza que deseja desbloquear todos usuários bloqueados? s/n")
                    
                    if unblockuser == 's' or unblockuser == 'S':
                        with open("tentativas.txt","w") as arquivo:
                            arquivo.write("")
                    
                    elif unblockuser == 'n' or unblockuser == 'N':
                        continue
                elif 'admin' not in permissoes[nome_usuario]:
                    print("apenas admins têm acesso à esta feature!")
                
                time.sleep(1)
                    
            case 8:
                print("We out...")
                time.sleep(1)
                break
              
menu_inicial()