'''
Crie um programa que peça ao usuário para adivinhar um número entre 1 e 10. Use
um laço while para continuar pedindo até que o usuário acerte.
'''
import random
num = int(input("Adivinhe o número: "))
sort = random.randint(1,10)

while num != sort:
    print("Número Errado, tente novamente: ")
    num = int(input())
    
print("Você acertou!!")