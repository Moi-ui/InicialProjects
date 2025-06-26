'''
Escreva um programa que imprima os números de 1 a 10, mas pule os múltiplos de
3 usando continue.
'''

for i in range (1,11):
    if i%3 == 0:
        continue
    print(i)