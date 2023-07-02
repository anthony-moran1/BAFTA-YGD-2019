from Modules.GameObject import *

class Wall(GameObject):
    def __init__(self, size):
        super().__init__()
        self.Name = "Wall"
        
        self.rect = pygame.Rect((0,0), size)
        self.rectCollision = pygame.Rect(self.rect)

    def Update(self):
        super().Update()
        if not self.UPDATE:
            return
        self.rectCollision.topleft = self.rect.topleft

class WallGood(Wall):
    def __init__(self, topleft, bottomright):
        w = bottomright[0]-topleft[0]+1
        h = bottomright[1]-topleft[1]+1
        size = Modules.Background.GetPosBackground((w, h))
        super().__init__(size)

        self.rect.topleft = Modules.Background.GetPosBackground(topleft)

class WallTemp(Wall):
    def __init__(self, topleft, bottomright, checkRemove):
        w = bottomright[0]-topleft[0]+1
        h = bottomright[1]-topleft[1]+1
        size = Modules.Background.GetPosBackground((w, h))
        super().__init__(size)

        self.rect.topleft = Modules.Background.GetPosBackground(topleft)
        self.checkRemove = checkRemove

    def Update(self):
        super().Update()
        if self.checkRemove():
            self.Remove()

    def Show(self):
        pygame.draw.rect(Modules.Basic.GetScreen(),
                         (255,255,255),
                         pygame.Rect(Modules.Object.GetObjectVar({"Name":"Camera"}).GetPosCam(self.rectCollision.topleft),
                                     self.rectCollision.size))

class WallFantasy(Wall):
    def Add(self):
        Modules.Control.AddFantasyObject(self)
    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)

    def __init__(self, size):
        size = Modules.Background.GetPosBackground(size)
        super().__init__(size)
