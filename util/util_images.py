from PIL import ImageTk, Image

# Redimensionar imagen a un tamaño dado
def read_image(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size,Image.ADAPTIVE))