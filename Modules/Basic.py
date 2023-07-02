import pygame
import Modules.Event

def Initialise(w=640, h=640, fps=30):
    pygame.init()
    
    SetScreenSize(640, 640)
    SetClock(30)

    Modules.Event.UpdateEvents()

def CreateScreen():
    global screen
    screen = pygame.display.set_mode(GetScreenSize())

def GetScreen():
    return screen

def GetScreenSize():
    return (screenWidth, screenHeight)

def SetScreenSize(w, h):
    global screenWidth, screenHeight
    screenWidth = w
    screenHeight = h

def FillScreen(colour):
    GetScreen().fill(colour)

def CreateClock():
    global clock
    clock = pygame.time.Clock()

def SetClock(fps):
    global FPS
    FPS = fps

def GetClock():
    return FPS

def UpdateClock():
    clock.tick(FPS)
    pygame.display.flip()

def StartLoop(update):
    CreateScreen()
    CreateClock()
    
    while True:
        Modules.Event.UpdateEvents()
        if CheckQuit():
            break
        
        update()
        UpdateClock()

    Quit()

forceQuit = False
def ForceQuit():
    global forceQuit
    forceQuit = True
    
def CheckQuit():
    for e in Modules.Event.GetEvents():
        if e.type == pygame.QUIT:
            return True
    if forceQuit:
        return True
    return False
    
def Quit():
    pygame.quit()
    quit()
