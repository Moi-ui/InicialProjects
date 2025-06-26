#Escreva um programa que verifique se um número é positivo e par.
num1 = float(input("Insira um número: "))

if num1 > 0 and num1 % 2 == 0:
    print("O valor é positivo e par")
else:
    print("O número não atende as condições")