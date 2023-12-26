import tkinter as tk
from tkinter import font
from config import COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.util_windows as util_windows
import util.util_images as util_img
from forms.form_info import FormInfoDesign
from forms.form_yt import FormYTDesign

class FormMasterDesign(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.logo = util_img.read_image("./images/pytLogo.png",(560,136))
        self.profile = util_img.read_image("./images/pytLogo.png",(100,100))
        self.config_windows()
        self.panels()
        self.menu_lateral_controls()
        self.body_controls()

    def config_windows(self):
        # Configuración inicial de la ventana
        self.title('PYT Media Downloader')
        self.iconbitmap("./images/logo.ico")
        w,h = 1024,600
        util_windows.center_windows(self,w,h)

    def panels(self):
        # Crea panel menu lateral y cuerpo principal
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.main_body = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.main_body.pack(side =tk.RIGHT,fill='both', expand=True)

    def menu_lateral_controls(self):
        # Configuración del menú
        width_menu = 150  # Aumentar el ancho del botón si es necesario
        height_menu = 30  # Aumentar la altura del botón si es necesario
        font_size = 12  # Aumentar el tamaño de la fuente para el texto si es necesario
        font_awesome = font.Font(family='FontAwesome', size=font_size)

        # Etiqueta de perfil
        self.labelProfile = tk.Label(self.menu_lateral, image=self.profile, bg=COLOR_MENU_LATERAL)
        self.labelProfile.pack(side=tk.TOP, pady=10)

        # Botones
        self.buttonYT = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)

        # Imágenes para los botones
        img_youtube = util_img.read_image("./images/youtube.png", (20, 20))
        img_info = util_img.read_image("./images/info.png", (20, 20))

        buttons_info = [
            ("Youtube", img_youtube, self.buttonYT, self.open_panel_yt),
            ("Info", img_info, self.buttonInfo, self.open_panel_info),
        ]

        for text, img, button, command in buttons_info:
            self.configure_button_menu(button, text, img, font_awesome, width_menu, height_menu, command)

    def configure_button_menu(self, button, text, img, font_awesome, width_menu, height_menu, command):
        # Configura el botón con imagen y texto
        button.config(image=img, text=f"  {text}", compound="left", anchor="w", font=font_awesome,
                    bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=width_menu, height=height_menu, command=command)
        button.pack(side=tk.TOP, fill='x', padx=5, pady=5)  # fill='x' hace que el botón llene el espacio horizontal
        button.image = img  # Guardar referencia a la imagen
        self.bind_hover_events(button)

    
    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')
    
    # Control del cuerpo principal
    def body_controls(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.main_body, image=self.profile, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Función para limpiar el contenido del panel
    def clear_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()

    # Apertura de paneles
    def open_panel_info(self):   
        self.clear_panel(self.main_body)     
        FormInfoDesign(self.main_body)  
    
    def open_panel_yt(self):   
        self.clear_panel(self.main_body)     
        FormYTDesign(self.main_body) 