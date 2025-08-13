class Animal:
    pass
'''
Classe base para animais. Define um método 'falar' que será sobescrito pelas subclasses
'''
class Cachorro(Animal):
    def falar(self):
        return "Au!"
class Gato(Animal):
    def falar(self):
        return "Miau!"
class Pato(Animal):
    def falar(self):
        return"Quack!"
def fazer_animal_falar(animal):
    print(animal.falar())
    
cachorro = Cachorro()
pato = Pato()
gato = Gato()

print("--- EXEMPLO 1: POLIMORFISMO COM HERANÇA ---")
fazer_animal_falar(pato)
fazer_animal_falar(gato)
fazer_animal_falar(cachorro)
print("\n--------------------------------------------------\n")

class Carro:
    def ligar_motor(self):
        return "O motor está ligado!"
    def mover(self):
        return "O carro está andando!"
    
class Bicicleta:
    def mover(self):
        return "A bicicleta está andando!"
    def tocar_campanhinha(self):
        return "Prim! Prim!"
    
class Pessoa:
    def mover(self):
        return "A pessoa está andando!"

def simular_movimento(veiculo):
    print(veiculo.mover())
    
carro = Carro()
bicicleta = Bicicleta()
pessoa = Pessoa()

print("--- EXEMPLO 2: POLIMORFISMO COM DUCK TYPING ---")
simular_movimento(carro)
simular_movimento(bicicleta)
simular_movimento(pessoa)