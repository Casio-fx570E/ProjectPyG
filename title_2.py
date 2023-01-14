import pygame
from load_pic import load_image


class Tile_Sec(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        image = load_image('Background/DarkCastle.jpg')
        image_scaled = pygame.transform.scale(image, (64, 64))
        self.image = image_scaled
        self.rect = self.image.get_rect(topleft=pos)
