from Modules.Lifeform import *
import Modules.BoatBox, Modules.Sword

class Pirate1(Lifeform):
    def Add(self):
        Modules.Control.AddFantasyObject(self)
    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.Name = "Pirate1"
        self.SetSprite(Modules.GameSprite.Pirate1())

        self.PLAYERITEMFUNC = True

    def PlayerItemFunc(self):
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        teddyBear = Modules.Object.GetObjectVar({"Name":"TeddyBear"})
        
        if not Modules.Control.Pirate1QuestStarted:
            boat = Modules.BoatBox.Boat
            
            self.Speak("Hello there captain, I'm afraid that we're missing one cannon ball")                
            self.Speak("There is one at camp however it is quite heavy", boat.BathMat.ForceNonFantasy)
            player.Speak("Let's pretend that I'm super strong! I'll get my bouncy ball from my room!")
            Modules.Control.Pirate1QuestStarted = True
            self.PLAYERITEMFUNC = False
        elif player.CheckFollowItemExists("Ball"):
            player.RemoveFollowItem("Ball")
            ball = Modules.Object.GetObjectVar({"Name":"Ball"})
            ball.Remove()
            self.Speak("Thanks captain, I knew I could count on you!")
            teddyBear.Speak("Take this as our thanks",
                            lambda:player.AddItem(Modules.Sword.RandomSword()))
            player.Speak("Wow thanks!")
            Modules.Control.Pirate1QuestFinished = True
            self.PLAYERITEMFUNC = False

