import pygame
from random import randint
# initailize step
pygame.init() # initailize pygame


size = 20
rows = 25
cols = 25
screen_size = size * rows, size * cols

snake = [(12, 12)] # init -> snake head
apple = (randint(0, rows-1), randint(0, cols-1))
direction = (0, -1)
game_over = False


screen = pygame.display.set_mode()



def move():
    global snake, apple, direction, game_over

    # create new head in the current direction 
    head = snake[-1][0] + direction[0], snake[-1][1] + direction[1]

    if head[0] < 0 or head[0] >= rows or head[1] < 0 or head[1] >= cols:
        game_over = True
        return 
    
    if head in snake[:-1]:
        game_over = True
        return 
    
    snake.append(head)
    
    if head == apple:
        apple = (randint(0, rows-1), randint(0, cols-1))
    else:
        snake.pop(0)

    

def draw():
    global snake, apple, direction, game_over

    screen.fill((0,0,0))
    

    # draw body
    for snake_part in snake[:-1]:
        pygame.draw.rect(screen, (0, 255 ,0),(snake_part[0] * size, snake_part[1] * size, size ,size))

    # draw head
    pygame.draw.rect(screen, (0, 255 ,255),(snake[-1][0] * size, snake[-1][1] * size, size ,size))

    # draw apple
    pygame.draw.rect(screen, (0, 255 ,255),(apple[0] * size, apple[1] * size, size ,size))

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render('Game Over!', True, (255, 255, 255))
        screen.blit(text, (screen_size[0] / 2 - text.get_width() / 2, screen_size[1] / 2 - text.get_height() / 2))
        return

    pygame.display.update()

def reset():
    global snake, apple, direction, game_over
    snake = [(12, 12)] # init -> snake head
    apple = (randint(0, rows-1), randint(0, cols-1))
    direction = (0, -1)
    game_over = False


clock = pygame.time.Clock()


# game loop:
game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)
            elif event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)
            elif event.key == pygame.K_r:
                reset()


    # game logic
    move()
    draw()
    # 
    clock.tick(10)
    

