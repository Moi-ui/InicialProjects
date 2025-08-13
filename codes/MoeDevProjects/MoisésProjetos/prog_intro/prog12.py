'''
crie um programa que compare dois números e imprima se o primeiro é maior, menor ou igual ao segundo.
'''
a = float(input("Insira o primeiro valor: "))
b = float(input("Insira o segundo valor: "))

if a > b:
    print("O maior valor é: ", a)
elif a < b:
    print("O maior valor é: ", b)
else:
    print("Os valores são iguais.")