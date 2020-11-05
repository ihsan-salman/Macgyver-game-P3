import pygame 

pygame.init()

screen = pygame.display.set_mode((800,600))
image = pygame.image.load("image.png").convert_alpha()

run=True
while run:
    screen.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            run = False
    pygame.display.flip()

pygame.quit()