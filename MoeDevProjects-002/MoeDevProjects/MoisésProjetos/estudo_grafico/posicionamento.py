import tkinter as tk

tela = tk.Tk()
tela.title("Grid")
label1 = tk.Label(tela, text="Label 1", font=("Arial", 16, "bold"))
label2 = tk.Label(tela, text="Label 2", font=("Arial", 16, "bold"))
botao1 = tk.Button(tela, text="Botão 1", font=("Arial", 16, "bold"))
botao2 = tk.Button(tela, text="Botão 2", font=("Arial", 16, "bold"))

label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
botao1.grid(row=0, column=1, padx=5, pady=5)
botao2.grid(row=1, column=1, padx=5, pady=5)

tela.mainloop()