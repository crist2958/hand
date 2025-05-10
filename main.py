# main.py
import tkinter as tk
from tkinter import Tk
import pygame
from audio_manager import AudioManager
from views.inicio import InicioFrame
from views.lecciones import LeccionesFrame
from views.abecedario import AbecedarioFrame
from views.abecedario_leccion import AbecedarioLeccionFrame
from views.frases import FrasesFrame
from views.frases_leccion import FrasesLeccionFrame
#from views.examen import 

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.audio_manager = AudioManager()
        self._configure_window()
        self._setup_ui()
        self._setup_audio()

    def _configure_window(self):
        self.title("Sistema de Aprendizaje LSE")
        # Pantalla completa
        self.attributes("-fullscreen", True)
        # Salir de fullscreen con ESC
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

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
        # Registrar cada pantalla con su clase correspondiente
        frames = {
            "InicioFrame": InicioFrame,
            "LeccionesFrame": LeccionesFrame,
            "AbecedarioFrame": AbecedarioFrame,
            "AbecedarioLeccionFrame": AbecedarioLeccionFrame,
            "FrasesFrame": FrasesFrame,
            "FrasesLeccionFrame": FrasesLeccionFrame,
        }
        for name, FrameClass in frames.items():
            frame = FrameClass(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Expandir contenedor
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

    def show_frame(self, frame_name, letter=None):
        """Muestra el frame indicado; opcionalmente pasa una letra a set_letter()."""
        frame = self.frames.get(frame_name)
        if not frame:
            raise ValueError(f"Frame no registrado: {frame_name}")

        if letter and hasattr(frame, 'set_letter'):
            frame.set_letter(letter)

        frame.tkraise()
        if hasattr(frame, 'on_show'):
            frame.on_show()

    
    def _update_audio(self):
        self.audio_manager.check_channels()
        self.after(100, self._update_audio)

    def destroy(self):
        pygame.quit()
        super().destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
