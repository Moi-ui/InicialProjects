'''
Escreva um programa que remova os espaços em branco do início e do fim de uma
string.
'''
mensagem = input("Digite a mensagem: ").strip()
print(f"Mensagem sem espaços nas extremidades: '{mensagem}'")
print (len(str(" " in mensagem)))