def adicionar(valor):
    #Na funcão externa (adicionar), estamos atribuindo outra função dentro dela.
    def clousure(numero):
    #A função interna (numero), atribuida à função externa.
        return numero + valor
    #A função interna retorna (numero + valor).
    return clousure
    #Função externa retorna (o valor da funcao interna (clousure)).
adicionar_cinco = adicionar(5)
    #Atribui o valor do retorno da funcao à variável (adicionar_cinco).
print(adicionar_cinco(10)) #?