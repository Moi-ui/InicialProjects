class Produto:
    # Atributo de classe - compartilhado por todas as instâncias
    categoria = "Geral"
    
    # Método construtor
    def __init__(self, nome, preco, estoque=0):
        # Atributos de instância - específicos para cada objeto
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self._vendido = False  # Atributo com convenção de "privado"
    
    # Método de instância
    def calcular_valor_total(self):
        return self.preco * self.estoque
    
    # Outro método de instância
    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            return False
    
    # Método especial para representação em string
    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Estoque: {self.estoque}"
    
    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade
        
    def verificar_estoque(self):
        return self.estoque > 0