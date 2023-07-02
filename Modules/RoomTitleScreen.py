from Modules.Room import *
from Modules.GameObject import *
import Modules.RoomHouse

class ArrowMenuSelect(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.ArrowMenuSelect())

        self.points = []
        self.pointIndex = 0

        self.uk = pygame.K_UP
        self.dk = pygame.K_DOWN

        self.selectKey = pygame.K_RETURN

    def Update(self):
        super().Update()
        if Modules.Event.GetKeyPressed(self.uk):
            self.pointIndex -= 1
        elif Modules.Event.GetKeyPressed(self.dk):
            self.pointIndex += 1
            
        if self.pointIndex < 0:
            self.pointIndex = len(self.points)-1
        elif self.pointIndex >= len(self.points):
            self.pointIndex = 0

        self.rect.topleft = self.points[self.pointIndex][0]

        if Modules.Event.GetKeyPressed(self.selectKey):
            self.points[self.pointIndex][1]()

    def AddPoint(self, pos, func):
        self.points.append((Modules.Background.GetPosBackground(pos), func))
        
class room(Room):
    def __init__(self):
        super().__init__(player=False)
        Modules.Background.Background().Add()
        Modules.Background.GetBackground().SetSprite(Modules.GameSprite.BckTitleScreen())

        arrow = ArrowMenuSelect()
        arrow.AddPoint((48, 83), Modules.RoomHouse.room)
        arrow.AddPoint((48, 100), Modules.Basic.ForceQuit)
        arrow.Add()

        Modules.Control.Initialise()
