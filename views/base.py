# views/base.py

import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
import pygame


class BaseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Resolución base y escalado
        self.base_width = 1440
        self.base_height = 1024
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.scale_x = self.screen_width / self.base_width
        self.scale_y = self.screen_height / self.base_height

        self.assets_path = self.get_assets_path()
        self.images = {}
        self.sounds = {}

        self.load_assets()
        self.create_widgets()

    def get_assets_path(self):
        """
        Obtiene la ruta de la carpeta de assets basada en el nombre del frame actual.
        Por ejemplo: AbecedarioLeccionFrame → assets/abecedarioleccion
        """
        class_name = self.__class__.__name__.replace("Frame", "").lower()
        return Path(__file__).parent.parent / "assets" / class_name

    def load_assets(self):
        """
        Carga la imagen de fondo (nombre_panel.png) y todas las demás imágenes .png del directorio.
        """
        fondo_path = self.assets_path / f"{self.assets_path.name}_panel.png"
        if fondo_path.exists():
            self._load_image(fondo_path, "background")

        for asset_file in self.assets_path.glob("*.png"):
            if asset_file.name != f"{self.assets_path.name}_panel.png":
                self._load_image(asset_file, asset_file.stem)

    def _load_image(self, path, key):
        try:
            img = Image.open(path)
            if key == "background":
                target_size = (self.screen_width, self.screen_height)
            else:
                width = int(img.width * self.scale_x)
                height = int(img.height * self.scale_y)
                target_size = (width, height)

            resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
            self.images[key] = ImageTk.PhotoImage(resized_img)
        except Exception as e:
            print(f"[ERROR] Cargando imagen '{path}': {e}")

    def create_widgets(self):
        """
        Crea un canvas y establece el fondo si está disponible.
        """
        self.canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            width=self.screen_width,
            height=self.screen_height,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(expand=True, fill="both")

        if "background" in self.images:
            self.canvas.create_image(
                self.screen_width // 2,
                self.screen_height // 2,
                image=self.images["background"],
                tags="background"
            )
        else:
            print("[INFO] Fondo no cargado.")

    def add_button(self, image_key, command, pos_x, pos_y, width, height):
        """
        Agrega un botón con imagen escalado a la posición y tamaño proporcionados.
        """
        if image_key not in self.images:
            print(f"[WARNING] Imagen '{image_key}' no encontrada.")
            return

        scaled_x, scaled_y = self.scale_position(pos_x, pos_y)
        scaled_width, scaled_height = self.scale_size(width, height)

        button = tk.Button(
            self.canvas,
            image=self.images[image_key],
            command=command,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.canvas.create_window(scaled_x, scaled_y, window=button, width=scaled_width, height=scaled_height)

    def scale_position(self, x, y):
        return int(x * self.scale_x), int(y * self.scale_y)

    def scale_size(self, width, height):
        return int(width * self.scale_x), int(height * self.scale_y)

    def load_sound(self, sound_name, filename):
        """
        Carga un efecto de sonido desde el audio manager del controlador.
        """
        sound = self.controller.audio_manager.load_effect(filename)
        if sound:
            self.sounds[sound_name] = sound
        else:
            print(f"[ERROR] No se pudo cargar el sonido: {filename}")

    def play_sound(self, sound_name, channel=1, duck_volume=0.2):
        """
        Reproduce un sonido si ha sido cargado.
        """
        if sound_name in self.sounds:
            self.controller.audio_manager.play_effect(
                self.sounds[sound_name],
                channel=channel,
                duck_volume=duck_volume
            )
        else:
            print(f"[WARNING] Sonido '{sound_name}' no encontrado.")



    def on_show(self):
        """
        Método que puede sobrescribirse en subclases para acciones al mostrar el frame.
        """
        pass

    def stop_sound(self, channel=1):
        if channel in self.controller.audio_manager.effect_channels:
            self.controller.audio_manager.effect_channels[channel].stop()


