from .base import BaseFrame
import tkinter as tk
from pathlib import Path

class FrasesFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()

        self.assets_path = Path(__file__).parent.parent / 'assets' / 'inicio'
        self._load_common_images()
        self._create_phrase_buttons()
        self._create_back_button()

    def _load_common_images(self):
        image_names = [
            "Regresar", "hola", "DeNada", "ComoEstas", "Adios", "PorFavor",
            "Gracias", "Perdon", "BuenosDias", "BuenasNoches", "Examen"
        ]

        for name in image_names:
            path = self.assets_path / f"{name}.gif"
            if path.exists():
                self._load_image(path, name)
            else:
                print(f"[WARN] Imagen '{name}.gif' no encontrada en assets.")

    def _create_phrase_buttons(self):
        button_data = [
            ("hola", 170.0, 347.0, 150.0, 150.0),
            ("DeNada", 170.0, 567.0, 150.0, 150.0),
            ("ComoEstas", 380.746, 567.0, 149.254, 150.0),
            ("Adios", 376.0, 347.0, 152.515, 150.0),
            ("PorFavor", 590.0, 567.0, 150.0, 150.0),
            ("Gracias", 590.0, 347.0, 150.0, 150.0),
            ("Perdon", 800.746, 567.0, 149.254, 150.0),
            ("BuenosDias", 796.0, 347.0, 152.515, 150.0),
            #("Examen", 1010.0, 567.0, 150.0, 150.0),
            ("BuenasNoches", 1010.0, 347.0, 150.0, 150.0),
        ]

        for name, x, y, w, h in button_data:
            self._create_phrase_button(name, lambda n=name: self._handle_phrase(n), x, y, w, h)

    def _create_phrase_button(self, image_name, command, x, y, width, height):
        if image_name not in self.images:
            print(f"[WARN] Imagen {image_name} no cargada.")
            return

        btn = tk.Button(
            self.canvas,
            image=self.images[image_name],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=command
        )
        pos_x, pos_y = self.scale_position(x, y)
        sw, sh = self.scale_size(width, height)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images[image_name]

    def _create_back_button(self):
        if "Regresar" not in self.images:
            print("[WARN] Imagen 'Regresar' no cargada.")
            return

        btn = tk.Button(
            self.canvas,
            image=self.images["Regresar"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.controller.show_frame("LeccionesFrame")
        )
        pos_x, pos_y = self.scale_position(959.0, 209.0)
        sw, sh = self.scale_size(200.0, 71.0)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images["Regresar"]

    def _handle_phrase(self, phrase_name):
        frases_dict = {
            "hola": "hola",
            "DeNada": "Denada",
            "ComoEstas": "Comoestas",
            "Adios": "Hastaluego",
            "PorFavor": "Porfa",
            "Gracias": "Gracias",
            "Perdon": "perdon",
            "BuenosDias": "Buenosdias",
            "BuenasNoches": "Buenasnoches"
        }

        mensaje = frases_dict.get(phrase_name, "Frase no encontrada")

        # Redirigir al frame que muestra la frase y pasarle el mensaje
        frame_destino = self.controller.frames["FrasesLeccionFrame"]
        frame_destino.set_letter(mensaje)
        self.controller.show_frame("FrasesLeccionFrame")
