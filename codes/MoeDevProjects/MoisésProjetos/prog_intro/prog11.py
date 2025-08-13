'''
Escreva um programa que calcule a soma, subtração, multiplicação e divisão de dois
números fornecidos pelo usuário.
'''
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
opcao = input("Escolha a operação que deseja realizar: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão:\n")
res = None

try:

    match opcao:
        case '1':
            res = num1 + num2
        case '2':
            res = num1 - num2
        case '3':
            res = num1 * num2
        case '4':
            if num2 != 0:
                res = num1 / num2
            else:
                print("Erro: Divisão por zero não é permitida.")
        case _:
            print("Escolha Inválida")

    if res is not None:
        print("O resultado da sua operação é:", res)

except ValueError:
    print("Erro: Por favor, insira números válidos.")