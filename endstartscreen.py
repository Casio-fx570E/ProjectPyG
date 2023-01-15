import pygame, sys
from load_pic import load_image
from main import *

def end_screen():
    time = str(pygame.time.get_ticks() // 1000)
    con = sqlite3.connect('Records.db')
    cur = con.cursor()
    result = "SELECT Time FROM Recs ORDER BY Time"
    res = cur.execute(result).fetchall()
    print(res)
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
            elif keys[pygame.K_TAB]:
                play()
            elif keys[pygame.K_SPACE]:
                play_2nd()
            elif keys[pygame.K_END]:
                start_screen()

        pygame.display.flip()
        clock.tick(FPS)

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

def terminate():
    pygame.quit()
    sys.exit()