# Classe base (abstrata) para uma conta bancária
class Conta:
    def __init__(self, titular, saldo=0):
        self._titular = titular      # Encapsulamento: atributo "protegido"
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado para {self._titular}.")

    def sacar(self, valor):
        # Abstração de comportamento genérico
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado para {self._titular}.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Titular: {self._titular} | Saldo: R${self._saldo:.2f}")

    def get_titular(self):
        return self._titular

    def get_saldo(self):
        return self._saldo

    def set_titular(self, novo_titular):
        self._titular = novo_titular

# Herança: ContaCorrente herda de Conta
class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self._limite = limite  # Limite especial do cheque especial

    # Polimorfismo: comportamento diferente para sacar
    def sacar(self, valor):
        if self._saldo + self._limite >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com cheque especial.")
        else:
            print("Saldo + limite insuficiente.")

# Herança: ContaPoupanca herda de Conta
class ContaPoupanca(Conta):
    def render_juros(self, taxa):
        # Polimorfismo: novo comportamento exclusivo
        rendimento = self._saldo * taxa
        self._saldo += rendimento
        print(f"Juros de R${rendimento:.2f} aplicados.")

# Exemplo de uso
if __name__ == "__main__":
    # Criando contas diferentes
    conta1 = ContaCorrente("Moisés", saldo=100)
    conta2 = ContaPoupanca("Lima", saldo=2000)

    # Operações básicas
    conta1.mostrar_saldo()
    conta1.depositar(400)
    conta1.sacar(600)  # usa limite especial
    conta1.mostrar_saldo()

    print("\n----\n")

    conta2.mostrar_saldo()
    conta2.render_juros(taxa=0.05)  # rendimento de 5%
    conta2.sacar(300)
    conta2.mostrar_saldo()
