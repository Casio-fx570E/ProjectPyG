import pygame
from title import Tile
from map import tile_size
from player import Player
from mob import Mob
from invisible_tiles import Invisible_tiles


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.invisible_tiles = pygame.sprite.Group()
        self.hero = Player
        self.player = pygame.sprite.GroupSingle()
        self.mob = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'I':
                    invisible_tiles = Invisible_tiles((x, y), tile_size)
                    self.invisible_tiles.add(invisible_tiles)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player_sprite = player_sprite
                    self.player.add(player_sprite)
                if cell == 'Z':
                    mob_sprite = Mob((x, y))
                    self.mob.add(mob_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        is_attacking = Player.attack_is(self.player_sprite)
        print(is_attacking)
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        for sprite in self.invisible_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        for sprite in self.mob.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                if (player.direction.x < 0 or player.direction.x == 0) and is_attacking:
                    sprite.kill()
                elif (player.direction.x > 0 or player.direction.x == 0) and is_attacking:
                    player.rect.right = sprite.rect.left
                    sprite.kill()

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        for sprite in self.invisible_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        for sprite in self.mob.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    sprite.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    sprite.direction.y = 0


    def horizontal_movement_collision_mob(self):
        mob = self.mob.sprites()
        for sprite in self.mob.sprites():
            sprite.rect.x += sprite.direction.x * sprite.speed
        for mob in self.mob.sprites():
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(mob.rect):
                    if mob.direction.x < 0:
                        mob.rect.left = sprite.rect.right
                    elif mob.direction.x > 0:
                        mob.rect.right = sprite.rect.left
        for mob in self.mob.sprites():
            for sprite in self.invisible_tiles.sprites():
                if sprite.rect.colliderect(mob.rect):
                    if mob.direction.x < 0:
                        mob.rect.left = sprite.rect.right
                    elif mob.direction.x > 0:
                        mob.rect.right = sprite.rect.left

    def vertical_movement_collision_mob(self):
        mob = self.mob.sprites()
        for sprite in self.mob.sprites():
            sprite.apply_gravity()
        for mob in self.mob.sprites():
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(mob.rect):
                    if mob.direction.y > 0:
                        mob.rect.bottom = sprite.rect.top
                        mob.direction.y = 0
                    elif mob.direction.y < 0:
                        mob.rect.top = sprite.rect.bottom
                        mob.direction.y = 0
        for mob in self.mob.sprites():
            for sprite in self.invisible_tiles.sprites():
                if sprite.rect.colliderect(mob.rect):
                    if mob.direction.y > 0:
                        mob.rect.bottom = sprite.rect.top
                        mob.direction.y = 0
                    elif mob.direction.y < 0:
                        mob.rect.top = sprite.rect.bottom
                        mob.direction.y = 0


    def run(self):
        self.tiles.draw(self.display_surface)

        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        self.player.update()
        self.mob.update()
        self.mob.draw(self.display_surface)
        self.vertical_movement_collision_mob()
        self.horizontal_movement_collision_mob()
