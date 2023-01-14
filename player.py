import pygame
from load_pic import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((0, 64))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(100, 300)
        self.speed = 10
        self.gravity = 5
        self.jump_speed = -50
        self.jumped = 0
        self.frames_run = []
        self.frames_run_count = 0
        self.run = 'Character/Run/Run-Sheet_original.png'
        self.cut_sheet(load_image(self.run), 8, 1, self.frames_run)
        self.frames_idle = []
        self.frames_idle_count = 0
        self.idle = 'Character/Idle/Idle-Sheet.png'
        self.cut_sheet(load_image(self.idle), 4, 1, self.frames_idle)
        self.frames_idle_left = []
        self.frames_idle_left_count = 0
        self.idle_left = 'Character/Idle/Idle-Sheet-Left.png'
        self.cut_sheet(load_image(self.idle_left), 4, 1, self.frames_idle_left)
        self.frames_run_left = []
        self.frames_run_left_count = 0
        self.run_left = 'Character/Run/Run-Sheet_left_original.png'
        self.cut_sheet(load_image(self.run_left), 8, 1, self.frames_run_left)
        self.frames_attack = []
        self.frames_attack_count = 0
        self.attack = 'Character/Attack-01/Attack-01-Sheet.png'
        self.cut_sheet(load_image(self.attack), 8, 1, self.frames_attack)
        self.frames_attack_left = []
        self.frames_attack_left_count = 0
        self.attack_left = 'Character/Attack-01/Attack-02-Sheet.png'
        self.cut_sheet(load_image(self.attack_left), 8, 1, self.frames_attack_left)
        self.side = 0
        self.position = pos
        self.timer = pygame.time.Clock()
        self.last_jump_tick = 0
        self.attack_is_true = False
        self.hp = 1
        self.kills_of_mob = 0

    def animated_move(self, frames_run_count, frames_run):
        frames_run_count = (frames_run_count + 1) % len(frames_run)
        self.image = frames_run[frames_run_count]
        return frames_run_count, frames_run

    def animated_move_left(self, frames_run_count, frames_run):
        frames_run_count = (frames_run_count - 1) % len(frames_run)
        self.image = frames_run[frames_run_count]
        return frames_run_count, frames_run

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.attack_is_true = False
            self.frames_run_count, self.frames_run = self.animated_move(self.frames_run_count,
                                                                        self.frames_run)
            self.direction.x = 1
            self.side = 1
        elif keys[pygame.K_a]:
            self.attack_is_true = False
            self.frames_run_left_count, self.frames_run_left = self.animated_move_left(self.frames_run_left_count,
                                                                                       self.frames_run_left)
            self.direction.x = -1
            self.side = 0

        elif keys[pygame.K_e]:
            self.attack_is_true = True
            self.frames_attack_count, self.frames_attack = self.animated_move(self.frames_attack_count,
                                                                              self.frames_attack)
            self.direction.x = 0
            self.side = 1

        elif keys[pygame.K_q]:
            self.attack_is_true = True
            self.frames_attack_left_count, self.frames_attack_left = self.animated_move_left(
                self.frames_attack_left_count,
                self.frames_attack_left)
            self.direction.x = 0
            self.side = 0

        else:
            self.direction.x = 0
            if self.side == 1:
                self.attack_is_true = False
                self.frames_idle_count, self.frames_idle = self.animated_move(self.frames_idle_count,
                                                                              self.frames_idle)
            elif self.side == 0:
                self.attack_is_true = False
                self.frames_idle_left_count, self.frames_idle_left = self.animated_move(self.frames_idle_left_count,
                                                                                        self.frames_idle_left)
        if keys[pygame.K_SPACE] and self.jumped == 0:
            self.attack_is_true = False
            if self.direction.y == 0 and pygame.time.get_ticks() > self.last_jump_tick + 1000:
                self.jumped = 1
                self.image = load_image('Character/Jump/Jump.png')
                self.jump_yes()
                self.last_jump_tick = pygame.time.get_ticks()

        if not keys[pygame.K_SPACE]:
            self.jumped = 0

    def cut_sheet(self, sheet, columns, rows, frames):
        self.rect = pygame.Rect(self.direction.x, self.direction.y, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
                frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def attack_is(self):
        return self.attack_is_true

    def death(self):
        self.kill()

    def jump_yes(self):
        self.direction.y = self.jump_speed

    def update(self):
        print(self.hp)
        self.get_input()
