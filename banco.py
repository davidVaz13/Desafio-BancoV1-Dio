menu = """

    [1] Depósito
    [2] Saque
    [3] Saque especial
    [4] Extrato
    [5] Informações
    [0] Sair

=> """

saldo = 0
limite_especial = 1500
LIMITE_SAQUES_ESPECIAIS = 1
numero_saques_especiais = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print("\nSelecione uma operação:")

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"       Depósito: R$ {valor:.2f}\n"

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

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

        else:
            print("\nOperação falhou! O valor informado é inválido.")
    
    elif opcao == "3":
        valor = float(input("Informe o valor do saque especial: "))

        excedeu_saldo_especial = valor > saldo
        excedeu_limite_especial = valor > limite_especial
        excedeu_saques_especial = numero_saques_especiais >= LIMITE_SAQUES_ESPECIAIS

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
        else:
            print("\nOperação falhou! O valor informado é inválido.")


    elif opcao == "4":
        print("\n==================== EXTRATO ====================")
        print("    Histórico de saques e depósitos")
        print("         Não foram realizadas movimentações." if not extrato else extrato)
        print(f"   \n    Saldo: R$ {saldo:.2f}")
        print("==================================================")

    elif opcao == "5":
       while True:
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
            elif opcao == "0":
                break

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")