import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL

class FormYTDesign():
    def __init__(self, panel_principal):

        # Panel Titulo
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 
        
        self.labelTitulo = tk.Label(self.barra_superior, text="YouTube")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Panel Input URL
        self.frame_input = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.frame_input.pack(side=tk.TOP, fill='both', padx=20, pady=10)
        self.label_url = tk.Label(self.frame_input, text="URL:", font=("Arial", 14), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_url.pack(side=tk.LEFT, padx=(0, 10))
        self.entry_informacion = tk.Entry(self.frame_input, font=("Arial", 14))
        self.entry_informacion.pack(side=tk.LEFT, fill='both')

        #Botón imprimir input
        self.boton_mostrar_info = tk.Button(panel_principal, text="Mostrar Información", command=self.mostrar_informacion)
        self.boton_mostrar_info.pack(side=tk.TOP, pady=10)

    def mostrar_informacion(self):
            texto_ingresado = self.entry_informacion.get()
            if texto_ingresado:
                print("Texto ingresado:", texto_ingresado)
            else:
                print("Por favor, ingresa información antes de hacer clic en Mostrar Información")
