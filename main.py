import pygame, sys
from map import *
from level import Level
from load_pic import load_image
from musica import fmusic, downm, upm

pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Zombie Fight X')
pygame.display.set_icon(pygame.image.load('data/icon.bmp'))
clock = pygame.time.Clock()
level = Level(level_map_1, screen)
FPS = 30
background_image = pygame.image.load('data/Background2.0/BG1.png')
background_image_2 = pygame.image.load('data/Background2.0/BG2.png')
image1 = pygame.transform.scale(background_image, (1200, 700))
image2 = pygame.transform.scale(background_image_2, (1200, 700))


def play():
    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif key[pygame.K_BACKSPACE]:
                end_screen()
                terminate()

        screen.blit(image2, (0, 0))
        screen.blit(image1, (0, 0))

        level.run()
        pygame.display.update()
        clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Нажмите "TAB" для игры', ''
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

    fon = pygame.transform.scale(load_image('fon/fon.jpg'), (1200, 700))
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
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif keys[pygame.K_TAB]:
                return
            elif keys[pygame.K_LEFT]:
                downm()
            elif keys[pygame.K_RIGHT]:
                upm()

        pygame.display.flip()
        clock.tick(FPS)


start_screen()


def end_screen():
    intro_text = ['                               СЕМЁН']

    fon = pygame.transform.scale(load_image('fon/endingscreen.jpg'), (1200, 700))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
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
            elif keys[pygame.K_TAB]:
                play()
            elif keys[pygame.K_END]:
                start_screen()

        pygame.display.flip()
        clock.tick(FPS)


while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif key[pygame.K_BACKSPACE]:
            end_screen()
            terminate()
        elif key[pygame.K_END]:
            start_screen()
        elif key[pygame.K_LEFT]:
            downm()
        elif key[pygame.K_RIGHT]:
            upm()

    screen.blit(image1, (0, 0))
    screen.blit(image2, (0, 0))
    level.run()
    pygame.display.update()
    clock.tick(FPS)