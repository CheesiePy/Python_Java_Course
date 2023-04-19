import pygame

pygame.init() # initailize pygame

screen = pygame.display.set_mode((500, 500))
player = pygame.Rect(0, 0, 50, 50)

def draw(): # draw function
    screen.fill((0, 0, 0)) # fill screen with black
    pygame.draw.rect(screen, (255, 255, 255), player) # draw player

def move(): # move function
    player.x += 1 # move player 1 pixel to the right

# game loop:
game_run = True # game loop flag
while game_run: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT: # event handler
            game_run = False 
    # game logic
    move()
    # draw
    draw()
    
    pygame.display.update()
    # set frame rate
    pygame.time.delay(10)

pygame.quit()