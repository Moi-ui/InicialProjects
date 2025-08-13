# Escreva um programa que formate um número com duas casas decimais.
num = float(input("Insira um número para a formatação: "))
formatacao = f"{num:.2f}"

print(f"Seu número após a fromatação é {formatacao}")
