from GameObject import *

class Orb(GameObject):
    def Add(self):
        Control.AddFantasyObject(self)

    def Remove(self):
        Control.RemoveFantasyObject(self)
        
    def __init__(self, colour):
        super().__init__()
        
        self.Solid = False
        self.CanCollide = False
        self.rectOffset = pygame.Rect(self.rect)
        
        self.colour = colour
        self.SetSprite(eval("GameSprite.Orb"+self.colour)())
        self.depthLayer = "Hih"

        self.target = None
        self.dest = None
        
        self.canUse = True
        self.canUseMax = Basic.GetClock()*2
        self.canUseCurrent = 0

    def Update(self):                
        if not self.UPDATE:
            return
        
        super().Update()
        self.Rotate(math.pi/90)
        self.MoveControl()

        if self.canUse or self.target:
            self.SetSprite(eval("GameSprite.Orb"+self.colour)())
        else:
            self.SetSprite(GameSprite.OrbGrey())
            if not self.target:
                if self.canUseCurrent < self.canUseMax:
                    self.canUseCurrent += 1
                else:
                    self.canUse = True

    def Rotate(self, angle):
        sin = math.sin(angle)
        cos = math.cos(angle)

        x, y = self.rectOffset.center
        rx, ry = round(cos*x-sin*y), round(sin*x+cos*y)

        self.rectOffset.center = (rx, ry)

    def MoveControl(self):
        if not self.dest:
            return
        
        xDif = self.dest[0]-self.rect.centerx
        yDif = self.dest[1]-self.rect.centery
            
        xMove = xDif*.3
        yMove = yDif*.3

        if abs(xMove) <= 1 and abs(yMove) <= 1 and self.target:
            self.NoTarget()
            return
        
        self.rect.x += xMove
        self.rect.y += yMove

    def SetTarget(self, target):
        self.canUse = False
        self.canUseCurrent = 0
        
        self.target = target
        self.dest = self.target.rect.center

    def NoTarget(self):
        if self.target in Object.GetObjects():
            self.target.OrbFunc()
        
        self.target = None
        self.dest = None

class Red(Orb):
    def __init__(self):
        super().__init__("Red")

class Yellow(Orb):
    def __init__(self):
        super().__init__("Yellow")

class Green(Orb):
    def __init__(self):
        super().__init__("Green")

class Blue(Orb):
    def __init__(self):
        super().__init__("Blue")
