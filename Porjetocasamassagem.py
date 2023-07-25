# CASA DE MASSAGENS 

from os import system #Biblioteca que permite utilizar a função que limpa o terminal 

clientes = {} #Dicionario para os clientes
massagem = {}
tipo_massagem = {}

## de onde? trcho retirado do CHAT_GPT
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "") #Troca os pontos e traços por espaços vazios
    if len(cpf) != 11: #Confere se o CPF tem 11 digitos
        return False
    elif cpf == cpf[0] * 11: #Verifica se todos os numeros não são iguais 
        return False

#Calcula o primeiro digito verificador (utilizando uma fórmula que envolve a soma dos produtos dos dígitos do CPF pelos pesos 10, 9, 8, ..., 2. O resultado é dividido por 11 e o resto é obtido. Se o resto for igual a 10, o dígito verificador é considerado como 0. Se o dígito verificador calculado for diferente do nono dígito do CPF, a função retorna False.)
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    elif digito1 != int(cpf[9]):
        return False

#Calcula o segundo digito verificador (O segundo dígito verificador é calculado de forma semelhante, mas os pesos utilizados são 11, 10, 9, ..., 2. O resultado também é dividido por 11 e o resto é obtido. Se o resto for igual a 10, o dígito verificador é considerado como 0. Se o dígito verificador calculado for diferente do décimo dígito do CPF, a função retorna False.)
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    elif digito2 != int(cpf[10]):
        return False

    return True


def menu():
    system("cls || clear") #Função que limpa o terminal "CLS" limpa para Windows e "Clear" para Linux
    print("""   ======CASA DE MASSAGENS======
    [1] Menu de Clientes
    [2] Agendamento de massagens
    [3] Listar massagens agendadas
    [4] Gerenciar tipos de massagens 
    [5] Parar programa
    [0] Informações sobre o desenvolvedor
    =============================""")
    x1 = (input("Digite a opção:"))
    return x1


def cadastro():
    system("cls || clear")
    print("""    ================
    MENU DE CLIENTES
    ================
    [1] Cadastrar novo cliente
    [2] Pesquisar cliente
    [3] Editar/Excluir cliente
    [4] Listar clientes
    [5] Voltar ao menu principal""")
    x = (input("Digite a opção:"))
    return x


def massagens():
    system("cls || clear")
    print("""    =========
    Massagens
    =========
    [1] Agendar massagem
    [2] Cancelar massagem
    [3] Voltar ao menu principal
    """)
    x = (input("Digite a opção:"))
    return x


def gerenciar_massagem():
    system("cls || clear")
    print("=============================")
    print("Gerenciar tipos de massagens")
    print("=============================")
    print("[1] Cadastrar novo tipo de massagem")
    print("[2] Excluir algum tipo de massagem")
    print("[3] Tipos de massagens ")
    print("[4] Voltar ao menu principal")
    x = (input("Digite a opção:"))
    return x


def info_dev():
    system("cls || clear")
    print("============================")
    print("Informações do Desenvolvedor")
    print("============================")
    print("")
    print("Gabriel Ygor Canuto")
    print("Aluno do curso de Sistemas de Informação na UFRN")
    print("Trabalho referente a terceira avaliação da disciplina de ALGORITMOS E LÓGICA DE PROGRAMAÇÃO ")
    input("Enter para continuar")


def novo_tipo_mass():
    system("cls || clear")
    tipo = input("Digite o tipo de massagem que deseja ofertar:").strip().lower() # Remove os espaçoes e deixa tudo em minusculo, respectivamente
    preco = input("Digite o preço sugerido para a massagem:").strip().lower()
    resumo = input("Explique de forma resumida como a massagem funciona:").strip().lower()
    tipo_massagem[tipo] = {"preço": preco, "resumo": resumo} #Adiciona as informações do Tipo de massagem no dicionario
    for tipo, dados in tipo_massagem.items(): #Cria um laço e da Print nas informações salvas
        print("========================")
        print("Tipo da massagem:", tipo)
        print("Preço sugerido:", dados['preço'])
        print("Resumo da massagem:", dados['resumo'])
        print("========================")
    input("Enter para continuar")


def excluir_tipo_mass():
    system("cls || clear")
    tipo = input("Digite o nome da massagem que deseja excluir:")
    del tipo_massagem[tipo] #Da DEL no Tipo da massagem e nas informações vinculadas a essa KEY
    print("Massagem removida com sucesso do catálogo!")


def lista_tipo_mass():
    system("cls || clear")
    print("=== Tipos de Massagens ===")
    for tipo, dados in tipo_massagem.items(): #Cria um laço para conseguir listar todos os tipos de massagens
        print("Tipo da massagem:", tipo)
        print("Preço:", dados['preço'])
        print("Resumo:", dados['resumo'])
        print("========================")
    input("Enter para continuar")


def cadastro_novo():
    system("cls || clear")
    print("Cadastro para novo cliente.")
    nome = input("Nome do cliente:").strip().lower()                             #CPF de teste = 123.456.789-09
    telefone = input("Digite o telefone do cliente:").strip()
    cpf = input("Digite o CPF do cliente (somente números):").strip()
    if validar_cpf(cpf):
        clientes[cpf] = {'nome': nome, 'telefone': telefone} #Se o CPF for valido adicinona as informações dos clientes no dicionario
        print("Cliente cadastrado com sucesso!")
    else:
        print("CPF inválido!")

    input("Enter para continuar")


def pesquisar():
    system("cls || clear")
    cpf = input("Digite o CPF do cliente para pesquisa (somente números):").strip()
    if cpf in clientes: #Confere se o CPF existe no dicionario
        print("Nome:", clientes[cpf]['nome']) #Se existir da print nas informações
        print("CPF:", cpf)
        print("Telefone:", clientes[cpf]['telefone'])
    else:
        print("CPF não encontrado")
    input("Enter para continuar")


def editar_excluir():
    system("cls || clear")
    cpf = input("Digite o CPF do cliente para editar/excluir (somente números):").strip()
    if cpf in clientes:  #Confere se o CPF existe no dicionario
        print("O que você deseja fazer com o cliente de CPF", cpf + "?")
        print("[1] Editar informações")
        print("[2] Excluir cliente")
        opcao = input("Digite a opção:")
        if opcao == "1":
            nome = input("Digite o novo nome do cliente:").strip()
            telefone = input("Digite o novo telefone do cliente:").strip()
            clientes[cpf]['nome'] = nome #Substitui as informações antigas pelas novas
            clientes[cpf]['telefone'] = telefone
            print("Informações atualizadas com sucesso!")
        elif opcao == "2":
            del clientes[cpf]  #Deleta as informações vinculadas ao CPF
            print("Cliente excluído com sucesso!")
        else:
            print("Opção inválida!")
    else:
        print("CPF não encontrado")
    input("Enter para continuar")


def listar_clientes():
    system("cls || clear")
    print("=== Lista de Clientes ===")
    for cpf, dados in clientes.items(): #Cria uma laço para listar todos os clientes
        print("CPF:", cpf)
        print("Nome:", dados['nome'])
        print("Telefone:", dados['telefone'])
        print("========================")
    input("Enter para continuar")


def agendar_massagem():
    system("cls || clear")
    print("Agendamento de Massagem.")
    cpf = input("Digiteo CPF do cliente (somente números):").strip()
    if cpf in clientes: #Confere se o cliente existe no sistemas
        lista_tipo_mass()
        tipo_massagem = input("Digite o tipo de massagem:").strip().lower()
        horario = input("Digite o horário da massagem:").strip()
        data = input("Digite a data da massagem:").strip()
        if cpf in massagem:
            massagem[cpf].append({'massagem': tipo_massagem, 'horario': horario, 'data': data}) #Adiciona as informaçoes ao dicionario
        else:
            massagem[cpf] = [{'massagem': tipo_massagem, 'horario': horario, 'data': data}]
        print("Massagem agendada com sucesso!")
    else:
        print("CPF não encontrado")
    input("Enter para continuar")


def cancelar_massagem():
    system("cls || clear")
    print("Cancelar Massagem.")
    cpf = input("Digite o CPF do cliente:").strip()
    if cpf in massagem:  #Confere se o cliente existe no sistemas
        print("=== Lista de Massagens Agendadas ===")
        for i, agendamento in enumerate(massagem[cpf]): #Adiciona um contador nas massagens
            print(f"Massagem {i+1}:")
            print("Tipo de Massagem:", agendamento['massagem'])
            print("Horário:", agendamento['horario'])
            print("Data:", agendamento['data'])
            print("========================")
        opcao = int(input("Digite o número da massagem a ser cancelada:"))
        if opcao > 0 and opcao <= len(massagem[cpf]): #Verificar se a opção é maior que 0 e menor/igual ao numero demassagens agendadas
            massagem[cpf].pop(opcao - 1) #Menos 1 porque a massagem é removida pelo indece (que começa com 0) e o contador começa com 1
            print("Massagem cancelada com sucesso!")
        else:
            print("Opção inválida!")
    else:
        print("CPF não encontrado ou não possui massagens agendadas")
    input("Enter para continuar")


def listar_massagens():
    system("cls || clear")
    print("=== Lista de Massagens Agendadas ===")
    for cpf, agendamentos in massagem.items():
        print("CPF:", cpf)
        for agendamento in agendamentos:
            print("Tipo de Massagem:", agendamento['massagem'])
            print("Horário:", agendamento['horario'])
            print("Data:", agendamento['data'])
            print("========================")
    input("Pressione Enter para continuar...")


def salvar_dados():
    arq = open("clientes.txt", "w") #Abre um arquivo para salvar os dados dos clientes
    for cpf, dados in clientes.items():#Cria uma laço para conferir os dados
        arq.write(f"CPF: {cpf}\n") #Escreve os dados do dicionario no arquivo TXT
        arq.write(f"Nome: {dados['nome']}\n")
        arq.write(f"Telefone: {dados['telefone']}\n")
        arq.write("========================\n")
    arq.close() #Fecha o arquivo

    arq = open("tiposmassagem.txt", "w") #Repete o mesmo processo de cima
    for tipo, dados in tipo_massagem.items():
        arq.write(f"Tipo: {tipo}\n")
        arq.write(f"Preço: {dados['preço']}\n")
        arq.write(f"Resumo: {dados['resumo']}\n")
        arq.write("========================\n")
    arq.close()

    arq = open("massagens.txt", "w") #Repete o mesmo processo de cima
    for cpf, agendamentos in massagem.items():
        arq.write(f"CPF: {cpf}\n")
        for i, agendamento in enumerate(agendamentos):
            arq.write(f"Massagem: {agendamento['massagem']}\n")
            arq.write(f"Horário: {agendamento['horario']}\n")
            arq.write(f"Data: {agendamento['data']}\n")
            arq.write("========================\n")
    arq.close()


def carregar_dados(): 
    try:
        arq = open("clientes.txt", "r") #Abre o arquivo
        lines = arq.readlines() #le as linhas do arquivo
        arq.close() # Fecha o arquivo depois de ter lido as linhas

        cpf_cliente = "" #Cria as 3 variaveis vazias 
        nome = ""
        telefone = ""

        for line in lines: #Cria um laço
            line = line.strip() #Remove os espaços das linhas
            if line.startswith("CPF:"): #Le a linha que começa com CPF
                cpf_cliente = line.replace("CPF: ", "") #Troca o CPF que tem no arquivo TXT pela variavel vazia criada acima
            elif line.startswith("Nome:"):
                nome = line.replace("Nome: ", "")
            elif line.startswith("Telefone:"):
                telefone = line.replace("Telefone: ", "")
            elif line == "========================":
                clientes[cpf_cliente] = {'nome': nome, 'telefone': telefone} #Atualiza o dicionario

        arq = open("tiposmassagem.txt", "r") #Repete o mesmo processo do codigo acima 
        lines = arq.readlines()
        arq.close()

        tipo = ""
        preco = ""
        resumo = ""

        for line in lines:
            line = line.strip()
            if line.startswith("Tipo:"):
                tipo = line.replace("Tipo: ", "")
            elif line.startswith("Preço:"):
                preco = line.replace("Preço: ", "")
            elif line.startswith("Resumo:"):
                resumo = line.replace("Resumo: ", "")
            elif line == "========================":
                tipo_massagem[tipo] = {'preço': preco, 'resumo': resumo}

        arq = open("massagens.txt", "r") #Repete o mesmo processo do codigo acima 
        lines = arq.readlines()
        arq.close()

        cpf_cliente = ""
        tipo_massagem_cliente = ""
        horario = ""
        data = ""

        for line in lines:
            line = line.strip()
            if line.startswith("CPF:"):
                cpf_cliente = line.replace("CPF: ", "")
                massagem[cpf_cliente] = []
            elif line.startswith("Massagem"):
                tipo_massagem_cliente = line.replace("Massagem: ", "")
            elif line.startswith("Horário:"):
                horario = line.replace("Horário: ", "")
            elif line.startswith("Data:"):
                data = line.replace("Data: ", "")
            elif line == "========================":
                massagem[cpf_cliente].append({'massagem': tipo_massagem_cliente, 'horario': horario, 'data': data})

    except FileNotFoundError:
        pass


while True:
    carregar_dados() #Carrega os dados assim que inicia o programa
    op = menu()

    if op == '1':
        while True:
            op2 = cadastro()

            if op2 == '1':
                cadastro_novo()
            elif op2 == '2':
                pesquisar()
            elif op2 == '3':
                editar_excluir()
            elif op2 == '4':
                listar_clientes()
            elif op2 == '5':
                break
            elif op == "":
                pass
            else:
                print("Opção inválida!")

    elif op == '2':
        while True:
            op3 = massagens()

            if op3 == '1':
                agendar_massagem()
            elif op3 == '2':
                cancelar_massagem()
            elif op3 == '3':
                break
            elif op == "":
                pass
            else:
                print("Opção inválida!")

    elif op == '3':
        listar_massagens()

    elif op == '4':
        while True:
            op4 = gerenciar_massagem()

            if op4 == '1':
                novo_tipo_mass()
            elif op4 == '2':
                excluir_tipo_mass()
            elif op4 == '3':
                lista_tipo_mass()
            elif op4 == '4':
               break
            elif op4 == "":
                pass
            else:
                print("Opção inválida!")

    elif op == "5":
        salvar_dados() #Quando fechar o programa salva os dados contidos no dicionario
        print("Programa encerrado!")
        break
    elif op == '0':
        info_dev()

    else:
        print("Opção inválida!")

#Resumo de algumas massagens para teste

#Massagem Sueca: Relaxa o corpo, alivia a tensão muscular e melhora a circulação sanguínea, utilizando movimentos suaves, deslizantes e firmes ao longo dos músculos.

#Massagem Tailandesa: Originária da Tailândia, combina alongamentos assistidos, pressões rítmicas e acupressão para promover o alívio do estresse, flexibilidade muscular e um fluxo energético equilibrado.

#Massagem Desportiva: Especialmente para atletas e pessoas envolvidas em atividades físicas intensas, ajuda no preparo e recuperação muscular. Utiliza técnicas de fricção profunda, alongamentos e liberação miofascial para melhorar a flexibilidade, reduzir lesões e aliviar dores musculares.

#Massagem Shiatsu: Originária do Japão, envolve a aplicação de pressão nos pontos de acupuntura do corpo, utilizando os dedos, as mãos e até mesmo os cotovelos. Busca equilibrar o fluxo de energia vital, aliviar a tensão e promover bem-estar geral.

#Massagem com Pedras Quentes: Utiliza pedras lisas e aquecidas, colocadas sobre o corpo, combinadas com movimentos suaves. O calor das pedras relaxa os músculos, alivia o estresse e proporciona conforto e equilíbrio.

#Massagem Reflexologia: Baseia-se no princípio de pontos reflexos nos pés, mãos e orelhas que correspondem a órgãos e sistemas do corpo. Ao aplicar pressão nessas áreas, estimula a saúde e o equilíbrio do corpo, aliviando tensões e promovendo relaxamento