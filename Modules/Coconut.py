from Modules.GameObject import *

class Coconut(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Coconut())
        self.Name = "Coconut"
        self.Solid = False
        self.depthLayer = "Hih"

        self.target = None

    def Update(self):
        super().Update()
        if not self.target:
            return

        xMove = (self.target.rect.centerx-self.rect.centerx)*.1
        yMove = (self.target.rect.centery-self.rect.centery)*.1
        self.rect.x += xMove
        self.rect.y += yMove

        if abs(xMove) < 1 and abs(yMove) < 1:
            if self.target.Name == "Fireplace":
                self.target.TakeDamage()
            self.Remove()

    def RemoveFollowFunc(self):
        self.target = Modules.Control.Player().LockOn.target
