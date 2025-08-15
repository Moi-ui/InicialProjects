# Crie um programa que verifique se uma string contém apenas letras.
frase = input("insira um texto: ")
if frase.isalpha() == True:
    print("Essa string possui apenas letras.")
else:
    print("Essa string não possui apenas letras.")