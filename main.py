menu = '''
Escolha a opção desejada:
1 - Depósito
2 - Saque
3 - Extrato
0 - Sair

=>> '''

saldo = 0.00
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        deposito = float(input("Valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"\n Depósito +R$ {deposito:.2f}\n"
            print(f"\nDepósito de R$ {deposito:.2f} concluído.\n\nNovo saldo R$ {saldo:.2f}\n")
            continue
        else:
            print("\n\nERRO: Valor precisa ser maior que ZERO.\n")
            continue

    if opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            retirada = float(input("Valor de retirada: "))
            if retirada <= 0:
                print("\n\nERRO: Valor precisa ser maior que ZERO.\n")
                continue
            elif retirada > limite:
                print(f"\n\nERRO: Seu limite para saque é de R$ {limite:.2f}")
                continue
            elif retirada > saldo:
                print(f"\n\nERRO: Saldo insuficiente.")
                continue
            else:
                saldo -= retirada
                print(f"\nSaque de R$ {retirada:.2f} concluído.\n\nNovo saldo R$ {saldo:.2f}\n")
                extrato += f"\n Saque -R$ {retirada:.2f}\n"
                numero_saques += 1
                continue
        else:
            print("Limite de saques diários excedido.")
            continue
    
    if opcao == "3":
        if extrato == "":
            print("\nNão foram realizadas movimentações." + f"\n\nR$ {saldo:.2f}\n\n")
            continue
        else:
            print(extrato + f"\n\nR$ {saldo:.2f}\n\n")
            continue
    
    if opcao == "0":
        print("Atendimento encerrado.")
        break
    else:
        print("\nOpção inválida!")
