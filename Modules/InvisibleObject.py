from Modules.GameObject import *

class InvisibleObject(GameObject):
    def __init__(self):
        super().__init__()
        self.Solid = False
