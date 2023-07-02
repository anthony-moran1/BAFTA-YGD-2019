from Modules.GameObject import *
import Modules.Coconut

class Plant(GameObject):
    def ResetCoconutRegen(self):
        self.PLAYERITEMFUNC = False
        
        self.CoconutMax = random.randint(5, 10)*Modules.Basic.GetClock()
        self.CoconutCurrent = 0
        
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Plant())

        self.Coconut = False
        self.ResetCoconutRegen()

    def Update(self):
        super().Update()
        if not Modules.Control.Fantasy:
            self.PLAYERITEMFUNC = False
            return
        if Modules.Object.GetObjectVar({"Name":"Fireplace"}).hpCurrent <= 0:
            self.PLAYERITEMFUNC = False
            return
        if self.CoconutCurrent < self.CoconutMax:
            self.CoconutCurrent += 1
            return
        self.PLAYERITEMFUNC = True

    def PlayerItemFunc(self):
        if Modules.Control.FirstCoconutReceived:
            Modules.Control.Player().Speak("I can direct these coconuts at the octopus by using my sword!")
            Modules.Control.FirstCoconutReceived = False
        coconut = Modules.Coconut.Coconut()
        coconut.rect.center = self.rect.center
        Modules.Control.Player().AddFollowItem(coconut)
        self.ResetCoconutRegen()
