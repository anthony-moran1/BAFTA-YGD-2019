from Modules.GameObject import *
import Modules.Timer

class Alert(GameObject):
    def __init__(self):
        super().__init__()
        self.Name = "Alert"
        self.SHOW = False

        self.SetSprite(GameSprite.Alert())
        self.Sound = Audio.alert

        self.coolDownMax = Basic.GetClock()*5
        self.coolDownCurrent = self.coolDownMax

    def Update(self):
        super().Update()
        self.rect.midtop = (Basic.GetScreenSize()[0]//2, 8)

        if self.coolDownCurrent < self.coolDownMax:
            self.coolDownCurrent += 1

    def Show(self):
        if not self.SHOW:
            return
        Basic.GetScreen().blit(self.Sprite.sprite, self.rect.topleft)

    def StartAlerting(self):
        if self.coolDownCurrent < self.coolDownMax:
            return
        self.coolDownCurrent = 0
        
        self.SHOW = True
        self.Sound.Play()

        Timer.Timer(3, self.StopAlerting).Add()

    def StopAlerting(self):
        self.SHOW = False
