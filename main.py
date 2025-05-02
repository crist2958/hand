from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1440x1024")
        self.configure(bg="#FFFFFF")
        self.title("LSE Learning System")
        self.resizable(False, False)

        # Contenedor principal
        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")

        # Diccionario de frames
        self.frames = {}

        # Inicializar frames
        for F in (InicioFrame, LeccionesFrame):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Usar grid para tkraise

        self.show_frame("InicioFrame")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


class BaseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.assets_path = Path(__file__).parent / "assets" / self.get_assets_folder()
        self.images = {}
        self.load_assets()
        self.create_widgets()

    def get_assets_folder(self):
        return self.__class__.__name__.replace("Frame", "").lower()

    def load_assets(self):
        # Cargar imagen de fondo
        fondo_path = self.assets_path / f"{self.get_assets_folder()}_panel.png"
        if fondo_path.exists():
            img = Image.open(fondo_path)
            self.images["background"] = ImageTk.PhotoImage(img.resize((1440, 1024)))
        else:
            raise FileNotFoundError(f"Fondo no encontrado: {fondo_path}")


class InicioFrame(BaseFrame):
    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=1024, width=1440)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.create_image(720, 512, image=self.images["background"])

        # Botón Rename
        button_img = ImageTk.PhotoImage(Image.open(self.assets_path / "rename.png"))
        self.button = tk.Button(
            self.canvas,
            image=button_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame("LeccionesFrame"),
            relief="flat"
        )
        self.button.image = button_img
        self.button.place(x=150, y=572, width=434, height=113)


class LeccionesFrame(BaseFrame):
    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=1024, width=1440)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.create_image(720, 512, image=self.images["background"])

        # Cargar botones
        buttons = [
            ("leccion_abecedario", 180, 398),
            ("leccion_vocal", 560, 398),
            ("leccion_frase", 933, 398)
        ]

        for name, x, y in buttons:
            img_path = self.assets_path / f"{name}.png"
            btn_img = ImageTk.PhotoImage(Image.open(img_path))
            btn = tk.Button(
                self.canvas,
                image=btn_img,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            btn.image = btn_img
            btn.place(x=x, y=y, width=300, height=300)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()