import time

import pygame
class pipes:
    xChange = 0
    lives = 3
    checker = 0
    velocity = 8
    def __init__(self, x, width, size, GroundHeight):
        # self.name = name
        self.x = x
        self.size = size
        self.GroundHeight = GroundHeight
        self.width = width
        # self.name = pygame.Rect([self.x, self.GroundHeight-self.size, self.size, self.size])
        # pygame.Rect([self.x, self.GroundHeight-self.size, self.size, self.size])
        # self = pygame.Rect(x, GroundHeight-size, size, size)
    # def draw(self):
    #     # self.rectPipe = rectPipe
    #     numOfPipes1 = str(numOfPipes1)
    #     rectPipe = rectPipe + numOfPipes1
    #     rectPipe = pygame.Rect([self.x, self.GroundHeight-self.size, self.size, self.size])
    @classmethod
    def update(cls):
        cls.xChange += cls.velocity

    def draw(self):
        return self.x - self.xChange, self.GroundHeight-self.size, self.width, self.size

    def drawBound(self):
        return (self.x - 7) - self.xChange, self.GroundHeight-self.size + 10, self.width + 10, self.size

    def drawTop(self):
        return self.x - self.xChange, self.GroundHeight - self.size - 2.1, self.width - 4, 2
    # def drawLeft(self):
    #     return self.x - self.xChange, self.GroundHeight - self.size + 5, 2, self.size
    @classmethod
    def respawn(cls):
        cls.xChange = 0

class goomba:
    change = 4
    width = 40
    count = 0
    size = 40
    GroundHeight = 521
    xChange = 0
    velocity = 8
    walkCountGoomba = 0
    time = 0
    goombaBound = 550
    goombaBound1 = 0
    topper = 0
    # if time % 5 == 0:
    #     goombaChill = goombaWalk1
    # if time % 10 == 0:
    #     goombaChill = goombaWalk2
    def __init__(self, x, xChange, change, walkCountGoomba, goombaBound, goombaBound1, count, velocity, yChange):
        self.x = x
        self.xChange = xChange
        self.change = change
        self.walkCountGoomba = walkCountGoomba
        self.goombaBound = goombaBound
        self.goombaBound1 = goombaBound1
        self.count = count
        self.velocity = velocity
        self.yChange = yChange
        # self.length = length

    def updateGoomba2(self):
        self.xChange += self.velocity
        self.goombaBound += self.velocity
        self.goombaBound1 += self.velocity
        self.count = 1

    def updateGoomba(self):
        if self.walkCountGoomba == 0:
            self.xChange += self.change

        if self.walkCountGoomba == 1:
            self.xChange -= self.change
            # if cls.count == 1:
            #     cls.xChange += 8

        if self.xChange >= self.goombaBound:
            self.walkCountGoomba = 1

        if self.xChange <= self.goombaBound1:
            self.walkCountGoomba = 0

    @classmethod
    def checker(cls):
        cls.xChange += 4

    def draw(self):
        return self.x - self.xChange, self.GroundHeight-self.size - self.yChange, self.size, self.size

    def drawBound(self):
        return self.x - self.xChange, self.GroundHeight-self.size - self.yChange + 4, self.size, self.size

    def drawTop(self):
        return self.x - self.xChange + self.topper + 1, self.GroundHeight - self.size - 2.1, self.size - 2, 2

    def move(self):
        self.yChange -= 20
        self.change = 0
        self.topper = 1000

    def dead(self):
        self.yChange -= 20
        self.change = 0
        self.x = -20
    # def respawn(self):
    #     # self.xChange = 0
    #     self.yChange = 0
    #     self.change = 0
    # def drawLeft(self):
    #     return self.x - self.xChange, self.GroundHeight - self.size + 5, 2, self.size