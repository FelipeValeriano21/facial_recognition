import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import conn

class Formulario:
    def __init__(self):
        self.form_window = Toplevel()
        self.form_window.title("Formulário")
        self.form_window.config(bg="black")
        self.form_window.minsize(300, 300)
        self.center_window(self.form_window)

        style = ttk.Style()
        style.configure("TFrame", background="black")
        style.configure("TLabel", background="black")
        style.configure("TButton", background="lightgreen")

        frm = ttk.Frame(self.form_window, padding=20, style="TFrame")
        frm.grid(sticky=(N, S, E, W))

        ttk.Label(frm, text="RA", style="TLabel").grid(column=0, row=0, pady=10, padx=5, sticky=W)
        self.ra_entry = ttk.Entry(frm)
        self.ra_entry.grid(column=1, row=0, pady=10, padx=5)

        ttk.Label(frm, text="Nome", style="TLabel").grid(column=0, row=1, pady=10, padx=5, sticky=W)
        self.nombre_entry = ttk.Entry(frm)
        self.nombre_entry.grid(column=1, row=1, pady=10, padx=5)

        ttk.Label(frm, text="Professor", style="TLabel").grid(column=0, row=2, pady=10, padx=5, sticky=W)
        self.professor_combobox = ttk.Combobox(frm)
        self.professor_combobox.grid(column=1, row=2, pady=10, padx=5)

        ttk.Label(frm, text="Senha", style="TLabel").grid(column=0, row=3, pady=10, padx=5, sticky=W)
        self.senha_entry = ttk.Entry(frm, show='*')
        self.senha_entry.grid(column=1, row=3, pady=10, padx=5)

        # Carregar os professores no combobox
        self.carregar_professores()

        ttk.Button(frm, text="Enviar", command=self.enviar_formulario).grid(column=0, row=4, columnspan=2, pady=20)

        self.form_window.columnconfigure(0, weight=1)
        self.form_window.rowconfigure(0, weight=1)
        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=1)
        frm.rowconfigure(0, weight=1)
        frm.rowconfigure(1, weight=1)
        frm.rowconfigure(2, weight=1)
        frm.rowconfigure(3, weight=1)
        frm.rowconfigure(4, weight=1)

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def carregar_professores(self):
        # Criar uma instância da classe Connection
        conn_instance = conn.Connection()
        
        # Conectar ao banco de dados e carregar os professores no combobox
        conn_instance.carregar_professores(self.professor_combobox)

    def enviar_formulario(self):
        ra = self.ra_entry.get()
        nombre = self.nombre_entry.get()
        professor_id = self.professor_combobox.professores_ids.get(self.professor_combobox.get())
        senha = self.senha_entry.get()

        # Inserir dados na tabela tb_aluno
        conn_insert = conn.Connection()
        conn_insert.inserir_aluno(ra, professor_id, nombre, senha)

        # Guardar os dados do formulário em um arquivo temporário
        with open("dados_aluno.txt", "w") as f:
            f.write(f"{ra}\n{nombre}\n{professor_id}\n{senha}")

        # Executar o script main.py com os dados do formulário
        subprocess.Popen(["python", "main.py"])

        self.form_window.destroy()

        # Iniciar o processo de verificação do sucesso
        self.check_success()



    def check_success(self):
        if os.path.exists("captura_exitosa.txt"):
            os.remove("captura_exitosa.txt")
            messagebox.showinfo("Éxito", "Captura de fotos exitosa")
        else:
            self.form_window.after(1000, self.check_success)  # Verificar cada segundo

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Ocultar a janela principal do Tkinter
    Formulario()
    root.mainloop()
