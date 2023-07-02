from Modules.GameObject import *
import Modules.SpeechBubble, Modules.BoatBox

class Bath(GameObject):        
    def __init__(self):
        super().__init__()
        self.Name = "Bath"
        self.Solid = not Modules.Control.Fantasy
        
        self.SetSprite(Modules.GameSprite.Bath())
        self.target = None

        self.BathMat = None
        self.rectOriginalPlayer = None
        
        self.speechBubble = None

    def Update(self):
        self.Solid = self != Modules.BoatBox.Boat
        if Modules.Control.Fantasy and self.target:
            self.rect.midbottom = self.target.rect.midbottom
            self.rect.y += self.target.vspd+1
            
        super().Update()
        
        self.PLAYERITEMFUNC = self.BathMat and not Modules.BoatBox.Boat

        if self.speechBubble:
            inObjects = self.speechBubble in Modules.Object.GetObjects()
            inSpeechBubbles = self.speechBubble in Modules.SpeechBubble.SpeechBubbles

            if not inObjects and not inSpeechBubbles:
                self.speechBubble = None

    def PlayerItemFunc(self):
        if not self.BathMat:
            return

        player = Modules.Object.GetObjectVar({"Name":"Player"})
        if not self.BathMat.CheckCollide(player):
            if not self.speechBubble:
                self.speechBubble = Modules.SpeechBubble.SpeechBubble("I think it would be safer to get into the bath while standing on the bath mat", player)
                self.speechBubble.Add()
            return
        Modules.Control.FantasySwap()
        if not Modules.Control.Fantasy:
            return
        
        self.target = player
        self.rectOriginal = pygame.Rect(self.rect)
        self.BathMat.rectOriginalPlayer = pygame.Rect(player.rect)
        player.rect.midbottom = self.rect.midbottom

        Modules.BoatBox.Boat = self        

class BathParents(Bath):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.BathParents())
