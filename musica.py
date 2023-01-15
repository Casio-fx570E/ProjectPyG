import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
global vol
vol = 1.0


def fmusic():
    fonm = pygame.mixer.music.load('data/musics/fonmusic.mp3')
    pygame.mixer.music.play(loops=-1, start=11.5)
    return fonm


def downm():
    global vol
    vol -= 0.1
    pygame.mixer.music.set_volume(vol)
    print(pygame.mixer.music.get_volume())
    return


def upm():
    global vol
    if vol != 1.0:
        vol += 0.1
        pygame.mixer.music.set_volume(vol)
    print(pygame.mixer.music.get_volume())
    return

def udar():
    s = pygame.mixer.Sound('data/musics/randomeffects/zvuk-udara.wav')
    s.play()