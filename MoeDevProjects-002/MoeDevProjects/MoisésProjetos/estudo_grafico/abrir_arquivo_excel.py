import tkinter as tk
from tkinter import ttk
import pandas as pd

def abrir_arquivo_excel():
    file_path = r'C:\Users\Mois�sAm�ncioPereira\Downloads\PLANILHA RAPTORS.xlsx'
    df = pd.read_excel(file_path)
    
    # Limpar a tabela atual, se houver.
    for row in tree.get_children():
        tree.delete(row)
        
    # Configurar as colunas da tabela.
    tree["columns"] = list(df.columns)
    tree["show"] = "headings" #Exibir apenas os cabeçalhos.
    
    # Adicionar cabeçalhos de colunas
    for columns in df.columns:
        tree.heading(columns, text=columns)
        tree.column(columns, widht=100, anchor="center")
    
    # Adicionar linhas de dados.
    for _, row in df.iterrows():
        tree.insert("","end", values=list(row))
        

# Configuração da janela principal

janela = tk.Tk()
janela.title("Exibindo dados do Excel")
janela.geometry("800x600")

# Criar button para carregar o arquivo Excel.
open_button = tk.Button(janela, text="Carregar arquivo Excel", command=abrir_arquivo_excel)
open_button.pack(pady=10)

# Criar uma tabela (Treeview) para exibir os dados.
tree = ttk.Treeview(janela)
tree.pack(fill='both', expand=True)

janela.mainloop()