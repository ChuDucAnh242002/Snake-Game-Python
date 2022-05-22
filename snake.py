import pygame

BLOCK_SIZE = 80


class node():
    def __init__(self, x, y, side, part):
        self.x = x
        self.y = y
        self.side = side
        self.part = part
        self.child = None
        self.parent = None

class SNAKE():
    def __init__(self):
        self.length = 3

        self.head = None
        self.tail = None
        self.bodies = []
        self.initialize_position()

    def initialize_position(self):


        self.head = node(BLOCK_SIZE , 0, "right", "head")
        self.tail = node(0, 0, "left", "tail")

        self.head.child = self.tail
        self.tail.parent = self.head


    def move(self, keys_pressed):
        pass
    #     head_side = self.position[0][2]
    #     if keys_pressed[pygame.K_a] :
            
    #         self.position[0][0] -= BLOCK_SIZE
    #         if head_side != "left":
    #             self.position[0][2] = "left"

    #     if keys_pressed[pygame.K_d] :

    #         self.position[0][0] += BLOCK_SIZE
    #         if head_side != "right":
    #             self.position[0][2] = "right"
            
    #     if keys_pressed[pygame.K_w] :

    #         self.position[0][1] -= BLOCK_SIZE
    #         if head_side != "up":
    #             self.position[0][2] = "up"

    #     if keys_pressed[pygame.K_s] :

    #         self.position[0][1] += BLOCK_SIZE
    #         if head_side != "down":
    #             self.position[0][2] = "down"
    #     pass

    def add_body(self, x, y, side):
        body = node(x, y, side, "body")
        body.child = self.tail
        self.tail.parent = self.child

        if self.bodies == []:
            body.parent = self.head
            self.head.child = body
            self.bodies.append(body)
            return

        last_body = self.bodies[-1]
        body.parent = last_body
        last_body.child = body
        self.bodies.append(body)
        
    def reset(self):
        pass

    def root(self):
        return self.head

   