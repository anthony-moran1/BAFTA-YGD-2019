from Modules.GameObject import *

class Table(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Table())
        self.depthLayer = "Low"

class TableBig(Table):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.TableBig())
