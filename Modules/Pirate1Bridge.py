from Modules.GameObject import *

class Pirate1Bridge(GameObject):
    def __init__(self):
        super().__init__()
        self.depthLayer = "Low"
        self.Solid = False
        self.SetSprite(Modules.GameSprite.Pirate1Bridge())
