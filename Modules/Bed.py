from Modules.GameObject import *

class Bed(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Bed())

class BedParents(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.BedParents())
