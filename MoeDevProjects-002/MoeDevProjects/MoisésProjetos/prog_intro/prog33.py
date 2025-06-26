'''
Escreva um programa que imprima apenas os números ímpares de 1 a 10 usando
continue.
'''

for i in range (1,11):
    if i%2 == 0:
        continue
    print(i)