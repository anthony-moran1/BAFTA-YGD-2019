from Modules.GameObject import *

class Box(GameObject):
    def Add(self):
        Modules.Control.AddFantasyObject(self)

    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.Name = "Box"
        self.SetSprite(Modules.GameSprite.Box())

        self.Item = None
        self.PLAYERITEMFUNC = True

    def Open(self):
        self.Remove()
        if not self.Item:
            return
        
        self.Item.Add()
        self.Item.rect.center = self.rect.center
        self.Item = None

    def PlayerItemFunc(self):
        self.Open()

    def AssignItem(self, item):
        self.Item = item
