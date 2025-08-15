import tkinter as tk
from tkinter import messagebox

current_color = 'blue'
marca = '❌'
board = [''] * 9

def alter_turn(button, indice):
    global current_color, marca

    if button["text"] != "":
        return 
    
    button.config(bg=current_color, text=marca)
    board[indice] = marca

    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != '':
            messagebox.showinfo("Fim de Jogo", f"{marca} venceu!")
            desativar_botoes()
            return

    if '' not in board:
        messagebox.showinfo("Empate", "O jogo empatou!")
        return

    current_color = 'red' if current_color == 'blue' else 'blue'
    marca = '⭕' if marca == '❌' else '❌'

def desativar_botoes():
    for button in botoes:
        button.config(state='disabled')

def resetar_jogo():
    global current_color, marca, board
    current_color = 'blue'
    marca = '❌'
    board = [''] * 9
    for button in botoes:
        button.config(text='', bg='SystemButtonFace', state='normal')

window = tk.Tk()
window.title("MEU JOGO DA VELHA")
window.geometry("480x650")

botoes = []
for i in range(9):
    button = tk.Button(window, width=5, height=2, font=("Arial", 32, "bold"), foreground='white')
    button.config(command=lambda b=button, i=i: alter_turn(b, i))
    button.grid(row=i//3, column=i%3, padx=10, pady=10)
    botoes.append(button)

reset = tk.Button(window, text="Resetar", command=resetar_jogo, width=10, height=2, font=("Arial", 16, "bold"), bg='gray', fg='white')
reset.grid(row=3, column=0, columnspan=3, pady=20)

window.mainloop()