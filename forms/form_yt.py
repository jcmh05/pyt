import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from config import COLOR_CUERPO_PRINCIPAL
from PIL import Image, ImageTk
from pytube import YouTube
from io import BytesIO
import requests
import re
import os

#
# 
#
#
#

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
        self.frame_input.pack(side=tk.TOP, padx=20, pady=10)
        self.label_url = tk.Label(self.frame_input, text="URL:", font=("Arial", 14), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_url.pack(side=tk.LEFT, padx=(0, 10))
        self.entry_informacion = tk.Entry(self.frame_input, font=("Arial", 14))
        self.entry_informacion.pack(side=tk.LEFT, fill='both')
        self.boton_mostrar_info = tk.Button(self.frame_input, text="Search", command=self.search_url)
        self.boton_mostrar_info.pack(side=tk.LEFT, padx=10)

        # Panel de log para mensajes
        self.log_panel = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.log_panel.pack(side=tk.BOTTOM, fill=tk.X)
        self.log_label = tk.Label(self.log_panel, text="", fg="red", bg=COLOR_CUERPO_PRINCIPAL)
        self.log_label.pack(side=tk.LEFT, padx=10)

    # Funcionamiento del botón de búsqueda
    def search_url(self):
        url = self.entry_informacion.get()
        if self.validate_url_youtube(url):
            try:
                video = YouTube(url)
                image_url = video.thumbnail_url
                title_url = video.title
                self.show_video_info(image_url, title_url) # Mostramos la información del video
            except Exception as e:
                self.mostrar_mensaje("Error: " + str(e))
        else:
            self.mostrar_mensaje("URL no válida")

    # Comprueba si la url corresponde youtube
    def validate_url_youtube(self, url):
        regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$'
        return re.match(regex, url) is not None

    # Muestra la miniatura y titulo del video
    def show_video_info(self, image_url, title_url):
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        if hasattr(self, 'video_options'):
            self.video_options.destroy()

        self.video_options = tk.Frame(self.panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.video_options.pack(padx=20, pady=10)

        self.video_info = tk.Frame(self.video_options, bg=COLOR_CUERPO_PRINCIPAL)
        self.video_info.pack(side=tk.LEFT, padx=20, pady=10)

        # Miniatura
        self.youtube_thumbnail = tk.Label(self.video_info, image=img)
        self.youtube_thumbnail.image = img  # mantener referencia
        self.youtube_thumbnail.pack(side=tk.TOP, pady=10)

        # Titulo video
        self.youtube_title = tk.Label(self.video_info, text=title_url, bg=COLOR_CUERPO_PRINCIPAL)
        self.youtube_title.pack(side=tk.BOTTOM, pady=10)

        # Botones Video/Audio
        self.right_panel = tk.Frame(self.video_options)
        self.right_panel.pack(side=tk.RIGHT, padx=10)
        self.formato_seleccionado = tk.StringVar(value="mp4") # Variable para almacenar la selección
        rb_mp4 = ttk.Radiobutton(self.right_panel, text="Video (MP4)", variable=self.formato_seleccionado, value="mp4")
        rb_mp4.pack(side=tk.TOP, padx=5, pady=5)
        rb_mp3 = ttk.Radiobutton(self.right_panel, text="Audio (MP3)", variable=self.formato_seleccionado, value="mp3")
        rb_mp3.pack(side=tk.TOP, padx=5, pady=5)

        # Verificar si ya existe el panel de descarga y destruirlo si es necesario
        if hasattr(self, 'download_panel'):
            self.download_panel.destroy()

        # Crear el panel para la selección de la ruta de descarga
        self.download_panel = tk.Frame(self.panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.download_panel.pack(side=tk.TOP, padx=20, pady=10)

        self.label_download_path = tk.Label(self.download_panel, text="Ruta de Descarga:", font=("Arial", 14), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_download_path.pack(side=tk.LEFT, padx=(0, 10))

        self.entry_download_path = tk.Entry(self.download_panel, font=("Arial", 14))
        self.entry_download_path.pack(side=tk.LEFT, fill='both', expand=True)
        self.entry_download_path.insert(0, os.path.join(os.path.expanduser('~'), 'Downloads'))

        self.button_select_path = tk.Button(self.download_panel, text="Seleccionar", command=self.select_download_path)
        self.button_select_path.pack(side=tk.LEFT, padx=10)

        # Botón de descarga
        self.button_download = tk.Button(self.download_panel, text="Descargar", command=self.download_video)
        self.button_download.pack(side=tk.LEFT, padx=10)

    def mostrar_mensaje(self, mensaje):
        # Actualizar el texto del log
        self.log_label.config(text=mensaje)

        # Auto-limpiar el mensaje después de un tiempo
        self.log_label.after(5000, lambda: self.log_label.config(text=""))

    def select_download_path(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.entry_download_path.delete(0, tk.END)
            self.entry_download_path.insert(0, folder_selected)

    def download_video(self):
        url = self.entry_informacion.get()
        download_path = self.entry_download_path.get()
        formato = self.formato_seleccionado.get()

        if self.validate_url_youtube(url):
            try:
                video = YouTube(url)
                if formato == "mp4":
                    video_stream = video.streams.get_highest_resolution()
                else:  # formato == "mp3"
                    video_stream = video.streams.filter(only_audio=True).first()

                # Descargar el video
                video_stream.download(output_path=download_path)
                self.mostrar_mensaje("Descarga completada en: " + download_path)
            except Exception as e:
                self.mostrar_mensaje("Error: " + str(e))
        else:
            self.mostrar_mensaje("URL no válida")
