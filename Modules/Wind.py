from Modules.GameObject import *

class Wind(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Wind())
        self.Solid = False

        self.hspd = 0
        self.vspd = 3

        self.timerVspdMax = Modules.Basic.GetClock()
        self.timerVspdCurrent = 0

    def Update(self):
        super().Update()
        self.rect.x += self.hspd
        self.rect.y += self.vspd

        if self.CheckCollide(Modules.Control.Player()):
            yMove = self.rectCollision.bottom-Modules.Control.Player().rectCollision.top
            Modules.Control.Player().rect.y += yMove

        if self.rect.top >= Modules.Background.BackgroundSize()[1]:
            self.Remove()

        if self.timerVspdCurrent <= self.timerVspdMax:
            self.timerVspdCurrent += 1
            return
        self.vspd += 1
        self.timerVspdCurrent = 0
