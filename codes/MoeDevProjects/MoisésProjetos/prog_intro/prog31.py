'''
Escreva um programa que imprima os números de 1 a 10, mas pule o número 5
usando continue.
'''

for i in range (1,11):
    if i == 5:
        continue
    print(i)