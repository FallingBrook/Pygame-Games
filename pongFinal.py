# 1. import the pygame files
import pygame# lets us use pygame files
from pygame.locals import *# to make life easier for us
import random
import math
from random import randint


pygame.init()  # MUST write this before using any pygame functions
# global variable declarations
windowWidth = 800
windowHeight = 600
timer = None
window = None
fps = 60

# background colour
bgColour = pygame.Color(0, 0, 0)

#Colors
white = (255, 255, 255)

# load the images

# resize the images

# 2. initalize the window
timer = pygame.time.Clock()  # this is a variable btw
window = pygame.display.set_mode((windowWidth, windowHeight))  # set the size of the window
pygame.display.set_caption("Introduction to Pygame")  # set the title of the window

# character coordinates
rectP1 = pygame.Rect(20, 63, 10, 75)
# rectP12 = pygame.Rect(20, 100, 10, 75)
rectP2 = pygame.Rect(770, 63, 10, 75)
# rectP22 = pygame.Rect(770, 100, 10, 37.5)
rectBall = pygame.Rect(500, 100, 15, 15)
rectTop = pygame.Rect(0, 0, 800, 1)
rectBottom = pygame.Rect(0, 600, 800, 1)
# velocity = 7.5
velocity = 5
randomHeight = random.randint(200, 400)
numPosNeg = randint(0, 1)
randomVyPos = random.randint(1, 6)
randomVyNeg = random.randint(-6, -1)
vyChange = random.randint(-6, 6)
if numPosNeg == 0:
    randomVy = randomVyPos
else:
    randomVy = randomVyNeg
# random number to see which side the ball goes to first
sideStart = randint(0, 1)
if sideStart == 0:
    x = 400
    y = randomHeight
    vx = -3
    vy = randomVy
if sideStart == 1:
    x = 400
    y = randomHeight
    vx = 3
    vy = randomVy
# only once is used to make sure when two rects collide it only counts once not multiple times
onlyOnce = 0
# onceThru is used to know when the program went through moveBall() once
onceThru = 0
# num2 = randint(-10, 10)
direction = 400
distance = 10
done1 = False
done = False
numPos = randint(5, 10)
numNeg1 = randint(5, 10)
numNeg = -numNeg1
# score
scoreP1int = 0
scoreP2int = 0
winner = "none"
def moveBall():
    global x, y, vx, vy, rectBall, onlyOnce, onceThru, numPos, numNeg1, numNeg, randomVyNeg, randomVyPos
    # Bouncing Algorithm when the Ball hit the edge of the canvas
    x = x + vx
    y = y + vy
    numPos = randint(5, 10)
    numNeg1 = randint(5, 10)
    numNeg = -numNeg1
    randomVyPos = random.randint(1, 6)
    randomVyNeg = random.randint(-6, -1)
    if y <= 7.5 or y >= 592.5:
        vy = -vy
        y = y + vy
    if rectBall.colliderect(rectP1) and onlyOnce == 0:
        # make ball speed up after hitting a paddle
        #     onceThru = 1
        onlyOnce = 1
        if vy == 1 or vy == 2 or vy == 3 or vy == 4 or vy == 5 or vy == 6:
            vy = randomVyPos
        if vy == -1 or vy == -2 or vy == -3 or vy == -4 or vy == -5 or vy == -6:
            vy = randomVyNeg
        vx = numPos
        x = x + vx
    else:
        onlyOnce = 0
    if rectBall.colliderect(rectP2) and onlyOnce == 0:
        # make ball speed up after hitting a paddle
        #     onceThru = 1
        onlyOnce = 1
        if vy == 1 or vy == 2 or vy == 3 or vy == 4 or vy == 5 or vy == 6:
            vy = randomVyPos
        if vy == -1 or vy == -2 or vy == -3 or vy == -4 or vy == -5 or vy == -6:
            vy = randomVyNeg
        vx = numNeg
        x = x + vx
    else:
        onlyOnce = 0
    rectBall = pygame.Rect(x, y, 15, 15)
# 3. set up the basic game loop
while done == False:
    for event in pygame.event.get():
        if event.type == QUIT:  # detecting a quit event
            pygame.quit()
            done = True
        keys = pygame.key.get_pressed()  # use for continuous movement
        if keys[pygame.K_SPACE]:
            print("o")
            done1 = False
            scoreP2int = 0
            scoreP1int = 0
    while done1 == False:
        moveBall()
        for event in pygame.event.get():
            if event.type == QUIT:  # detecting a quit event
                pygame.quit()
                done1 = True
        numPosNeg = randint(0, 1)
        randomVyPos = random.randint(1, 6)
        randomVyNeg = random.randint(-6, -1)
        if numPosNeg == 0:
            randomVy = randomVyPos
        else:
            randomVy = randomVyNeg
        if x <= 0:
            scoreP2int += 1
            x = 400
            y = randomHeight
            vx = 3
            vy = randomVy
            onceThru = 0
        if x >= 800:
            scoreP1int += 1
            x = 400
            y = randomHeight
            vx = -3
            vy = randomVy
            onceThru = 0
        if scoreP1int == 10:
            winner = "Player 1"
            done1 = True
        if scoreP2int == 10:
            winner = "Player 2"
            done1 = True
        # make sure rectangle doesnt go past border
        if rectP1.top <= 0:
            rectP1.top = 0
        if rectP1.bottom >= 600:
            rectP1.bottom = 600
        if rectP2.top <= 0:
            rectP2.top = 0
        if rectP2.bottom >= 600:
            rectP2.bottom = 600
        # if rectP12.top <= 37.5:
        #     rectP12.top = 37
        # if rectP12.bottom >= 600:
        #     rectP12.bottom = 600
        # if rectP22.top <= 37.5:
        #     rectP22.top = 37
        # if rectP22.bottom >= 600:
        #     rectP22.bottom = 600
            # if event.type == pygame.KEYDOWN:  # check to see if a key is being pressed
            #     if event.key == pygame.K_w:  # check which specific key
            #         rectP1.centery -= 5
            #     if event.key == pygame.K_s:
            #         rectP1.centery += 5
        keys = pygame.key.get_pressed()  # use for continuous movement


        if keys[pygame.K_w]:
             rectP1.centery -= velocity
        if keys[pygame.K_s]:
            rectP1.centery += velocity
        if keys[pygame.K_UP]:
            rectP2.centery -= velocity
        if keys[pygame.K_DOWN]:
            rectP2.centery += velocity
        # if keys[pygame.K_w]:
        #      rectP12.centery -= velocity
        # if keys[pygame.K_s]:
        #     rectP12.centery += velocity
        # if keys[pygame.K_UP]:
        #     rectP22.centery -= velocity
        # if keys[pygame.K_DOWN]:
        #     rectP22.centery += velocity
        # check collision
        # if rectBall.colliderect(rectP1) or rectBall.colliderect(rectP2) or rectBall.colliderect(rectP22) or rectBall.colliderect(rectP12):
        # moveBall()
        # print("ye")


        # set the background colour
        window.fill(bgColour)
        # text
        black = (0, 0, 0)
        white = (255, 255, 255)
        # change int to str
        scoreP1 = str(scoreP1int)
        scoreP2 = str(scoreP2int)
        # player 1 score text
        fontObj = pygame.font.Font("kemcoPixelBold.ttf", 50)
        scoreTextP1 = fontObj.render("" + scoreP1, True, white)
        rectScoreTextP1 = scoreTextP1.get_rect()
        rectScoreTextP1.center = (325, 100)
        # player 2 score text
        fontObj = pygame.font.Font("kemcoPixelBold.ttf", 50)
        scoreTextP2 = fontObj.render("" + scoreP2, True, white)
        rectScoreTextP2 = scoreTextP1.get_rect()
        rectScoreTextP2.center = (475, 100)
        # draw the images onto the screen
        # window.blit(player1, player1)
        pygame.draw.rect(window, white, rectP1)
        pygame.draw.rect(window, white, rectP2)
        pygame.draw.rect(window, white, rectBall)
        # pygame.draw.rect(window, white, rectTop)
        # pygame.draw.rect(window, white, rectBottom)
        window.blit(scoreTextP1, rectScoreTextP1)
        window.blit(scoreTextP2, rectScoreTextP2)
        # update the screen
        pygame.display.flip()
        timer.tick(fps)
    white = (255, 255, 255)
    fontObj = pygame.font.Font("kemcoPixelBold.ttf", 50)
    endText = fontObj.render("" + winner + " wins", True, white)
    rectEndText = endText.get_rect()
    rectEndText.center = (400, 300)

    fontObj = pygame.font.Font("kemcoPixelBold.ttf", 20)
    endText2 = fontObj.render("press space to replay", True, white)
    rectEndText2 = endText2.get_rect()
    rectEndText2.center = (400, 400)
    window.blit(endText2, rectEndText2)
    window.blit(endText, rectEndText)
    pygame.display.flip()
    timer.tick(fps)