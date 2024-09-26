import textwrap

def deposito(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"       Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")

    else:
            print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"       Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def saque_especial(saldo, valor, extrato, limite_especial, numero_saques_especiais, LIMITE_SAQUES_ESPECIAIS):
    # valor = float(input("Informe o valor do saque especial: "))

    excedeu_limite_especial = valor > limite_especial
    excedeu_saques_especial = numero_saques_especiais >= LIMITE_SAQUES_ESPECIAIS
    excedeu_saldo_especial = valor > saldo

    if excedeu_saldo_especial:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite_especial:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques_especial:
        print("\nOperação falhou! Número máximo de saques especiais excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"       Saque especial: R$ {valor:.2f}\n"
        numero_saques_especiais += 1
        print("\nSaque especial realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")


    return saldo, extrato, numero_saques_especiais

def mostrar_extrato(saldo, /,*,extrato):
    print("\n==================== EXTRATO ====================")
    print("    Histórico de saques e depósitos")
    print("         Não foram realizadas movimentações." if not extrato else extrato)
    print(f"   \n    Saldo: R$ {saldo:.2f}")
    print("==================================================")
    return None

def info(menu):
    # Se o extrato estiver vazio, informa que
    # não foram realizadas movimentações
    
    while True:
        menu = """


        [1] Depósito
        [2] Saque
        [3] Saque especial
        [4] Extrato
        [0] Sair

        > """
        print("Selecione uma opção que você deseja informações:")
        opcao = input(menu)

        if opcao == "1":
            print("Você não tem limite de depósitos diários.")
        elif opcao == "2":
            print("Você tem 3 saques por dia com o limite de R$ 500.00 por saque.")
        elif opcao == "3":
            print("Você tem 1 saque especial por dia com o limite de R$ 1500.00 por saque.")
        elif opcao == "4":
            print("Clique em Extrato para ver o histórico de saques e depósitos e o saldo atual.")
        elif opcao == "5":
            print("Cadastre um usuário adicionando as informações: nome, nascimentom, cpf, email e endereço.")
        elif opcao == "6":
            print("Cadastre uma conta adicionando o seu cpf. Somente cpf que já estejam cadastrados podem abrir uma conta.")
        elif opcao == "7":
            print("Mostra os Usuários Cadastrados")     
        elif opcao == "8":
            print("Mostra as contas Cadastradas")
        elif opcao == "0":
            break

    return None

def verifica_cpf(lista_usuarios, cliente):
    while True:
        cpf = input("CPF do cliente: ").replace('.', '').replace('-', '')
        if not cpf:
            print("CPF inválido. Tente novamente.")
            continue

        if lista_usuarios:
            for usuario in lista_usuarios:
                if "cpf" in usuario and usuario["cpf"] == cpf:
                    print("CPF ja existente. Tente novamente.")
                    break
            else:
                cliente["cpf"] = cpf
                break
        else:
            cliente["cpf"] = cpf
            break
        
def cadrastrar_usuario(lista_usuarios):
    cliente = {}
    cliente["nome"] = input("Nome do cliente: ")
    cliente["nascimento"] = (input("Data de nascimento: "))
    verifica_cpf(lista_usuarios, cliente)
    cliente["email"] = input("Email do cliente: ")
    cliente["endereço"] = input("Endereço do cliente: ")
    lista_usuarios.append(cliente)
    print("\nUsuário cadastrado com sucesso!")
    return  lista_usuarios

def verifica_cpf_conta(conta, lista_usuarios):
    while True:
        cpf = input("CPF do cliente: ").replace('.', '').replace('-', '')
        if not cpf:
            print("CPF inválido. Tente novamente.")
            continue

        if lista_usuarios:
            for usuario in lista_usuarios:
                if "cpf" in usuario and usuario["cpf"] == cpf:
                    if "nome" in usuario:
                        conta["titular"] = usuario["nome"]
                    else:
                        print("Erro: Usuário sem nome. Tente novamente.")
                        continue
                    break
            else:
                print("CPF inválido. Tente novamente.")
                continue
        else:
            print("Erro: A lista de usuários está vazia. Tente novamente.")
            continue
        break

def cadrastrar_conta(lista_contas, lista_usuarios):
    conta = {}
    conta["agencia"] = "0001"
    conta["numero"] = len(lista_contas) + 1
    verifica_cpf_conta(conta, lista_usuarios)
    lista_contas.append(conta)
    print("\nConta criada com sucesso!")
    return lista_contas

def mostrar_usuarios(lista_usuarios):

    print("==================== CLIENTES CADASTRADOS ====================")
    print(f"                     {lista_usuarios}                        ")

def mostrar_contas(lista_contas):
    for conta in lista_contas:
        linha = f"""\
        Agência:\t{conta["agencia"]}
        Conta:\t{conta["numero"]}
        Titular:\t{conta["titular"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    menu = """
    [1] Depósito
    [2] Saque
    [3] Saque especial
    [4] Extrato
    [5] Cadastrar usuário
    [6] Cadastrar conta
    [7] Mostrar usuários
    [8] Mostrar contas
    [9] Informações
    [0] Sair

    """

    
    saldo = 0
    limite_especial = 1500
    LIMITE_SAQUES_ESPECIAIS = 1
    numero_saques_especiais = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    lista_usuarios = []
    lista_contas = []

    while True:

        print("\nSelecione uma operação:")
        opcao = input(menu)

        if opcao == "1":
            valor = float(input("\nQuanto deseja depositar? "))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("\nQuanto deseja sacar? "))
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES= LIMITE_SAQUES)

        elif opcao == "3":
            valor = float(input("\nQuanto deseja sacar? "))
            saldo, extrato, numero_saques_especiais = saque_especial(saldo, valor, extrato, limite_especial, numero_saques_especiais, LIMITE_SAQUES_ESPECIAIS)

        elif opcao == "4":
            mostrar_extrato(saldo, extrato = extrato )

        elif opcao == "5":
            lista_usuarios = cadrastrar_usuario(lista_usuarios)

        elif opcao == "6":
            lista_contas = cadrastrar_conta(lista_contas, lista_usuarios)
        
        elif opcao == "7":
            mostrar_usuarios(lista_usuarios)
        
        elif opcao == "8":
            mostrar_contas(lista_contas)

        elif opcao == "9":
            info(menu)

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        

main()
    

    