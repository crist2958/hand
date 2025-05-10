# views/lecciones.py
from .base import BaseFrame
import tkinter as tk

class LeccionesFrame(BaseFrame):
    def create_widgets(self):
        # Crear canvas con fondo
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=self.screen_height, width=self.screen_width)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.create_image(self.screen_width // 2, self.screen_height // 2, image=self.images["background"])


        self._create_back_button()
        # Botones con posiciones y tamaños ajustados
        self.add_button("leccion_abecedario", lambda: self.controller.show_frame("AbecedarioFrame"), 350, 398, 300, 300)
        self.add_button("leccion_frase", lambda: self.controller.show_frame("FrasesFrame"), 800, 398, 300, 300)

    def add_button(self, image_name, command, x, y, width, height):
        """Método para crear botones con imágenes y escalarlos según la resolución"""
        btn = tk.Button(
            self.canvas,
            image=self.images[image_name],
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        )
        pos_x, pos_y = self.scale_position(x, y)  # Escalar la posición
        scaled_width, scaled_height = self.scale_size(width, height)  # Escalar el tamaño
        btn.place(x=pos_x, y=pos_y, width=scaled_width, height=scaled_height)
        btn.image = self.images[image_name]  # Mantener la referencia de la imagen

    def _create_back_button(self):
        if "button_26" not in self.images:
            return
        btn = tk.Button(
            self.canvas,
            image=self.images["button_26"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.controller.show_frame("InicioFrame")
        )
        pos_x, pos_y = self.scale_position(1032.0, 228.0)
        sw, sh = self.scale_size(200.0, 71.0)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images["button_26"]


