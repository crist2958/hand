from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/examen"  # Ruta relativa corregida

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

# Imagen centrada
image_image_1 = PhotoImage(file=relative_to_assets("examen_panel.png"))
canvas.create_image(
    720,  # Centro horizontal (1440/2)
    512,  # Centro vertical (1024/2)
    image=image_image_1
)

# Botón con posición y tamaño original
button_image_1 = PhotoImage(file=relative_to_assets("comenzar_regre.png"))
Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
).place(
    x=112.0,
    y=609.0,
    width=455.0,
    height=84.368896484375  # Mantenemos la precisión original
)

window.resizable(False, False)
window.mainloop()