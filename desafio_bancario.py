menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print("Falha na operação. Informe um valor válido.")

    elif opcao == "s":
        valor = float(input("Informe o valor que desejar sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Falha na operação. Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação. O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha na operação. Número máximo de saques já atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1

        else:
            print("Falha na operação. Informe um valor válido")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Selecione novamente a operação desejada.")

