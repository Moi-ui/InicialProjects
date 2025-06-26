import tkinter as tk
from tkinter import messagebox

def exibir_nome():
    nome = entrada_nome.get()
    sobrenome = entrada_sobrenome.get()
    if nome:
        messagebox.showinfo("Nome digitado", f"Olá {nome} {sobrenome}!")
    else:
        messagebox.showwarning("Entrada vazia", "Por favor, digite seu nome. Infeliz!")

janela = tk.Tk()
janela.title("Usando o campos de entrada")

rot1 = tk.Label(janela, text="Digite seu nome: ")
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)
rot1.pack(pady=10)

rot2 = tk.Label(janela, text="Digite seu sobrenome: ")
entrada_sobrenome = tk.Entry(janela, width=40)
entrada_sobrenome.pack(pady=5)
rot2.pack(pady=10)

botao_exibir = tk.Button(janela, text="Exibir", command=exibir_nome)
botao_exibir.pack(pady=5)
janela.mainloop()