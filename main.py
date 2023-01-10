import pygame, sys, os
from map import *
from level import Level


pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Zombie Fight X')
pygame.display.set_icon(pygame.image.load('data/icon.bmp'))
clock = pygame.time.Clock()
level = Level(level_map_1, screen)
FPS = 30
background_image = pygame.image.load('data/Background/BG3.png')
background_image_2 = pygame.image.load('data/Background/BG1.png')
background_image_3 = pygame.image.load('data/Background/BG2.png')
image1 = pygame.transform.scale(background_image, (1200, 700))
image2 = pygame.transform.scale(background_image_2, (1200, 700))
image3 = pygame.transform.scale(background_image_3, (1200, 700))


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image



def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Нажмите "TAB" для игры', ''
                    '', '                             ', ''
                        '                              ', ''
                        '                              ', ''
                        '',''
                        '','                                                     '
                  'Правила - Для совершения прыжка нужно нажать space', ''
                  '                                                                     '
                  'Для ходьбы вправо - D, влево - A']

    fon = pygame.transform.scale(load_image('fon/fon.jpg'), (1200, 700))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('#99FF99'))
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
                terminate()

        pygame.display.flip()
        clock.tick(FPS)

start_screen()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(image2, (0, 0))
    screen.blit(image3, (0, 0))
    screen.blit(image1, (0, 0))

    level.run()
    pygame.display.update()
    clock.tick(FPS)