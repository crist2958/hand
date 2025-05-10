# views/abecedario.py
from .base import BaseFrame
import tkinter as tk
from pathlib import Path

class AbecedarioFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()

        # Cargar imagen 'rename' para botón de regreso


        self._create_buttons()
        #self._create_exam_button()
        self._create_back_button()

    def _create_buttons(self):
        # Datos de los botones: número, letra, posición y tamaño
        button_data = [
            (1, 'A', 180.0, 357.0, 100.0, 80.0),
            (2, 'H', 180.0, 467.0, 100.0, 80.0),
            (3, 'I', 340.0, 467.0, 100.0, 80.0),
            (4, 'B', 342.623, 357.0, 97.377, 80.0),
            (5, 'J', 500.0, 467.0, 100.0, 80.0),
            (6, 'C', 500.0, 357.0, 100.0, 80.0),
            (7, 'K', 660.0, 467.0, 100.0, 80.0),
            (8, 'D', 662.623, 357.0, 97.377, 80.0),
            (9, 'L', 820.0, 467.0, 100.0, 80.0),
            (10, 'E', 820.0, 357.0, 100.0, 80.0),
            (11, 'G', 1140.0, 357.0, 100.0, 80.0),
            (12, 'N', 1140.0, 467.0, 100.0, 80.0),
            (13, 'T', 1140.0, 577.0, 100.0, 80.0),
            (14, 'V', 1140.0, 687.0, 100.0, 80.0),
            (15, 'Ñ', 180.0, 577.0, 100.0, 80.0),
            (16, 'O', 342.623, 577.0, 97.377, 80.0),
            (17, 'P', 500.0, 577.0, 100.0, 80.0),
            (18, 'Q', 662.623, 577.0, 97.377, 80.0),
            (19, 'X', 820.0, 687.0, 100.0, 80.0),
            (26, 'Y', 659.0, 686.0, 100.0, 80.0),
            (21, 'R', 820.0, 577.0, 100.0, 80.0),
            (22, 'M', 980.0, 467.0, 100.0, 80.0),
            (23, 'V', 980.0, 357.0, 100.0, 80.0),
            (24, 'W', 980.0, 687.0, 100.0, 80.0),
            (27, 'S', 980.0, 577.0, 100.0, 80.0),
            (25, 'Z', 500.0, 687.0, 100.0, 80.0),
        ]
        for num, letter, x, y, w, h in button_data:
            self._create_button(num, letter, x, y, w, h)


    def _create_button(self, num, letter, x, y, width, height):
        image_name = f"button_{num}"
        if image_name not in self.images:
            print(f"[WARN] Imagen {image_name} no encontrada.")
            return

        btn = tk.Button(
            self.canvas,
            image=self.images[image_name],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda l=letter:  self._go_to_leccion(l)
        )
        pos_x, pos_y = self.scale_position(x, y)
        sw, sh = self.scale_size(width, height)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images[image_name]

    def _go_to_leccion(self, letter):
        self.controller.show_frame("AbecedarioLeccionFrame", letter)


    def _create_back_button(self):
        if "button_28" not in self.images:
            return
        btn = tk.Button(
            self.canvas,
            image=self.images["button_28"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.controller.show_frame("LeccionesFrame")
        )
        pos_x, pos_y = self.scale_position(1032.0, 228.0)
        sw, sh = self.scale_size(200.0, 71.0)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images["button_28"]

    def _create_exam_button(self):
        if "button_20" not in self.images:
            return
        btn = tk.Button(
            self.canvas,
            image=self.images["button_20"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: print("Botón examen presionado")  # Puedes cambiar esta acción
        )
        pos_x, pos_y = self.scale_position(342.623, 687.0)
        sw, sh = self.scale_size(97.377, 80.0)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images["button_20"]

    




