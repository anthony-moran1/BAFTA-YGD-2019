import pygame

def UpdateEvents():
    global events
    events = pygame.event.get()

def GetEvents():
    return events

def GetKey(key):
    return pygame.key.get_pressed()[key]

def GetKeyPressed(key):
    for e in GetEvents():
        if e.type == pygame.KEYDOWN:
            if e.key == key:
                return True
    return False
