from GameObject import *

class Bridge(GameObject):
    def Add(self):
        Control.AddFantasyObject(self)

    def Remove(self):
        Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.SetSprite(GameSprite.Bridge())
        self.depthLayer = "Low"
        
        self.Solid = False
        self.OPEN = False

    def Update(self):
        super().Update()
        
        dist = Function.dist(self.rect.center, Object.GetObjectVar({"Name":"Player"}).rect.center)
        if dist < 128 and not self.OPEN and Object.GetObjectVar({"Name":"Boat"}):
            self.Open()
        elif dist >= 128 and self.OPEN:
            self.Close()

    def Open(self):
        self.OPEN = True
        self.Sprite.SetFrame(1)

    def Close(self):
        self.OPEN = False
        self.Sprite.SetFrame(0)
