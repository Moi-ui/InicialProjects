def chave_valor(**kwargs):
    # print(kwargs['nome'])
    x = kwargs.get('nome')
    print(x)
chave_valor(nome="Carlos",idade=20,altura=1.80)