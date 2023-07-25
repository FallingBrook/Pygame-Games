# 1. import the pygame files
import pygame  # lets us use pygame files
from pygame.locals import *  # to make life easier for us
import time
from time import sleep
from marioBrosClasses import pipes
from marioBrosClasses import goomba

# global variable declarations
windowWidth = 1000
windowHeight = 600
timer = None
window = None
fps = 30

# background colour
bgColour = pygame.Color(0, 0, 0)


# load the images
marioStill = pygame.image.load('marioChill.png')
marioRunning1 = pygame.image.load('marioRunning1.png')
marioRunning2 = pygame.image.load('marioRunning2.png')
marioRunning3 = pygame.image.load('marioRunning3.png')
marioJumping = pygame.image.load('marioJumping.png')
bowserStill = pygame.image.load('bowserStill.png')
bowserRunning1 = pygame.image.load('bowserWalking1.png')
bowserRunning2 = pygame.image.load('bowserWalking2.png')
floor = pygame.image.load('marioGround.png')
backGround = pygame.image.load('background.png')
peachChill = pygame.image.load('peachChill.png')
peachRope = pygame.image.load('princessRope.png')
peachRope1 = pygame.image.load('princessRope2.png')
marioPoint = pygame.image.load('marioPoint.png')
backGroundBlue = pygame.image.load('backGroundBlue.png')
pipeUp = pygame.image.load('pipeup.png')
goombaWalk1 = pygame.image.load('goombaWalk1.png')
goombaWalk2 = pygame.image.load('goombaWalk2.png')
goombaSquish = pygame.image.load('goombaSquish.png')
finger = pygame.image.load('finger.png')
castle = pygame.image.load('castle.png')

# resize the images
backGroundBlue = pygame.transform.scale(backGroundBlue, (windowWidth, windowHeight))
pipeUp = pygame.transform.scale(pipeUp, (75, 300))
marioChill = pygame.transform.scale(marioStill, (40, 40))
finger = pygame.transform.scale(finger, (20, 30))
goombaChill = pygame.transform.scale(goombaWalk1, (40, 40))
goombaChill2 = pygame.transform.scale(goombaWalk1, (40, 40))
goombaChill3 = pygame.transform.scale(goombaWalk1, (40, 40))
goombaChill4 = pygame.transform.scale(goombaWalk1, (40, 40))
goombaSquish = pygame.transform.scale(goombaSquish, (40, 20))
goombaWalk1 = pygame.transform.scale(goombaWalk1, (40, 40))
goombaWalk2 = pygame.transform.scale(goombaWalk2, (40, 40))
marioJumping = pygame.transform.scale(marioJumping, (50, 45))
marioVar = pygame.transform.scale(marioStill, (40, 40))
marioPoint = pygame.transform.scale(marioPoint, (50, 40))
marioRunning1 = pygame.transform.scale(marioRunning1, (50, 40))
marioRunning2 = pygame.transform.scale(marioRunning2, (50, 40))
marioRunning3 = pygame.transform.scale(marioRunning3, (50, 40))
bowserChill = pygame.transform.scale(bowserStill, (55, 55))
bowserVar = pygame.transform.scale(bowserStill, (55, 55))
bowserRunning1 = pygame.transform.scale(bowserRunning1, (55, 55))
bowserRunning2 = pygame.transform.scale(bowserRunning2, (55, 55))
ground = pygame.transform.scale(floor, (3000, 120))
backGround = pygame.transform.scale(backGround, (1000, 600))
peachChill = pygame.transform.scale(peachChill, (40, 40))
peachRope = pygame.transform.scale(peachRope, (40, 40))
peachRope1 = pygame.transform.scale(peachRope1, (40, 40))
castle = pygame.transform.scale(castle, (500, 300))
# 2. initalize the window
pygame.init()  # MUST write this before using any pygame functions
timer = pygame.time.Clock()  # this is a variable btw
window = pygame.display.set_mode((windowWidth, windowHeight))  # set the size of the window
pygame.display.set_caption("Introduction to Pygame")  # set the title of the window

# character coordinates
rectMarioIntro = pygame.Rect(-50, 480, 40, 40)
# rectMario = pygame.Rect(50, 480, 40, 40)
rectMario = marioChill.get_rect()
rectMario.centery = 500
rectFinger = finger.get_rect()
rectCastle = castle.get_rect()
rectCastle.centerx = 2500
print(rectMario)
# rectPipe1 = pygame.Rect(1200, 200, 40, 40)
# rectGoomba1 = pygame.Rect(750, 480, 40, 40)
# marioChill = pygame.transform.flip(marioChill, True, False)
rectPeachIntro = pygame.Rect(500, 480, 10, 10)
rectBowserIntro = pygame.Rect(1050, 465, 55, 55)
bowserVar = pygame.transform.flip(bowserVar, True, False)
rectGround = pygame.Rect(0, 510, 3000, 120)
# 3. set up the basic game loop
doneGame = False
doneIntro = True
walkBowser = 0
walkMario = False
time1 = 0
checkLocIntroBowser = 0
yum = ""
sum = 0
sumPeach = 0
sumBowser = 0
sumMario = 0
bumTum = 0
bowserCheckPickPeach = 0
introText = False
introTextPeach = False
introTextBowser = False
introTextMario = False
black = (0, 0, 0)
typeWriter3 = "Hey Shawty, tryna take me out to dinner?"
typeWriter2 = list(typeWriter3)
typeWriter = ""
typeWriter1 = ""

typeWriterPeach3 = "Ew No"
typeWriterPeach2 = list(typeWriterPeach3)
typeWriterPeach = ""
typeWriterPeach1 = ""

typeWriterBowser3 = "Tuff"
typeWriterBowser2 = list(typeWriterBowser3)
typeWriterBowser = ""
typeWriterBowser1 = ""

typeWriterMario3 = "You goofy ah, nobody takes my girl"
typeWriterMario2 = list(typeWriterMario3)
typeWriterMario = ""
typeWriterMario1 = ""
doneLevel1 = False
jump = False
jumpCount = 0
jumpMax = 20
directionCheck = 0
run1 = 1
run2 = 0
run3 = 0
keysCheck1 = 0
keysCheck2 = 0
marioSpeed = 8
jumpMaxer = 0
bum = 0
velocity = 8
colour = (255, 255, 255)
lives = 3

bounceCount = 10
bouncer = 0
fall = False
rectGoomba1 = goomba(560, 0, 4, 0, 550, 0, 0, 8, 0)
rectGoomba2 = goomba(1220, 0, 4, 0, 550, 0, 0, 8, 0)
rectGoomba3 = goomba(1560, 0, 4, 0, 240, 0, 0, 8, 0)
rectPipe1 = pipes(600, 80, 80, 510)
rectPipe2 = pipes(1260, 80, 120, 510)
rectPipe3 = pipes(1600, 80, 160, 510)
rectPipe4 = pipes(1800, 80, 240, 510)
fallCounter = 0
tummy = 0
jumpImportant = False
jumpImportantCheck = False
yJump = 0
bounceCounter = 0
respawn = False
fingerCounter = 0
fingerChecker = False
fingerCount = 0
fingerGone = False
def spawnFinger():
    global rectFinger, finger, fingerCounter, fingerGone, fingerCount
    if fingerCounter == 0:
        rectFinger.centerx = rectMario.centerx
        rectFinger.centery = rectMario.centery
        fingerCounter = 1
    fingerCount += 4
    if fingerCount >= 100:
        fingerGone = True
    if directionCheck == 0 and fingerCount <= 200:
        rectFinger.centerx += 4

    if directionCheck == 1 and fingerCount <= 200:
        rectFinger.centerx -= 4
def bounce():
    global bounceCount
    # if bounceCount >= 5:
    #     pass
    if directionCheck == 0:
        rectMario.centery -= 20
    if directionCheck == 1:
        rectMario.centery -= 20
        # time.sleep(0.1)
bounceActivate = 0
deadCounter = 0
deadCounter2 = 0
deadCounter3 = 0
deadCounter4 = 0
deaddy = 0
deaddy2 = 0
deaddy3 = 0
deaddy4 = 0
deadG1 = False
deadG2 = False
deadG3 = False
runOnce = 0
gOnce1 = 0
gOnce2 = 0
gOnce3 = 0
def Check():
    global jumpMax, marioSpeed, jump, bouncer, bounceCount, rectMario, jumpImportant, jumpImportantCheck, goombaChill, \
        goombaSquish, rectGoomba1, yJump, bounceCounter, bounceActivate, deadCounter, deaddy, jump, deadG1, deadG2, \
        deadG3, runOnce, lives, doneLevel1, goombaChill2, goombaChill3, goombaChill4, deaddy2, deaddy3, deaddy4 \
        , deadCounter2, deadCounter3, deadCounter4, gOnce1, gOnce2, gOnce3
    # rectMario.clamp_ip(window)
    if rectMario.colliderect(rectPipe1.drawBound()) or rectMario.colliderect(rectPipe2.drawBound()) or \
            rectMario.colliderect(rectPipe3.drawBound()) or rectMario.colliderect(rectPipe4.drawBound()):
        print("yeas")
        if directionCheck == 0:
            rectMario.centerx -= 1
            marioSpeed = 0
        if directionCheck == 1:
            rectMario.centerx += 1
            marioSpeed = 0
    else:
        if rectMario.centerx <= 700 and rectMario.centerx >= 20:
            marioSpeed = 8
    if rectMario.colliderect(rectPipe1.drawTop()) or rectMario.colliderect(rectPipe2.drawTop())\
            or rectMario.colliderect(rectPipe3.drawTop()) or rectMario.colliderect(rectPipe4.drawTop()):
        jump = False


    # else:
    #     jump = True
    if rectMario.colliderect(rectGround) and jump == False:
        rectMario.centery = 500
    if not rectMario.colliderect(rectPipe1.drawTop()) and not rectMario.colliderect(rectGround) and jump == False\
        and not rectMario.colliderect(rectPipe2.drawTop()) and not rectMario.colliderect(rectPipe3.drawTop())\
            and not rectMario.colliderect(rectPipe4.drawTop()):
                jump = True

    if rectMario.colliderect(rectGoomba1.drawTop()) and gOnce1 == 0 or rectFinger.colliderect(rectGoomba1.draw()) and \
            gOnce1 == 0:
        yJump += 1
        goombaChill = goombaSquish
        deaddy = 1
        gOnce1 = 1
        rectGoomba1.move()
        print("yes")
        if rectMario.colliderect(rectGoomba1.drawTop()):
            jump = True
        deadG1 = True

    if deaddy == 1:
        deadCounter += 1
        if deadCounter >= 30:
            rectGoomba1.dead()
            deaddy = 0
    else:
        deadCounter = 0

    if rectMario.colliderect(rectGoomba1.drawBound()) and gOnce1 == 0 or rectFinger.colliderect(rectGoomba1.draw()) \
            and gOnce1 == 0:
        if not deadG1 and runOnce == 0:
            lives -= 1
            runOnce = 1
            doneLevel1 = True
            gOnce1 = 1
    else:
        runOnce = 0
        # gOnce1 = 0

    if rectMario.colliderect(rectGoomba2.drawTop()) and gOnce2 == 0 or rectFinger.colliderect(rectGoomba2.draw()) \
            and gOnce2 == 0:
        yJump += 1
        goombaChill2 = goombaSquish
        deaddy2 = 1
        rectGoomba2.move()
        if rectMario.colliderect(rectGoomba2.drawTop()):
            jump = True
        deadG2 = True

    if rectMario.colliderect(rectGoomba2.drawBound()) and gOnce2 == 0 or rectFinger.colliderect(rectGoomba2.draw()) \
            and gOnce2 == 0:
        if not deadG2 and runOnce == 0:
            lives -= 1
            runOnce = 1
            doneLevel1 = True
            gOnce2 = 1
    else:
        runOnce = 0
        gOnce2 = 0

    if deaddy2 == 1:
        deadCounter2 += 1
        if deadCounter2 >= 30:
            rectGoomba2.dead()
            deaddy2 = 0
    else:
        deadCounter2 = 0

    if rectMario.colliderect(rectGoomba3.drawTop()) and gOnce3 == 0 or rectFinger.colliderect(rectGoomba3.draw()) \
            and gOnce3 == 0:
        yJump += 1
        goombaChill3 = goombaSquish
        deaddy3 = 1
        rectGoomba3.move()
        if rectMario.colliderect(rectGoomba3.drawTop()):
            jump = True
        deadG3 = True

    if rectMario.colliderect(rectGoomba3.drawBound()) and gOnce3 == 0 or rectFinger.colliderect(rectGoomba3.draw()) \
            and gOnce3 == 0:
        if not deadG3 and runOnce == 0:
            lives -= 1
            runOnce = 1
            doneLevel1 = True
            gOnce1 = 1
    else:
        runOnce = 0
        gOnce1 = 0

    if deaddy3 == 1:
        deadCounter3 += 1
        if deadCounter3 >= 30:
            rectGoomba3.dead()
            deaddy3 = 0
    else:
        deadCounter3 = 0


            # bounceCounter += 1



        # rectMario.centery = 500
    # print(rectMario.centery)
                # rectGround.centerx -= 8
# pipes.Check()
# pipes.draw(rectPipe1)
# rectPipe1.draw(window)
bossChecker = False
def fadeout():
    fadeout = pygame.Surface((windowWidth, windowHeight))
    fadeout = fadeout.convert()
    fadeout.fill(black)
    for i in range(150):
        fadeout.set_alpha(i)
        window.blit(fadeout, (0, 0))
        pygame.display.update()


def fadein():
    fadein = pygame.Surface((windowWidth, windowHeight))
    fadein = fadein.convert()
    fadein.fill(black)
    for i in range(1):
        fadein.set_alpha(255-i)
        window.blit(fadein, (0, 0))
        pygame.display.update()
tum = 0
keys = pygame.key.get_pressed()  # use for continuous movement
while doneGame == False:
    keys = pygame.key.get_pressed()  # use for continuous movement
    time1 += 1
    # contents of the game loop
    for event in pygame.event.get():
        if event.type == QUIT:  # detecting a quit event
            pygame.quit()
            doneGame = True
    while doneIntro == False:
        time1 += 1
        for event in pygame.event.get():
            if event.type == QUIT:  # detecting a quit event
                pygame.quit()
                doneGame = True
                doneIntro = True
        if rectBowserIntro.centerx >= 700 and checkLocIntroBowser == 0:
            walkBowser = 0
            rectBowserIntro.centerx -= 4
        if rectBowserIntro.centerx <= 701 and checkLocIntroBowser == 0:
            walkBowser = 1
            checkLocIntroBowser = 1
            bowserVar = bowserChill
            bowserVar = pygame.transform.flip(bowserVar, True, False)
            peachChill = pygame.transform.flip(peachChill, True, False)
        if introText == False and time1 % 3 == 0 and rectBowserIntro.centerx <= 701:
            typeWriter1 = str(typeWriter2[sum])
            typeWriter = typeWriter + typeWriter1
            sum += 1
        if typeWriter1 == "?":
            introText = True
        if introTextPeach == False and introText == True and time1 % 3 == 0 and rectBowserIntro.centerx <= 701:
            typeWriterPeach1 = str(typeWriterPeach2[sumPeach])
            typeWriterPeach = typeWriterPeach + typeWriterPeach1
            if typeWriterPeach1 == "o":
                introTextPeach = True
            sumPeach += 1
        if introTextBowser == False and introTextPeach == True and time1 % 3 == 0:
            typeWriterBowser1 = str(typeWriterBowser2[sumBowser])
            typeWriterBowser = typeWriterBowser + typeWriterBowser1
            if typeWriterBowser == "Tuff":
                introTextBowser = True
            sumBowser += 1
        if introTextBowser == True:
            if rectBowserIntro.centerx > 0:
                walkBowser = 0
            if rectBowserIntro.centerx >= 550 and bowserCheckPickPeach == 0:
                rectBowserIntro.centerx -= 4
            if rectBowserIntro.centerx <= 550:
                bowserCheckPickPeach = 1
            if bowserCheckPickPeach == 1:
                rectBowserIntro.centerx += 4
                rectPeachIntro = rectBowserIntro.midtop
                if rectBowserIntro.centerx <= 550:
                    # peachChill = peachRope
                    rectPeachIntro = pygame.Rect(500, 483, 10, 10)
                    # bowserVar = pygame.transform.flip(bowserVar, True, False)
                    # peachChill = pygame.transform.flip(peachChill, True, False)
                    rectBowserIntro.centerx += 4
                if rectBowserIntro.centerx >= 1100:
                    fadeout()
                    doneIntro = True
        if bowserCheckPickPeach != 1:
            if walkBowser == 0 and time1 % 15 == 0:
                bowserVar = bowserChill
                bowserVar = pygame.transform.flip(bowserVar, True, False)
            if walkBowser == 0 and time1 % 20 == 0:
                bowserVar = bowserRunning1
                bowserVar = pygame.transform.flip(bowserVar, True, False)
            if walkBowser == 0 and time1 % 25 == 0:
                bowserVar = bowserRunning2
                bowserVar = pygame.transform.flip(bowserVar, True, False)
        if bowserCheckPickPeach == 1:
            if walkBowser == 0 and time1 % 15 == 0:
                bowserVar = bowserChill
            if walkBowser == 0 and time1 % 20 == 0:
                bowserVar = bowserRunning1
            if walkBowser == 0 and time1 % 25 == 0:
                bowserVar = bowserRunning2
            if rectMarioIntro.centerx < 100:
                rectMarioIntro.centerx += 5
                walkMario = True
            if rectMarioIntro.centerx >= 100:
                rectMarioIntro.centerx += 0
                walkMario = False
                marioVar = marioPoint
        if walkMario == True:
            if walkMario == 0 and time1 % 15 == 0:
                marioVar = marioRunning1
            if walkMario == 0 and time1 % 20 == 0:
                marioVar = marioRunning2
            if walkMario == 0 and time1 % 25 == 0:
                marioVar = marioRunning3
        if introTextMario == False and rectMarioIntro.centerx > 90 and time1 % 3 == 0:
            typeWriterMario1 = str(typeWriterMario2[sumMario])
            typeWriterMario = typeWriterMario + typeWriterMario1
            if typeWriterMario1 == "l":
                introTextMario = True
            sumMario += 1

        # if event.type == pygame.KEYDOWN:  # check to see if a key is being pressed
        #     if event.key == pygame.K_w:  # check which specific key
        #     if event.key == pygame.K_s:
        #
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_a or event.key == pygame.K_d:

        # set the background colour
        window.fill(bgColour)

        # draw the images onto the screen
        window.blit(backGround, (0, 0))
        window.blit(marioVar, rectMarioIntro)
        window.blit(bowserVar, rectBowserIntro)
        window.blit(peachChill, rectPeachIntro)
        # pygame.draw.rect(window, bgColour, rectMarioIntro)
        # window.blit(ground, rectGround)
            # window.blit(textBowserHey, rectTextBowserHey)
            # window.blit(textPeach, rectTextPeach)
            # window.blit(textPeachEw, rectTextPeachEw)
            # window.blit(textBowserSec, rectTextBowserSec)
            # window.blit(textBowserSec1, rectTextBowserSec1)
        if rectBowserIntro.centerx <= 701 and tum == 0:
            fontObj = pygame.font.Font("Super Mario Bros. 2.ttf", 10)
            textBowser = fontObj.render("Bowser:", True, black)
            rectTextBowser = textBowser.get_rect()

            textBowserHey = fontObj.render("" + typeWriter, True, black)
            rectTextBowserHey = textBowserHey.get_rect()
            rectTextBowserHey.center = (500, 130)
            rectTextBowser.center = (500, 110)
            window.blit(textBowser, rectTextBowser)
            window.blit(textBowserHey, rectTextBowserHey)
        if introText == True and tum == 0:
            textPeach = fontObj.render("Princess Peach:", True, black)
            rectTextPeach = textPeach.get_rect()

            textPeachEw = fontObj.render("" + typeWriterPeach, True, black)
            rectTextPeachEw = textPeachEw.get_rect()
            rectTextPeachEw.center = (500, 170)
            rectTextPeach.center = (500, 150)
            window.blit(textPeachEw, rectTextPeachEw)
            window.blit(textPeach, rectTextPeach)
        if introTextPeach == True and tum == 0:
            textBowserSec1 = fontObj.render("Bowser:", True, black)
            rectTextBowserSec1 = textBowserSec1.get_rect()

            textBowserSec = fontObj.render("" + typeWriterBowser, True, black)
            rectTextBowserSec = textBowserSec.get_rect()
            rectTextBowserSec.center = (500, 210)
            rectTextBowserSec1.center = (500, 190)
            window.blit(textBowserSec1, rectTextBowserSec1)
            window.blit(textBowserSec, rectTextBowserSec)
        if rectMarioIntro.centerx > 90:
            textMarioSec1 = fontObj.render("Mario:", True, black)
            rectTextMarioSec1 = textMarioSec1.get_rect()
            rectTextMarioSec1.center = (500, 150)

            textMarioSec = fontObj.render("" + typeWriterMario, True, black)
            rectTextMarioSec = textMarioSec.get_rect()
            rectTextMarioSec.center = (500, 170)
            window.blit(textMarioSec1, rectTextMarioSec1)
            window.blit(textMarioSec, rectTextMarioSec)
        if bowserCheckPickPeach == 1:
            tum = 1
        if bowserCheckPickPeach == 1:
            rectTextPeachEw.centery -= 3
            rectTextPeach.centery -= 3
            rectTextBowser.centery -= 3
            rectTextBowserSec.centery -= 3
            rectTextBowserSec1.centery -= 3
            rectTextBowserHey.centery -= 3
            window.blit(textBowserSec1, rectTextBowserSec1)
            window.blit(textBowserSec, rectTextBowserSec)
            window.blit(textPeachEw, rectTextPeachEw)
            window.blit(textPeach, rectTextPeach)
            window.blit(textBowser, rectTextBowser)
            window.blit(textBowserHey, rectTextBowserHey)
        # update the screen
        pygame.display.flip()
        timer.tick(fps)
    marioVar = marioChill
    directionCheck = 0
    while respawn == False and lives > 0:
        for event in pygame.event.get():
            if event.type == QUIT:  # detecting a quit event
                pygame.quit()
                doneLevel1 = True

            if lives > 0 and doneLevel1 and not bossChecker:
                doneLevel1 = False
                rectGoomba1 = goomba(560, 0, 4, 0, 550, 0, 0, 8, 0)
                rectGoomba2 = goomba(1220, 0, 4, 0, 550, 0, 0, 8, 0)
                rectGoomba3 = goomba(1560, 0, 4, 0, 260, 0, 0, 8, 0)
                rectPipe1 = pipes(600, 80, 80, 510)
                rectPipe2 = pipes(1260, 80, 120, 510)
                rectPipe3 = pipes(1600, 80, 60, 510)
                rectPipe4 = pipes(1800, 80, 240, 510)
                rectMario.centerx = 20
                pipes.respawn()
                goombaChill = goombaWalk1
                goombaChill2 = goombaWalk1
                goombaChill3 = goombaWalk1
                # rectGoomba1.respawn()
                # rectGoomba2.respawn()

        while doneLevel1 == False and lives > 0:
            time1 += 1
            keys = pygame.key.get_pressed()  # use for continuous movement
            # if keys[pygame.K_SPACE]:
            # contents of the game loop
            for event in pygame.event.get():
                if event.type == QUIT:  # detecting a quit event
                    pygame.quit()
                    doneLevel1 = True
                if event.type == pygame.KEYDOWN:
                    if not jump and event.key == pygame.K_SPACE or not jump and event.key == pygame.K_w:
                        jump = True
                        jumpCount = jumpMax
                    else:
                        jump = False
                        # marioVar = marioJumping
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_d and keysCheck1 == 0:
            #         keysCheck1 = 0
            #         keysCheck2 = 1
            #     if event.key == pygame.K_a and keysCheck2 == 0:
            #         keysCheck1 = 1
            #         keysCheck2 = 0
            # algorithm for jumping
            # print(rectMario.centery)
            # if rectMario.colliderect(rectPipe1.drawTop()) or rectMario.colliderect(rectPipe2.drawTop()) or rectMario.centery >= 500\
            #         or rectMario.colliderect(rectPipe3.drawTop()) or rectMario.colliderect(rectPipe4.drawTop()):
            #     jumpImportant = True
            # if jump and jumpImportant:
            #     rectMario.centery -= jumpCount
            #     if keys[pygame.K_w] and jumpMaxer <= 15 and fallCounter == 0 and tumBum == 0:
            #         jumpMax += 1
            #         jumpMaxer += 1
            #         tummy = 1
            #     if keys[pygame.K_SPACE] and jumpMaxer <= 15 and fallCounter == 0 and tumBum == 0:
            #         print(jumpMax)
            #         jumpMax += 1
            #         jumpMaxer += 1
            #         print(jumpMaxer)
            #         tummy = 1
            #     if not keys[pygame.K_w] and not keys[pygame.K_SPACE] and tummy == 1 or jumpMaxer > 15:
            #         fallCounter = 1
            #         tumBum = 1
            #     if rectMario.centery >= 500:
            #         rectMario.centery = 500
            #         jumpMaxer = 0
            #         jump = False
            #     if jumpCount > -jumpMax and fallCounter == 1:
            #         print("skda ")
            #         rectMario.centery += 0
            #         jumpCount -= 1
            #         # print(jumpCount)
            # else:
            #     fallCounter = 0
            #     jumpMax = 10
            #     jumpMaxer = 0
            #     tummy = 0
            #     tumBum = 0
            if jump:
                rectMario.y -= jumpCount
                if jumpCount > -jumpMax:
                    jumpCount -= 1
                else:
                    jump = False

            Check()
            rectGoomba2.updateGoomba()
            rectGoomba3.updateGoomba()
            rectGoomba1.updateGoomba()
            if jump and directionCheck == 1:
                marioVar = marioJumping
                marioVar = pygame.transform.flip(marioVar, True, False)
            if jump and directionCheck == 0:
                marioVar = marioJumping
            if jump == True and directionCheck == 1:
                marioVar = marioJumping
                marioVar = pygame.transform.flip(marioVar, True, False)
            if jump == True and directionCheck == 0:
                marioVar = marioJumping
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_a and keysCheck1 == 0:
            #         marioVar = marioChill
            #         marioVar = pygame.transform.flip(marioVar, True, False)
            #     if event.key == pygame.K_d and keysCheck1 == 0:
            #         marioVar = marioChill
            # if not keys[pygame.K_a]:
            #     marioVar = marioChill
            if keys[pygame.K_a] and keysCheck1 == 0 and not keys[pygame.K_d]:  # check to see if a key is being pressed
                rectMario.centerx -= marioSpeed
                if directionCheck == 0:
                    directionCheck = 1
                    marioVar = pygame.transform.flip(marioVar, True, False)
                if time1 % 2 == 0 and run1 == 1 and not jump:
                    marioVar = marioRunning1
                    # marioVar = pygame.transform.flip(marioVar, True, False)
                    run1 = 0
                    run2 = 1
                    run3 = 0
                if time1 % 4 == 0 and run2 == 1 and not jump:
                    marioVar = marioRunning2
                    # marioVar = pygame.transform.flip(marioVar, True, False)
                    run1 = 0
                    run2 = 0
                    run3 = 1
                if time1 % 6 == 0 and run3 == 1 and not jump:
                    marioVar = marioRunning3
                    # marioVar = pygame.transform.flip(marioVar, True, False)
                    run1 = 1
                    run2 = 0
                    run3 = 0
            if keys[pygame.K_d] and keysCheck1 == 0 and not keys[pygame.K_a]:
                rectMario.centerx += marioSpeed
                if directionCheck == 1:
                    directionCheck = 0
                    marioVar = pygame.transform.flip(marioVar, True, False)
                if time1 % 2 == 0 and run1 == 1 and not jump:
                    marioVar = marioRunning1
                    marioVar = pygame.transform.flip(marioVar, True, False)
                    run1 = 0
                    run2 = 1
                    run3 = 0
                if time1 % 4 == 0 and run2 == 1 and not jump:
                    marioVar = marioRunning2
                    marioVar = pygame.transform.flip(marioVar, True, False)
                    run1 = 0
                    run2 = 0
                    run3 = 1
                if time1 % 6 == 0 and run3 == 1 and not jump:
                    marioVar = marioRunning3
                    marioVar = pygame.transform.flip(marioVar, True, False)
                    run1 = 1
                    run2 = 0
                    run3 = 0
            if not jump and not keys[pygame.K_d] and not keys[pygame.K_a]:
                if directionCheck == 0:
                    marioVar = marioChill
                if directionCheck == 1:
                    marioVar = marioChill
                    marioVar = pygame.transform.flip(marioVar, True, False)
            if keys[pygame.K_a] and keys[pygame.K_d] and not jump:
                keysCheck1 = 1
                if directionCheck == 0:
                    marioVar = marioChill
                if directionCheck == 1:
                    marioVar = marioChill
                    marioVar = pygame.transform.flip(marioVar, True, False)
            else:
                keysCheck1 = 0
            if rectMario.centerx <= 20:
                marioSpeed = 0
                if keys[pygame.K_a]:
                    marioSpeed = 0
                if keys[pygame.K_d]:
                    marioSpeed = 8
            if rectGround.centerx <= -400:
                rectGround.centerx = 1500
            if time1 % 5 == 0 and goombaChill != goombaSquish:
                goombaChill = goombaWalk1
            if time1 % 10 == 0 and goombaChill != goombaSquish:
                goombaChill = goombaWalk2
            if time1 % 5 == 0 and goombaChill2 != goombaSquish:
                goombaChill2 = goombaWalk1
            if time1 % 10 == 0 and goombaChill2 != goombaSquish:
                goombaChill2 = goombaWalk2

            if keys[pygame.K_s] and not jump and not keys[pygame.K_a] and not keys[pygame.K_d]:
                if directionCheck == 0:
                    marioVar = marioPoint
                if directionCheck == 1:
                    marioVar = marioPoint
                    marioVar = pygame.transform.flip(marioVar, True, False)
                fingerChecker = True
                marioSpeed = 0
            else:
                fingerChecker = False
                fingerCounter = 0
                fingerCount = 0
                marioSpeed = 8
                rectFinger.centerx = rectMario.centerx

            if fingerChecker:
                spawnFinger()

            if rectMario.centerx > 700:
                if keys[pygame.K_d]:
                    marioSpeed = 0
                    rectGround.centerx -= velocity
                    pipes.update()
                    rectGoomba2.updateGoomba2()
                    rectGoomba3.updateGoomba2()
                    rectGoomba1.updateGoomba2()
                    rectCastle.centerx -= velocity
                if keys[pygame.K_a]:
                    marioSpeed = 8

            if rectMario.centerx >= rectCastle.centerx:
                bossChecker = True
                doneLevel1 = True
                fadeout()

            # if rectMario.centerx < 700 and rectMario.centerx > 20:
            #     marioSpeed = 8
            # if rectGoomba1.centerx >= 11 and bum == 0:
            #     rectGoomba1.centerx -= 4
            # if rectGoomba1.centerx == 10:
            #     bum = 1
            # if bum == 1:
            #     rectGoomba1.centerx += 4
            # set the background colour
            # window.fill(bgColour)
            white = (255, 255, 255)
            # draw the images onto the screen
            # window.blit(backGround, (0, 0))
            window.blit(backGroundBlue, (0, 0))
            window.blit(pipeUp, (rectPipe1.draw()))
            window.blit(pipeUp, (rectPipe2.draw()))
            window.blit(pipeUp, (rectPipe3.draw()))
            window.blit(pipeUp, (rectPipe4.draw()))
            # window.blit(pipeUp, (rectGoomba1.draw()))
            window.blit(ground, rectGround)
            window.blit(castle, rectCastle)
            if rectMario.centerx >= 700 and bumTum == 0:
                rectCastle.centery = 375
                rectCastle.centerx = 2500
                bumTum = 1
            window.blit(marioVar, rectMario)
            pygame.draw.rect(window, white, rectPipe1.drawTop())
            pygame.draw.rect(window, white, rectPipe2.drawTop())
            pygame.draw.rect(window, white, rectGoomba1.drawBound())
            pygame.draw.rect(window, white, rectGoomba1.drawTop())
            pygame.draw.rect(window, white, rectPipe2.drawBound())
            pygame.draw.rect(window, white, rectPipe1.drawBound())
            # pygame.draw.rect(window, white, rectFinger)
            window.blit(goombaChill, rectGoomba1.draw())
            window.blit(goombaChill2, rectGoomba2.draw())
            window.blit(goombaChill3, rectGoomba3.draw())
            if fingerCounter == 1:
                window.blit(finger, rectFinger)
            # window.blit(finger, rectFinger)
            # update the screen
            pygame.display.flip()
            timer.tick(fps)

        fadein()
        while bossChecker:
            for event in pygame.event.get():
                if event.type == QUIT:  # detecting a quit event
                    pygame.quit()
                    doneLevel1 = True



            black = (0, 0, 0)
            window.fill(black)
            rectBowserIntro = (800, 465, 55, 55)
            window.blit(bowserChill, rectBowserIntro)
            pygame.display.flip()
            timer.tick(fps)
        pygame.display.flip()
        timer.tick(fps)

    # set the background colour
    window.fill(bgColour)

    # draw the images onto the screen
    window.blit(backGround, (0, 0))
    # window.blit(marioChill, rectMarioIntro)
    # window.blit(ground, rectGround)

    # update the screen
    pygame.display.flip()
    timer.tick(fps)

