from .base import BaseFrame
import tkinter as tk


class VocalesFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()
        self._create_vowel_buttons()
        self._create_action_buttons()

    def _create_vowel_buttons(self):
        # Botones de vocales
        vowels = [
            ("a_vocal", 170, 347, "a"),
            ("vocal_e", 560, 347, "e"),
            ("vocal_i", 950, 347, "i"),
            ("vocal_o", 170, 567, "o"),
            ("vocal_u", 560, 567, "u")
        ]

        for img_name, x, y, vowel in vowels:
            self._create_button(img_name, x, y, lambda v=vowel: self._handle_vowel(v))

    def _create_action_buttons(self):
        # Botón de examen
        self._create_button("examen_vocal", 950, 567, lambda: self.controller.show_frame("ExamenFrame"))

        # Botón de regreso
        self._create_button("regresar", 950, 209, lambda: self.controller.show_frame("LeccionesFrame"))

    def _create_button(self, image_name, x, y, command):
        if image_name not in self.images:
            return

        btn = tk.Button(
            self.canvas,
            image=self.images[image_name],
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        )
        btn.place(x=x, y=y, width=200, height=71 if image_name == "regresar" else 200)
        btn.image = self.images[image_name]  # Mantener referencia

    def _handle_vowel(self, vowel):
        print(f"Vocal seleccionada: {vowel.upper()}")
        # Lógica específica para cada vocal
        # Ej: self.controller.show_frame(f"{vowel}VocalFrame")