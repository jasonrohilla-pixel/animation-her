import sys
import subprocess
from pathlib import Path

try:
    import pygame
except ImportError:
    print("Pygame is not installed.")
    print("Open Command Prompt in this folder and run: py -m pip install pygame")
    input("Press Enter to close...")
    raise SystemExit

folder = Path(__file__).resolve().parent
animation_file = folder / "love.py"
music_file = folder / "music.mp3"

if not animation_file.exists():
    print("Could not find love.py in this folder.")
    input("Press Enter to close...")
    raise SystemExit

if not music_file.exists():
    print("Could not find music.mp3 in this folder.")
    input("Press Enter to close...")
    raise SystemExit

try:
    pygame.mixer.init()
    pygame.mixer.music.load(str(music_file))
    pygame.mixer.music.play(-1)  # Loop the music

    print("Playing music and starting your animation...")
    subprocess.run([sys.executable, str(animation_file)], cwd=str(folder))

except Exception as error:
    print("Something went wrong:", error)
    input("Press Enter to close...")

finally:
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()
        pygame.mixer.quit()
