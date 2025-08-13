import tkinter as tk
from tkinter import messagebox

# Janela principal
janela = tk.Tk()
janela.title("MEU TESTE")

# Função chamada ao clicar no botão
def enviar_alerta():
    nome_valor = nome.get()
    d_nasc_valor = d_nasc.get()
    cid_est_valor = cid_est.get()

    mensagem = (f"Olá caro {nome_valor}\n"
                f"Você nasceu dia {d_nasc_valor}\n"
                f"E reside em {cid_est_valor}")
    
    # Apagar conteúdo anterior e inserir novo
    texto.delete("1.0", tk.END)
    texto.insert(tk.END, mensagem)

# Rótulos e entradas
tk.Label(janela, text="NOME:", fg="black").grid(row=0, column=0, sticky="w")
nome = tk.Entry(janela, width=40)
nome.grid(row=0, column=1)

tk.Label(janela, text="DATA DE NASCIMENTO:", fg="black").grid(row=1, column=0, sticky="w")
d_nasc = tk.Entry(janela, width=40)
d_nasc.grid(row=1, column=1)

tk.Label(janela, text="CIDADE/ESTADO:", fg="black").grid(row=2, column=0, sticky="w")
cid_est = tk.Entry(janela, width=40)
cid_est.grid(row=2, column=1)

# Botão
botao = tk.Button(janela, width=10, height=2, text="Enviar", command=enviar_alerta)
botao.grid(row=3, column=0, columnspan=2, pady=10)

# Área de exibição de texto
texto = tk.Text(janela, height=5, width=50)
texto.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
