import json
import pprint
import getpass


def cadastrar():
    print("\n- Cadastro de usuário")

    print("Digite os dados do novo usuário: ")
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)

    for usuario in usuarios:
        if usuario["username"] == username:
            print("Nome de usuário já existe!")
            return
        else:
            usuario = usuarios + [{
                "username": username,
                "password": password
            }]
            with open("usuarios.json", "w") as file:
                json.dump(usuario, file)

            with open("base_atorizacao.json", "r") as base:
                base = json.load(base)

            usuario = base + [{
                "username": username,
                "permissao": {
                    "arquivo": "nenhum",
                    "leitura": False,
                    "escrita": False,
                    "execucao": False,
                    "exclusao": False,
                    "criar": False
                }
            }]

            with open("base_atorizacao.json", "w") as base:
                base.write(json.dumps(usuario))

            print("Usuário cadastrado com sucesso!")
            break


def autenticar():
    print("\n- Autenticação de usuário")

    username = input("\nNome de usuário: ")
    password = input("Senha:")

    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)

    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            print("Usuário autenticado com sucesso! ")
            menu_autenticado(username)
            return
    print("Usuário ou senha inválidos!")
    return


def menu_autenticado(username):
    while True:
        print("\nComandos disponíveis: ")
        print("1- Listar arquivos")
        print("2- Criar arquivo")
        print("3- Ler arquivo")
        print("4- Excluir arquivo")
        print("5- Executar arquivo")
        print("6- Voltar")

        opcao = input("\n- Escolha uma opção: ")

        with open("base_atorizacao.json", "r") as base:
            base = json.load(base)
            while True:
                if opcao == "1":
                    for arquivo in base:
                        print(arquivo["permissao"]["arquivo"])
                    break    
                elif opcao == "2":
                    arquivoInput = input("Digite o nome do arquivo: ")      
                    for arquivo in base:
                        if (arquivo["username"] == username and arquivo["permissao"]["criar"] == True) and arquivo["permissao"]["arquivo"] == arquivoInput:
                            print("Acesso concedido!")
                            break
                        elif (arquivo["username"] == username and arquivo["permissao"]["criar"] == False) or (arquivo["username"] == username and arquivo["permissao"]["arquivo"] != arquivoInput):
                            print("Arquivo inexistente ou acesso negado!")
                    break        
                elif opcao == "3":
                    arquivoInput = input("Digite o nome do arquivo: ")      
                    for arquivo in base:
                        if (arquivo["username"] == username and arquivo["permissao"]["leitura"] == True) and arquivo["permissao"]["arquivo"] == arquivoInput:
                            print("Acesso concedido!")
                            break
                        elif (arquivo["username"] == username and arquivo["permissao"]["leitura"] == False) or (arquivo["username"] == username and arquivo["permissao"]["arquivo"] != arquivoInput):
                            print("Arquivo inexistente ou acesso negado!")
                    break        
                elif opcao == "4":
                    arquivoInput = input("Digite o nome do arquivo: ")      
                    for arquivo in base:
                        if (arquivo["username"] == username and arquivo["permissao"]["exclusao"] == True) and arquivo["permissao"]["arquivo"] == arquivoInput:
                            print("Acesso concedido!")
                            break
                        elif (arquivo["username"] == username and arquivo["permissao"]["exclusao"] == False) or (arquivo["username"] == username and arquivo["permissao"]["arquivo"] != arquivoInput):
                            print("Arquivo inexistente ou acesso negado!")
                    break        
                elif opcao == "5":
                    arquivoInput = input("Digite o nome do arquivo: ")      
                    for arquivo in base:
                        if (arquivo["username"] == username and arquivo["permissao"]["execucao"] == True) and arquivo["permissao"]["arquivo"] == arquivoInput:
                            print("Acesso concedido!")
                            break
                        elif (arquivo["username"] == username and arquivo["permissao"]["execucao"] == False) or (arquivo["username"] == username and arquivo["permissao"]["arquivo"] != arquivoInput):
                            print("Arquivo inexistente ou acesso negado!")
                    break        
                elif opcao == "6":
                    return
                else:
                    print("Opção inválida!")


def listar_arquivos():
    arquivo = input("Digite o nome do arquivo: ")

    with open("base_atorizacao.json", "r") as base:
        base = json.load(base)

    for arquivo in base:
        if arquivo == arquivo:
            print("\n- Arquivo encontrado!\n")
            pprint.pprint(arquivo)
            break
        else:
            print(f"Arquivo {arquivo} não encontrado!")
            break


print("=-"*20)
print("Bem-vindo ao sistema de autenticação!")
print("=-"*20)

while True:
    opcao = input("1- Cadastrar\n2- Autenticar\n3- Sair\nEscolha uma opção: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        autenticar()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
