# import pygame

BLOCK_SIZE = 80

"""
    a node for each part of a snake, head, body, tail
"""
class node():
    def __init__(self, x, y, side, part):
        self.x = x
        self.y = y
        self.side = side
        self.part = part
        self.child = None
        self.parent = None

"""
    Snake is able to add more body when eating apple
"""
class SNAKE():
    def __init__(self):

        # the length is the score
        self.length = 2

        self.head = None
        self.tail = None
        self.bodies = []
        self.last_tail = node(None, None, None, "tail")
        self.initialize_position()

    def initialize_position(self):

        # Initial position of snake
        self.head = node(BLOCK_SIZE , 0, "right", "head")
        self.tail = node(0, 0, "right", "tail")

        self.head.child = self.tail
        self.tail.parent = self.head

    def add_body(self):
        """
            When eating apple, the snake add body the the last element body near the tail
        """

        # duplicate tail
        x = self.tail.x
        y = self.tail.y
        side = self.tail.side
        side = self.body_side(self.tail.side)
        if side == "left" or side == "right": side = "horizontal"
        elif side == "up" or side == "down": side = "verticle"
        
        # body to tail
        body = node(x, y, side, "body")
        body.child = self.tail
        self.tail.parent = body
        self.tail.x = self.last_tail.x
        self.tail.y = self.last_tail.y
        self.tail.side = self.last_tail.side

        # The first body, body to head
        if self.bodies == []:
            body.parent = self.head
            self.head.child = body
            self.bodies.append(body)
            return

        # body to body
        last_body = self.bodies[-1]
        body.parent = last_body
        last_body.child = body
        self.bodies.append(body)
        self.length += 1

    def body_side(self, side):

        # Get the side when it turn
        if side == "up" and self.last_tail.side == "right" or side == "left" and self.last_tail.side == "down":
            side = "rd"
        elif side == "down" and self.last_tail.side == "right" or side == "left" and self.last_tail.side == "up":
            side = "ru"
        elif side == "up" and self.last_tail.side == "left" or side == "right"  and self.last_tail.side == "down":
            side = "ld"
        elif side == "right" and self.last_tail.side == "up" or side == "down" and self.last_tail.side == "left":
            side = "lu"      
        return side

    def root(self):
        return self.head

    

   