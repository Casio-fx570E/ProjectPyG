import pygame
import random


class Mob(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((1, 170, 1))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 10
        self.gravity = 5
        self.jump_speed = -50
        self.pos = pos
        self.timer = pygame.time.Clock()
        self.last_pos_tick = 0
        self.last_jump_tick = 0

    def move(self):
        if pygame.time.get_ticks() > self.last_pos_tick + 2000:
            n = random.randint(0, 1)
            self.direction.x = 1 if n else -1
            self.last_pos_tick = pygame.time.get_ticks()
        if pygame.time.get_ticks() > self.last_jump_tick + 4000:
            n = random.randint(0, 1)
            self.direction.y = self.jump_speed if n else 0
            self.last_jump_tick = pygame.time.get_ticks()

    def jump(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.move()
