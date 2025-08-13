# livros.py - Módulo para gerenciamento de livros

# Base de dados simplificada (em produção seria um banco de dados real)
_base_livros = {}
_proximo_id = 1

def adicionar_livro(titulo, autor, ano, genero):
    """Adiciona um novo livro à biblioteca.

    Args:
    titulo: Título do livro
    autor: Nome do autor
    ano: Ano de publicação
    genero: Gênero literário

    Returns:
    ID do livro adicionado
    """
    global _proximo_id
    id_livro = _proximo_id
    _proximo_id += 1

    _base_livros[id_livro] = {
    "id": id_livro,
    "titulo": titulo,
    "autor": autor,
    "ano": ano,
    "genero": genero,
    "disponivel": True
    }

    return id_livro

def buscar_livro(id_livro):
    """Busca um livro pelo ID.

    Args:
    id_livro: ID do livro a ser buscado

    Returns:
    Dicionário com informações do livro ou None se não encontrado
    """
    return _base_livros.get(id_livro)

def listar_livros(filtro=None):
    """Lista todos os livros, opcionalmente filtrados.

    Args:
    filtro: Função que recebe um livro e retorna True se deve ser incluído
    
    Returns:
    Lista de livros que atendem ao critério de filtro
    """
    if filtro is None:
        return list(_base_livros.values())
    else:
        return [livro for livro in _base_livros.values() if filtro(livro)]

def atualizar_disponibilidade(id_livro, disponivel):
    """Atualiza o status de disponibilidade de um livro.

    Args:
    id_livro: ID do livro
    disponivel: True se disponível, False se emprestado

    Returns:
    True se a atualização foi bem-sucedida, False caso contrário
    """
    livro = buscar_livro(id_livro)
    if livro:
        livro["disponivel"] = disponivel
        return True
    return False

    # Funções auxiliares específicas
def livros_por_autor(autor):
    """Retorna todos os livros de um determinado autor.

    Args:
    autor: Nome do autor a filtrar

    Returns:
    Lista de livros do autor
    """
    return listar_livros(lambda livro: livro["autor"].lower() == autor.lower())

def livros_disponiveis():
    """Retorna todos os livros disponíveis para empréstimo.

    Returns:
    Lista de livros disponíveis
    """
    return listar_livros(lambda livro: livro["disponivel"])

#teste
adicionar_livro("João e Maria","CB",2017,"Drama")
adicionar_livro("Diário de Banana","Moe", 1899,"Drama")
adicionar_livro("Vasco","José Mourinho", 1500,"Terror")
atualizar_disponibilidade(2, False)
print(livros_disponiveis())