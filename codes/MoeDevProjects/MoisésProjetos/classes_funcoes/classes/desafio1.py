class Calcular:
    res = 0
    def soma(self, *args):
        return sum(args)
    

class Somador:
    def somar(self, *args):
        if all(isinstance(arg,(int, float)) for arg in args):
            print(f"Somando todos os números: {sum(args)}")
        else:
            print(f"Os valores passados não são valores válidos")

class SomarValores:
    def somar_valor(self,*args):
        soma = 0.0
        for valor in args:
            if isinstance(valor,(int, float)):
                soma += valor
            else:
                raise ValueError(f"O valor {soma} não é um número inteiro ou ponto flutuantes.")
        return soma        

sv = SomarValores()
smd = Somador()
calc = Calcular()

print(sv.somar_valor(5,6,7,8,9))
smd.somar(5,6,7,8,9)
print(calc.soma(5,6,7,8,9))