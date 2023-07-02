from Modules.GameObject import *
import Modules.Map

class MapCollectable(GameObject):
    def Add(self):
        Modules.Control.AddFantasyObject(self)

    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.Name = "MapCollectable"
        self.SetSprite(Modules.GameSprite.MapCollectable())

        self.PLAYERITEMFUNC = True

    def PlayerItemFunc(self):
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        player.Map = True
        self.Remove()
        mp = Modules.Map.Map()
        mp.AddEnemyBase("BedroomParents")
        mp.AddChallenger("ToyRoom")
        mp.AddEnemyBase("StudyRoom")
        mp.AddEnemyBase("LivingRoom")
        mp.AddTreasure("DiningRoom")
        mp.Add()
