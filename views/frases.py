from .base import BaseFrame
import tkinter as tk


class FrasesFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()
        self._create_phrase_buttons()
        self._create_back_button()

    def _create_phrase_buttons(self):
        # Lista de botones con sus propiedades (imagen, posición, tamaño)
        buttons = [
            ("hola", 170.0, 347.0, 150.0, 150.0, self._handle_hola),
            ("DeNada", 170.0, 567.0, 150.0, 150.0, self._handle_denada),
            ("ComoEstas", 380.746, 567.0, 149.254, 150.0, self._handle_como_estas),
            ("Adios", 376.0, 347.0, 152.515, 150.0, self._handle_adios),
            ("PorFavor", 590.0, 567.0, 150.0, 150.0, self._handle_por_favor),
            ("Gracias", 590.0, 347.0, 150.0, 150.0, self._handle_gracias),
            ("Perdon", 800.746, 567.0, 149.254, 150.0, self._handle_perdon),
            ("BuenosDias", 796.0, 347.0, 152.515, 150.0, self._handle_buenos_dias),
            ("Examen", 1010.0, 567.0, 150.0, 150.0, self._handle_examen),
            ("BuenasNoches", 1010.0, 347.0, 150.0, 150.0, self._handle_buenas_noches)
        ]

        for img, x, y, w, h, cmd in buttons:
            self._create_phrase_button(img, x, y, w, h, cmd)

    def _create_phrase_button(self, image_name, x, y, width, height, command):
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
        btn.place(x=x, y=y, width=width, height=height)
        btn.image = self.images[image_name]

    def _create_back_button(self):
        if "Regresar" not in self.images:
            return

        btn = tk.Button(
            self.canvas,
            image=self.images["Regresar"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame("LeccionesFrame"),
            relief="flat"
        )
        btn.place(x=959.0, y=209.0, width=200.0, height=71.0)
        btn.image = self.images["Regresar"]

    # Manejadores para cada frase
    def _handle_hola(self):
        print("Mostrando frase: Hola")

    def _handle_denada(self):
        print("Mostrando frase: De nada")

    def _handle_como_estas(self):
        print("Mostrando frase: ¿Cómo estás?")

    def _handle_adios(self):
        print("Mostrando frase: Adiós")

    def _handle_por_favor(self):
        print("Mostrando frase: Por favor")

    def _handle_gracias(self):
        print("Mostrando frase: Gracias")

    def _handle_perdon(self):
        print("Mostrando frase: Perdón")

    def _handle_buenos_dias(self):
        print("Mostrando frase: Buenos días")

    def _handle_examen(self):
        self.controller.show_frame("ExamenFrame")

    def _handle_buenas_noches(self):
        print("Mostrando frase: Buenas noches")