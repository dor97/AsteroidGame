import pygame
from Bullet import bullet

width, height = 700, 500

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BULE = (0,0,255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


class player:
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.pos = (self.x, self.y)
        self.dir1 = pygame.Vector2(0, -1)
        self.dir2 = self.dir1.rotate(120)
        #self.dir2.scale_to_length(self.dir1.length() / 2)
        self.dir3 = self.dir2.rotate(120)
        self.color = RED
        self.bullets = []
        self.val = 0
        self.speedX = 0
        self.speedY = 0
        self.hitBoxRotateDegree = 0
        self.isAlive = True
        self.score = 0

    def draw(self, win, displayHitBox):
        if self.isAlive:
            pygame.draw.polygon(win, self.color, [self.pos + self.dir1 / self.dir1.length() * 20, self.pos + self.dir2 / self.dir2.length() * 10, self.pos + self.dir3 / self.dir3.length() * 10], 3)
            self.hitBoxPos1 = self.dir2 * 10
            self.hitBoxPos2 = self.dir3 * 10
            self.hitBoxPos3 = self.dir1 * 16 - (self.hitBoxPos1 - self.hitBoxPos2) / 2
            self.hitBoxPos4 = self.dir1 * 16 + (self.hitBoxPos1 - self.hitBoxPos2) / 2
            if displayHitBox:
                pygame.draw.polygon(win, BULE, [self.pos + self.hitBoxPos1, self.pos + self.hitBoxPos2, self.pos + self.hitBoxPos3, self.pos + self.hitBoxPos4], 2)
                pygame.draw.line(win, GREEN, self.pos , self.pos + self.dir1 * 20)        
        #print(self.rectPos1, self.rectPos2, self.rectPos3, self.rectPos4)

        # ship = pygame.image.load("spaceShip_red.png")
        # ship = pygame.transform.scale(ship, (80, 80))
        # win.blit(ship, (self.x, self.y))
    def move(self):
        # self.x += self.dir1[0]
        # self.y += self.dir1[1]
        # if self.dir1.length() > 10:
        #     self.dir1.scale_to_length(10)
        # self.pos = (self.x, self.y)
        
        if self.val > 4:
            self.val = 4
        if self.val < -4:
            self.val = -4
        self.x += self.val * self.dir1[0]
        self.y += self.val * self.dir1[1]
        self.val -= self.val / abs(self.val) / 5
        self.pos = (self.x, self.y) 
        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        if self.y < 0:
            self.y = height
        elif self.y > height:
            self.y = 0

    def rotate(self, angle):
        self.hitBoxRotateDegree = (self.hitBoxRotateDegree + angle) % 360
        self.dir1 = self.dir1.rotate(angle)
        self.dir2 = self.dir2.rotate(angle)
        self.dir3 = self.dir3.rotate(angle)

    def addBullet(self):
        if len(self.bullets) < 10:
            self.bullets.append(bullet(self.x + self.dir1[0], self.y + self.dir1[1], self.dir1, 100))

    def drawBullet(self, win):
        rem = []
        for bullet in self.bullets:
            bullet.draw(win)
            bullet.move()
            bullet.count -= 1
            if bullet.count == 0:
                rem.append(bullet)
        for i in rem:
            self.bullets.remove(i)

    def removeBullet(self, bullet):
        self.bullets.remove(bullet)

    def makeLossAnime(self):
        self.explosions = [bullet(self.x, self.y, self.dir2, 10), bullet(self.x, self.y, self.dir2.rotate(360 - 60), 10), bullet(self.x, self.y, self.dir3, 10), bullet(self.x, self.y, self.dir3.rotate(60), 10)]

    def lossAnime(self, win):
        self.explosions[0].count -= 1
        for explosion in self.explosions:
            explosion.draw(win)
            explosion.move()