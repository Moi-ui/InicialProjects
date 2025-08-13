'''
Crie um programa que solicite ao usuário que insira números até que a soma deles
seja maior que 50, usando break.
'''
soma = 0
while True:
 num = int(input("Insira um número: "))
 soma += num
 print(f"A soma atual é: {soma}")
 if soma > 50:
     print("A soma é maior que 50")
     break