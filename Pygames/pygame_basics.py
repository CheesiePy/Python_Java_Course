import pygame

# initailize step
pygame.init() # initailize pygame

screen_width = 500
screen_height = 500


screen = pygame.display.set_mode((screen_width, screen_height))

# game loop:
game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    # game logic
    screen.fill((255, 255, 255))
    # 
    pygame.display.update()

pygame.quit()