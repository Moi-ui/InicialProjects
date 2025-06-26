# Crie um programa que extraia uma substring de uma string fornecida pelo usuário.

frase = input("Insira uma frase: ")
pos_i = int(input("Insira a posição inicial da substring: "))
pos_f = int(input("Insira a posição final da substring: "))
frase = frase.replace(" ","")
substring = frase[pos_i-1:pos_f]

print(f"Sua substring é: {substring}")
