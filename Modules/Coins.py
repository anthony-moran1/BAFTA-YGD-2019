from Modules.GameObject import *
import Modules.BoatBox

class Coins(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Coins())

    def Update(self):
        super().Update()
        self.PLAYERITEMFUNC = Modules.Control.Fantasy

    def PlayerItemFunc(self):
        player = Modules.Control.Player()
        
        player.Speak("Mmmm chocolate coins")
        player.Speak("I'll put these coins in my stash", self.Remove)
        player.Speak("Good find crew!")
