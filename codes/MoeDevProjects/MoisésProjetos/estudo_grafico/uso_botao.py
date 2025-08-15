import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Minha primeira janela com BOTÃO")

def fechar_janela():
    janela.destroy()

# botao_fechar = tk.Button(janela, text="Fechar",command=fechar_janela)
# botao_fechar.pack(pady=100, padx=100)
# botao_fechar.config(bg="red", fg="yellow",  font=("Times New Roman" ,100), border="20")

def exibir_mensagem_info():
    messagebox.showinfo(f"INFOMAÇÃO: Dará tudo certo, se não der errado!")

botao = tk.Button(janela, text="Clica em mim 😏", command=exibir_mensagem_info)
botao.pack(pady=100, padx=100)
botao.config(bg="white", fg="black", font=("Times New Roman" ,10), border="20")

janela.mainloop()