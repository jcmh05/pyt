import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL
from PIL import Image, ImageTk
from pytube import YouTube
from io import BytesIO
import requests
import re

class FormYTDesign():
    def __init__(self, panel_principal):
        self.panel_principal = panel_principal # Guardamos referencia al panel principal

        # Panel Titulo
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 
        
        self.labelTitulo = tk.Label(self.barra_superior, text="YouTube")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Panel Input URL (Etiqueta, input y botón)
        self.frame_input = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.frame_input.pack(side=tk.TOP, fill='both', padx=20, pady=10)
        self.label_url = tk.Label(self.frame_input, text="URL:", font=("Arial", 14), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_url.pack(side=tk.LEFT, padx=(0, 10))
        self.entry_informacion = tk.Entry(self.frame_input, font=("Arial", 14))
        self.entry_informacion.pack(side=tk.LEFT, fill='both')
        self.boton_mostrar_info = tk.Button(self.frame_input, text="Search", command=self.search_url)
        self.boton_mostrar_info.pack(side=tk.LEFT, padx=10)

        # Miniatura y opciones

    def search_url(self):
        url = self.entry_informacion.get()
        if self.validar_url_youtube(url):
            try:
                video = YouTube(url)
                image_url = video.thumbnail_url
                title_url = video.title
                self.show_video_info(image_url, title_url) # Mostramos la información del video
            except Exception as e:
                self.mostrar_mensaje("Error: " + str(e))
        else:
            self.mostrar_mensaje("URL no válida")

    def validar_url_youtube(self, url):
        regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$'
        return re.match(regex, url) is not None

    def show_video_info(self, image_url, title_url):
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        if hasattr(self, 'miniatura_label'):
            self.miniatura_label.destroy()
        if hasattr(self, 'titulo_label'):
            self.titulo_label.destroy()

        self.miniatura_label = tk.Label(self.panel_principal, image=img)
        self.miniatura_label.image = img  # mantener referencia
        self.miniatura_label.pack(side=tk.LEFT, pady=10)

        # Mostrar el título debajo de la miniatura
        self.titulo_label = tk.Label(self.panel_principal, text=title_url)
        self.titulo_label.pack(side=tk.BOTTOM, pady=10)

    def mostrar_mensaje(self, mensaje):
        if hasattr(self, 'miniatura_label'):
            self.miniatura_label.destroy()
        if hasattr(self, 'titulo_label'):
            self.titulo_label.destroy()
        self.miniatura_label = tk.Label(self.panel_principal, text=mensaje)
        self.miniatura_label.pack(side=tk.LEFT, pady=10)
