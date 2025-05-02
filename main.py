import tkinter as tk
from tkinter import Tk
import pygame
from audio_manager import AudioManager
from views.inicio import InicioFrame
from views.lecciones import LeccionesFrame
from views.abecedario import AbecedarioFrame
from views.frases import FrasesFrame

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.audio_manager = AudioManager()
        self._configure_window()
        self._setup_ui()
        self._setup_audio()

    def _configure_window(self):
        self.width = 1440
        self.height = 1024
        self.title("Sistema de Aprendizaje LSE")
        self.resizable(False, False)
        self._center_on_screen()

    def _center_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height // 2) - (self.height // 2)
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def _setup_audio(self):
        if self.audio_manager.load_ambient_music():
            self.audio_manager.play_ambient_music()
            self.after(100, self._update_audio)
        else:
            print("Error: Archivo de música ambiental no encontrado")

    def _setup_ui(self):
        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")
        self.frames = {}
        self._register_frames()
        self.show_frame("InicioFrame")

    def _register_frames(self):
        frames = {
            "InicioFrame": InicioFrame,
            "LeccionesFrame": LeccionesFrame,
            "AbecedarioFrame": AbecedarioFrame,
            "FrasesFrame": FrasesFrame
        }

        for name, frame_class in frames.items():
            frame_instance = frame_class(self.container, self)
            self.frames[name] = frame_instance
            frame_instance.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_name):
        if frame_name in self.frames:
            self.frames[frame_name].tkraise()
            self.frames[frame_name].on_show()
        else:
            raise ValueError(f"Frame no registrado: {frame_name}")

    def _update_audio(self):
        self.audio_manager.check_channels()
        self.after(100, self._update_audio)

    def destroy(self):
        pygame.quit()
        super().destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()