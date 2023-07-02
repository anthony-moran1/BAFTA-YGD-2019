from Modules.GameObject import *

class CollisionBox(GameObject):
    def __init__(self, topleft, bottomright, func, oneTime=True):
        super().__init__()
        self.Solid = False

        w = bottomright[0]-topleft[0]+1
        h = bottomright[1]-topleft[1]+1
        topleft = Modules.Background.GetPosBackground(topleft)
        size = Modules.Background.GetPosBackground((w, h))
        self.rect = pygame.Rect(topleft, size)
        self.rectCollision = pygame.Rect(self.rect)
        
        self.func = func
        self.oneTime = oneTime

    def Update(self):
        super().Update()

        if self.CheckCollide(Modules.Object.GetObjectVar({"Name":"Player"})):
            self.func(Modules.Object.GetObjectVar({"Name":"Player"}))
            if self.oneTime:
                self.Remove()
        
