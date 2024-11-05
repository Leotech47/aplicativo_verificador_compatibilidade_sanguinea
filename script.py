import tkinter as tk
from tkinter import ttk


def verificar_compatibilidade(doador, receptor):
    compatibilidade = {
        1: (1, 5, 6),  # A+
        2: (2, 6),  # A-
        3: (3, 5, 6),  # B+
        4: (4, 6),  # B-
        5: (5, 6),  # O+
        6: (6,),  # O-
        7: (1, 2, 3, 4, 5, 6, 7, 8),  # AB+
        8: (2, 4, 6, 8)  # AB-
    }
    if doador in compatibilidade:
        if receptor in compatibilidade[doador]:
            return 'Doação compatível!'
        else:
            return 'Doação incompatível!'
    else:
        return "Tipo sanguíneo inválido!"

def verificar():
    try:
        receptor = int(receptor_combo.get())
        doador = int(doador_combo.get())
        resultado_label.config(text=verificar_compatibilidade(doador, receptor))
    except ValueError:
        resultado_label.config(text="Selecione os tipos sanguíneos.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Testador de Compatibilidade Sanguínea")
janela.geometry("800x500")  # Definir tamanho da janela
janela.configure(bg="#E0E0E0")  # Cor de fundo

# Criar os elementos da interface
style = ttk.Style()
style.configure("TLabel", background="lightgray", font=("Arial", 14))  # Define o estilo dos labels

ttk.Label(janela, text="Tipo Sanguíneo do Receptor:", style="TLabel").grid(row=0, column=0, padx=50, pady=50)
receptor_combo = ttk.Combobox(janela, values=[1, 2, 3, 4, 5, 6, 7, 8])
receptor_combo.grid(row=0, column=1, padx=50, pady=50)

ttk.Label(janela, text="Tipo Sanguíneo do Doador:", style="TLabel").grid(row=1, column=0, padx=50, pady=50)
doador_combo = ttk.Combobox(janela, values=[1, 2, 3, 4, 5, 6, 7, 8])
doador_combo.grid(row=1, column=1, padx=50, pady=50)

verificar_button = ttk.Button(janela, text="Verificar", command=verificar)
verificar_button.grid(row=2, column=0, columnspan=2, pady=100)

resultado_label = ttk.Label(janela, text="")
resultado_label.grid(row=3, column=0, columnspan=2)


# Iniciar a interface
janela.mainloop()
