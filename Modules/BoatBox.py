from Modules.CollisionBox import *
import Modules.Bath

Boat = None
class BoatBox(CollisionBox):
    def Add(self):
        Modules.Control.AddFantasyObject(self)

    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)
        
    def Func(self, player):
        if not Boat:
            return
        boatInObjects = Boat in Modules.Object.GetObjects()
        if not boatInObjects:
            player.rect.topleft = self.posBoat
            Boat.Add()
        else:
            player.rect.topleft = self.posNoBoat
            Boat.Remove()
            
    def __init__(self, topleft, bottomright, posBoat, posNoBoat):
        super().__init__(topleft, bottomright, self.Func, oneTime=False)
        self.posBoat = Modules.Background.GetPosBackground(posBoat)
        self.posNoBoat = Modules.Background.GetPosBackground(posNoBoat)
