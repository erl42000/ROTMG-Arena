import pygame

class Character:

    def __init__(self, hp, mp, attack, defense, dexterity, speed, vitality, wisdom):
        self.counter = 0
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.speed = speed
        self.vitality = vitality
        self.wisdom = wisdom
        self.lastDirection = "down"
        self.sprite = pygame.image.load("ArcherNeutralDown.png").convert_alpha()

    def leftWalk(self):
        self.lastDirection = "left"
        self.counter += 1
        if self.counter < 10:
            self.sprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()
        elif self.counter < 20:
            self.sprite = pygame.image.load("ArcherWalkLeft2.png").convert_alpha()
        else:
            self.counter = 0

    def rightWalk(self):
        self.lastDirection = "right"
        self.counter += 1
        if self.counter < 10:
            self.sprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()
        elif self.counter < 20:
            self.sprite = pygame.image.load("ArcherWalkRight2.png").convert_alpha()
        else:
            self.counter = 0

    def upWalk(self):

        self.lastDirection = "up"
        self.counter += 1

        if self.counter < 10:

            self.sprite = pygame.image.load("ArcherWalkUp1.png").convert_alpha()

        elif self.counter < 20:

            self.sprite = pygame.image.load("ArcherWalkUp2.png").convert_alpha()

        else:

            self.counter = 0

    def downWalk(self):

        self.lastDirection = "down"
        self.counter += 1

        if self.counter < 10:

            self.sprite = pygame.image.load("ArcherWalkDown1.png").convert_alpha()

        elif self.counter < 20:

            self.sprite = pygame.image.load("ArcherWalkDown2.png").convert_alpha()

        else:

            self.counter = 0

    def leftShoot(self):

        self.lastDirection = "left"
        self.counter += 1

        if self.counter < 10:

            self.sprite = pygame.image.load("ArcherShootLeft1.png").convert_alpha()

        elif self.counter < 20:

            self.sprite = pygame.image.load("ArcherShootLeft2.png").convert_alpha()

        else:

            self.counter = 0

    def rightShoot(self):

        self.lastDirection = "right"

        self.counter += 1

        if self.counter < 10:

            self.sprite = pygame.image.load("ArcherShootRight1.png").convert_alpha()

        elif self.counter < 20:

            self.sprite = pygame.image.load("ArcherShootRight2.png").convert_alpha()

        else:

            self.counter = 0

    def upShoot(self):

        self.lastDirection = "up"
        self.counter += 1

        if self.counter < 10:

            self.sprite = pygame.image.load("ArcherShootUp1.png").convert_alpha()

        elif self.counter < 20:

            self.sprite = pygame.image.load("ArcherShootUp2.png").convert_alpha()

        else:

            self.counter = 0

    def downShoot(self):

        self.lastDirection = "down"
        self.counter += 1

        if self.counter < 10:

            self.sprite = pygame.image.load("ArcherShootDown1.png").convert_alpha()

        elif self.counter < 20:

            self.sprite = pygame.image.load("ArcherShootDown2.png").convert_alpha()

        else:

            self.counter = 0

    def release(self):

        self.counter = 0

        if self.lastDirection == "left":

            self.sprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()

        elif self.lastDirection == "right":

            self.sprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()

        elif self.lastDirection == "up":

            self.sprite = pygame.image.load("ArcherNeutralUp.png").convert_alpha()

        elif self.lastDirection == "down":

            self.sprite = pygame.image.load("ArcherNeutralDown.png").convert_alpha()

class Projectile():

    def __init__(self, angle, lifespan, x, y, xOffset, yOffset, speed, damage, alignment, image):

        self.angle = angle
        self.lifespan = lifespan
        self.x = x
        self.y = y
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.speed = speed
        self.damage = damage
        self.alignment = alignment
        self.image = image