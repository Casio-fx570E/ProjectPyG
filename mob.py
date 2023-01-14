import pygame
import random
from load_pic import load_image


class Mob(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((1, 170, 1))
        self.rect = self.image.get_rect(topleft=pos)
        image = load_image('Monster/necromancer_run_anim_f1.png')
        self.image_scaled = pygame.transform.scale(image, (48, 64))
        image2 = load_image('Monster/necromancer_run_anim_f2.png')
        self.image_scaled2 = pygame.transform.scale(image2, (48, 64))
        image3 = load_image('Monster/necromancer_run_anim_f3.png')
        self.image_scaled3 = pygame.transform.scale(image3, (48, 64))
        image4 = load_image('Monster/run_left_one.png')
        self.image_scaled4 = pygame.transform.scale(image4, (48, 64))
        image5 = load_image('Monster/run_left_two.png')
        self.image_scaled5 = pygame.transform.scale(image5, (48, 64))
        image6 = load_image('Monster/run_left_three.png')
        self.image_scaled6 = pygame.transform.scale(image6, (48, 64))
        self.image = self.image_scaled
        self.frames_run = [self.image_scaled, self.image_scaled2, self.image_scaled3]
        self.frames_run_count = 0
        self.frames_run_left = [self.image_scaled4, self.image_scaled5, self.image_scaled6]
        self.frames_run_left_count = 0

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 10
        self.gravity = 5
        self.jump_speed = -50
        self.pos = pos
        self.timer = pygame.time.Clock()
        self.last_pos_tick = 0
        self.last_jump_tick = 0

    def move(self):
        if pygame.time.get_ticks() > self.last_pos_tick + 1000:
            n = random.randint(0, 1)
            self.direction.x = 1 if n else -1
            self.last_pos_tick = pygame.time.get_ticks()
        if pygame.time.get_ticks() > self.last_jump_tick + 4000:
            n = random.randint(0, 1)
            self.direction.y = self.jump_speed if n else 0
            self.last_jump_tick = pygame.time.get_ticks()
        if self.direction.x > 0:
            self.frames_run_count, self.frames_run = self.animated_move(self.frames_run_count,
                                                                        self.frames_run)
        elif self.direction.x < 0:
            self.frames_run_left_count, self.frames_run_left = self.animated_move_left(self.frames_run_left_count,
                                                                                       self.frames_run_left)

    def animated_move(self, frames_run_count, frames_run):
        frames_run_count = (frames_run_count + 1) % len(frames_run)
        self.image = frames_run[frames_run_count]
        return frames_run_count, frames_run

    def animated_move_left(self, frames_run_count, frames_run):
        frames_run_count = (frames_run_count - 1) % len(frames_run)
        self.image = frames_run[frames_run_count]
        return frames_run_count, frames_run

    def jump(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.move()
