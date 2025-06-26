def soma_numeros(*args):
    soma = 0
    for i in args:
        soma = soma + i
    print(soma)
    
soma_numeros(20, 25, 5)