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

WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
LIGHTBLUE = (167,199,231)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GOODGREEN = (0, 100, 0)
ACTDIMGRAY = (105, 105, 105)
DARKGREEN = (0, 155, 0)
RED = (255, 0, 0)
DIMGRAY = (0, 0, 0)
GOODRED = (200, 0, 0)
BLUE = (0, 0, 255)

# loading and scaling start background
start_bg = pygame.image.load(os.path.join("./images", "BetterTree.png"))
start_bg = pygame.transform.scale(start_bg, (WINDOWWIDTH, WINDOWHEIGHT))
question_bg = pygame.image.load(os.path.join("./images", "Winter Background.png"))
question_bg = pygame.transform.scale(question_bg, (WINDOWWIDTH, WINDOWHEIGHT/2))


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 40)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 35)
    pygame.display.set_caption('Holiday Trivia')

    loadQuestions()

    pygame.mixer.music.load(os.path.join("./sound", "bg_music.wav"))
    pygame.mixer.music.play(-1)

    pygame.mixer.music.set_volume(.3)

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
    pygame.display.update()
    global life
    i = range(len(questions))
    indices = sorted(i, key=lambda x: random.random())
    for ind in indices:
        if life > 0:
            showQuestion(ind)
            showPoints()
            if checkForKeyPress():
                pygame.event.clear()  # clear event queue
            pygame.display.update()
    showGameOverScreen()


def showQuestion(n):
    pygame.event.clear()

    clock = pygame.time.Clock()
    counter, text = 5, 'TIME LEFT: 5'.rjust(2)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    global NRQ
    global life

    questionRect = question_bg.get_rect()
    questionRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)
    DISPLAYSURF.blit(question_bg, (0,0))
    drawText(DISPLAYSURF, questions[n][0], WHITE, questionRect, BIGFONT)

    a1Rect = pygame.Rect((0, WINDOWHEIGHT/2), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
    pygame.draw.rect(DISPLAYSURF, GOODRED, a1Rect)
    drawText(DISPLAYSURF, questions[n][1], DIMGRAY, a1Rect, BIGFONT)

    a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),
                         (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
    pygame.draw.rect(DISPLAYSURF, GOODGREEN, a2Rect)
    drawText(DISPLAYSURF, questions[n][2], DIMGRAY, a2Rect, BIGFONT)

    a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
    pygame.draw.rect(DISPLAYSURF, GOODGREEN, a3Rect)
    drawText(DISPLAYSURF, questions[n][3], DIMGRAY, a3Rect, BIGFONT)

    a4Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
    a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
    pygame.draw.rect(DISPLAYSURF, GOODRED, a4Rect)
    drawText(DISPLAYSURF, questions[n][4], DIMGRAY, a4Rect, BIGFONT)

    notPressed = TRUE

    answer = 0
    
    while notPressed:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter == -1:
                    notPressed = False
                else:
                    text = "TIME LEFT:" + str(counter).rjust(3)

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
                    notPressed = False
        
        DISPLAYSURF.blit(question_bg, (0,0))
        drawText(DISPLAYSURF, questions[n][0], WHITE, questionRect, BIGFONT)
        pygame.draw.rect(DISPLAYSURF, GOODRED, a1Rect)
        drawText(DISPLAYSURF, questions[n][1], DIMGRAY, a1Rect, BIGFONT)
        pygame.draw.rect(DISPLAYSURF, GOODGREEN, a2Rect)
        drawText(DISPLAYSURF, questions[n][2], DIMGRAY, a2Rect, BIGFONT)
        pygame.draw.rect(DISPLAYSURF, GOODGREEN, a3Rect)
        drawText(DISPLAYSURF, questions[n][3], DIMGRAY, a3Rect, BIGFONT)
        pygame.draw.rect(DISPLAYSURF, GOODRED, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], DIMGRAY, a4Rect, BIGFONT)

        DISPLAYSURF.blit(BIGFONT.render(text, True, RED), (WINDOWWIDTH/2 + 35, WINDOWHEIGHT/2 - 35))
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
    
    if int(questions[n][5]) == 1:
        a1Rect = pygame.Rect((0, WINDOWHEIGHT/2),
                             (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, GOODGREEN, a1Rect)
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
        pygame.draw.rect(DISPLAYSURF, GOODGREEN, a2Rect)
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
        pygame.draw.rect(DISPLAYSURF, GOODGREEN, a3Rect)
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
        pygame.draw.rect(DISPLAYSURF, GOODGREEN, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], DIMGRAY, a4Rect, BIGFONT)
    if answer  == 1 and int(questions[n][5]) != answer:
        a1Rect = pygame.Rect((0, WINDOWHEIGHT/2),(WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a1Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, GOODRED, a1Rect)
        drawText(DISPLAYSURF, questions[n][1], WHITE, a1Rect, BIGFONT)
    elif answer == 2 and int(questions[n][5]) != answer:
        a2Rect = pygame.Rect((0, WINDOWHEIGHT*3/4),(WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a2Rect.center = (WINDOWWIDTH / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, GOODRED, a2Rect)
        drawText(DISPLAYSURF, questions[n][2], WHITE, a2Rect, BIGFONT)
    elif answer == 3 and int(questions[n][5]) != answer:
        a3Rect = pygame.Rect((WINDOWWIDTH/2, 0), (WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a3Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 5 / 8)
        pygame.draw.rect(DISPLAYSURF, GOODRED, a3Rect)
        drawText(DISPLAYSURF, questions[n][3], WHITE, a3Rect, BIGFONT)
    elif answer == 4 and int(questions[n][5]) != answer:
        a4Rect = pygame.Rect((WINDOWWIDTH/2, 0),(WINDOWWIDTH/2, WINDOWHEIGHT/4))
        a4Rect.center = (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT * 7 / 8)
        pygame.draw.rect(DISPLAYSURF, GOODRED, a4Rect)
        drawText(DISPLAYSURF, questions[n][4], WHITE, a4Rect, BIGFONT)
    pygame.display.update()
    if int(questions[n][5]) == answer: 
        NRQ += 1
        ding_sound = pygame.mixer.Sound(os.path.join("./sound", "ding.wav"))
        pygame.mixer.Sound.play(ding_sound)
    else:
        life -= 1
        wrong_sound = pygame.mixer.Sound(os.path.join("./sound", "wrong.wav"))
        pygame.mixer.Sound.play(wrong_sound)
    pygame.time.wait(2000)
    
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
    end_sound = pygame.mixer.Sound(os.path.join("./sound", "end_sound.wav"))
    pygame.mixer.Sound.play(end_sound)
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
    pygame.display.update()
    pygame.time.wait(2000)

# draws message to press any key in bottom right of screen


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 400, WINDOWHEIGHT - 70)
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
