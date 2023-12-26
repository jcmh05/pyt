import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL

class FormInfoDesign():
    def __init__(self, panel_principal):

        # Crear paneles: Titulo y Texto
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 
        self.panel_informacion = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.panel_informacion.pack(side=tk.TOP, fill='both', expand=True)

        # Panel titulo
        self.labelTitulo = tk.Label(self.barra_superior, text="Info")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Panel Texto
        info = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 
        Sed nisi.
        """
        self.labelInformacion = tk.Label( self.panel_informacion, text=info, justify=tk.LEFT, padx=20, pady=10)
        self.labelInformacion.config(fg="#333", font=("Arial", 14), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelInformacion.pack(side=tk.TOP, fill='both', expand=True)
