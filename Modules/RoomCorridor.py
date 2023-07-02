from Room import *
import RoomHouseFloorTop

class Corridor(Room):
    def __init__(self):
        super().__init__()
        self.Name = "Corridor"

    def StartRoom(self):
        Background.GetBackground().SetSprite(GameSprite.BckCorridor())
