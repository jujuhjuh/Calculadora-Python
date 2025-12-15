def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            print("Programa encerrado. Até mais 👋")
            break

        elif opcao in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

            if opcao == "1":
                resultado = num1 + num2
                print(f"Resultado: {resultado}")

            elif opcao == "2":
                resultado = num1 - num2
                print(f"Resultado: {resultado}")

            elif opcao == "3":
                resultado = num1 * num2
                print(f"Resultado: {resultado}")

            elif opcao == "4":
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida ❌")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")

        else:
            print("Essa opção não existe ❌")

# Chamando a função
calculadora()