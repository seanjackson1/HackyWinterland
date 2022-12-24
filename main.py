import random, pygame, sys, os
from pygame.locals import *
'''
[[Q1, A1, A2, A3, A4],
[Q2, A1, A2, A3, A4],
[Q3, A1, A2, A3, A4],...]
'''
questions = []

points = 0

numRightQuestions = 0

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK     = (  0,   0,   0)
DARKGREEN = (0, 155, 0)

# loading and scaling start background
start_bg = pygame.image.load(os.path.join("./images", "tree.jpg"))
start_bg = pygame.transform.scale(start_bg, (WINDOWWIDTH, WINDOWHEIGHT))

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
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
        line = line.strip() # remove \n
        line = line.split(";")
        questions.append([line[0],line[1],line[2],line[3],line[4]])

# running the game (does nothing for now)
def runGame():
    while True:
        checkForKeyPress()

# show game over screen (does nothing for now)
def showGameOverScreen():
    while True:
        checkForKeyPress()

# showing the start screen
def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Holiday Trivia!', True, WHITE, DARKGREEN)
    while True:
        DISPLAYSURF.blit(start_bg, (0,0))
        # DISPLAYSURF.fill(BLACK)
        titleRect = titleSurf1.get_rect()
        titleRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(titleSurf1, titleRect)
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
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