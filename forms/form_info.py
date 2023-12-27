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
        self.labelTitulo = tk.Label(self.barra_superior, text="Guidelines and Responsibilities")
        self.labelTitulo.config(fg="#141414", font=("Times New Roman", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Panel Texto
        info = """
        It is essential that users understand the restrictions and responsibilities when using this application. 
        Make sure to read and accept the terms of service of YouTube and various platforms before downloading any content. 
        Here are some key points to keep in mind when using this application:

        -Copyright: Downloading copyrighted videos without proper authorization is illegal. Only download content for which
                    you have the appropriate rights or that is in the public domain.
        -Personal Use: Video downloads should be limited to personal use and comply with copyright laws and YouTube's terms 
                    of service. Commercial use is not allowed without authorization.
        -Legal Information: This application uses the YouTube Data API to retrieve information about videos. Ensure compliance
                    with the YouTube Data API terms of service.
        -Quality and Formats: When downloading videos, select the appropriate quality and format according to options allowed 
                    by YouTube and its API. Do not bypass platform restrictions.
        -User Responsibility: Users are responsible for any violation of YouTube's terms of service or copyright laws. The 
                    application and its developer do not endorse or promote illegal downloading or misuse of content.
        -Updates and Compliance: The application may require updates to comply with changes in YouTube's terms of service. 
                    Users should review and accept any updates before continuing to use the application.

        Remember, the goal is to promote responsible and ethical use of the application, always respecting copyright and policies.
        """
        self.labelInformacion = tk.Label( self.panel_informacion, text=info, justify=tk.LEFT, padx=20, pady=10)
        self.labelInformacion.config(fg="#333", font=("Arial", 11), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelInformacion.pack(side=tk.TOP, fill='both', expand=True)
