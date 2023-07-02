import pygame, math
pygame.init()

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

def dist(a, b):
    xDif = a[0]-b[0]
    yDif = a[1]-b[1]

    dist = math.sqrt(xDif**2+yDif**2)
    return dist

def text(txt, colour, font):
    txtBlit = font.render(txt, True, colour)
    rect = pygame.Rect((0,0), txtBlit.get_size())
    return (txtBlit, rect)
