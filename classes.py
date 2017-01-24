import pygame

playerProjectileList = []
enemyProjectileList = []

class Character:

    def __init__(self, hp, mp, attack, defense, dexterity, speed, vitality, wisdom):

        self.leftCounter = 0
        self.rightCounter = 0
        self.upCounter = 0
        self.downCounter = 0
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.speed = speed
        self.vitality = vitality
        self.wisdom = wisdom
        self.lastDirection = "down"
        self.characterSprite = pygame.image.load("ArcherNeutralDown.png").convert_alpha()

    def leftWalk(self):

        self.lastDirection = "left"
        self.leftCounter += 1

        if self.leftCounter < 10:

            self.characterSprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()

        elif self.leftCounter < 20:

            self.characterSprite = pygame.image.load("ArcherWalkLeft2.png").convert_alpha()

        else:

            self.leftCounter = 0

    def rightWalk(self):

        self.lastDirection = "right"
        self.rightCounter += 1

        if self.rightCounter < 10:

            self.characterSprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()

        elif self.rightCounter < 20:

            self.characterSprite = pygame.image.load("ArcherWalkRight2.png").convert_alpha()

        else:

            self.rightCounter = 0

    def upWalk(self):

        self.lastDirection = "up"
        self.upCounter += 1

        if self.upCounter < 10:


            self.characterSprite = pygame.image.load("ArcherWalkUp1.png").convert_alpha()

        elif self.upCounter < 20:

            self.characterSprite = pygame.image.load("ArcherWalkUp2.png").convert_alpha()

        else:

            self.upCounter = 0

    def downWalk(self):

        self.lastDirection = "down"
        self.downCounter += 1

        if self.downCounter < 10:

            self.characterSprite = pygame.image.load("ArcherWalkDown1.png").convert_alpha()

        elif self.downCounter < 20:

            self.characterSprite = pygame.image.load("ArcherWalkDown2.png").convert_alpha()

        else:

            self.downCounter = 0

    def leftShoot(self):

        self.lastDirection = "left"
        self.leftCounter += 1

        if self.leftCounter < 10:

            self.characterSprite = pygame.image.load("ArcherShootLeft1.png").convert_alpha()

        elif self.leftCounter < 20:

            self.characterSprite = pygame.image.load("ArcherShootLeft2.png").convert_alpha()

        else:

            self.leftCounter = 0

    def rightShoot(self):

        self.lastDirection = "right"

        self.rightCounter += 1

        if self.rightCounter < 10:

            self.characterSprite = pygame.image.load("ArcherShootRight1.png").convert_alpha()

        elif self.rightCounter < 20:

            self.characterSprite = pygame.image.load("ArcherShootRight2.png").convert_alpha()

        else:

            self.rightCounter = 0

    def upShoot(self):

        self.lastDirection = "up"
        self.upCounter += 1

        if self.upCounter < 10:

            self.characterSprite = pygame.image.load("ArcherShootUp1.png").convert_alpha()

        elif self.upCounter < 20:

            self.characterSprite = pygame.image.load("ArcherShootUp2.png").convert_alpha()

        else:

            self.upCounter = 0

    def downShoot(self):

        self.lastDirection = "down"
        self.downCounter += 1

        if self.downCounter < 10:

            self.characterSprite = pygame.image.load("ArcherShootDown1.png").convert_alpha()

        elif self.downCounter < 20:

            self.characterSprite = pygame.image.load("ArcherShootDown2.png").convert_alpha()

        else:

            self.downCounter = 0

    def release(self):

        self.leftCounter = 0
        self.rightCounter = 0
        self.downCounter = 0
        self.upCounter = 0

        if self.lastDirection == "left":

            self.characterSprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()

        elif self.lastDirection == "right":

            self.characterSprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()

        elif self.lastDirection == "up":

            self.characterSprite = pygame.image.load("ArcherNeutralUp.png").convert_alpha()

        elif self.lastDirection == "down":

            self.characterSprite = pygame.image.load("ArcherNeutralDown.png").convert_alpha()

class Projectile():

    def __init__(self, angle, lifespan, x, y, xOffset, yOffset, speed, damage, image):

        self.angle    = angle
        self.lifespan = lifespan
        self.x        = x
        self.y        = y
        self.xOffset  = xOffset
        self.yOffset  = yOffset
        self.speed    = speed
        self.damage   = damage
        self.image    = image
    
