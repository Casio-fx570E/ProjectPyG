import pygame
from player import Player


class Mob(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 10
        self.gravity = 5
        self.jump_speed = -32

    def move(self):
        pass

    def jump(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.move()