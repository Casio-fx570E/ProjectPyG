import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

def fmusic():
    pygame.mixer.music.load('data/musics/fonmusic.mp3')
    pygame.mixer.music.play(loops=-1, start=11.5)