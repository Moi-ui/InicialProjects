''' POLIMORFISMO: SOBSOBRECARGA - Parâmetros Opicionais '''
class CalculadoraSimples:
    def somar(self,a,b,c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b
print("--- EXEMPLO 1: PARÂMETROS OPICIONAIS ---")
calc = CalculadoraSimples()
print(f"Soma de 5 e 3: {calc.somar(5,3)}")
print(f"Soma de 5, 3 e 2: {calc.somar(5,3,2)}")

print("\n----------------------------------------------\n")
'''
POLIMORFISMO: SOBRECARGA - Argumentos Variável (*args e **Kwargs)
'''
class ProcessadorDeDados:
    def processar(self, *args,**kwargs):
        if args and not kwargs:
            if all(isinstance(arg, (int, float)) for arg in args):
                print(f"Somando todos os numeros: {sum(args)}")
            else:
                print(f"Processando lista de itens: {list(args)}")
        elif kwargs and not args:
            #Se apenas argumentos nomeados forem passados
            print("Processando informações nomeadas:")
            for key, value in kwargs.itens():
                print(f"{key}:{value}")
            else:
                print("Nenhum argumento ou combinação suportada.")
                
print("---EXEMPLO 2: *args e *kwargs")
proc = ProcessadorDeDados()
proc.processar(10,20,30)
proc.processar("Cereja","Melão","Jerimum")
proc.processar(nome="Carlos", idade=20, cidade="RJ")