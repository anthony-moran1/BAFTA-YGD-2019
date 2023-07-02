from Modules.GameObject import *
import Modules.Croissant

class EnemySpawn(GameObject):
    def Spawn(self):
        enemy = Modules.Croissant.Red()
        enemy.rect.center = self.rect.center
        enemy.Add()

    def Add(self):
        super().Add()
        self.timer.Add()

    def Remove(self):
        super().Remove()
        self.timer.Remove()
        
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.EnemySpawn())

        self.Solid = False
        def SpawnFunc():
            self.Spawn()
            self.timer = Modules.Timer.Timer(random.randint(0, 3), SpawnFunc)
            self.timer.Add()
        self.timer = Modules.Timer.Timer(1, SpawnFunc)
