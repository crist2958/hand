from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / ("assets/inicio")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Cargar y redimensionar la imagen
img_path = relative_to_assets("inicio.png")
image = Image.open(img_path)
resized_image = image.resize((1440, 1024))
image_image_1 = ImageTk.PhotoImage(resized_image)

image_1 = canvas.create_image(
    720,
    512,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("rename.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
# Posición modificada: x aumentado de 129.0 a 329.0
button_1.place(
    x=150.0,  # Cambiado de 129.0 a 329.0 (200 píxeles a la derecha)
    y=572.0,
    width=434.0,
    height=113.0
)

window.resizable(False, False)
window.mainloop()