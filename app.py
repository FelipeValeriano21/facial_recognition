from tkinter import *
from tkinter import ttk, messagebox
import subprocess
import os
import formulario  # Importa el archivo que contiene la lógica del formulario
import tabela

def abrir_formulario():
    formulario.Formulario()  # Llama a la clase que crea el formulario

def abrir_tabela():
    tabela.TabelaSimples()  # Chama a classe que cria a tabela simples


def start_training():
    # Crear una nueva ventana para el progreso del entrenamiento
    progress_window = Toplevel()
    progress_window.title("Treinamento")
    progress_window.config(bg="lightblue")
    progress_window.geometry("300x100")
    
    ttk.Label(progress_window, text="Treinando o modelo...", style="TLabel").pack(pady=20)
    progress_bar = ttk.Progressbar(progress_window, mode='indeterminate')
    progress_bar.pack(fill=X, padx=20, pady=10)
    progress_bar.start()

    # Iniciar el proceso de entrenamiento
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

# Crear la ventana principal
root = Tk()

# Cambiar el título de la ventana
root.title("Mi Programa")

# Cambiar el color de fondo de la ventana
root.config(bg="blue")

# Crear un estilo personalizado para el frame y otros widgets
style = ttk.Style()
style.configure("TFrame", background="blue", foreground="white")
style.configure("TLabel", background="blue", foreground="white")
style.configure("TButton", background="blue", foreground="white")

# Crear un frame con padding
frm = ttk.Frame(root, padding=20, style="TFrame")
frm.grid(sticky=(N, S, E, W))

# Añadir un título en la parte superior
ttk.Label(frm, text="Título Principal", style="TLabel", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=3, pady=10)

# Añadir tres botones en la parte inferior
ttk.Button(frm, text="Botón 1", command=start_testing).grid(column=0, row=1, padx=5, pady=20)
ttk.Button(frm, text="Botón 2", command=start_training).grid(column=1, row=1, padx=5, pady=20)
ttk.Button(frm, text="Abrir Formulario", command=abrir_formulario).grid(column=2, row=1, padx=5, pady=20)
ttk.Button(frm, text="Abrir Tabela", command=abrir_tabela).grid(column=3, row=1, padx=5, pady=20)


# Añadir un footer en la parte inferior
footer = ttk.Label(frm, text="Hecho por [Tu Nombre]", style="TLabel", font=("Helvetica", 10))
footer.grid(column=0, row=2, columnspan=3, pady=20, sticky=(S, W, E))

# Configurar el frame para que se expanda con la ventana
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.columnconfigure(2, weight=1)
frm.rowconfigure(0, weight=1)
frm.rowconfigure(1, weight=1)
frm.rowconfigure(2, weight=1)

# Centrar la ventana
def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

center_window(root)

# Iniciar el bucle principal
root.mainloop()
