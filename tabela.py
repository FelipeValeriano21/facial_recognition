from tkinter import *
from tkinter import ttk
import conn

class TabelaSimples:
    def __init__(self):
        self.tabela_window = Toplevel()
        self.tabela_window.title("Tabela Simples")

        self.conn = conn.Connection()

        style = ttk.Style()
        style.configure("TFrame", background="lightblue")
        style.configure("TLabel", background="lightblue", font=("Helvetica", 16))
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.configure("Treeview", font=("Helvetica", 10))

        main_frame = ttk.Frame(self.tabela_window, padding=20, style="TFrame")
        main_frame.grid(sticky=(N, S, E, W))

        titulo = ttk.Label(main_frame, text="Título da Tabela", style="TLabel")
        titulo.grid(row=0, column=0, pady=10, padx=5, sticky=W)

        self.tree = ttk.Treeview(main_frame, columns=("col1", "col2", "col3"), show="headings")
        self.tree.heading("col1", text="Nome do Aluno")
        self.tree.heading("col2", text="Data de Presença")
        self.tree.heading("col3", text="Status de Presença")

        self.tree.grid(row=1, column=0, pady=10, padx=5, sticky=(N, S, E, W))

        self.atualizar_tabela()

        self.tabela_window.columnconfigure(0, weight=1)
        self.tabela_window.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=0)
        main_frame.rowconfigure(1, weight=1)

    def atualizar_tabela(self):
        # Limpar a árvore antes de adicionar os novos dados
        for child in self.tree.get_children():
            self.tree.delete(child)

        # Obter os dados de presença do banco de dados
        presencas = self.conn.listar_presencas()

        # Preencher a árvore com os dados de presença
        for presenca in presencas:
            self.tree.insert("", END, values=presenca)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    TabelaSimples()
    root.mainloop()
