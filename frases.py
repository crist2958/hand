from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/Frases"  # Ruta relativa corregida

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

# Imagen centrada (1440x1024)
image_image_1 = PhotoImage(file=relative_to_assets("FrasesPanel.png"))
canvas.create_image(
    720,  # Centro horizontal (1440/2)
    512,  # Centro vertical (1024/2)
    image=image_image_1
)

# Botones con posiciones y tamaños originales
button_image_1 = PhotoImage(file=relative_to_assets("hola.png"))
Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
).place(x=170.0, y=347.0, width=150.0, height=150.0)

button_image_2 = PhotoImage(file=relative_to_assets("DeNada.png"))
Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
).place(x=170.0, y=567.0, width=150.0, height=150.0)

button_image_3 = PhotoImage(file=relative_to_assets("ComoEstas.png"))
Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
).place(x=380.746, y=567.0, width=149.254, height=150.0)

button_image_4 = PhotoImage(file=relative_to_assets("Regresar.png"))
Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
).place(x=959.0, y=209.0, width=200.0, height=71.0)

button_image_5 = PhotoImage(file=relative_to_assets("Adios.png"))
Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
).place(x=376.0, y=347.0, width=152.515, height=150.0)

button_image_6 = PhotoImage(file=relative_to_assets("PorFavor.png"))
Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
).place(x=590.0, y=567.0, width=150.0, height=150.0)

button_image_7 = PhotoImage(file=relative_to_assets("Gracias.png"))
Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
).place(x=590.0, y=347.0, width=150.0, height=150.0)

button_image_8 = PhotoImage(file=relative_to_assets("Perdon.png"))
Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
).place(x=800.746, y=567.0, width=149.254, height=150.0)

button_image_9 = PhotoImage(file=relative_to_assets("BuenosDias.png"))
Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
).place(x=796.0, y=347.0, width=152.515, height=150.0)

button_image_10 = PhotoImage(file=relative_to_assets("Examen.png"))
Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
).place(x=1010.0, y=567.0, width=150.0, height=150.0)

button_image_11 = PhotoImage(file=relative_to_assets("BuenasNoches.png"))
Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
).place(x=1010.0, y=347.0, width=150.0, height=150.0)

window.resizable(False, False)
window.mainloop()