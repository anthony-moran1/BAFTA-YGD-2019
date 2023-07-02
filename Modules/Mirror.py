from Modules.GameObject import *

class Mirror(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Mirror())
