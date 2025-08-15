#falta algo?
from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        super().__init__(nome,idade)
        self.matricula = matricula
        
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}, tenho {self.idade} anos e minha metrícula é {self.matricula}")
        
aluno = Aluno("José",17,23072)
aluno.apresentar()