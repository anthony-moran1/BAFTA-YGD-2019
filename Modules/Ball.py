from Modules.GameObject import *
import Modules.BoatBox

class Ball(GameObject):
    def __init__(self):
        super().__init__()
        self.Name = "Ball"
        self.SetSprite(Modules.GameSprite.Ball())

    def Update(self):
        super().Update()
        self.UPDATEPLAYERITEMFUNC()
        
        player = Modules.Control.Player()
        if self in Modules.Control.Player().ItemsFollow and Modules.Control.Fantasy:
            player.hspd = 4
            player.vspd = 4
        else:
            player.hspd = player.hspdOriginal
            player.vspd = player.vspdOriginal

    def UPDATEPLAYERITEMFUNC(self):
        PLAYERITEMFUNC = True
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        if not Modules.Control.Pirate1QuestStarted:
            PLAYERITEMFUNC = False
        elif self in player.ItemsFollow:
            PLAYERITEMFUNC = False
        self.PLAYERITEMFUNC = PLAYERITEMFUNC

    def PlayerItemFunc(self):
        def Pirate1Check():
            return Modules.Object.GetObjectVar({"Name":"Pirate1"})
        def Pirate1():
            Modules.Object.GetObjectVar({"Name":"Pirate1"}).PLAYERITEMFUNC = True
        Modules.Timer.Check(Pirate1Check, Pirate1).Add()
        
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        player.AddFollowItem(self)
        if not Modules.BoatBox.Boat:
            player.Speak("I'll need my boat to sail the sea and see my crew again")

        def HeavyPromptCheck():
            return Modules.Control.Fantasy
        def HeavyPrompt():
            player.Speak("This sure is a heavy cannon ball... This could take a while")
        Modules.Timer.Check(HeavyPromptCheck, HeavyPrompt).Add()

    def RemoveFollowFunc(self):
        player = Modules.Control.Player()
        player.hspd = player.hspdOriginal
        player.vspd = player.vspdOriginal
