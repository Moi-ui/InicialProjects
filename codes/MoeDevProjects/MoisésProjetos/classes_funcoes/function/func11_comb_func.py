def imprimir_estrutura_dir(path, identacao= 0):
    import os
    # Obtém o nome do diretório ou arquivo.
    nome = os.path.basename(path)
    # Imprime com a indentação apropriada
    print(' ' * identacao + nome)
    # Verifica se é um diretório
    if os.path.isdir(path):
        # Listar todos os itens no diretório
        try:
            itens = os.listdir(path)
            for item in itens:
                # Chamada recursiva para cada item
                imprimir_estrutura_dir(os.path.join(path, item), identacao + 4)
        except PermissionError:
            print(' ' * (identacao + 4) + '- [Sem permissão para acessar]')

# Chamada correta da função
imprimir_estrutura_dir('D:\Chrome Downloads')