from Modules.GameObject import *
import Modules.BoatBox, Modules.Wind
import Modules.RoomTitleScreen

class Fireplace(GameObject):
    def ResetWind(self):
        self.windMax = random.randint(3, 8)*Modules.Basic.GetClock()
        self.windCurrent = 0
        
    def __init__(self):
        super().__init__()
        self.Name = "Fireplace"
        self.SetSprite(Modules.GameSprite.Fireplace())

        self.hpMax = 6
        self.hpCurrent = self.hpMax

        self.ResetWind()
        self.NoSwordPrompt = False

    def Update(self):
        super().Update()
        self.PLAYERITEMFUNC = Modules.Control.Fantasy and self.hpCurrent > 0

        if not Modules.Control.Fantasy:
            return
        if self.windCurrent < self.windMax:
            self.windCurrent += 1
            return
        wind = Modules.Wind.Wind()
        wind.rect.center = self.rect.center
        wind.Add()
        self.ResetWind()

    def PlayerItemFunc(self):
        player = Modules.Control.Player()
        if not player.CheckFollowItemExists("Coconut") and not self.NoSwordPrompt:
            player.Speak("My swords don't seem to be affecting this ocotopus!")
            player.Speak("I'll have to try something else")
            self.NoSwordPrompt = True
            return
        player.RemoveFollowItem("Coconut")

    def TakeDamage(self):
        if self.hpCurrent <= 0:
            return
        
        self.hpCurrent -= 1

        player = Modules.Control.Player()
        if self.hpCurrent <= 0:
            def MumInterrupt():
                mum = Modules.Mum.Mum()
                mum.rect.topleft = Modules.Background.GetPosBackground((329, 510))
                mum.Add()
                mum.Speak("Captain Noah! What are you doing?!")
                player.Speak("I have slayed the octopus that had haunted our waters!",
                             Modules.BoatBox.Boat.BathMat.ForceNonFantasy)
                mum.Speak("Of course you have *chuckles*")
                mum.Speak("I have finished making your lunch, it's time to go to school now")
                player.Speak("Okay! I can't wait to tell my friends about all of the fun I've had!",
                             Modules.RoomTitleScreen.room)
            player.Speak("Arghh we have slayed the mighty octopus!",
                         MumInterrupt)
