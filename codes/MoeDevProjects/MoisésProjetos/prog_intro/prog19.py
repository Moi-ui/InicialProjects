'''
Crie um programa que verifique se uma pessoa é maior de idade (idade maior ou
igual a 18 anos) ou se possui autorização dos pais.
'''
idade = int(input("Insira sua idade: "))
if idade >= 18:
    print("Você é maior de idade, está autorizado!")
elif idade < 18:
    resp = input("Você possui autorização de seus pais? (Sim ou Não): ").lower().strip()
    if resp == 'sim':
        print("Você está autorizado!")
    elif resp == 'não':
        print("Você não está autorizado!")