from .base import BaseFrame
import tkinter as tk
from tkinter import Label
from pathlib import Path
import pygame
from views.Analisis import run_detection  # ✅ Importar aquí

class AbecedarioLeccionFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()

        self.img_folder = self.assets_path / "Img_Alfabeto"
        self.audio_folder = self.assets_path / "alfabetowav"

        self.letra_img_label = Label(self.canvas, bg="#FFFFFF")
        self.canvas.create_window(
            self.screen_width // 2,
            int(self.screen_height * 0.45),
            window=self.letra_img_label
        )

        self.letra_actual = None
        self._create_back_button()
        self._create_next()

        # Cargar música ambiental
        ambient_path = self.audio_folder / "ambient_music.wav"
        if ambient_path.exists():
            self.load_sound("ambient", ambient_path)
            self.play_sound("ambient", loop=True)
        else:
            print(f"[WARN] Música ambiental no encontrada en {ambient_path}")

    def set_letter(self, letra):
        """Recibe la letra desde AbecedarioFrame, muestra su imagen y reproduce el audio"""
        self.letra_actual = letra.lower()

        img_path = self.img_folder / f"{self.letra_actual}.png"
        if img_path.exists():
            self._load_image(img_path, self.letra_actual)
            self._fade_in_image(self.images[self.letra_actual])
        else:
            print(f"[WARN] Imagen para '{self.letra_actual}' no encontrada en {img_path}")

        sound_path = self.audio_folder / f"{self.letra_actual}.wav"
        if sound_path.exists():
            self.load_sound("letra", sound_path)
            self.play_sound("letra", duck_volume=0.2)
        else:
            print(f"[WARN] Sonido para '{self.letra_actual}' no encontrado en {sound_path}")

    def _create_next(self):
        if "rename" not in self.images:
            return

        def on_next():
            if self.letra_actual:
                self.stop_sound(1)
                run_detection(self, self.letra_actual)  # ✅ Ejecutar análisis con la letra
                self.controller.show_frame("AbecedarioFrame")  # ✅ Regresar al menú principal

        btn = tk.Button(
            self.canvas,
            image=self.images["rename"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=on_next
        )
        pos_x, pos_y = self.scale_position(1000.0, 900.0)
        sw, sh = self.scale_size(434.0, 119.0)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images["rename"]

    def _create_back_button(self):
        if "button_26" not in self.images:
            return

        def on_back():
            self.stop_sound(1)
            self.controller.show_frame("AbecedarioFrame")

        btn = tk.Button(
            self.canvas,
            image=self.images["button_26"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=on_back
        )
        pos_x, pos_y = self.scale_position(1032.0, 228.0)
        sw, sh = self.scale_size(200.0, 71.0)
        btn.place(x=pos_x, y=pos_y, width=sw, height=sh)
        btn.image = self.images["button_26"]

    def _fade_in_image(self, image, steps=10, delay=50):
        self.letra_img_label.config(image=image)
        self.letra_img_label.image = image
        self.letra_img_label.attributes = {"alpha": 0}

        def _fade(step):
            alpha = step / steps
            self.letra_img_label.tk.call(self.letra_img_label._w, 'configure', '-alpha', alpha)
            if step < steps:
                self.after(delay, lambda: _fade(step + 1))

        try:
            self.letra_img_label.tk.call(self.letra_img_label._w, 'configure', '-alpha', 0)
            _fade(0)
        except tk.TclError:
            pass

    def on_hide(self):
        self.stop_effects()

    def stop_effects(self):
        for name, channel in self.channels.items():
            if name != "ambient":
                channel.stop()
