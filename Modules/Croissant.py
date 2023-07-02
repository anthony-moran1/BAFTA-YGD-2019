from Modules.Enemy import *

class Croissant(Enemy):
    def __init__(self, colour):
        super().__init__()
        self.colour = colour
        self.SetSprite(eval("Modules.GameSprite.Croissant"+self.colour)())

class Red(Croissant):
    def __init__(self):
        super().__init__("Red")

class Orange(Croissant):
    def __init__(self):
        super().__init__("Orange")
