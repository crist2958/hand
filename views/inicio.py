from .base import BaseFrame
import tkinter as tk

class InicioFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()
        self.load_sound("inicio", "inicio.mp3")
        self.play_sound("inicio", duck_volume=0.2)

        # Corregido para llamar a add_button con los parámetros necesarios
        self.add_button(
            "rename",
            lambda: (self.stop_sound(1), self.controller.show_frame("LeccionesFrame")),
            150, 550, 434.0, 113.0
        )

    def add_button(self, image_key, command, pos_x, pos_y, width, height):
        """ Método para agregar un botón con imagen escalada """
        if image_key not in self.images:
            return  # Asegúrate de que la imagen esté cargada

        button = tk.Button(
            self.canvas,
            image=self.images[image_key],
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        )

        # Escalar la posición y el tamaño del botón
        scaled_x, scaled_y = self.scale_position(pos_x, pos_y)
        scaled_width, scaled_height = self.scale_size(width, height)
        
        # Colocar el botón en el canvas con la posición y tamaño escalados
        button.place(x=scaled_x, y=scaled_y, width=scaled_width, height=scaled_height)

        button.image = self.images[image_key]  # Mantener referencia de la imagen

    