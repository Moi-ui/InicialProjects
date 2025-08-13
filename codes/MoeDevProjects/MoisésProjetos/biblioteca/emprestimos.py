# emprestimos.py - Módulo para gerenciamento de empréstimos

import datetime
import livros
import usuarios

_base_emprestimos = {}
_proximo_id = 1

def realizar_emprestimo(id_usuario, id_livro, dias=14):
    """Registra o empréstimo de um livro para um usuário.

    Args:
    id_usuario: ID do usuário que está pegando o livro
    id_livro: ID do livro a ser emprestado
    dias: Duração do empréstimo em dias (padrão: 14)

    Returns:
    ID do empréstimo ou None se não for possível realizá-lo
    """
    # Verificações
    usuario = usuarios.buscar_usuario(id_usuario)
    livro = livros.buscar_livro(id_livro)

    if not usuario or not usuario["ativo"]:
        return None # Usuário não existe ou não está ativo

    if not livro or not livro["disponivel"]:
        return None # Livro não existe ou não está disponível

    # Registra empréstimo
    global _proximo_id
    id_emprestimo = _proximo_id
    _proximo_id += 1

    data_emprestimo = datetime.datetime.now()
    data_devolucao = data_emprestimo + datetime.timedelta(days=dias)

    _base_emprestimos[id_emprestimo] = {
    "id": id_emprestimo,
    "id_usuario": id_usuario,
    "id_livro": id_livro,
    "data_emprestimo": data_emprestimo,
    "data_devolucao_prevista": data_devolucao,
    "data_devolucao_efetiva": None,
    "status": "ativo"
    }

    # Atualiza disponibilidade do livro
    livros.atualizar_disponibilidade(id_livro, False)

    return id_emprestimo

def registrar_devolucao(id_emprestimo):
    """Registra a devolução de um livro.

    Args:
    id_emprestimo: ID do empréstimo a ser finalizado

    Returns:
    True se a devolução foi registrada com sucesso, False caso contrário
    """
    if id_emprestimo not in _base_emprestimos:
        return False

    emprestimo = _base_emprestimos[id_emprestimo]
    if emprestimo["status"] != "ativo":
        return False # Já foi devolvido

    # Atualiza o empréstimo
    emprestimo["data_devolucao_efetiva"] = datetime.datetime.now()
    emprestimo["status"] = "concluído"

    # Libera o livro para novo empréstimo
    livros.atualizar_disponibilidade(emprestimo["id_livro"], True)

    return True

def listar_emprestimos_ativos():
    """Lista todos os empréstimos ativos.

    Returns:
    Lista de empréstimos não devolvidos
    """
    return [e for e in _base_emprestimos.values() if e["status"] == "ativo"]

def verificar_atrasos():
    """Verifica empréstimos com devolução em atraso.

    Returns:
    Lista de empréstimos em atraso
    """
    hoje = datetime.datetime.now()
    return [
    e for e in _base_emprestimos.values()
    if e["status"] == "ativo" and e["data_devolucao_prevista"] < hoje
    ]

#teste
realizar_emprestimo(1, 1, dias=5)
print(listar_emprestimos_ativos())
def listar_emprestimos_usuarios(id_usuario):
    '''
    Lista todos os empréstimos de um usuário específico
    keyword arguments:
    argument -- id_usuario: ID do usuario
    Return: Lista de empréstimo do usuário
    '''
    return[e for e in _base_emprestimos.values() if e ["id_usuario"] == id_usuario]