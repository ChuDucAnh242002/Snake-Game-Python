import pygame
import os
from snake import SNAKE

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 800
BLOCK_SIZE = WIDTH //10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

FPS = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SNAKE_WIDTH, SNAKE_HEIGHT = 80, 80
BORDER_SIZE = 1

SNAKE_HEAD_RIGHT_IMAGE = pygame.image.load(os.path.join('img', 'head', 'head_right.png'))
SNAKE_HEAD_RIGHT_IMAGE = pygame.transform.scale(SNAKE_HEAD_RIGHT_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_HEAD_LEFT_IMAGE = pygame.transform.rotate(SNAKE_HEAD_RIGHT_IMAGE, 180)
SNAKE_HEAD_UP_IMAGE = pygame.transform.rotate(SNAKE_HEAD_RIGHT_IMAGE, 90)
SNAKE_HEAD_DOWN_IMAGE = pygame.transform.rotate(SNAKE_HEAD_RIGHT_IMAGE, 270)

SNAKE_TAIL_RIGHT_IMAGE = pygame.image.load(os.path.join('img', 'tail', 'tail_right.png'))
SNAKE_TAIL_RIGHT_IMAGE = pygame.transform.scale(SNAKE_TAIL_RIGHT_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_TAIL_LEFT_IMAGE = pygame.transform.rotate(SNAKE_TAIL_RIGHT_IMAGE, 180)
SNAKE_TAIL_UP_IMAGE = pygame.transform.rotate(SNAKE_TAIL_RIGHT_IMAGE, 90)
SNAKE_TAIL_DOWN_IMAGE = pygame.transform.rotate(SNAKE_TAIL_RIGHT_IMAGE, 270)

SNAKE_BODY_VERTICLE_IMAGE = pygame.image.load(os.path.join('img', 'body', 'body_verticle.png'))
SNAKE_BODY_VERTICLE_IMAGE = pygame.transform.scale(SNAKE_BODY_VERTICLE_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_BODY_HORIZONTAL_IMAGE = pygame.transform.rotate(SNAKE_BODY_VERTICLE_IMAGE, 90)

SNAKE_TURN_LD_IMAGE = pygame.image.load(os.path.join('img', 'turn', 'turn_ld.png'))
SNAKE_TURN_LD_IMAGE = pygame.transform.scale(SNAKE_TURN_LD_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_TURN_LU_IMAGE = pygame.transform.rotate(SNAKE_TURN_LD_IMAGE, 90)
SNAKE_TURN_RD_IMAGE = pygame.transform.rotate(SNAKE_TURN_LD_IMAGE, 270)
SNAKE_TURN_RU_IMAGE = pygame.transform.rotate(SNAKE_TURN_LD_IMAGE, 180)

def draw_window(snake):
    WIN.fill(WHITE)

    draw_border()
    draw_snake(snake.root())

    
    # WIN.blit(SNAKE_BODY_VERTICLE_IMAGE, (0, HEIGHT * 2//10))

    # WIN.blit(SNAKE_HEAD_IMAGE, (0, 0))
    # WIN.blit(SNAKE_TAIL_IMAGE, (100, 200))
    # WIN.blit(SNAKE_BODY_IMAGE, (100, 300))
    # WIN.blit(SNAKE_TURN_IMAGE, (100, 400))
    

    pygame.display.update()

def draw_snake(cur_node):
    if cur_node == None:
        return

    if cur_node.part == "head":
        if (cur_node.side == "right"):
            WIN.blit(SNAKE_HEAD_RIGHT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "left"):
            WIN.blit(SNAKE_HEAD_LEFT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "up"):
            WIN.blit(SNAKE_HEAD_UP_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "down"):
            WIN.blit(SNAKE_HEAD_DOWN_IMAGE, (cur_node.x, cur_node.y))
        
    elif cur_node.part == "tail":
        if (cur_node.side == "right"):
            WIN.blit(SNAKE_TAIL_RIGHT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "left"):
            WIN.blit(SNAKE_TAIL_LEFT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "up"):
            WIN.blit(SNAKE_TAIL_UP_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "down"):
            WIN.blit(SNAKE_TAIL_DOWN_IMAGE, (cur_node.x, cur_node.y))

    elif cur_node.part == "body":
        if(cur_node.side == "horizontal"):
            WIN.blit(SNAKE_BODY_HORIZONTAL_IMAGE, (cur_node.x, cur_node.y))
        if(cur_node.side == "verticle"):
            WIN.blit(SNAKE_BODY_VERTICLE_IMAGE, (cur_node.x, cur_node.y))
        if(cur_node.side == "ld"):
            WIN.blit(SNAKE_TURN_LD_IMAGE, (cur_node.x, cur_node.y))
        if(cur_node.side == "lu"):
            WIN.blit(SNAKE_TURN_LU_IMAGE, (cur_node.x, cur_node.y))
        if(cur_node.side == "rd"):
            WIN.blit(SNAKE_TURN_RD_IMAGE, (cur_node.x, cur_node.y))
        if(cur_node.side == "ru"):
            WIN.blit(SNAKE_TURN_RU_IMAGE, (cur_node.x, cur_node.y))

    draw_snake(cur_node.child)

def draw_border():
    
    for i in range(1, 10):
        border_verticle = pygame.Rect(BLOCK_SIZE * i, 0, BORDER_SIZE, HEIGHT)
        border_horizontal = pygame.Rect(0, BLOCK_SIZE * i, WIDTH, BORDER_SIZE)
        pygame.draw.rect(WIN, BLACK, border_verticle)
        pygame.draw.rect(WIN, BLACK, border_horizontal)



def main():

    board = [[" " for i in range (10)] for i in range (10)]
    snake = SNAKE()

    # scale_image()

    clock = pygame.time.Clock()
    run = True
    while run:
        pygame.time.delay(50)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()

        # snake.move(keys_pressed)

        draw_window(snake)
        

if __name__ == "__main__":
    main()