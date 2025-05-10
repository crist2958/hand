# views/frases_leccion.py

from .base import BaseFrame
import tkinter as tk
from tkinter import Label
from pathlib import Path
import pygame
from PIL import Image, ImageTk, ImageSequence
from views.Analisis import run_detection  # Asegúrate de que aquí esté expuesto run_detection(parent, frase)


class FrasesLeccionFrame(BaseFrame):
    def create_widgets(self):
        super().create_widgets()

        self.img_folder   = self.assets_path / "Img_Frases"
        self.audio_folder = self.assets_path / "fraseswav"

        # Lugar donde va el GIF
        self.frase_img_label = Label(self.canvas, bg="#FFFFFF")
        self.canvas.create_window(
            int(self.screen_width * 0.5),
            int(self.screen_height * 0.55),
            window=self.frase_img_label
        )

        self.frase_actual = None
        self._create_back_button()
        self._create_next()

    # —– sección GIF —–
    def _animate_gif(self):
        if not getattr(self, "gif_frames", None):
            return
        frame = self.gif_frames[self.gif_index]
        self.frase_img_label.config(image=frame)
        self.frase_img_label.image = frame
        self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        delay = self.gif_info.get("duration", 100)
        self.gif_after_id = self.after(delay, self._animate_gif)

    def _start_gif_animation(self, gif_path):
        if hasattr(self, "gif_after_id"):
            self.after_cancel(self.gif_after_id)
        self._load_gif(gif_path)
        self._animate_gif()

    def _load_gif(self, path):
        self.gif_frames = []
        self.gif_index  = 0
        try:
            gif = Image.open(path)
            self.gif_info = gif.info
            scale = 2
            for frm in ImageSequence.Iterator(gif):
                w, h = int(frm.width*scale), int(frm.height*scale)
                img = frm.resize((w, h), Image.Resampling.LANCZOS)
                self.gif_frames.append(ImageTk.PhotoImage(img))
        except Exception as e:
            print(f"[ERROR] Cargando GIF '{path}': {e}")

    def set_letter(self, frase):
        """Recibe la frase de FrasesFrame y la muestra"""
        key = frase.lower().replace(" ", "_").replace("¿", "").replace("?", "")
        self.frase_actual = key

        img_path = self.img_folder / f"{key}.gif"
        if img_path.exists():
            self._start_gif_animation(img_path)
        else:
            print(f"[WARN] GIF no encontrado: {img_path}")

        wav = self.audio_folder / f"{key}.wav"
        if wav.exists():
            self.load_sound("frase", wav)
            self.play_sound("frase", duck_volume=0.2)
        else:
            print(f"[WARN] WAV no encontrado: {wav}")

    def on_hide(self):
        self.stop_effects()
        if hasattr(self, "gif_after_id"):
            self.after_cancel(self.gif_after_id)

    def stop_effects(self):
        for name, ch in getattr(self, "channels", {}).items():
            if name != "ambient":
                ch.stop()

    # —– Botón “Regresar” —–
    def _create_back_button(self):
        if "button_back" not in self.images:
            return
        def on_back():
            self.stop_sound(1)
            self.controller.show_frame("FrasesFrame")
        btn = tk.Button(
            self.canvas, image=self.images["button_back"],
            borderwidth=0, highlightthickness=0, relief="flat",
            command=on_back
        )
        x, y = self.scale_position(1032.0, 228.0)
        w, h = self.scale_size(200.0, 71.0)
        btn.place(x=x, y=y, width=w, height=h)
        btn.image = self.images["button_back"]

    # —– Botón “Siguiente” que lanza la detección OpenCV —–
    def _create_next(self):
        if "rename" not in self.images:
            return
        def on_next():
            if self.frase_actual:
                # detener audio de frase
                self.stop_sound(1)
                # lanzar detection pasando self como parent y la frase
                run_detection(self, self.frase_actual)
                # una vez la ventana de detección cierre, volvemos
                self.controller.show_frame("FrasesFrame")
        btn = tk.Button(
            self.canvas, image=self.images["rename"],
            borderwidth=0, highlightthickness=0, relief="flat",
            command=on_next
        )
        x, y = self.scale_position(1000.0, 900.0)
        w, h = self.scale_size(434.0, 119.0)
        btn.place(x=x, y=y, width=w, height=h)
        btn.image = self.images["rename"]
