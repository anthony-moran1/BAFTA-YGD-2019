from Modules.Lifeform import *

class Mum(Lifeform):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Mum())
