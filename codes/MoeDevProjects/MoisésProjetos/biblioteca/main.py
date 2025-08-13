# main.py - Ponto de entrada do programa
import livros
import usuarios
import emprestimos


def inicializar_dados_exemplo():
    """Adiciona alguns dados de exemplo ao sistema."""
    id_livro1 = livros.adicionar_livro(
        "O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia"
    )
    livros.adicionar_livro(
        "1984", "George Orwell", 1949, "Ficção Distópica"
    )
    livros.adicionar_livro(
        "Dom Casmurro", "Machado de Assis", 1899, "Romance Brasileiro"
    )

    id_usuario1 = usuarios.cadastrar_usuario(
        "Ana Silva", "ana@exemplo.com", "11999998888"
    )
    usuarios.cadastrar_usuario(
        "Carlos Oliveira", "carlos@exemplo.com"
    )

    emprestimos.realizar_emprestimo(id_usuario1, id_livro1)

    print("Dados de exemplo inicializados com sucesso!")


def menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n==== SISTEMA DE BIBLIOTECA ====")
    print("1. Gerenciar Livros")
    print("2. Gerenciar Usuários")
    print("3. Gerenciar Empréstimos")
    print("0. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        menu_livros()
    elif opcao == "2":
        menu_usuarios()
    elif opcao == "3":
        menu_emprestimos()
    elif opcao == "0":
        print("Encerrando o programa. Até logo!")
        return False
    else:
        print("Opção inválida!")

    return True


def menu_livros():
    """Submenu para gerenciamento de livros."""
    print("\n==== GERENCIAMENTO DE LIVROS ====")
    print("1. Adicionar novo livro")
    print("2. Buscar livro por ID")
    print("3. Listar todos os livros")
    print("4. Listar livros disponíveis")
    print("5. Listar livros por autor")
    print("0. Voltar")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano de publicação: "))
        genero = input("Gênero: ")
        id_livro = livros.adicionar_livro(titulo, autor, ano, genero)
        print(f"Livro adicionado com sucesso! ID: {id_livro}")

    elif opcao == "2":
        id_livro = int(input("Digite o ID do livro: "))
        livro = livros.buscar_livro(id_livro)

        if livro:
            print(f"\nLivro encontrado:")
            print(f"ID: {livro['id']}")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Gênero: {livro['genero']}")
            print(f"Disponível: {'Sim' if livro['disponivel'] else 'Não'}")
        else:
            print("Livro não encontrado!")

    elif opcao == "3":
        todos_livros = livros.listar_livros()
        if todos_livros:
            print("\nLista de todos os livros:")
            for livro in todos_livros:
                status = "Disponível" if livro["disponivel"] else "Emprestado"
                print(f"{livro['id']} - {livro['titulo']} ({livro['autor']}) - {status}")
        else:
            print("Nenhum livro cadastrado!")

    else:
        print("Voltando ao menu principal...")


def menu_usuarios():
    """Submenu para gerenciamento de usuários."""
    print("\n==== GERENCIAR USUÁRIOS ====")
    print("1. Cadastrar novo Usuário")
    print("2. Buscar Usuário por ID")
    print("3. Listar todos os usuários")
    print("4. Listar empréstimos do usuário")
    print("0. Voltar")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone (opcional): ")

        if telefone:
            id_usuario = usuarios.cadastrar_usuario(nome, email, telefone)
        else:
            id_usuario = usuarios.cadastrar_usuario(nome, email)
        print(f"Usuário cadastrado com sucesso! ID: {id_usuario}")

    elif opcao == "2":
        id_usuario = int(input("Digite o ID do Usuário: "))
        usuario = usuarios.buscar_usuario(id_usuario)
        if usuario:
            print(f"\nUsuário encontrado:")
            print(f"ID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Telefone: {usuario.get('telefone', 'Não encontrado')}")
        else:
            print("Usuário não encontrado.")

    elif opcao == "3":
        todos_usuarios = usuarios.listar_usuarios()
        if todos_usuarios:
            print("\nLista de Usuários:")
            for usuario in todos_usuarios:
                telefone = usuario.get("telefone", "Não encontrado")
                print(f"{usuario['id']} - {usuario['nome']} - {usuario['email']} - Tel: {telefone}")
        else:
            print("Nenhum usuário encontrado.")

    elif opcao == "4":
        id_usuario = int(input("Digite o ID do Usuário: "))
        emprestimos_usuario = emprestimos.listar_emprestimos_do_usuario(id_usuario)
        if emprestimos_usuario:
            print(f"\nEmpréstimos do usuário {id_usuario}:")
            for emp in emprestimos_usuario:
                livro = livros.buscar_livro(emp['id_livro'])
                status = "Em andamento" if emp['data_devolucao'] is None else "Devolvido"
                print(f"Livro: {livro['titulo']} - Status: {status}")
        else:
            print("Nenhum empréstimo encontrado para esse usuário.")


def menu_emprestimos():
    """Submenu para gerenciamento de empréstimos."""
    print("\n==== GERENCIAR EMPRÉSTIMOS ====")
    print("1. Realizar Empréstimo")
    print("2. Devolver Livro")
    print("3. Listar Empréstimos")
    print("0. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario_id = int(input("ID do Usuário: "))
        livro_id = int(input("ID do Livro: "))
        try:
            emprestimo = emprestimos.realizar_emprestimo(usuario_id, livro_id)
            print(f"Empréstimo realizado! ID: {emprestimo['id']}")
        except Exception as e:
            print(f"Erro ao realizar o empréstimo: {str(e)}")

    elif opcao == "2":
        emprestimo_id = int(input("ID do Empréstimo: "))
        try:
            if emprestimos.devolver_livro(emprestimo_id):
                print("Livro devolvido com sucesso.")
            else:
                print("Não foi possível devolver o livro.")
        except Exception as e:
            print(f"Erro ao devolver o livro: {str(e)}")

    elif opcao == "3":
        todos = emprestimos.listar_emprestimos()
        if todos:
            print("\nLista de todos os empréstimos:")
            for emprestimo in todos:
                usuario = usuarios.buscar_usuario(emprestimo['id_usuario'])
                livro = livros.buscar_livro(emprestimo['id_livro'])
                status = "Em andamento" if emprestimo['status'] == "ativo" else "Devolvido"
                print(f"ID: {emprestimo['id']} - Usuário: {usuario['nome']} - Livro: {livro['titulo']} - Status: {status}")
        else:
            print("Nenhum empréstimo registrado.")

    elif opcao == "0":
        print("Voltando ao menu principal...")


if __name__ == "__main__":
    inicializar_dados_exemplo()
    continuar = True
    while continuar:
        continuar = menu_principal()
    print("Programa encerrado.")
    
# Esse é o ponto de entrada do programa, onde o sistema de biblioteca é iniciado.
# Ele importa os módulos de livros, usuários e empréstimos, inicializa alguns dados de exemplo
# e exibe um menu principal para o usuário interagir com o sistema.