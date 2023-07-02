from Modules.GameObject import *

class Carpet(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Carpet())
        self.Solid = False
        self.depthLayer = "Low"

        self.timerDone = True

    def Update(self):
        super().Update()
        self.PLAYERITEMFUNC = Modules.Control.Fantasy and self.timerDone

    def PlayerItemFunc(self):
        self.Sprite.Fantasy.NextFrame()
        self.SetTimerDone(False)
        Modules.Timer.Timer(5, lambda:self.SetTimerDone(True)).Add()

    def SetTimerDone(self, trueFalse):
        self.timerDone = trueFalse
