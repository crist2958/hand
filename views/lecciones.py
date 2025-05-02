# Ejemplo views/lecciones.py
from .base import BaseFrame
import tkinter as tk


class LeccionesFrame(BaseFrame):
    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=1024, width=1440)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.create_image(720, 512, image=self.images["background"])

        # Botones
        self.create_button("leccion_abecedario", 180, 398, "AbecedarioFrame")
        self.create_button("leccion_frase", 933, 398, "FrasesFrame")

    def create_button(self, image_name, x, y, target_frame):
        btn = tk.Button(
            self.canvas,
            image=self.images[image_name],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame(target_frame),
            relief="flat"
        )
        btn.place(x=x, y=y, width=300, height=300)

