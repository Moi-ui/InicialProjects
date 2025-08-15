from carro import Carro

# Criando instâncias (objetos) a partir da classecarro1 = Carro("Toyota", "Corolla", 2020)
carro1 = Carro("Toyota", "Corolla",2020)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Volkswagen", "Golf", 2021)

# Cada instância tem seus próprios valores de atributos
# print(f"Carro 1: {carro1.marca} {carro1.modelo}")
# print(f"Carro 2: {carro2.marca} {carro2.modelo}")

# Podemos invocar métodos em cada instância

# carro1.acelerar(30)
# carro2.acelerar(20)
carro3.acelerar(40)

# print(f"Velocidade do carro 1: {carro1.velocidade} km/h")
# print(f"Velocidade do carro 2: {carro2.velocidade} km/h")
print(f"Carro 3: {carro3.marca} {carro3.modelo} {carro3.velocidade} km/h")