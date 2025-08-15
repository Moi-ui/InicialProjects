# Escreva um programa que verifique se um número não é nem positivo nem par.
num1 = float(input("Insira um número: "))

if num1 < 0 and num1 % 2 != 0:
    print("O valor não é positivo nem par")
else:
    print("O número não atende as condições")