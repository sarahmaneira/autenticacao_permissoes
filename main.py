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
                    "leitura": False,
                    "escrita": False,
                    "execucao": False
                }
            }] 
                
            with open("base_atorizacao.json", "w") as base:
               base.write(json.dumps(usuario))
                
            print("Usuário cadastrado com sucesso!")
            break
    
def autenticar():
    print("\n- Autenticação de usuário")

    username = input("\nNome de usuário: ")
    password =  input("Senha:")
    
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)
        
    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            print("Usuário autenticado com sucesso! ")
            menu_autenticado()
            return
    print("Usuário ou senha inválidos!")

def menu_autenticado():
    print("Comandos disponíveis: ")
    print("1- Listar arquivos")
    print("2- Criar arquivo")
    print("3- Ler arquivo")
    print("4- Excluir arquivo")
    print("5- Executar arquivo")
    print("6- Sair")
    
    opcao = input("\n- Escolha uma opção: ")
    
    if opcao == "1":
        listar_arquivos()
    # elif opcao == "2":
    #     criar_arquivo()
    # elif opcao == "3":
    #     ler_arquivo()
    # elif opcao == "4":
    #     excluir_arquivo()
    # elif opcao == "5":
    #     executar_arquivo()
    # elif opcao == "6":
    #     print("Saindo...")
    #     break
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
    options = input("1- Cadastrar\n2- Autenticar\n3- Sair\nEscolha uma opção: ")
    if options == "1":
        cadastrar()
    elif options == "2":
        autenticar()
        
    elif options == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        
          




        
        
        
    
    
    