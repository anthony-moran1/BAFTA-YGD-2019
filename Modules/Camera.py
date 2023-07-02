from Modules.InvisibleObject import *
import Modules.Background

class Camera(InvisibleObject):
    def __init__(self):
        super().__init__()
        self.Name = "Camera"
        self.target = None
        self.rect.size = Modules.Basic.GetScreenSize()

    def Update(self):
        super().Update()
        if self.target == None:
            return

        sw, sh = Modules.Basic.GetScreenSize()
        xDif = (self.target.rect.centerx-sw//2)-self.rect.x
        yDif = (self.target.rect.centery-sh//2)-self.rect.y
        xMove = xDif*.1
        yMove = yDif*.1

        self.rect.x += xMove
        self.rect.y += yMove

        bw, bh = Modules.Background.BackgroundSize()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > bw:
            self.rect.right = bw
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > bh:
            self.rect.bottom = bh

    def SetTarget(self, target):
        self.target = target

    def GetPosCam(self, pos):
        cx, cy = pos
        cx -= self.rect.x
        cy -= self.rect.y

        posCam = (cx, cy)
        return posCam
