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
            WIN.blit(SNAKE_TAIL_LEFT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "left"):
            WIN.blit(SNAKE_TAIL_RIGHT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "up"):
            WIN.blit(SNAKE_TAIL_DOWN_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "down"):
            WIN.blit(SNAKE_TAIL_UP_IMAGE, (cur_node.x, cur_node.y))

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

def handle_movement(root, keys_pressed):
    if keys_pressed[pygame.K_a] and root.side != "right" and root.x > 0:
        move_recursive(root, "left", None, None, None)
        return
        
    if keys_pressed[pygame.K_d] and root.side != "left" and root.x < WIDTH - BLOCK_SIZE:
        move_recursive(root, "right", None, None, None)
        return
        
    if keys_pressed[pygame.K_w] and root.side != "down" and root.y > 0:
        move_recursive(root, "up", None, None, None)
        return
        
    if keys_pressed[pygame.K_s] and root.side != "up" and root.y < HEIGHT - BLOCK_SIZE:
        move_recursive(root, "down", None, None, None)
        return
    

def move_recursive(cur_node, side, last_x , last_y, last_side):
    if cur_node == None:
        return

    if cur_node.parent == None:
        last_side = change_last_side(cur_node, side)
        last_x = cur_node.x
        last_y = cur_node.y
        move_head(cur_node, side)
        return move_recursive(cur_node.child, side, last_x, last_y, last_side)

    if cur_node.child == None:
        pass

    tempx = cur_node.x
    tempy = cur_node.y
    temp_side = cur_node.side
    cur_node.x = last_x
    cur_node.y = last_y
    cur_node.side = last_side
    last_x = tempx
    last_y = tempy
    last_side = temp_side

    move_recursive(cur_node.child, side, last_x, last_y, last_side)


def move_head(head_node, side):

    if side == "left":
        head_node.x -= BLOCK_SIZE

    elif side == "right":
        head_node.x += BLOCK_SIZE

    elif side == "up":
        head_node.y -= BLOCK_SIZE

    elif side == "down":
        head_node.y += BLOCK_SIZE

    change_head_side(head_node, side)

def change_head_side(head_node, side):
    if head_node.side != side:
        head_node.side = side

def change_last_side(head_node, side):
    if head_node.child.part == "tail":
        return side

    if side == "left": 
        if head_node.side == "up":
            return "lu"
        if head_node.side == "down":
            return "ld"

    if side == "right": 
        if head_node.side == "up":
            return "ru"
        if head_node.side == "down":
            return "rd"

    if side == "up": 
        if head_node.side == "left":
            return "lu"
        if head_node.side == "right":
            return "ru"

    if side == "right": 
        if head_node.side == "left":
            return "ld"
        if head_node.side == "right":
            return "rd"
    


def move_tail(tail_node):
    
    pass


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

        handle_movement(snake.root(), keys_pressed)

        draw_window(snake)
        

if __name__ == "__main__":
    main()