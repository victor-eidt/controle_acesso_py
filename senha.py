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
        
    return [t.strip() for t in tentativas]

def registrar_tentativa(login):
    with open("tentativas.txt", "a") as arquivo:
        arquivo.write(f"{login}\n")

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
            break
        else:
            print("Usuário Inexistente ou senha incorreta")
            registrar_tentativa(login)

        if i == 4:
            print("Limite de tentativas excedida, conta bloqueada temporariamente")

aut(usuarios)