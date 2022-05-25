"""
    Author : Chu Duc Anh
    GitHub : https://github.com/ChuDucAnh242002
    A 2D snake game. Move the snake by pressing WASD key.
    Try to eat as much apples as you can. 
    You will lose when you bite yourself.
"""

# Using pygame module
import pygame
import os
import random

from snake import SNAKE

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 800
BLOCK_SIZE = WIDTH //10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SNAKE_WIDTH, SNAKE_HEIGHT = 80, 80
BORDER_SIZE = 1

LOSSER_FONT = pygame.font.SysFont('comicsans', 120)
SCORE_FONT = pygame.font.SysFont('comicsans', 60)

# event when eat apple and bite yourself
EAT_APPLE = pygame.USEREVENT + 1
BITE = pygame.USEREVENT + 2

# GET eat and die sound tracks
EAT_SOUND = pygame.mixer.Sound(os.path.join('sound', 'EatSound.ogg'))
DIE_SOUND = pygame.mixer.Sound(os.path.join('sound', 'DieSound.ogg'))

# GET every parts of snake images
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

# When snake turn
SNAKE_TURN_LD_IMAGE = pygame.image.load(os.path.join('img', 'turn', 'turn_ld.png'))
SNAKE_TURN_LD_IMAGE = pygame.transform.scale(SNAKE_TURN_LD_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_TURN_LU_IMAGE = pygame.transform.rotate(SNAKE_TURN_LD_IMAGE, 270)
SNAKE_TURN_RD_IMAGE = pygame.transform.rotate(SNAKE_TURN_LD_IMAGE, 90)
SNAKE_TURN_RU_IMAGE = pygame.transform.rotate(SNAKE_TURN_LD_IMAGE, 180)

# Apple
FOOD_IMAGE = pygame.image.load(os.path.join('img', 'food.png'))
FOOD_IMAGE = pygame.transform.scale(FOOD_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))

# Background
GRASS_IMAGE = pygame.image.load(os.path.join('img', 'grass_bg.png'))
GRASS_IMAGE = pygame.transform.scale(GRASS_IMAGE, (WIDTH, HEIGHT))

def draw_window(snake, board):
    """
        Drawing background, border, food and snake
    """

    WIN.blit(GRASS_IMAGE, (0, 0))

    draw_border()
    draw_food(board)
    draw_snake(snake.root())
    
    pygame.display.update()

def draw_snake(cur_node):
    """
        Recursive function that print every parts of the snake
    """
    if cur_node == None:
        return

    # Head
    if cur_node.part == "head":
        if (cur_node.side == "right"):
            WIN.blit(SNAKE_HEAD_RIGHT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "left"):
            WIN.blit(SNAKE_HEAD_LEFT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "up"):
            WIN.blit(SNAKE_HEAD_UP_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "down"):
            WIN.blit(SNAKE_HEAD_DOWN_IMAGE, (cur_node.x, cur_node.y))
        
    # Tail
    elif cur_node.part == "tail":
        if (cur_node.side == "right"):
            WIN.blit(SNAKE_TAIL_LEFT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "left"):
            WIN.blit(SNAKE_TAIL_RIGHT_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "up"):
            WIN.blit(SNAKE_TAIL_DOWN_IMAGE, (cur_node.x, cur_node.y))
        elif (cur_node.side == "down"):
            WIN.blit(SNAKE_TAIL_UP_IMAGE, (cur_node.x, cur_node.y))

    # Body
    elif cur_node.part == "body":
        if(cur_node.side == "horizontal"):
            WIN.blit(SNAKE_BODY_HORIZONTAL_IMAGE, (cur_node.x, cur_node.y))
        if(cur_node.side == "verticle"):
            WIN.blit(SNAKE_BODY_VERTICLE_IMAGE, (cur_node.x, cur_node.y))
        # When body turn
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
    # 10 by 10 border
    for i in range(1, 10):
        border_verticle = pygame.Rect(BLOCK_SIZE * i, 0, BORDER_SIZE, HEIGHT)
        border_horizontal = pygame.Rect(0, BLOCK_SIZE * i, WIDTH, BORDER_SIZE)
        pygame.draw.rect(WIN, BLACK, border_verticle)
        pygame.draw.rect(WIN, BLACK, border_horizontal)

def draw_food(board):

    i, j = food_position(board)
    if i == None or j == None:
        return
    WIN.blit(FOOD_IMAGE, (i*BLOCK_SIZE, j*BLOCK_SIZE))

def draw_losser(losser_text, score):
    # When snake bites itself, the game is over
    draw_text = LOSSER_FONT.render(losser_text, 1, RED)
    score_text = SCORE_FONT.render(score, 1, RED)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2,
                         HEIGHT//2 - draw_text.get_height()/2))
    WIN.blit(score_text, (WIDTH//2 - score_text.get_width()/2,
                         HEIGHT//2 + draw_text.get_height()/2 + score_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(1000)
    
def handle_movement(root, keys_pressed, snake):
    # Pressing key WASD
    if keys_pressed[pygame.K_a] and root.side != "right" and root.x > 0:
        move_recursive(root, "left", None, None, None, snake)
        return
        
    if keys_pressed[pygame.K_d] and root.side != "left" and root.x < WIDTH - BLOCK_SIZE:
        move_recursive(root, "right", None, None, None, snake)
        return
        
    if keys_pressed[pygame.K_w] and root.side != "down" and root.y > 0:
        move_recursive(root, "up", None, None, None, snake)
        return
        
    if keys_pressed[pygame.K_s] and root.side != "up" and root.y < HEIGHT - BLOCK_SIZE:
        move_recursive(root, "down", None, None, None, snake)
        return
    
def move_recursive(cur_node, side, last_x , last_y, last_side, snake):

    # Moving when a key is pressed and the whole snake move
    if cur_node == None:
        return

    # Head 
    if cur_node == snake.head:
        last_side = change_last_side(cur_node, side)
        
        last_x = cur_node.x
        last_y = cur_node.y
        move_head(cur_node, side)
        return move_recursive(cur_node.child, side, last_x, last_y, last_side, snake)

    # Tail
    if cur_node == snake.tail:
        snake.last_tail.x = cur_node.x
        snake.last_tail.y = cur_node.y
        snake.last_tail.side = cur_node.side
        cur_node.x = last_x
        cur_node.y = last_y
        if cur_node.parent.parent == None :    
            cur_node.side = last_side
            return
        move_tail_side(cur_node, last_side)
        return 

    # Body
    tempx = cur_node.x
    tempy = cur_node.y
    temp_side = cur_node.side
    cur_node.x = last_x
    cur_node.y = last_y
    cur_node.side = last_side
    last_x = tempx
    last_y = tempy
    last_side = temp_side

    move_recursive(cur_node.child, side, last_x, last_y, last_side, snake)

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
    # change head side when it is not currently in the side the key pressed
    if head_node.side != side:
        head_node.side = side

def change_last_side(head_node, side):
    # Find the last side of head and fit to other parts

    # Tail part
    if head_node.child.part == "tail":
        return side

    # Body part. When snake change direction
    if side == "left": 
        if head_node.side == "up":
            return "ru"
        if head_node.side == "down":
            return "rd"

    if side == "right": 
        if head_node.side == "up":
            return "lu"
        if head_node.side == "down":
            return "ld"

    if side == "up": 
        if head_node.side == "left":
            return "ld"
        if head_node.side == "right":
            return "rd"

    if side == "down": 
        if head_node.side == "left":
            return "lu"
        if head_node.side == "right":
            return "ru"

    # Body part. When snake go the same direction
    if (side == "right" and head_node.side == "right") or (side == "left" and head_node.side == "left"):
        return "horizontal"

    if (side == "down" and head_node.side == "down") or (side == "up" and head_node.side == "up"):
        return "verticle"
    
def move_tail_side(tail_node, last_side):

    # Moving the tail as the last body part moves
    if (last_side == "ru" and tail_node.side == "right") or (last_side == "lu" and tail_node.side == "left"):
        tail_node.side = "down"
    elif (last_side == "rd" and tail_node.side == "right") or (last_side == "ld" and tail_node.side == "left"):
        tail_node.side = "up"
    elif (last_side == "rd" and tail_node.side == "down") or (last_side == "ru" and tail_node.side == "up"):
        tail_node.side = "left"
    elif (last_side == "ld" and tail_node.side == "down") or (last_side == "lu" and tail_node.side == "up"):
        tail_node.side = "right"

def snake_on_board(snake, cur_node, board):
    """
        Print the snake on board 10x10 array
    """
    if cur_node == None:
        if snake.last_tail.x != None and snake.last_tail.y != None:
            x = snake.last_tail.x // BLOCK_SIZE
            y = snake.last_tail.y // BLOCK_SIZE
            board[x][y] = " "
        return
    
    # 2 Dimensional list
    x = cur_node.x // BLOCK_SIZE
    y = cur_node.y // BLOCK_SIZE

    # Set 1 if it snake parts
    if board[x][y] == "0" and cur_node == snake.head:
        pygame.event.post(pygame.event.Event(EAT_APPLE))
    elif board[x][y] == "1" and cur_node == snake.head:
        pygame.event.post(pygame.event.Event(BITE))
        return
    
    board[x][y] = "1"
    if cur_node == snake.head:
        board[x][y] = "2"
    if cur_node == snake.tail:
        board[x][y] = "3"

    snake_on_board(snake, cur_node.child, board)

def available_move(board):

    # return available move in the board
    positions = []
    for i in range(10):
        for j in range(10):
            if board[i][j] == " ":
                positions.append([i,j])
    return positions

def food_on_board(board):

    # Take a random place on a board to get the food position
    a, b = food_position(board)
    if a != None and b != None:
        board[a][b] = " "
    
    random_position = random.choice(available_move(board))
    i, j = random_position[0], random_position[1]
    
    board[i][j] = "0"
    

def food_position(board):
    # Get food position
    for a in range(10):
        for b in range(10):
            if board[a][b] == "0":
                return a, b
    return None, None

def main():

    board = [[" " for i in range (10)] for i in range (10)]
    snake = SNAKE()

    # Create food
    food_on_board(board)

    losser_text = " "

    clock = pygame.time.Clock()
    run = True

    while run:
        pygame.time.delay(50)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            # Eat apple
            if event.type == EAT_APPLE:
                snake.add_body()
                snake_on_board(snake, snake.root(), board)

                food_on_board(board)
                EAT_SOUND.play()

            # Bite yourself
            if event.type == BITE:
                losser_text = "YOU LOSE!"
                DIE_SOUND.play()
                
        keys_pressed = pygame.key.get_pressed()

        handle_movement(snake.root(), keys_pressed, snake)
        snake_on_board(snake, snake.root(), board)

        draw_window(snake, board)

        # End game
        if losser_text == "YOU LOSE!":
            score = "Score:" + str(snake.length)
            draw_losser(losser_text, score)
            losser_text = " "
            run = False


if __name__ == "__main__":
    while True:
        main()