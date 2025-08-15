class Pessoa:
    """
    CONSTRUTOR DA CLASSE PESSOA.
    Inicializar os atributos nome e idade.
    """
    def __init__(self, nome,idade):
    #atributos de instância
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade}")

# class Aluno(Pessoa):
#     def __init__(self, nome, idade, matricula):
#         super().__init__(nome, idade)
#         self.matricula = matricula
        
#     def apresentar(self):
#         super().apresentar()
#         print(f"e minha matrícula é {self.matricula}")
    
    
# pessoa1 = Pessoa("Moisés", 17)
# aluno = Aluno("Ana", 20, "12568")
# pessoa1.apresentar()
# aluno.apresentar()