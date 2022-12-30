import pygame, sys

pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
background_image = pygame.image.load('data/Background/BG3.png')
background_image_2 = pygame.image.load('data/Background/BG1.png')
background_image_3 = pygame.image.load('data/Background/BG2.png')
image1 = pygame.transform.scale(background_image, (1200, 700))
image2 = pygame.transform.scale(background_image_2, (1200, 700))
image3 = pygame.transform.scale(background_image_3, (1200, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(image2, (0, 0))
    screen.blit(image3, (0, 0))
    screen.blit(image1, (0, 0))
    pygame.display.update()
    clock.tick(60)
