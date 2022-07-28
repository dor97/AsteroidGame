import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BULE = (0,0,255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

class bullet:
    def __init__(self, x, y, dir, count):
        self.val = 8
        self.x = x
        self.y = y
        self.dir = dir
        self.count = count
    
    def move(self):
        self.x += self.val * self.dir[0]
        self.y += self.val * self.dir[1]

    def draw(self, win):
        pygame.draw.circle(win, RED, (self.x, self.y), 2)

