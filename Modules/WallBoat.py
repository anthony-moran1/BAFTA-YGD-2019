from Modules.Wall import *
import Modules.BoatBox

class WallExceptBoat(Wall):
    def Update(self):
        super().Update()
        self.Solid = not Modules.BoatBox.Boat

class WallOnlyBoat(Wall):
    def Update(self):
        super().Update()
        self.Solid = Modules.BoatBox.Boat
