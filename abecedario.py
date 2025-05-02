from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/abecedario"

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

# Imagen de fondo centrada
image_image_1 = PhotoImage(file=relative_to_assets("abecedario_panel.png"))
canvas.create_image(720, 512, image=image_image_1)

# Botones con posiciones originales
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
).place(x=180.0, y=357.0, width=100.0, height=80.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
).place(x=180.0, y=467.0, width=100.0, height=80.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
).place(x=340.0, y=467.0, width=100.0, height=80.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
).place(x=342.623, y=357.0, width=97.377, height=80.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
).place(x=500.0, y=467.0, width=100.0, height=80.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
).place(x=500.0, y=357.0, width=100.0, height=80.0)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
).place(x=660.0, y=467.0, width=100.0, height=80.0)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
).place(x=662.623, y=357.0, width=97.377, height=80.0)

button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
).place(x=820.0, y=467.0, width=100.0, height=80.0)

button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
).place(x=820.0, y=357.0, width=100.0, height=80.0)

button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
).place(x=1140.0, y=357.0, width=100.0, height=80.0)

button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
).place(x=1140.0, y=467.0, width=100.0, height=80.0)

button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))
Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
).place(x=1140.0, y=577.0, width=100.0, height=80.0)

button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
).place(x=1140.0, y=687.0, width=100.0, height=80.0)

button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))
Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
).place(x=180.0, y=577.0, width=100.0, height=80.0)

button_image_16 = PhotoImage(file=relative_to_assets("button_16.png"))
Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
).place(x=342.623, y=577.0, width=97.377, height=80.0)

button_image_17 = PhotoImage(file=relative_to_assets("button_17.png"))
Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
).place(x=500.0, y=577.0, width=100.0, height=80.0)

button_image_18 = PhotoImage(file=relative_to_assets("button_18.png"))
Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
).place(x=662.623, y=577.0, width=97.377, height=80.0)

button_image_19 = PhotoImage(file=relative_to_assets("button_19.png"))
Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
).place(x=820.0, y=687.0, width=100.0, height=80.0)

button_image_20 = PhotoImage(file=relative_to_assets("button_20.png"))
Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
).place(x=659.0, y=686.0, width=100.0, height=80.0)

button_image_21 = PhotoImage(file=relative_to_assets("button_21.png"))
Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
).place(x=820.0, y=577.0, width=100.0, height=80.0)

button_image_22 = PhotoImage(file=relative_to_assets("button_22.png"))
Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
).place(x=980.0, y=467.0, width=100.0, height=80.0)

button_image_23 = PhotoImage(file=relative_to_assets("button_23.png"))
Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
).place(x=980.0, y=357.0, width=100.0, height=80.0)

button_image_24 = PhotoImage(file=relative_to_assets("button_24.png"))
Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
).place(x=980.0, y=687.0, width=100.0, height=80.0)

button_image_25 = PhotoImage(file=relative_to_assets("button_25.png"))
Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
).place(x=980.0, y=577.0, width=100.0, height=80.0)

button_image_26 = PhotoImage(file=relative_to_assets("button_26.png"))
Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
).place(x=1032.0, y=228.0, width=200.0, height=71.0)

window.resizable(False, False)
window.mainloop()