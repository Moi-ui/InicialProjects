def combinar_funcao(f1,f2):
    def combinada(x):
        return f2(f1(x))
    return combinada

dobrar = lambda x: x * 2
#Ele vai dobrar o valor de (x) declarado na função {combinada}.
adicionar_um = lambda x: x + 1
#Ele vai somar 1 ao valor de (x) declarado na função {combinada}.
combinada = combinar_funcao(dobrar, adicionar_um)

print(combinada(3))