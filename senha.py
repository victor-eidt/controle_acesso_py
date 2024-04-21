### Victor Gabriel Eidt e Giordano Diniz Serafini ###

from getpass import getpass

with open("usuarios.txt", "r") as arquivo:
    linhas = arquivo.readlines()

usuarios = []
for linha in linhas:
    linha = linha.strip()
    campos = linha.split(",")
    usuarios.append((campos[0], campos[1]))

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
    
    selecao = int(input("What's the move?\n(1) Cadastrar\n(2) Autenticar\n(3) Sair\nDigite uma opção: "))
    
    match selecao:

        case 1:
            cadastro(usuarios)
            
        case 2:
            aut(usuarios)
            
        case 3:
            exit
            
def cadastro(usuarios):
    
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
            menu_usuario()
            break
        
        else:
            print("Usuário Inexistente ou senha incorreta")
            registrar_tentativa(login)

        if i == 4:
            print("Limite de tentativas excedida, conta bloqueada temporariamente")
            
def menu_usuario():
    
    selecao = input("What's the move?\n(1) listar arquivos\n(2) criar arquivo\n(3) ler arquivo\n(4) excluir arquivo\n(5) executar arquivo\n(6) Desbloquear Usuário\n(7) sair\nDigite uma opção: ")
    
menu_inicial()