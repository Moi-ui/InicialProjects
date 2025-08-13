'''
Crie um programa que determine o dia da semana com base em um número (1 para
segunda-feira, 2 para terça-feira, etc.).
'''
dia = input("Insira um número até 7: ")
match dia:
    case '1':
        print("Segunda-Feira")
    case '2':
        print("Terça-Feira")
    case'3':
        print("Quarta-Feira")
    case'4':
        print("Quinta-Feira")
    case'5':
        print("Sexta-Feira")
    case'6':
        print("Sábado")
    case'7':
        print("Domingo")
    case _:
        print("Não representa um dia da semana!")