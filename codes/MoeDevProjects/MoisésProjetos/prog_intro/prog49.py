#Crie um programa que verifique se um item está em uma lista.
lista = ['a', 'b', 'c', 'd']
verif = input("Veja se o intem está na lista: ").lower()
if verif in lista: 
    print("Esse item está na lista!")
else:
    print("Esse item não faz parte da lista!")
