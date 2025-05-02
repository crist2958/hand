import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

class BaseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.assets_path = self.get_assets_path()
        self.images = {}
        self.sounds = {}
        self.load_assets()
        self.create_widgets()

    def get_assets_path(self):
        class_name = self.__class__.__name__.replace("Frame", "").lower()
        return Path(__file__).parent.parent / "assets" / class_name

    def load_assets(self):
        fondo_path = self.assets_path / f"{self.assets_path.name}_panel.png"
        if fondo_path.exists():
            self._load_image(fondo_path, "background")

        for asset_file in self.assets_path.glob("*.png"):
            if asset_file.name != f"{self.assets_path.name}_panel.png":
                self._load_image(asset_file, asset_file.stem)

    def _load_image(self, path, key):
        try:
            img = Image.open(path)
            self.images[key] = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error cargando imagen {path}: {str(e)}")

    def create_widgets(self):
        self.canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(expand=True, fill="both")

        if "background" in self.images:
            self.canvas.create_image(720, 512, image=self.images["background"])

    def load_sound(self, sound_name, filename):
        sound = self.controller.audio_manager.load_effect(filename)
        if sound:
            self.sounds[sound_name] = sound

    def play_sound(self, sound_name, channel=1, duck_volume=0.2):
        if sound_name in self.sounds:
            self.controller.audio_manager.play_effect(
                self.sounds[sound_name],
                channel=channel,
                duck_volume=duck_volume
            )

    def stop_sounds(self):
        self.controller.audio_manager.stop_effects()

    def on_show(self):
        pass

    def on_hide(self):
        self.stop_sounds()