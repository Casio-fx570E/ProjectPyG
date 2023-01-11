import pygame
from load_pic import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image = load_image('Background2.0/Tiles1.png')
        self.rect = self.image.get_rect(topleft=pos)
