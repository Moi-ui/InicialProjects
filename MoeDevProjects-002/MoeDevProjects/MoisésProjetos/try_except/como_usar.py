def dividir(a,b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é peremitida")
    else:
        print(f"Resultado da divisão: {resultado}")
    finally:
        print(f"Operação de divisão cuncluída")

# # exemplo de uso
# dividir(10, 2)
# dividir(10, 0)

def converter_para_inteiro(valor):
    try:
        numero = int(valor)
    except ValueError:
        print(f"Erro: Entrada inválida. Por favor, digite um número válido")
    else:
        print(f"Número convertido: {numero}")
    finally:
        print(f"Operação de conversão concluída")
    
# #exemplo de uso
# converter_para_inteiro("568")
# converter_para_inteiro("abc")

def acessar_elemento(lista, indice):
    try:
        elemento = lista[indice]
    except IndexError:
        print(f"Erro:  Índice fora do intervalo")
    else:
        print(f"Elemento acessado: {elemento}")
    finally:
        print(f"Operação de acesso á lista concluída")

# exemplo de uso
lista = [10, 20, 50]
acessar_elemento(lista, 1)
acessar_elemento(lista, 5)