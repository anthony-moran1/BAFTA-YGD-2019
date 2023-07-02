from Modules.Lifeform import *

class TeddyBear(Lifeform):
    def __init__(self):
        super().__init__()
        self.Name = "TeddyBear"
        self.SetSprite(Modules.GameSprite.TeddyBear())
