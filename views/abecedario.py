from .base import BaseFrame
import tkinter as tk


class AbecedarioFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()
        self._create_buttons()
        self._create_back_button()

    def _create_buttons(self):
        # Lista de botones con sus coordenadas y tamaños exactos
        button_data = [
            (1, 180.0, 357.0, 100.0, 80.0),
            (2, 180.0, 467.0, 100.0, 80.0),
            (3, 340.0, 467.0, 100.0, 80.0),
            (4, 342.623, 357.0, 97.377, 80.0),
            (5, 500.0, 467.0, 100.0, 80.0),
            (6, 500.0, 357.0, 100.0, 80.0),
            (7, 660.0, 467.0, 100.0, 80.0),
            (8, 662.623, 357.0, 97.377, 80.0),
            (9, 820.0, 467.0, 100.0, 80.0),
            (10, 820.0, 357.0, 100.0, 80.0),
            (11, 1140.0, 357.0, 100.0, 80.0),
            (12, 1140.0, 467.0, 100.0, 80.0),
            (13, 1140.0, 577.0, 100.0, 80.0),
            (14, 1140.0, 687.0, 100.0, 80.0),
            (15, 180.0, 577.0, 100.0, 80.0),
            (16, 342.623, 577.0, 97.377, 80.0),
            (17, 500.0, 577.0, 100.0, 80.0),
            (18, 662.623, 577.0, 97.377, 80.0),
            (19, 820.0, 687.0, 100.0, 80.0),
            (20, 659.0, 686.0, 100.0, 80.0),
            (21, 820.0, 577.0, 100.0, 80.0),
            (22, 980.0, 467.0, 100.0, 80.0),
            (23, 980.0, 357.0, 100.0, 80.0),
            (24, 980.0, 687.0, 100.0, 80.0),
            (25, 980.0, 577.0, 100.0, 80.0)
        ]

        for btn in button_data:
            self._create_button(*btn)

    def _create_button(self, button_num, x, y, width, height):
        image_name = f"button_{button_num}"
        if image_name not in self.images:
            return

        btn = tk.Button(
            self.canvas,
            image=self.images[image_name],
            borderwidth=0,
            highlightthickness=0,
            command=lambda n=button_num: print(f"button_{n} clicked"),
            relief="flat"
        )
        btn.place(x=x, y=y, width=width, height=height)
        btn.image = self.images[image_name]

    def _create_back_button(self):
        """Botón de regreso (button_26)"""
        if "button_26" not in self.images:
            return

        btn = tk.Button(
            self.canvas,
            image=self.images["button_26"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame("LeccionesFrame"),
            relief="flat"
        )
        btn.place(x=1032.0, y=228.0, width=200.0, height=71.0)
        btn.image = self.images["button_26"]