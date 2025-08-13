import tkinter as tk
from tkinter import messagebox

def exibir_nome():
    nome = entrada_nome.get()
    if nome:
        messagebox.showinfo("Nome digitado", f"Olá {nome}!")
    else:
        messagebox.showwarning("Entrada vazia", "Por favor, digite seu nome. Infeliz!")

janela = tk.Tk()
janela.title("Usando o campos de entrada")

rotulo = tk.Label(janela, text="Digite seu nome: ")
rotulo.pack(pady=10)

entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

botao_exibir = tk.Button(janela, text="Exibir Nome", command=exibir_nome)
botao_exibir.pack(pady=5)
janela.mainloop()