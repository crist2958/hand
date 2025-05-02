from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/lecciones"  # Ruta relativa corregida

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

# Cargar imagen ya dimensionada correctamente
image_image_1 = PhotoImage(file=relative_to_assets("leccion_panel.png"))
# Centrar la imagen en la ventana
canvas.create_image(
    720,  # 1440/2
    512,  # 1024/2
    image=image_image_1
)

# Botones (posición original)
button_image_1 = PhotoImage(file=relative_to_assets("leccion_abecedario.png"))
Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
).place(x=180.0, y=398.0, width=300.0, height=300.0)

button_image_2 = PhotoImage(file=relative_to_assets("leccion_vocal.png"))
Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
).place(x=560.0, y=398.0, width=300.0, height=300.0)

button_image_3 = PhotoImage(file=relative_to_assets("leccion_frase.png"))
Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
).place(x=933.0, y=398.0, width=300.0, height=300.0)

window.resizable(False, False)
window.mainloop()