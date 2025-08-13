import tkinter as tk
from tkinter import messagebox

def exibir_soma():
    num1 = float(e_num1.get())
    num2 = float(e_num2.get())
    soma = num1 + num2
    if num1 and num2:
        messagebox.showinfo("Numero digitado", f"{num1} + {num2} = {soma}")
    else:
        messagebox.showwarning("Entrada vazia", "Por favor, digite um  número. Infeliz!")

janela = tk.Tk()
janela.title("Usando o campos de entrada")
janela.geometry("400x200")

rot1 = tk.Label(janela, text="Digite o  primeiro número: ")
e_num1 = tk.Entry(janela, width=40)
e_num1.pack(pady=5)
rot1.pack(pady=10)

rot2 = tk.Label(janela, text="Digite o segundo número: ")
e_num2 = tk.Entry(janela, width=40)
e_num2.pack(pady=5)
rot2.pack(pady=10)

botao_exibir = tk.Button(janela, text="SOMAR", command=exibir_soma)
botao_exibir.pack(pady=5)
janela.mainloop()