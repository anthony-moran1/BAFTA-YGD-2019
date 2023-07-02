from Modules.GameObject import *

class Wardrobe(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Wardrobe())
