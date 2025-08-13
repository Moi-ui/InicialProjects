
def criar_perfil_usuario(nome, idade, profissao=None, cidade="", interesses=""):
    
    perfil = {
        "nome": nome,
        "idade": idade
    }
    if profissao:
        perfil["profissao"] = profissao
    if cidade:
        perfil["cidade"] = cidade
    if interesses:
        perfil["interesses"] = interesses
        return perfil
    
    perfil = criar_perfil_usuario (
        nome = "Moisés Amancio",
        idade = 17,
        cidade = "Juazeiro do Norte",
        interesses = ["Motociclismo","Xadrez","Tecnologia"]
    )

    print(perfil)