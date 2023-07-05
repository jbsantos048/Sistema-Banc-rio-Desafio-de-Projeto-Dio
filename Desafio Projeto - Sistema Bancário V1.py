menu = ''''
------ Escolha a operação desejada ------

[d] = Depositar
[s] = Sacar
[e] = Extrato
[0] = Sair 

'''
saldo = 0
limite = 500
extrato = " "
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor desejado para depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Operação inválida, não é possível depositar valores negativos. Nesse caso você deve fazer um saque!")    

    elif opcao == "s":
        saque = float(input("Digite o valor a ser depositado: "))
        
        excede_saldo = saque > saldo

        excede_limite = saque > limite

        excede_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excede_saldo:
            print("Saldo Insuficiente.")
        
        if excede_limite:
            print("Limite de saque excedido.")

        if excede_saques:
            print("Limite de saques diários atingido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_de_saques += 1 

        else:
            print("Opção inválida")                         
    
    elif opcao == "e":
        print("\n---------- Extrato ----------")
        print("Não foram feitas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-------------------------------")

    elif opcao == 0:
        print("Obrigado por escolher nosso banco")
        break

    else:
        print("Opção invalida, tente outra vez!")


