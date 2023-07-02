import pygame, random, math, os

screenWidth = 640
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.SRCALPHA)
screenAlpha = pygame.Surface((screenWidth, screenHeight), pygame.SRCALPHA)

clock = pygame.time.Clock()
FPS = 30

black = (0,0,0)
grey = (128,128,128)
white = (255,255,255)

GRAVITY = 10

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Coords(self):
        return (self.x, self.y)

    def CoordsBlit(self):
        return self.CoordsInt()

    def CoordsInt(self):
        x, y = self.Coords()
        x = round(x)
        y = round(y)
        return (x, y)

    def Copy(self):
        return Vector(self.x, self.y)

    def Normalise(self):
        total = abs(self.x)+abs(self.y)
        self.x /= total
        self.y /= total

    def GetMag(self):
        return math.sqrt(self.x**2+self.y**2)

    def SetMag(self, mag):
        self.Normalise()
        self.MultVal(mag)

    def Add(self, v):
        self.x += v.x
        self.y += v.y

    def Sub(self, v):
        self.x -= v.x
        self.y -= v.y

    def MultVal(self, val):
        self.x *= val
        self.y *= val

class Attractor:
    def __init__(self):
        self.pos = Vector(random.randint(0, screenWidth),
                          random.randint(0, screenHeight))
        self.mass = 10

    def Show(self):
        pygame.draw.circle(screen, (0,255,0), self.pos.CoordsBlit(), 2)

class Particle:
    def __init__(self):
        self.pos = Vector(random.randint(0, screenWidth),
                          random.randint(0, screenHeight))
        self.mass = 1

        self.acc = Vector(0,0)
        self.vel = Vector(0,0)

    def Update(self):
        self.posPrev = self.pos.Copy()
        
        for a in Attractors:
            self.Attract(a)
            
        self.vel.Add(self.acc)
        self.pos.Add(self.vel)
        self.acc.MultVal(0)

        self.KeepOnScreen()

    def Show(self):
        pygame.draw.line(screenAlpha, (white[0], white[1], white[2], 50),
                           self.pos.CoordsBlit(), self.posPrev.CoordsBlit(), 1)

    def Attract(self, attractor):
        force = attractor.pos.Copy()
        force.Sub(self.pos)

        d = force.GetMag()
        d2 = d**2
        forceMag = GRAVITY*(self.mass*attractor.mass/d2)
        forceMag *= 10
        force.SetMag(forceMag)

        self.acc.Add(force)

    def KeepOnScreen(self):
        screenRect = pygame.Rect((0,0), screen.get_size())
        if screenRect.collidepoint(self.pos.Coords()):
            return 0

        self.vel.MultVal(0)
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > screenWidth:
            self.pos.x = screenWidth

        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.y > screenHeight:
            self.pos.y = screenHeight

Attractors = []
Particles = []

for i in range(2):
    Attractors.append(Attractor())
for i in range(10):
    Particles.append(Particle())

gameloop = True
while gameloop:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            gameloop = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_g:
                os.system("Game.py")

    screenAlpha.fill((0,0,0,2))

    for a in Attractors:
        a.Show()
        
    for p in Particles:
        p.Update()
        p.Show()

    screen.blit(screenAlpha, (0,0))

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
quit()
