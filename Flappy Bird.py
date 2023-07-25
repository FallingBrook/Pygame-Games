# 1. import the pygame files
import pygame  # lets us use pygame files
from pygame.locals import *  # to make life easier for us
import random
# import pipedown from './images/pipedown.png'

# global variable declarations
windowWidth = 500
windowHeight = 600
timer = None
window = None
fps = 30

# background colour
bgColour = pygame.Color(255, 255, 255)

# load the images
backGround = pygame.image.load('flappybirdbackground.png')
flapUp = pygame.image.load('flapup.png')
flap = pygame.image.load('flap.png')
flapDown = pygame.image.load('flapdown.png')
floor = pygame.image.load('ground.png')
pipeUp = pygame.image.load('pipeup.png')
pipeDown = pygame.image.load('pipedown.png')
grave = pygame.image.load('th (3).png')
dead = pygame.image.load('flap copy.png')

# resize the images
backGround = pygame.transform.scale(backGround, (1000, windowHeight))
flapUp = pygame.transform.scale(flapUp, (45, 35))
flap = pygame.transform.scale(flap, (45, 35))
flapDown = pygame.transform.scale(flapDown, (45, 35))
floor = pygame.transform.scale(floor, (1000, 50))
pipeUp = pygame.transform.scale(pipeUp, (75, 300))
pipeDown = pygame.transform.scale(pipeDown, (75, 300))
grave = pygame.transform.scale(grave, (45, 50))
dead = pygame.transform.scale(dead, (45, 35))

# 2. initalize the window
pygame.init()  # MUST write this before using any pygame functions
timer = pygame.time.Clock()  # this is a variable btw
window = pygame.display.set_mode((windowWidth, windowHeight))  # set the size of the window
pygame.display.set_caption("Introduction to Pygame")  # set the title of the window

# character coordinates
sick = random.randrange(-200, 0) # pipe down
sick1 = sick + 450 # pipe up
sick12 = random.randrange(-200, 0)  # pipe down
sick13 = sick12 + 450  # pipe up
rect = pygame.Rect(170, 200, 40, 40)
rectPipeUp = pygame.Rect(550, sick1, 75, 300)
rectPipeDown = pygame.Rect(550, sick, 75, 300)
rectPipeUp1 = pygame.Rect(900, sick13, 75, 300)
rectPipeDown1 = pygame.Rect(900, sick12, 75, 300)
rectPoint1 = pygame.Rect(575, 150, 75, 300)
rectPoint2 = pygame.Rect(925, 150, 75, 300)
# 0 max and -200 min for pipedown
# 500 max and 250 min for pipe up
rectGround = pygame.Rect(0, 520, 800, 100)
rectFloor = pygame.Rect(0, 550, 0, 0)
rectBack = pygame.Rect(0, 0, 0, 0)
vel = 5
jump = False
jumpCount = 0
jumpMax = 14
red = (255,0,0)
points = 0
sum = 0
pointCheck = 0
height = rect.midbottom

# Determine which coordinates
def spawnPipe():
    global rectPipeUp1
    global rectPipeDown1
    global rectPoint2
    global pointy12
    global sick12
    global sick13
    global rectPipeUp
    global rectPipeDown
    global rectPoint1
    global pointy11
    global sick
    global sick1
    sick = random.randrange(-200, 0) # pipe down
    sick1 = sick + 450 # pipe up
    rectPipeUp = pygame.Rect(550, sick1, 75, 300)
    rectPipeDown = pygame.Rect(550, sick, 75, 300)
    pointy11 = sick1 - 150
    rectPoint1 = pygame.Rect(550, pointy11, 20, 150)

    sick12 = random.randrange(-200, 0) # pipe down
    sick13 = sick12 + 450 # pipe up
    rectPipeUp1 = pygame.Rect(900, sick13, 75, 300)
    rectPipeDown1 = pygame.Rect(900, sick12, 75, 300)
    pointy12 = sick13 - 150
    rectPoint2 = pygame.Rect(900, pointy12, 20, 150)
def newPipe():
    global rectPipeUp
    global rectPipeDown
    global rectPoint1
    global pointy11
    global sick
    global sick1
    sick = random.randrange(-200, 0) # pipe down
    sick1 = sick + 450 # pipe up
    rectPipeUp = pygame.Rect(550, sick1, 75, 300)
    rectPipeDown = pygame.Rect(550, sick, 75, 300)
    pointy11 = sick1 - 150
    rectPoint1 = pygame.Rect(575, pointy11, 20, 150)
def newPipe1():
    global rectPipeUp1
    global rectPipeDown1
    global rectPoint2
    global pointy12
    global sick12
    global sick13
    sick12 = random.randrange(-200, 0) # pipe down
    sick13 = sick12 + 450 # pipe up
    rectPipeUp1 = pygame.Rect(550, sick13, 75, 300)
    rectPipeDown1 = pygame.Rect(550, sick12, 75, 300)
    pointy12 = sick13 - 150
    rectPoint2 = pygame.Rect(575, pointy12, 20, 150)
# second loop for restart
done2 = False
done = False
momma = False
count = 0
direction = "left"
bruh = False
angle = 0
scale = 1
while done2 == False:
    for event in pygame.event.get():
        if event.type == QUIT:  # detecting a quit event
            pygame.quit()
            done2 = True
    # make the bird fall when dead
        if bruh == True:
            if event.type == pygame.KEYDOWN:
                # print("hi")
                score2 = 0
                done = False
                rect = pygame.Rect(170, 200, 40, 40)
                # rectPipeUp = pygame.Rect(550, 450, 75, 300)
                # rectPipeDown = pygame.Rect(550, 0, 75, 300)
                # rectPipeUp1 = pygame.Rect(900, 450, 75, 300)
                # rectPipeDown1 = pygame.Rect(900, 0, 75, 300)
                # rectPoint1 = pygame.Rect(575, 150, 75, 300)
                # rectPoint2 = pygame.Rect(925, 150, 75, 300)
                spawnPipe()
                points = 0
                pointCheck = 0
# 3. set up the basic game loop
    while done == False:
        # contents of the game loop
        for event in pygame.event.get():
            if event.type == QUIT:  # detecting a quit event
                pygame.quit()
                done = True

            if event.type == pygame.KEYDOWN:  # check to see if a key is being pressed
                if event.key == pygame.K_SPACE or event.key == pygame.KEYUP: # jump if space is pressed
                    jump = True
                    jumpCount = jumpMax
        # make objects move left
        if direction == "left":
            rectFloor.centerx -= 5
        if direction == "left":
            rectPipeDown.centerx -= 5
            rectPipeUp.centerx -= 5
            rectPoint1.centerx -= 5
        if direction == "left":
            rectPipeDown1.centerx -= 5
            rectPipeUp1.centerx -= 5
            rectPoint2.centerx -= 5
        # make objects repeat
        if rectFloor.centerx < -150:
            rectFloor.centerx = 0
        if rectPipeUp.centerx < -75 or rectPipeDown.centerx < -75:
            rectPipeUp.centerx = 575
            rectPipeDown.centerx = 575
            newPipe()
        if rectPipeUp1.centerx < -75 or rectPipeDown1.centerx < -75:
            rectPipeUp1.centerx = 575
            rectPipeDown1.centerx = 575
            newPipe1()
        # check collision and add points
        if rect.colliderect(rectGround) == True or rect.colliderect(rectPipeUp) == True or rect.colliderect(rectPipeDown) == True or rect.colliderect(rectPipeUp1) == True or rect.colliderect(rectPipeDown1) == True and count == 0:
            momma = True
            done = True
        # if rect.colliderect(rectGround) == True or rect.colliderect(rectPipeUp) == True or rect.colliderect(rectPipeDown) == True or rect.colliderect(rectPipeUp1) == True or rect.colliderect(rectPipeDown1) == True and count == 0:
        #     done = True
        if rect.colliderect(rectPoint1) == True or rect.colliderect(rectPoint2) == True and pointCheck == 0:
            if pointCheck == 0:
                pointCheck = 1
                points += 1
        if rect.colliderect(rectPoint1) == False and rect.colliderect(rectPoint2) == False:
            pointCheck = 0
        points1 = str(points)

        # algorithm for jumping
        if jump:
            rect.y -= jumpCount
            if jumpCount > -jumpMax:
                jumpCount -= 1.3
            else:
                jump = False

        if jump == False:
            rect.y += 14
        sum = 0

        # text
        blue = (114, 199, 209)
        black = (0, 0, 0)
        white = (255, 255, 255)
        fontObj = pygame.font.Font("flappy-font.ttf", 75)
        textSurfaceObj = fontObj.render("" + points1, True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 150)
        # flap wings
        clock = pygame.time.get_ticks() / 1000 * 70
        sum1 = int(clock)
        sum = sum1 % 2
        if jump == True:
            if sum == 0:
                flap = flapDown
            if sum == 1:
                flap = flapUp
        else:
            flap = flapDown
        # set the background colour
        window.fill(bgColour)

        # draw the images onto the screen

        window.blit(backGround, (rectBack.center))
        window.blit(textSurfaceObj, (textRectObj))
        window.blit(pipeUp, (rectPipeUp))
        window.blit(pipeDown, (rectPipeDown))
        window.blit(pipeUp, (rectPipeUp1))
        window.blit(pipeDown, (rectPipeDown1))
        window.blit(floor, (rectFloor.center))
        window.blit(flap, (rect.topleft))
        # pygame.draw.rect(window, red, (rectPipeDown))
        # pygame.draw.rect(window, red, (rectPipeDown1))
        # pygame.draw.rect(window, red, (rectPipeUp))
        # pygame.draw.rect(window, red, (rectPipeUp1))
        # print(rectPipeDown)

        # update the screen
        pygame.display.flip()
        timer.tick(fps)



    flap = pygame.transform.rotozoom(flap, angle, scale)
    # if done == True and rect.y >= 520:
    window.blit(backGround, rectBack.center)
    window.blit(textSurfaceObj, textRectObj)
    window.blit(pipeUp, rectPipeUp)
    window.blit(pipeDown, rectPipeDown)
    window.blit(pipeUp, rectPipeUp1)
    window.blit(pipeDown, rectPipeDown1)
    window.blit(floor, rectFloor.center)
    window.blit(flap, rect.topleft)
    # make bird fall when dead and end screen
    if done == True and rect.y <= 505:
        flap = dead
        angle -= 10
        rect.centery += 10
    if done == True and rect.y >= 505:
        angle = 0
        scale = 1
        flap = grave
        bruh = True
        black = (0, 0, 0)
        fontObj = pygame.font.Font("KemcoPixelBold.ttf", 20)
        textSurfaceObj = fontObj.render("Your score was:" + points1, True, black)
        textSurfaceObj1 = fontObj.render("Please press enter to restart", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 200)
        textRectObj1 = textSurfaceObj1.get_rect()
        textRectObj1.center = (250, 220)
        window.blit(textSurfaceObj, textRectObj)
        window.blit(textSurfaceObj1, textRectObj1)

    pygame.display.flip()
    timer.tick(fps)