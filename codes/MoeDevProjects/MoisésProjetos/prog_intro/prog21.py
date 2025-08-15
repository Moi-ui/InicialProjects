'''
Escreva um programa que peça ao usuário para digitar um número e verifique se ele
é positivo, negativo ou zero.
'''
num1 = float(input("Insira um número: "))

if num1 > 0:
    print("O valor é positivo!")
elif num1 < 0:
    print("O valor é negativo!")
else:
    print("O valor é 0 (Zero)!")