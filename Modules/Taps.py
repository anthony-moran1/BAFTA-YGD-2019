from Modules.GameObject import *

class Taps(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Taps())
