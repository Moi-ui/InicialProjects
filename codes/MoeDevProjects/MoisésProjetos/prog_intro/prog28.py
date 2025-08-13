'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''
num = int(input("Inisira um número para ver sua tabuada: "))
print(f"A tabuada do {num} é: ")
for i in range(1,11):
    res = num*i
    print(f"\n|{num}x{i} = {res}|")