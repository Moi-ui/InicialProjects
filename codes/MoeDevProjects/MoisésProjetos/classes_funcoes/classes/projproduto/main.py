from produto import Produto
produto1 = Produto("Condicionador",23.45,11)
print(f"\n\n {produto1} \n")
produto1.vender(3)
print(f"Valor total em estoque R$ {produto1.calcular_valor_total():.2f}")
print(produto1.verificar_estoque())
print(produto1)