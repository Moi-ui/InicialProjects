import tkinter as tk

cor_atual = 'blue'
marca = '❌'

def alternar_turno(botao):
    global cor_atual, marca
    
    botao.config(bg=cor_atual, text=marca)
    
    cor_atual = 'red' if cor_atual == 'blue' else 'blue'
    marca = '⭕' if marca == '❌' else '❌'

janela = tk.Tk()
janela.title("MEU JOGO DA VELHA")

botoes = []
for i in range(9):
    botao = tk.Button(janela, width=5, height=2,font=("Arial", 32, "bold"),foreground='white')
    botao.config(command=lambda b=botao: alternar_turno(b))
    botao.grid(row=i//3, column=i%3, padx=10, pady=10)
    botoes.append(botao)

janela.mainloop()