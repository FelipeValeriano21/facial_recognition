from tkinter import *
from tkinter import ttk, messagebox
import subprocess
import os
import formulario  
import tabela

def abrir_formulario():
    formulario.Formulario()  

def abrir_tabela():
    tabela.TabelaSimples()  

def start_training():
    progress_window = Toplevel()
    progress_window.title("Treinamento")
    progress_window.config(bg="black")
    progress_window.geometry("300x100")
    
    ttk.Label(progress_window, text="Treinando o modelo...", style="TLabel").pack(pady=20)
    progress_bar = ttk.Progressbar(progress_window, mode='indeterminate')
    progress_bar.pack(fill=X, padx=20, pady=10)
    progress_bar.start()

    training_process = subprocess.Popen(["python", "train.py"])

    def check_training():
        if training_process.poll() is None:
            progress_window.after(1000, check_training)
        else:
            progress_bar.stop()
            progress_window.destroy()
            if os.path.exists("entrenamento_exitoso.txt"):
                os.remove("entrenamento_exitoso.txt")
                messagebox.showinfo("Éxito", "Treinamento realizado com sucesso!")

    check_training()

def start_testing():
    testing_process = subprocess.Popen(["python", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def check_testing():
        if testing_process.poll() is None:
            root.after(1000, check_testing)
        else:
            stdout, stderr = testing_process.communicate()
            if testing_process.returncode == 0:
                messagebox.showinfo("Resultado", stdout.decode(errors='ignore'))
            else:
                messagebox.showerror("Erro", stderr.decode(errors='ignore'))

    check_testing()


root = Tk()

root.title("Reconhecimento Facial App")

# Configuração da aparência do root
root.config(bg="black")  # Cor de fundo preta

style = ttk.Style()
style.configure("TFrame", background="black", foreground="black")  # Cor do quadro preto e texto branco
style.configure("TLabel", background="black", foreground="white")  # Cor dos rótulos preta e texto branco
style.configure("TButton", background="white", foreground="black")  # Cor dos botões preta e texto branco

frm = ttk.Frame(root, padding=20, style="TFrame")
frm.grid(sticky=(N, S, E, W))

ttk.Label(frm, text="Chamada da Turma por Reconhecimento Facial", style="TLabel", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=4, pady=5, sticky="ew")

ttk.Button(frm, text="Responder Chamada", command=start_testing).grid(column=0, row=1, padx=5, pady=20)
ttk.Button(frm, text="Treinar Modelo", command=start_training).grid(column=1, row=1, padx=5, pady=20)
ttk.Button(frm, text="Cadastrar novo aluno", command=abrir_formulario).grid(column=2, row=1, padx=5, pady=20)
ttk.Button(frm, text="Painel de presenças", command=abrir_tabela).grid(column=3, row=1, padx=5, pady=20)

footer = ttk.Label(frm, text="©️FelipeValeriano", style="TLabel", font=("Helvetica", 10))
footer.grid(column=0, row=2, columnspan=3, pady=20, sticky=(S, W, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.columnconfigure(2, weight=1)
frm.rowconfigure(0, weight=1)
frm.rowconfigure(1, weight=1)
frm.rowconfigure(2, weight=1)

def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

center_window(root)

root.mainloop()
