import pygame
from pathlib import Path

class AudioManager:
    def __init__(self):
        self.assets_path = Path(__file__).parent / "assets/audio"
        self.ambient_volume = 0.4  # Volumen base al 40%
        self.effect_volume = 0.8   # Volumen efectos al 80%
        self.original_ambient_volume = self.ambient_volume
        self._initialize()

    def _initialize(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(8)
        self.ambient_channel = pygame.mixer.Channel(0)
        self.effect_channels = {
            1: pygame.mixer.Channel(1),
            2: pygame.mixer.Channel(2),
            3: pygame.mixer.Channel(3)
        }
        pygame.mixer.music.set_volume(self.ambient_volume)

    def set_ambient_volume(self, volume):
        self.ambient_volume = volume
        pygame.mixer.music.set_volume(volume)

    def set_effect_volume(self, volume, channel=1):
        if channel in self.effect_channels:
            self.effect_channels[channel].set_volume(volume)

    def load_ambient_music(self, filename="Ambiente.wav"):
        file_path = self.assets_path / filename
        if file_path.exists():
            pygame.mixer.music.load(str(file_path))
            return True
        return False

    def play_ambient_music(self):
        pygame.mixer.music.play(-1)
        self.set_ambient_volume(self.ambient_volume)

    def load_effect(self, filename):
        """Carga un efecto de sonido desde la carpeta de audio"""
        file_path = self.assets_path / filename
        if file_path.exists():
            return pygame.mixer.Sound(str(file_path))
        else:
            print(f"[AudioManager] Archivo de efecto no encontrado: {file_path}")
            return None

    def play_effect(self, sound, channel=1, duck_volume=0.2):
        if channel in self.effect_channels and sound:
            self.original_ambient_volume = self.ambient_volume
            self.set_ambient_volume(duck_volume)
            self.effect_channels[channel].set_volume(self.effect_volume)
            self.effect_channels[channel].play(sound)
            return True
        return False

    def check_channels(self):
        """Restaura el volumen ambiental si todos los canales de efectos están libres"""
        if all(not ch.get_busy() for ch in self.effect_channels.values()):
            self._restore_ambient_volume()

    def _restore_ambient_volume(self):
        self.set_ambient_volume(self.original_ambient_volume)

    def stop_all_sounds(self):
        """Detiene todos los efectos, pero mantiene la música ambiental en loop"""
        for ch in self.effect_channels.values():
            ch.stop()  # Detiene los efectos de sonido, pero no la música ambiental

    def stop_effects(self):
        """Detener todos los efectos de sonido, incluida la música de letras"""
        # Detener la música de la letra, pero NO la música ambiental
        pygame.mixer.music.stop()  # Detener música de la letra

        if hasattr(self.controller.audio_manager, "stop_all_sounds"):
            self.controller.audio_manager.stop_all_sounds()  # Detener otros sonidos que no sean la música ambiental

        # Nota: Aquí no se detiene la música ambiental, se mantiene en bucle
