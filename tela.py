import tkinter as tk
from tkinter import messagebox
from crud import create_user, read_users, update_user, delete_user

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD USUÁRIOS")
        
        # Criação de Widgets
        
        self.create_widgets()
    
    def create_widgets(self):

        #Label
        tk.Label(self.root, text = "Nome: ").grid (row = 0, column = 0)
        tk.Label(self.root, text = "Telefone: ").grid (row = 1, column = 0)
        tk.Label(self.root, text = "E-mail: ").grid (row = 2, column = 0)
        tk.Label(self.root, text = "Usuario: ").grid (row = 3, column = 0)
        tk.Label(self.root, text = "Senha: ").grid (row = 4, column = 0)

        tk.Label(self.root, text = "UserID(for update/delete): ").grid (row = 5, column = 0)

        # CRIAR AS CAIXAS PARA DIGITAR OS VALORES E POSICIONAR

        self.nome_entry = tk.Entry(self.root).grid(row = 0, column = 1)
        self.telefone_entry = tk.Entry(self.root).grid(row = 1, column = 1)
        self.email_entry = tk.Entry(self.root).grid(row = 2, column = 1)
        self.usuario_entry = tk.Entry(self.root).grid(row = 3, column = 1)
        self.senha_entry = tk.Entry(self.root).grid(row = 4, column = 1)
        self.UserID_entry = tk.Entry(self.root).grid(row = 5, column = 1)

        # BOTÕES DO CRUID

        tk.Button(self.root, text = "Criar usuário", command = self.create_widgets).grid(row = 6, column = 0, columnspan = 1)

tk.mainloop()