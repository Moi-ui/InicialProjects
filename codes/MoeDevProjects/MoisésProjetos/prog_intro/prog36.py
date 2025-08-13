'''
Escreva um programa que peça ao usuário para digitar uma frase e imprima o
número de caracteres.
'''
frase = input("Escreva uma frase: ").strip()
FraseSemEspaco = frase.replace(" ","")
n_char = len(FraseSemEspaco)
print(f"O número possui {n_char} caracteres.")