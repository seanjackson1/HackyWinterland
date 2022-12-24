import random
import pygame
import sys
import os
import pygame_widgets
from pygame.locals import *
from pygame_widgets.textbox import TextBox
from tkinter import *

'''
[[Q1, A1, A2, A3, A4],
[Q2, A1, A2, A3, A4],
[Q3, A1, A2, A3, A4],...]
'''
questions = []

questionNum = 0

numRightQuestions = 2

WINDOWWIDTH = 800
WINDOWHEIGHT = 600


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FERNGREEN = (79, 121, 66)
BLACK = (0, 0, 0)
DARKGREEN = (0, 155, 0)
RED = (255, 0, 0)
DIMGRAY = (105, 105, 105)
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
    BIGFONT = pygame.font.Font('freesansbold.ttf', 50)
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

# running the game (does nothing for now)


def runGame():
    showQuestion(2)


def showQuestion(n):
    DISPLAYSURF.fill(BLACK)

    questionRect = pygame.Rect((0, 0), (WINDOWWIDTH, WINDOWHEIGHT/2))
    questionRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)
    pygame.draw.rect(DISPLAYSURF, DIMGRAY, questionRect)
    drawText(DISPLAYSURF, questions[n][0], WHITE, questionRect, BIGFONT)

    
    a1Rect = pygame.Rect((0, WINDOWHEIGHT/2), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
    pygame.draw.rect(DISPLAYSURF, RED, a1Rect)
    drawText(DISPLAYSURF, questions[n][1], DIMGRAY, a1Rect, BIGFONT)
    
    a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
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
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()

def showPoints():
    pointsFont = pygame.font.Font('freesansbold.ttf', 100)
    pointsSurf1 = pointsFont.render(str(numRightQuestions * 1000), True, WHITE, DARKGREEN)
    while True:
        DISPLAYSURF.fill(RED)
        pointsRect = pointsSurf1.get_rect()
        pointsRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(pointsSurf1, pointsRect)

        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
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
