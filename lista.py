#Desafio 10 // Lista telefonica
from os import system

senha = 123
nome = []
num = []

def novo_contato():
    system("cls")
    nome1 = input("Digite o nome do contato:").strip().lower()
    nome.append(nome1)
    num1 = int(input("Digite um numero:"))
    num.append(num1)
    print(nome)
    print(num)
    print("Contato adicionado com sucesso.")

def editar():
    system("cls")
    nome_editar = input("Digite o nome do contato que deseja editar: ").strip().lower()
    if nome_editar in nome:
        indice = nome.index(nome_editar)
        novo_nome = input("Digite o novo nome do contato: ").strip().lower()
        novo_numero = int(input("Digite o novo número de telefone: "))
        nome[indice] = novo_nome
        num[indice] = novo_numero
        print(nome)
        print(num)
        print("Contato editado com sucesso.")
    else:
        print("Contato não encontrado.")
    
def remover():
    system("cls")
    nome_remover = input("Digite o nome do contato que deseja remover: ")
    if nome_remover in nome:
        indice = nome.index(nome_remover)
        nome.pop(indice)
        num.pop(indice)
        print("Contato removido com sucesso.")
    else:
        print("Contato não encontrado.")

def pesquisa():
    system("cls")
    nome_pesquisa = input("Digite o nome do contato que deseja pesquisar: ")
    if nome_pesquisa in nome:
        indice = nome.index(nome_pesquisa)
        print("Contato encontrado:")
        print("Nome: ", nome[indice])
        print("Número: ", num[indice])
    else:
        print("Contato não encontrado.")

def lista():  
        system("cls")
        print(nome)
        print(num)


# Funcionamento
while True:
    senha1 = int(input("Digite a senha para ter acesso:"))
    if senha == senha1:
        print("Senha correta.")
        print("LISTA TELEFÔNICA")
        print("""    [0] Sair
    [1] Novo contato
    [2] Editar contato
    [3] Pesquisar contato
    [4] Apagar contato
    [5] Lista de contatos""")
        x = int(input("Faça sua escolha:"))

        if x == 1:
            novo_contato()

        elif x == 2:
            editar()

        elif x == 4:
            remover()

        elif x == 3:
            pesquisa()

        elif x == 5:
            lista()

        elif x == 0:
            print("Fim do programa.")
            break
        else:
            print("Digite uma opção válida.")
    else:
        print("Senha incorreta.")