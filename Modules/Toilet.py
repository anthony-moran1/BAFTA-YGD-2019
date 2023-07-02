from Modules.GameObject import *

class Toilet(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Toilet())
