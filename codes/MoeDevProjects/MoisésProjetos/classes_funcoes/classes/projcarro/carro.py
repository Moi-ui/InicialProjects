# Exemplo de classe e instâncias em Python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        
    def frear(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)
        