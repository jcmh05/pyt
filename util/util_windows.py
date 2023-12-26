#Centra la ventana en el centro de la pantalla al abrirse
def center_windows(windows, app_width, app_height):
    screen_width = windows.winfo_screenwidth()
    screen_height = windows.winfo_screenheight()
    x = int( (screen_width/2) - (app_width/2) )
    y = int( (screen_height/2) - (app_height/2) )
    return windows.geometry(f"{app_width}x{app_height}+{x}+{y}")
