'''
Escreva um programa que solicite ao usuário que insira um número decimal e
imprima o número com duas casas decimais.
'''
num_float = float(input("Digite um número decimal: "))
try:
    num_format = f"{num_float:.2f}"
    print(f"O número formatado é: {num_format}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número decimal.")