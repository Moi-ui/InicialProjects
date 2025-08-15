# usuarios.py - Módulo para gerenciamento de usuários

_base_usuarios = {}
_proximo_id = 1

def cadastrar_usuario(nome, email, telefone=None):
    """Cadastra um novo usuário no sistema.

    Args:
    nome: Nome completo do usuário
    email: Endereço de email
    telefone: Número de telefone (opcional)

    Returns:
    ID do usuário cadastrado
    """
    global _proximo_id
    id_usuario = _proximo_id
    _proximo_id += 1

    _base_usuarios[id_usuario] = {
        "id": id_usuario,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "ativo": True
    }

    return id_usuario

def buscar_usuario(id_usuario):
    """Busca um usuário pelo ID.

    Args:
    id_usuario: ID do usuário

    Returns:
    Dicionário com informações do usuário ou None se não encontrado
    """
    return _base_usuarios.get(id_usuario)

def buscar_usuario_por_email(email):
    """Busca um usuário pelo email.

    Args:
    email: Email do usuário

    Returns:
    Dicionário com informações do usuário ou None se não encontrado
    """
    for usuario in _base_usuarios.values():
        if usuario["email"].lower() == email.lower():
            return usuario
    return None

def listar_usuarios(apenas_ativos=True):
    """
    Lista todos os usuários, opcionalmente filtrando apenas ativos.

    Args:
    apenas_ativos: Se True, retorna apenas usuários ativos

    Returns:
    Lista de usuários
    """
    if apenas_ativos:
        return [u for u in _base_usuarios.values() if u["ativo"]]
    else:
        return list(_base_usuarios.values())
    
cadastrar_usuario("Moisés ", "mapl.hub.ftc@gmail.com", 88992821862)
cadastrar_usuario("Giorgian De Arrascaeta", "arrasquinha@gmail.com", 40028922)
print(listar_usuarios())