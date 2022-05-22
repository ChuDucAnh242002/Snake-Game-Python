import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

FPS = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SNAKE_WIDTH, SNAKE_HEIGHT = 70, 70
BORDER_SIZE = 1

SNAKE_HEAD_RIGHT_IMAGE = pygame.image.load(os.path.join('img', 'head', 'head_right.png'))
SNAKE_HEAD_LEFT_IMAGE = pygame.image.load(os.path.join('img', 'head', 'head_left.png'))
SNAKE_HEAD_UP_IMAGE = pygame.image.load(os.path.join('img', 'head', 'head_up.png'))
SNAKE_HEAD_DOWN_IMAGE = pygame.image.load(os.path.join('img', 'head', 'head_down.png'))

SNAKE_TAIL_RIGHT_IMAGE = pygame.image.load(os.path.join('img', 'tail', 'tail_right.png'))
SNAKE_TAIL_LEFT_IMAGE = pygame.image.load(os.path.join('img', 'tail', 'tail_left.png'))
SNAKE_TAIL_UP_IMAGE = pygame.image.load(os.path.join('img', 'tail', 'tail_up.png'))
SNAKE_TAIL_DOWN_IMAGE = pygame.image.load(os.path.join('img', 'tail', 'tail_down.png'))

SNAKE_BODY_HORIZONTAL_IMAGE = pygame.image.load(os.path.join('img', 'body', 'body_horizontal.png'))
SNAKE_BODY_VERTICLE_IMAGE = pygame.image.load(os.path.join('img', 'body', 'body_verticle.png'))

SNAKE_TURN_LD_IMAGE = pygame.image.load(os.path.join('img', 'turn', 'turn_ld.png'))
SNAKE_TURN_LU_IMAGE = pygame.image.load(os.path.join('img', 'turn', 'turn_lu.png'))
SNAKE_TURN_RD_IMAGE = pygame.image.load(os.path.join('img', 'turn', 'turn_rd.png'))
SNAKE_TURN_RU_IMAGE = pygame.image.load(os.path.join('img', 'turn', 'turn_ru.png'))

SNAKE_HEAD_IMAGE = pygame.transform.scale(SNAKE_HEAD_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_TAIL_IMAGE = pygame.transform.scale(SNAKE_TAIL_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_BODY_IMAGE = pygame.transform.scale(SNAKE_BODY_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_TURN_IMAGE = pygame.transform.scale(SNAKE_TURN_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))


def draw_window():
    WIN.fill(WHITE)

    draw_border()

    WIN.blit(SNAKE_HEAD_IMAGE, (0, 0))
    # WIN.blit(SNAKE_TAIL_IMAGE, (100, 200))
    # WIN.blit(SNAKE_BODY_IMAGE, (100, 300))
    # WIN.blit(SNAKE_TURN_IMAGE, (100, 400))
    

    pygame.display.update()

def draw_border():
    
    for i in range(1, 10):
        border_verticle = pygame.Rect(WIDTH * i // 10, 0, BORDER_SIZE, HEIGHT)
        border_horizontal = pygame.Rect(0, HEIGHT * i // 10, WIDTH, BORDER_SIZE)
        pygame.draw.rect(WIN, BLACK, border_verticle)
        pygame.draw.rect(WIN, BLACK, border_horizontal)



def main():

    board = [[" " for i in range (10)] for i in range (10)]
    snake = [1,3]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window()
        

if __name__ == "__main__":
    main()