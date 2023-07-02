from Modules.GameObject import *

class DiscoFloor(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.DiscoFloor())
        self.Solid = False
        self.depthLayer = "Low"
