'''
Escreva um programa que substitua todas as ocorrências de uma letra em uma
string por outra letra.
'''

frase = input("Insira uma frase: ")
letra_a = input("Qual letra você deseja trocar? ")
letra_n = input("Por qual letra você quer trocar? ")
frase_mod = frase.replace(letra_a,letra_n)

print(f"A frase com a letra trocada é: {frase_mod}")