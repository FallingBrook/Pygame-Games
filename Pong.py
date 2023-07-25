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
fps = 40

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
rectP1 = pygame.Rect(20, 63, 10, 37.5)
rectP12 = pygame.Rect(20, 100, 10, 37.5)
rectP2 = pygame.Rect(770, 63, 10, 37.5)
rectP22 = pygame.Rect(770, 100, 10, 37.5)
rectBall = pygame.Rect(500, 100, 15, 15)
velocity = 10
x = 400
y = 300
vx = 6
vy = 6
count = 0
count1 = 0
num1 = randint(-10, 10)
num2 = randint(-10, 10)
direction = 400
distance = 10
c1 = 1
c2 = 1
c3 = 1
c4 = 1
def moveBall():
    global x, y, vx, vy, windowWidth, windowHeight, rectBall, count, count1, num1, num2, direction, distance, c1, c2, c3, c4
    # background(200, 200, 200)
    # fill(112, 48, 160)
    # stroke(255, 255, 255)
    num1 = randint(-10, 10)
    num2 = randint(-10, 10)
    # Bouncing Algorithm when the Ball hit the edge of the canvas
    x = x + vx
    y = y + vy
    if x < 7.5 or x > 792.5:
        vx = -vx
        x = x + vx
    if y < 7.5 or y > 592.5:
        vy = -vy
        y = y + vy
    rectBall = pygame.Rect(x, y, 15, 15)
    print(rectBall.centery)
# 3. set up the basic game loop
done = False
bruv = 0
while done == False:
    moveBall()
    print("yes")
    # if done == False:
    #     rectP1.centery += 5
    #     rectP1.centerx += 5
    # if rectBall.centerx < 0:
    # contents of the game loop
    # moveBall()
    for event in pygame.event.get():
        if event.type == QUIT:  # detecting a quit event
            pygame.quit()
            done = True
    # make sure rectangle doesnt go past border
    if rectP1.top <= 0:
        rectP1.top = 0
    if rectP1.bottom >= 562.5:
        rectP1.bottom = 563
    if rectP2.top <= 0:
        rectP2.top = 0
    if rectP2.bottom >= 562.5:
        rectP2.bottom = 563
    if rectP12.top <= 37.5:
        rectP12.top = 37
    if rectP12.bottom >= 600:
        rectP12.bottom = 600
    if rectP22.top <= 37.5:
        rectP22.top = 37
    if rectP22.bottom >= 600:
        rectP22.bottom = 600
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
    if keys[pygame.K_w]:
         rectP12.centery -= velocity
    if keys[pygame.K_s]:
        rectP12.centery += velocity
    if keys[pygame.K_UP]:
        rectP22.centery -= velocity
    if keys[pygame.K_DOWN]:
        rectP22.centery += velocity
    # check collision
    # if rectBall.centerx <= 7.5:
    #     moveBall()
    # if rectBall.centerx >= 792.5:
    #     moveBall()
    # if rectBall.centery <= 7.5:
    #     moveBall()
    # if rectBall.centery >= 592.5:
    #     moveBall()


    # set the background colour
    window.fill(bgColour)

    # draw the images onto the screen
    # window.blit(player1, player1)
    pygame.draw.rect(window, white, rectP1)
    pygame.draw.rect(window, white, rectP2)
    pygame.draw.rect(window, white, rectP12)
    pygame.draw.rect(window, white, rectP22)
    pygame.draw.rect(window, white, rectBall)
    # update the screen
    pygame.display.flip()
    timer.tick(fps)