import pygame

print("music_manager module loaded")

is_muted = False
music_volume = 0.1

def toggle_mute():
    global is_muted  # Declare is_muted as a global variable
    is_muted = not is_muted
    if is_muted:
        pygame.mixer.music.set_volume(0)  # Mute music
    else:
        pygame.mixer.music.set_volume(music_volume)  # Unmute music
