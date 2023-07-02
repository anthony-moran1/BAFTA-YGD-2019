from Modules.GameObject import *
import Modules.SpeechBubble

class PlayerItem(GameObject):
    def Add(self):
        Modules.Control.AddFantasyObject(self)

    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)
        
    def __init__(self, name, colour):
        super().__init__()
        self.Name = name
        self.Sound = None
        
        self.Solid = False
        self.CanCollide = False
        self.rectOffset = pygame.Rect(self.rect)
        
        self.colour = colour
        self.SetSprite(eval("Modules.GameSprite."+self.Name+self.colour)())
        self.depthLayer = "Hih"

        self.target = None
        self.dest = None
        
        self.canUse = True
        self.canUseMax = Modules.Basic.GetClock()
        self.canUseCurrent = 0

    def Update(self):                
        if not self.UPDATE:
            return
        
        super().Update()
        self.Rotate(math.pi/90)
        self.MoveControl()

        if self.canUse or self.target:
            self.SetSprite(eval("Modules.GameSprite."+self.Name+self.colour)())
        else:
            self.SetSprite(eval("Modules.GameSprite."+self.Name+"Grey")())
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
            if self.Sound:
                self.Sound.Play()
            return
        
        self.rect.x += xMove
        self.rect.y += yMove

    def SetTarget(self, target):
        self.canUse = False
        self.canUseCurrent = 0
        
        self.target = target
        self.dest = self.target.rect.center

    def NoTarget(self):
        if self.target in Modules.Object.GetObjects():
            if Modules.Control.Player().INPUT:
                self.target.PlayerItemFunc()
        
        self.target = None
        self.dest = None
