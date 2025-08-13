def criar_relatorio(titulo ,autor ,data ,conteudo ,formato="PDF", confidencial=False, versao="1.0"):

    return{
        "titulo":titulo,
        "autor":autor,
        "data":data,
        "conteudo":conteudo,
        "formato":formato,
        "confidencial":confidencial,
        "versao":versao
    }
    
relatorio = criar_relatorio(
    "Análise de Mercado", #poscional
    "Akira Smith", #posicional(autor)
    "23-04-24", #posicional(data)
    "Mistério",#posicional(conteudo)
    confidencial=True, #nomeado
    versao=2.1 #nomeado
)

print(relatorio)