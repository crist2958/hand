from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/vocales"

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
image_image_1 = PhotoImage(file=relative_to_assets("panel_vocales.png"))
canvas.create_image(720, 512, image=image_image_1)

# Botones con declaración individual
button_image_1 = PhotoImage(file=relative_to_assets("a_vocal.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(x=170.0, y=347.0, width=200.0, height=200.0)

button_image_2 = PhotoImage(file=relative_to_assets("vocal_u.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(x=560.0, y=567.0, width=200.0, height=200.0)

button_image_3 = PhotoImage(file=relative_to_assets("regresar.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(x=950.0, y=209.0, width=200.0, height=71.0)

button_image_4 = PhotoImage(file=relative_to_assets("vocal_e.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(x=560.0, y=347.0, width=200.0, height=200.0)

button_image_5 = PhotoImage(file=relative_to_assets("examen_vocal.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(x=950.0, y=567.0, width=200.0, height=200.0)

button_image_6 = PhotoImage(file=relative_to_assets("vocal_i.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(x=950.0, y=347.0, width=200.0, height=200.0)

button_image_7 = PhotoImage(file=relative_to_assets("vocal_o.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(x=170.0, y=567.0, width=200.0, height=200.0)

window.resizable(False, False)
window.mainloop()