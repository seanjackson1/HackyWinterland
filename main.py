import random
import pygame
import sys
import os
from pygame.locals import *
from tkinter import *

'''
[[Q1, A1, A2, A3, A4],
[Q2, A1, A2, A3, A4],
[Q3, A1, A2, A3, A4],...]
'''
questions = []

questionNum = 0
NRQ = 0

life = 3

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
LIGHTBLUE = (167,199,231)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FERNGREEN = (79, 121, 66)
ACTDIMGRAY = (105, 105, 105)
DARKGREEN = (0, 155, 0)
RED = (255, 0, 0)
DIMGRAY = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# loading and scaling start background
start_bg = pygame.image.load(os.path.join("./images", "tree.jpg"))
start_bg = pygame.transform.scale(start_bg, (WINDOWWIDTH, WINDOWHEIGHT))


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 40)
    pygame.display.set_caption('Holiday Trivia')

    loadQuestions()

    # show start screen, then run game forever
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

# load questions into array


def loadQuestions():
    f = open(os.path.join("./", "questions.txt"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()  # remove \n
        line = line.split(";")
        questions.append([line[0], line[1], line[2],
                         line[3], line[4], line[5]])


def runGame():
    global life
    i = range(len(questions))
    indices = sorted(i, key=lambda x: random.random())
    print(indices)
    for ind in indices:
        if life > 0:
            showQuestion(ind)
            showPoints()
            if checkForKeyPress():
                pygame.event.clear()  # clear event queue
                return
            pygame.display.update()
    showGameOverScreen()


def showQuestion(n):
    DISPLAYSURF.fill(BLACK)


    pygame.event.clear()

    global NRQ

    global life

    questionRect = pygame.Rect((0, 0), (WINDOWWIDTH, WINDOWHEIGHT/2))
    questionRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)
    pygame.draw.rect(DISPLAYSURF, LIGHTBLUE, questionRect)
    drawText(DISPLAYSURF, questions[n][0], WHITE, questionRect, BIGFONT)

    a1Rect = pygame.Rect((0, WINDOWHEIGHT/2), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
    pygame.draw.rect(DISPLAYSURF, RED, a1Rect)
    drawText(DISPLAYSURF, questions[n][1], DIMGRAY, a1Rect, BIGFONT)

    a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),
                         (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
    pygame.draw.rect(DISPLAYSURF, GREEN, a2Rect)
    drawText(DISPLAYSURF, questions[n][2], DIMGRAY, a2Rect, BIGFONT)

    a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
    pygame.draw.rect(DISPLAYSURF, GREEN, a3Rect)
    drawText(DISPLAYSURF, questions[n][3], DIMGRAY, a3Rect, BIGFONT)

    a4Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
    pygame.draw.rect(DISPLAYSURF, RED, a4Rect)
    drawText(DISPLAYSURF, questions[n][4], DIMGRAY, a4Rect, BIGFONT)

    notPressed = TRUE

    answer = 0
    pygame.display.update()
    while notPressed:

        if checkForKeyPress():
            return

        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if pos[1] > WINDOWHEIGHT/2:
                    if pos[0] < WINDOWWIDTH/2:
                        if pos[1] < WINDOWHEIGHT * 3 / 4:
                            answer = 1
                        else:
                            answer = 2
                    else:
                        if pos[1] < WINDOWHEIGHT * 3 / 4:
                            answer = 3
                        else:
                            answer = 4
                    notPressed = FALSE
                    pygame.event.clear()


    if int(questions[n][5]) == 1:
        a1Rect = pygame.Rect((0, WINDOWHEIGHT/2),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, a1Rect)
        drawText(DISPLAYSURF, questions[n][1], DIMGRAY, a1Rect, BIGFONT)
        a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a2Rect)
        drawText(DISPLAYSURF, questions[n][2], WHITE, a2Rect, BIGFONT)

        a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a3Rect)
        drawText(DISPLAYSURF, questions[n][3], WHITE, a3Rect, BIGFONT)

        a4Rect = pygame.Rect((WINDOWWIDTH/2, 0),
                            (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], WHITE, a4Rect, BIGFONT)
    elif int(questions[n][5]) == 2:
        a1Rect = pygame.Rect((0, WINDOWHEIGHT/2),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a1Rect)
        drawText(DISPLAYSURF, questions[n][1], WHITE, a1Rect, BIGFONT)
        a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, a2Rect)
        drawText(DISPLAYSURF, questions[n][2], DIMGRAY, a2Rect, BIGFONT)

        a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a3Rect)
        drawText(DISPLAYSURF, questions[n][3], WHITE, a3Rect, BIGFONT)

        a4Rect = pygame.Rect((WINDOWWIDTH/2, 0),
                            (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], WHITE, a4Rect, BIGFONT)
    elif int(questions[n][5]) == 3:
        a1Rect = pygame.Rect((0, WINDOWHEIGHT/2),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a1Rect)
        drawText(DISPLAYSURF, questions[n][1], WHITE, a1Rect, BIGFONT)
        a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a2Rect)
        drawText(DISPLAYSURF, questions[n][2], WHITE, a2Rect, BIGFONT)

        a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, a3Rect)
        drawText(DISPLAYSURF, questions[n][3], DIMGRAY, a3Rect, BIGFONT)

        a4Rect = pygame.Rect((WINDOWWIDTH/2, 0),
                            (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], WHITE, a4Rect, BIGFONT)
    else:
        a1Rect = pygame.Rect((0, WINDOWHEIGHT/2),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a1Rect)
        drawText(DISPLAYSURF, questions[n][1], WHITE, a1Rect, BIGFONT)
        a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a2Rect)
        drawText(DISPLAYSURF, questions[n][2], WHITE, a2Rect, BIGFONT)

        a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, ACTDIMGRAY, a3Rect)
        drawText(DISPLAYSURF, questions[n][3], WHITE, a3Rect, BIGFONT)

        a4Rect = pygame.Rect((WINDOWWIDTH/2, 0),
                            (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], DIMGRAY, a4Rect, BIGFONT)
    if answer  == 1 and int(questions[n][5]) != answer:
        print("here")
        a1Rect = pygame.Rect((0, WINDOWHEIGHT/2),(WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, RED, a1Rect)
        drawText(DISPLAYSURF, questions[n][1], WHITE, a1Rect, BIGFONT)
    elif answer == 2 and int(questions[n][5]) != answer:
        a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),(WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, RED, a2Rect)
        drawText(DISPLAYSURF, questions[n][2], WHITE, a2Rect, BIGFONT)
    elif answer == 3 and int(questions[n][5]) != answer:
        a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, RED, a3Rect)
        drawText(DISPLAYSURF, questions[n][3], WHITE, a3Rect, BIGFONT)
    elif answer == 4 and int(questions[n][5]) != answer:
        a4Rect = pygame.Rect((WINDOWWIDTH/2, 0),(WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, RED, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], WHITE, a4Rect, BIGFONT)
    pygame.display.update()
    pygame.time.wait(2000)
    if int(questions[n][5]) == answer: 
        NRQ += 1
    else:
        life -= 1
    pygame.display.update()


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

# show game over screen (does nothing for now)


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameOverSurf = gameOverFont.render('GAME OVER', True, WHITE, DARKGREEN)
    DISPLAYSURF.fill(RED)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)
    DISPLAYSURF.blit(gameOverSurf, gameOverRect)
    pointsFont = pygame.font.Font('freesansbold.ttf', 100)
    pointsSurf1 = pointsFont.render("Points: " + str(NRQ * 1000), True, WHITE, DARKGREEN)
    pointsRect = pointsSurf1.get_rect()
    pointsRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT *2 / 3)
    DISPLAYSURF.blit(pointsSurf1, pointsRect)
    pygame.display.update()
    while True:
        checkForKeyPress()

# showing the start screen


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Holiday Trivia!', True, WHITE, DARKGREEN)
    while True:
        DISPLAYSURF.blit(start_bg, (0, 0))
        # DISPLAYSURF.fill(BLACK)
        titleRect = titleSurf1.get_rect()
        titleRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(titleSurf1, titleRect)
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.clear()  # clear event queue
            return
        pygame.display.update()


def showPoints():

    pygame.event.clear()

    pointsFont = pygame.font.Font('freesansbold.ttf', 100)
    pointsSurf1 = pointsFont.render("Points: " + str(NRQ * 1000), True, WHITE, DARKGREEN)
    lifeSurf1 = pointsFont.render("Lives: " + str(life), True, WHITE, DARKGREEN)
    DISPLAYSURF.fill(RED)
    pointsRect = pointsSurf1.get_rect()
    pointsRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 3)
    lifeRect = lifeSurf1.get_rect()
    lifeRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT * 2 / 3)
    DISPLAYSURF.blit(pointsSurf1, pointsRect)
    DISPLAYSURF.blit(lifeSurf1, lifeRect)

    if checkForKeyPress():
        pygame.event.clear()  # clear event queue
        return
    pygame.display.update()
    pygame.time.wait(2000)

# draws message to press any key in bottom right of screen


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

# checks for key press, terminates if ESC


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

# end program


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
