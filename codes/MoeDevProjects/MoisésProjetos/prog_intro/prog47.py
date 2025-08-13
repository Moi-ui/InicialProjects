#Crie  um programa que adicione, remova e ordene itens em uma lista.
itens = []

def adicionar_item(item):
    itens.append(item)
    print(f"'{item}' adicionado.")

def remover_item(item):
    if item in itens:
        itens.remove(item)
        print(f"'{item}' removido.")
    else:
        print(f"'{item}' não encontrado.")

def ordenar_lista():
    itens.sort()
    print("Lista ordenada.")

def exibir_lista():
    print("Lista:", itens)

while True:
    acao_str = input("Ação (add [item], rem [item], ord, ver, sair): ").lower()
    acao_lista = acao_str.split()
    comando = acao_lista[0] if acao_lista else ''

    match comando:
        case 'add':
            if len(acao_lista) > 1:
                adicionar_item(acao_lista[1])
            else:
                print("Informe o item para adicionar.")
        case 'rem':
            if len(acao_lista) > 1:
                remover_item(acao_lista[1])
            else:
                print("Informe o item para remover.")
        case 'ord':
            ordenar_lista()
        case 'ver':
            exibir_lista()
        case 'sair':
            break
        case _:
            print("Comando inválido.")