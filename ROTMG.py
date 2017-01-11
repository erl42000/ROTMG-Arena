import pygame
import sys
import os
from time import sleep
from math import asin, acos, sin, cos, pi, sqrt, hypot
from random import randint

from classes import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))
collision = pygame.Surface((800,600), pygame.SRCALPHA)
collision.fill((255,255,255,128))

red          = (255,  0,  0)
green        = (  0,255,  0)
blue         = (  0,  0,255)
white        = (255,255,255)
black        = (  0, 0,  0)
grey         = (127,127,127)

celestialTile = pygame.image.load("CelestialTile.png").convert_alpha()
blackTile     = pygame.image.load("BlackTile.png").convert_alpha()

tileList      = [blackTile, celestialTile]

playerHealth  = 600
enemyHealth   = 12000

sidebar       = [600, 0, 200, 800]
character     = Character(600, 0, 0, 0, 0, 0, 0, 0)
characterXY   = [275, 275]
characterXYHitbox  = [275, 275, 50, 50]
enemyXY = [250, 50]
enemyXYHitbox = [250, 50, 100, 100]

enemyXOffset  = 0
enemyYOffset  = 0

bulletAngle = 0

tileLength    = 50

centerX       = 300
centerY       = 300

frame         = 0
shotDelay     = 15
lastClick     = -60

playerProjectileList  = []
enemyProjectileList  = []

enemySprite1 = pygame.image.load("OldGodStatic1.png").convert_alpha()
enemySprite2 = pygame.image.load("OldGodStatic2.png").convert_alpha()
currentEnemySprite = enemySprite1
projectileSprite = pygame.image.load("arrow.png").convert_alpha()

map_ = open("ROTMG_Map.txt", "r")
mapList = [line.rstrip('\n') for line in map_]
map_.close()

for i in range(0, len(mapList)):

    mapList[i] = list(mapList[i])

mapWidth  = len(mapList) * tileLength
mapHeight = len(mapList[0]) * tileLength

xPos = (mapWidth) / 2
yPos = (mapHeight) / 2


ended = False

step = 0

died = False

while not ended:

    if playerHealth < 600 and died == False:

        playerHealth += 0.4

    playerHealthbar    = [610, 150, int(playerHealth * 3 / 10) , 20]

    enemyHealthbar     = [610, 200, int(enemyHealth * 3 / 200) , 20]

    screen.fill(black)
    collision.fill(white)

    for x in range(-6,7):

        for y in range(-6,7):

            if (xPos / 50) + x < 0 or (yPos / 50) + y < 0:

                pygame.draw.rect(screen, black, (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), tileLength, tileLength))

            else:

                try:

                    screen.blit(tileList[int(mapList[(int(xPos) / 50) + x][(int(yPos) / 50) + y])], (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50))))

                except IndexError:

                    pygame.draw.rect(screen, black, (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), tileLength, tileLength))

    keyDown = pygame.key.get_pressed()

    if playerHealth > 0:
    
        if keyDown[pygame.K_w]:

            yPos = max(0, yPos - 5)

            if yPos <= 0:

                enemyYOffset = 0

            else:

                for i in playerProjectileList:
                    
                    i.yOffset = i.yOffset - 5
                    
                enemyYOffset -= 5

                for i in enemyProjectileList:
                    
                    i.yOffset = i.yOffset - 5

        if keyDown[pygame.K_s]:

            yPos = min(mapHeight, yPos + 5)

            if yPos >= len(mapList[0]) * 50:

                enemyYOffset = 0

            else:

                for i in playerProjectileList:
                    
                    i.yOffset = i.yOffset + 5
                    
                enemyYOffset += 5

                for i in enemyProjectileList:
                    
                    i.yOffset = i.yOffset + 5

        if keyDown[pygame.K_a]:

            xPos = max(0, xPos - 5)

            if xPos <= 0:

                enemyXOffset = 0

            else:

                for i in playerProjectileList:
                    
                    i.xOffset = i.xOffset - 5
                    
                enemyXOffset -= 5

                for i in enemyProjectileList:
                    
                    i.xOffset = i.xOffset - 5

        if keyDown[pygame.K_d]:

            xPos = min(mapWidth, xPos + 5)

            if xPos >= len(mapList) * 50:

                enemyXOffset = 0

            else:

                for i in playerProjectileList:
                    i.xOffset = i.xOffset + 5
                enemyXOffset += 5

                for i in enemyProjectileList:
                    i.xOffset = i.xOffset + 5


    if keyDown[pygame.K_SPACE]:

        pass

    if pygame.mouse.get_pressed()[0]:

        if playerHealth > 0:

            mouseX, mouseY = pygame.mouse.get_pos()

            if frame >= lastClick + shotDelay:

                lastClick = frame

                xLength = centerX - mouseX
                yLength = centerY - mouseY
                distance = hypot(xLength, yLength)

                try:

                    angle = acos(xLength / distance)

                except ZeroDivisionError:

                    angle = 0

                if yLength < 0:

                    angle = 2 * pi - angle

                lifespan = 30
                x = 300
                y = 300
                xOffset = 0
                yOffset = 0
                speed = 10
                damage = 200
                image = projectileSprite

                projectile = Projectile(angle, lifespan, x, y, xOffset, yOffset, speed, damage, image)

                playerProjectileList.append(projectile)

    for i in playerProjectileList:
        
        hitbox = pygame.Rect(i.x, i.y, 5, 5)

        if hitbox.colliderect(enemyXYHitbox) == True and enemyHealth > 0:

            enemyHealth -= randint(i.damage - 25, i.damage + 25)

            playerProjectileList.remove(i)

        else:

            if i.lifespan <= 25:

                screen.blit(pygame.transform.rotate(i.image, (i.angle - 3 * pi/4) * (-180/pi)), (int(i.x - 30), int(i.y - 30)))

            pygame.draw.rect(collision, red, (int(i.x), int(i.y), 5, 5))

            i.x -= i.speed * cos(i.angle) + i.xOffset
            i.y -= i.speed * sin(i.angle) + i.yOffset
            i.xOffset = 0
            i.yOffset = 0

            i.lifespan -= 1

            if i.lifespan <= 0:

                playerProjectileList.remove(i)

    for i in enemyProjectileList:

        hitbox = pygame.Rect(i.x, i.y, 5, 5)

        if hitbox.colliderect(characterXYHitbox) == True and playerHealth > 0:

            playerHealth -= randint(i.damage - 25, i.damage + 25)

            enemyProjectileList.remove(i)
            
        else:

            screen.blit(pygame.transform.rotate(i.image, (i.angle - 3 * pi/4) * (-180/pi)), (int(i.x - 30), int(i.y - 30)))

            pygame.draw.rect(collision, red, (int(i.x), int(i.y), 5, 5))

            i.x -= i.speed * cos(i.angle) + i.xOffset
            i.y -= i.speed * sin(i.angle) + i.yOffset
            i.xOffset = 0
            i.yOffset = 0

            i.lifespan -= 1

            if i.lifespan <= 0:

                enemyProjectileList.remove(i)

    if pygame.mouse.get_pressed()[0]:

        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseY - 300 >= abs(mouseX - 300):

            character.downShoot()

        elif mouseX - 300 >= abs(mouseY - 300):

            character.rightShoot()

        elif -mouseY + 300 >= abs(mouseX - 300):

            character.upShoot()

        elif -mouseX + 300 >= abs(mouseY - 300):

            character.leftShoot()

    elif keyDown[pygame.K_w] and keyDown[pygame.K_s]:

        character.release()

    elif keyDown[pygame.K_a] and keyDown[pygame.K_d]:

        character.release()

    elif keyDown[pygame.K_a]:

        character.leftWalk()

    elif keyDown[pygame.K_d]:

        character.rightWalk()

    elif keyDown[pygame.K_w]:

        character.upWalk()

    elif keyDown[pygame.K_s]:

        character.downWalk()

    else:

        character.release()

    if frame % 90 == 0:

        currentEnemySprite = enemySprite1

    elif frame % 90 == 75:

        currentEnemySprite = enemySprite2
        
    if playerHealth > 0 and enemyHealth > 0:

        if frame % 30 == 0:

            xLength = centerX - enemyXY[0] - 50
            yLength = centerY - enemyXY[1] - 50
            distance = hypot(xLength, yLength)

            try:

                angle = acos(xLength / distance)

            except ZeroDivisionError:

                angle = 0

            if yLength < 0:

                angle = 2 * pi - angle

            angle = angle + pi

            lifespan = 75
            x = enemyXY[0] + 50
            y = enemyXY[1] + 50
            xOffset = 0
            yOffset = 0
            speed = 5
            damage = 120
            image = pygame.image.load("MediumEnergy.png").convert_alpha()

            projectile = Projectile(angle, lifespan, x, y, xOffset, yOffset, speed, damage, image)

            enemyProjectileList.append(projectile)

        if frame % 20 == 0:

            lifespan = 175
            x = enemyXY[0] + 75
            y = enemyXY[1] + 75
            xOffset = 0
            yOffset = 0
            speed = 3
            damage = 100
            image = pygame.image.load("SmallEnergy.png").convert_alpha()

            projectile = Projectile(bulletAngle, lifespan, x, y, xOffset, yOffset, speed, damage, image)

            enemyProjectileList.append(projectile)

            projectile = Projectile(bulletAngle + ((1/2.0) * pi), lifespan, x, y, xOffset, yOffset, speed, damage, image)

            enemyProjectileList.append(projectile)

            projectile = Projectile(bulletAngle + (pi), lifespan, x, y, xOffset, yOffset, speed, damage, image)

            enemyProjectileList.append(projectile)

            projectile = Projectile(bulletAngle + ((3 / 2.0) * pi), lifespan, x, y, xOffset, yOffset, speed, damage, image)

            enemyProjectileList.append(projectile)

            bulletAngle += (pi/3)

    enemyXY[0] -= enemyXOffset
    enemyXY[1] -= enemyYOffset
    enemyXYHitbox[0] -= enemyXOffset
    enemyXYHitbox[1] -= enemyYOffset

    enemyXOffset = 0
    enemyYOffset = 0

    if playerHealth > 0:
        
        screen.blit(character.characterSprite, characterXY)
        pygame.draw.rect(collision, grey, characterXYHitbox)
        
    if enemyHealth > 0:
        
        screen.blit(currentEnemySprite, enemyXY)
        pygame.draw.rect(collision, grey, enemyXYHitbox)
        
    pygame.draw.rect(screen, grey, sidebar)
    pygame.draw.rect(screen, black, (605, 145, 190, 30))
    pygame.draw.rect(screen, black, (605, 195, 190, 30))
    
    if playerHealth > 0:
        
        pygame.draw.rect(screen, green, playerHealthbar)

    if enemyHealth > 0:

        pygame.draw.rect(screen, red, enemyHealthbar)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            ended = True

    pygame.display.flip()

    sleep(1.0/60)

    frame += 1

    playerHealth = max(0, playerHealth)

    if playerHealth == 0:

        died = True

pygame.quit()
