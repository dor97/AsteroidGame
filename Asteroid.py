import random
import math
import pygame

width, height = 700, 500

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BULE = (0,0,255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

class asteroid:
    def __init__(self, size = 4, x = 0, y = 0, deg = 0, inScreen = 0):
        if size == 4:
            self.moveDegree = random.randint(0,45)
            self.corder = random.randint(1,8)
            self.xInCorder = random.randint(0, 200)
            self.yInCorder = random.randint(0, 200)
            self.inScreen = False
            self.findXandY()
        else:
            self.moveDegree = deg
            self.x = x
            self.y = y
            self.inScreen = inScreen
        self.val = 2
        self.pos = (self.x, self.y)
        #print(self.corder)
        self.size = size
        self.len = 8 * self.size
        self.dir = pygame.Vector2(0, -self.len).rotate(22.5)
        self.hitBoxVecX = (int)((self.len * math.sin(math.radians(67.5)) - self.len * math.sin(math.radians(22.5))) * (2 / 3) + self.x + self.len * math.sin(math.radians(22.5)))
        #self.rectX2 = (int)(self.x - (self.len * math.sin(math.radians(67.5)) - self.len * math.sin(math.radians(22.5))))
        self.hitBoxVecY = (int)(self.y - self.len * math.sin(math.radians(22.5)) - (self.len * math.sin(math.radians(67.5)) - self.len * math.sin(math.radians(22.5))) * (2 / 3))
        #self.rectY2 = (int)(self.y + (self.len * math.sin(math.radians(67.5)) - self.len * math.sin(math.radians(22.5))))
        self.hitBoxVec = pygame.Vector2(self.hitBoxVecX - self.x, self.hitBoxVecY - self.y)
        self.hitBoxRotateDegree = 0
        #self.vecDir = (pygame.Vector2(0, self.len)).rotate(self.deg)
        self.moveRadian = math.radians(self.moveDegree)
        self.vecDir = pygame.Vector2(self.len * math.cos(self.moveRadian), self.len * math.sin(self.moveRadian))
        


    def findXandY(self):
        if self.corder == 1:
            self.x = self.xInCorder - 200
            self.y = self.yInCorder
        elif self.corder == 2:
            self.x = self.xInCorder - 200
            self.y = height - self.yInCorder
            self.moveDegree += 315
        elif self.corder == 3:
            self.x = self.xInCorder
            self.y = height + self.yInCorder
            self.moveDegree += 270
        elif self.corder == 4:
            self.x = width - self.yInCorder
            self.y = height + self.yInCorder
            self.moveDegree += 225
        elif self.corder == 5:
            self.x = width + self.xInCorder
            self.y = height - self.yInCorder
            self.moveDegree += 180
        elif self.corder == 6:
            self.x = width + self.xInCorder
            self.y = self.yInCorder
            self.moveDegree += 135
        elif self.corder == 7:
            self.x = width - self.xInCorder
            self.y = -self.yInCorder
            self.moveDegree += 90
        else:
            self.x = self.xInCorder
            self.y = -self.yInCorder
            self.moveDegree += 45
        


    def draw(self, win, displayHitBox):
        self.pos = (self.x, self.y)
        #pygame.draw.polygon(win, BULE, [self.pos + temp, self.pos + temp.rotate(72), self.pos + temp.rotate(72*2), self.pos + temp.rotate(72*3), self.pos + temp.rotate(72*4)])
        #pygame.draw.polygon(win, BULE, [self.pos + temp, self.pos + temp.rotate(60), self.pos + temp.rotate(60*2), self.pos + temp.rotate(60*3), self.pos + temp.rotate(60*4), self.pos + temp.rotate(60*5)], 4)
        pygame.draw.polygon(win, BULE, [self.pos + self.dir, self.pos + self.dir.rotate(45), self.pos + self.dir.rotate(45*2), self.pos + self.dir.rotate(45*3), self.pos + self.dir.rotate(45*4), self.pos + self.dir.rotate(45*5), self.pos + self.dir.rotate(45*6), self.pos + self.dir.rotate(45*7)],5)
        if displayHitBox:
            pygame.draw.polygon(win, GREEN, [self.pos + self.hitBoxVec, self.pos + self.hitBoxVec.rotate(90), self.pos + self.hitBoxVec.rotate(2*90), self.pos + self.hitBoxVec.rotate(3*90)], 1)
            pygame.draw.line(win, RED, self.pos, self.pos + self.hitBoxVec)
            pygame.draw.line(win, BULE, self.pos, self.pos + self.vecDir)
        self.hitBoxRotateDegree = (self.hitBoxRotateDegree + 1) % 360
        self.dir = self.dir.rotate(1)
        self.hitBoxVec = self.hitBoxVec.rotate(1)



    def move(self):
        #print(self.x, self.y)
        self.x += self.val * math.cos(self.moveRadian)
        self.y += self.val * math.sin(self.moveRadian)
        if not self.inScreen:
            self.inScreen = self.checkInScren()
        
    def checkInScren(self):
        if 0 < self.x < width and 0 < self.y < height:
            return True
        else: 
            return False
