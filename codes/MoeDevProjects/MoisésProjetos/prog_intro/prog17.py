'''
Crie um programa que determine se uma pessoa pode votar (idade maior ou igual a
16 anos) e dirigir (idade maior ou igual a 18 anos).
'''

idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você pode votar e dirigir!")  
elif idade >= 16: #and idade < 18:
    print("Você pode votar, mas não dirigir!")
else:
    print("Você não pode votar, nem dirigir!")