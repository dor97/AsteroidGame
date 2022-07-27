from math import cos, sin
#from msilib.schema import Font
import pygame
import math
import numpy as np
from Player import player
from Asteroid import asteroid

pygame.init()
width, height = 700, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('ASTEROIDS')
FPS =60
FONT = pygame.font.SysFont('comicsans', 20)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BULE = (0,0,255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)



def collision(rectPos1, rectPos2, rectPos3, rectPos4, rotateDegree, checkCollisionPos1, checkCollisionPos2 = 0, checkCollisionPos3 = 0, checkCollisionPos4 = 0, checkCollisionPos5 = 0, checkCollisionPos6 = 0, checkCollisionPos7 = 0, checkCollisionPos8 = 0):
    # d = vec.angle_to(pygame.Vector2(1,1))
    # if d >= 0:
    #     deg = 360 - d
    # else:
    #     deg = -d
    rotateDegree = 360 - rotateDegree
    #deg = 360 - vec.angle_to(pygame.Vector2(1,0))
    rot = np.array([[math.cos(math.radians(rotateDegree)), math.sin(math.radians(rotateDegree))], [-math.sin(math.radians(rotateDegree)), math.cos(math.radians(rotateDegree))]])
    newRectpos1 = np.array(rectPos1) @ rot
    newRectpos2 = np.array(rectPos2) @ rot
    newRectpos3 = np.array(rectPos3) @ rot
    newRectpos4 = np.array(rectPos4) @ rot
    x = [newRectpos1[0], newRectpos2[0], newRectpos3[0], newRectpos4[0]]
    y = [newRectpos1[1], newRectpos2[1], newRectpos3[1], newRectpos4[1]]
    x.sort()
    y.sort()
    checkCollisionPos1 = np.array(checkCollisionPos1) @ rot

    if checkCollisionPos2 == 0:
        if x[0] < checkCollisionPos1[0] < x[-1] and y[0] < checkCollisionPos1[1] < y[-1]:
            return True
        else:
            return False
    else:
        checkCollisionPos2 = np.array(checkCollisionPos2) @ rot
        checkCollisionPos3 = np.array(checkCollisionPos3) @ rot

        #print(pos1, pos2, pos3, pos4, pos)
        if checkCollisionPos4 == 0:
            if (x[0] < checkCollisionPos1[0] < x[-1] and y[0] < checkCollisionPos1[1] < y[-1]) or (x[0] < checkCollisionPos2[0] < x[-1] and y[0] < checkCollisionPos2[1] < y[-1]) or (x[0] < checkCollisionPos3[0] < x[-1] and y[0] < checkCollisionPos3[1] < y[-1]):
                #print(deg)
                #print(cenPos + vec, cenPos + vec.rotate(90), cenPos + vec.rotate(2*90), cenPos + vec.rotate(3*90))
                #print(pos1, pos2, pos3, pos4, checkCollisionPos1)
                #print("next:")
                return True
            return False
        else:
            checkCollisionPos4 = np.array(checkCollisionPos4) @ rot
            checkCollisionPos5 = np.array(checkCollisionPos5) @ rot
            checkCollisionPos6 = np.array(checkCollisionPos6) @ rot
            checkCollisionPos7 = np.array(checkCollisionPos7) @ rot
            checkCollisionPos8 = np.array(checkCollisionPos8) @ rot
            if (x[0] < checkCollisionPos1[0] < x[-1] and y[0] < checkCollisionPos1[1] < y[-1]) or (x[0] < checkCollisionPos2[0] < x[-1] and y[0] < checkCollisionPos2[1] < y[-1]) or (x[0] < checkCollisionPos3[0] < x[-1] and y[0] < checkCollisionPos3[1] < y[-1]) or (x[0] < checkCollisionPos4[0] < x[-1] and y[0] < checkCollisionPos4[1] < y[-1]) or (x[0] < checkCollisionPos5[0] < x[-1] and y[0] < checkCollisionPos5[1] < y[-1]) or (x[0] < checkCollisionPos6[0] < x[-1] and y[0] < checkCollisionPos6[1] < y[-1]) or (x[0] < checkCollisionPos7[0] < x[-1] and y[0] < checkCollisionPos7[1] < y[-1]) or (x[0] < checkCollisionPos8[0] < x[-1] and y[0] < checkCollisionPos8[1] < y[-1]):
                return True
            return False



def draw(win, playersSpaceShip, asteroidsList, displayHitBox):
    win.fill(BLACK)
    score = FONT.render("score: " + str(playersSpaceShip.score), 1, WHITE)
    win.blit(score, (width - score.get_width() - 10, 10))
    playersSpaceShip.draw(win, displayHitBox)
    for i in asteroidsList:
        i.draw(win, displayHitBox)
    playersSpaceShip.drawBullet(win)
    if not playersSpaceShip.isAlive:
        restart = FONT.render("press r to restart game", 1, WHITE)
        win.blit(restart, (width // 2  - restart.get_width() // 2, height // 2 - restart.get_height() // 2))

def moveAsteroids(asteroidsList):
    rem = []
    for i in asteroidsList:
        i.move()
        if i.inScreen and not i.checkInScren():
            rem.append(i)
    for i in rem:
        asteroidsList.remove(i)

# def getColor(win, x, y):
#     return win.get_at((x, y))

def movePlayer(playersSpaceShip):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        playersSpaceShip.val +=1
    if keys_pressed[pygame.K_s]:
        playersSpaceShip.val -=1
    if keys_pressed[pygame.K_a]:
        playersSpaceShip.rotate(-5)
    if keys_pressed[pygame.K_d]:
        playersSpaceShip.rotate(5)

def checkForCollision(playersSpaceShip, asteroidsList):
    rem = []
    for i in asteroidsList:
        if collision(i.pos + i.hitBoxVec, i.pos + i.hitBoxVec.rotate(90), i.pos + i.hitBoxVec.rotate(2*90), i.pos + i.hitBoxVec.rotate(3*90), i.hitBoxRotateDegree, playersSpaceShip.pos + playersSpaceShip.dir1 * 20, playersSpaceShip.pos + playersSpaceShip.dir2 * 10, playersSpaceShip.pos + playersSpaceShip.dir3 * 10):
            playersSpaceShip.isAlive = False
            playersSpaceShip.makeLossAnime()
            break
        if collision(playersSpaceShip.pos + playersSpaceShip.hitBoxPos1, playersSpaceShip.pos + playersSpaceShip.hitBoxPos2, playersSpaceShip.pos + playersSpaceShip.hitBoxPos3, playersSpaceShip.pos + playersSpaceShip.hitBoxPos4, playersSpaceShip.hitBoxRotateDegree, i.pos + i.dir, i.pos + i.dir.rotate(60), i.pos + i.dir.rotate(2*60), i.pos + i.dir.rotate(3*60), i.pos + i.dir.rotate(4*60), i.pos + i.dir.rotate(5*60), i.pos + i.dir.rotate(6*60), i.pos + i.dir.rotate(7*60)):
            playersSpaceShip.isAlive = False
            playersSpaceShip.makeLossAnime()
            break
        for bullet in playersSpaceShip.bullets:
            if collision(i.pos + i.hitBoxVec, i.pos + i.hitBoxVec.rotate(90), i.pos + i.hitBoxVec.rotate(2*90), i.pos + i.hitBoxVec.rotate(3*90), i.hitBoxRotateDegree, (bullet.x, bullet.y)):
                rem.append(i)
                playersSpaceShip.removeBullet(bullet)
                playersSpaceShip.score += 1
                break
    for i in rem:
        if i.size == 4:
            asteroidsList.append(asteroid(2, i.x, i.y, i.moveDegree - 30, i.inScreen))
            asteroidsList.append(asteroid(2, i.x, i.y, i.moveDegree + 30, i.inScreen))
        asteroidsList.remove(i)
    

def main():
    run = True
    time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    displayHitBox = False

    while run:
        playersSpaceShip = player()
        asteroidsList = []
        game = True
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        playersSpaceShip.addBullet()
                    elif event.key == pygame.K_h:
                        displayHitBox = not displayHitBox
                    elif event.key == pygame.K_r:
                        game = False
            
            movePlayer(playersSpaceShip)
            
            if playersSpaceShip.isAlive:
                checkForCollision(playersSpaceShip, asteroidsList)
                if playersSpaceShip.val != 0:
                    playersSpaceShip.move()
                if len(asteroidsList) < 5 and time + 500 < pygame.time.get_ticks():
                    asteroidsList.append(asteroid())
                    time = pygame.time.get_ticks()
                moveAsteroids(asteroidsList)

                
            #a.draw(win)
            #print(getColor(win, p.x, p.y))
            draw(win, playersSpaceShip, asteroidsList, displayHitBox)
            if not playersSpaceShip.isAlive and playersSpaceShip.explosions[0].count > 0:
                playersSpaceShip.lossAnime(win)
            pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()