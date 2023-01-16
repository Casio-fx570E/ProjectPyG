import pygame, sys
from map import *
from level import Level
from load_pic import load_image
from musica import fmusic, downm, upm
from map2 import *
import sys
import sqlite3

pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fight X')
pygame.display.set_icon(pygame.image.load('data/icon.bmp'))
clock = pygame.time.Clock()
FPS = 30
background_image = pygame.image.load('data/Background2.0/BG1.png')
background_image_2 = pygame.image.load('data/Background2.0/BG2.png')
background_image_3 = pygame.image.load('data/Background/BG1.png')
background_image_4 = pygame.image.load('data/Background/BG2.png')
background_image_5 = pygame.image.load('data/Background/BG3.png')
image1 = pygame.transform.scale(background_image, (1200, 700))
image2 = pygame.transform.scale(background_image_2, (1200, 700))
image3 = pygame.transform.scale(background_image_3, (1200, 700))
image4 = pygame.transform.scale(background_image_4, (1200, 700))
image5 = pygame.transform.scale(background_image_5, (1200, 700))



def play():
    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.blit(image2, (0, 0))
        screen.blit(image1, (0, 0))

        level.run()
        pygame.display.update()
        clock.tick(FPS)


def play_2nd():
    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif key[pygame.K_BACKSPACE]:
                end_screen()
                terminate()

        screen.blit(image5, (0, 0))
        screen.blit(image4, (0, 0))
        screen.blit(image3, (0, 0))

        level.run()
        pygame.display.update()
        clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Нажмите "TAB" для 1 уровня, "SPACE" для уровня 2', ''
                                            'Для возврата обратно нажмите - "END"'
                                            '', '                             ', ''
                                                                                 '                              ', ''
                                                                                                                   '                              ',
                  ''
                  '', ''
                      '', '                                                     '
                          'Правила - Для совершения прыжка нужно нажать space', ''
                                                                                '                                                                     '
                                                                                'Для ходьбы вправо - D, влево - A', ''
                                                                                                                    '                                                                      '
                                                                                                                    'Для удара вправо - E, влево - Q']

    fon = pygame.transform.scale(load_image('fon/fon_game.jpg'), (1200, 700))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('#99FF99'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        global is_second
        global level
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif keys[pygame.K_TAB]:
                is_second = False
                level = Level(level_map_1, screen)
                return
            elif keys[pygame.K_SPACE]:
                is_second = True
                level = Level(level_map_2, screen)
                return
            elif keys[pygame.K_LEFT]:
                downm()
            elif keys[pygame.K_RIGHT]:
                upm()

        pygame.display.flip()
        clock.tick(FPS)


start_screen()


def end_screen():
    time = str(pygame.time.get_ticks() // 1000)
    con = sqlite3.connect('Records.db')
    cur = con.cursor()
    result = "SELECT Time FROM Recs ORDER BY Time"
    res = cur.execute(result).fetchall()
    intro_text = ['                              Game Over!',
                  f'                            Ваше время:{time}с',
                  f'                           Лучшее время:{res[0][0]}c',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',

                  f'                                                                                                                                           {total_kills}']

    fon = pygame.transform.scale(load_image('fon/endingscreen.jpg'), (1200, 700))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    con = sqlite3.connect('Records.db')
    cur = con.cursor()
    result = "INSERT INTO Recs(Time) VALUES('" + time + "')"
    "SELECT * FROM Info ORDER BY DateTime"
    res = cur.execute(result)
    con.commit()
    cur.close()
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif keys[pygame.K_LEFT]:
                downm()
            elif keys[pygame.K_RIGHT]:
                upm()
            elif keys[pygame.K_ESCAPE]:
                return
            elif keys[pygame.K_SPACE]:
                play_2nd()

        pygame.display.flip()
        clock.tick(FPS)

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif key[pygame.K_LEFT]:
            downm()
        elif key[pygame.K_RIGHT]:
            upm()
    total_kills = level.player_sprite.kills_of_mob
    hp = level.is_dead
    end_of_game = level.is_win
    if hp or end_of_game:
        end_screen()
        terminate()
    if is_second:
        screen.blit(image3, (0, 0))
        screen.blit(image4, (0, 0))
    else:
        screen.blit(image2, (0, 0))
        screen.blit(image1, (0, 0))
    level.run()
    pygame.display.update()
    clock.tick(FPS)