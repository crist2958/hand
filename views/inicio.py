from .base import BaseFrame
import tkinter as tk


class InicioFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()
        self._create_start_button()
        self.load_sound("inicio", "inicio.mp3")
        self.play_sound("inicio", duck_volume=0.2)

    def _create_start_button(self):
        if "rename" not in self.images:
            return

        self.start_btn = tk.Button(
            self.canvas,
            image=self.images["rename"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame("LeccionesFrame"),
            relief="flat"
        )
        self.start_btn.place(
            x=150.0,
            y=572.0,
            width=434.0,
            height=113.0
        )
        self.start_btn.image = self.images["rename"]  # Mantener referencia