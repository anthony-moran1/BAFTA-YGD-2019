from Modules.GameObject import *
import Modules.Background, Modules.Timer

SpeechBubbles = []
camTargetOriginal = None

SpeechNow = True

def ResetSpeech():
    global SpeechBubbles, SpeechNow
    while Modules.Object.GetObjectVar({"Name":"SpeechBubble"}):
        Modules.Object.GetObjectVar({"Name":"SpeechBubble"}).Remove()
    SpeechNow = True    
        
class SpeechBubble(GameObject):
    def SetText(self, txt):
        self.txt, self.rect = Modules.Function.text(txt, self.colour, self.font)

    def Add(self):
        global SpeechNow
        if not SpeechNow:
            if self not in SpeechBubbles:
                SpeechBubbles.insert(0, self)
            return
        
        super().Add()
        SpeechNow = False

        if not hasattr(self.where, "rect"):
            return
        cam = Modules.Object.GetObjectVar({"Name":"Camera"})
        if cam.target == self.where:
            return
        cam.SetTarget(self.where)

    def Remove(self):
        if self not in Modules.Object.GetObjects():
            return

        self.timer.Remove()
        
        global SpeechNow
        super().Remove()
        SpeechNow = True
        
        self.func()
        if len(SpeechBubbles) == 0:
            player = Modules.Object.GetObjectVar({"Name":"Player"})
            Modules.Object.GetObjectVar({"Name":"Camera"}).SetTarget(player)
            return
        nextSpeechBubble = SpeechBubbles[0]
        SpeechBubbles.remove(nextSpeechBubble)
        nextSpeechBubble.Add()
        
    def __init__(self, txt, where, func=lambda:None):
        super().__init__()
        self.Name = "SpeechBubble"
        self.Solid = False
        self.CanCollide = False
        self.depthLayer = "Gui"

        self.colour = (51, 51, 51)
        self.colourFill = (255,255,255)
        self.font = Modules.Control.FontSpeechBubble

        self.txtMax = txt
        self.txtCurrent = ""
        self.SetText(self.txtCurrent)

        self.where = where
        self.func = func

        self.timer = Modules.Timer.Timer(3, self.Remove)

        global SpeechBubbles, SpeechNow
        if not SpeechNow:
            SpeechBubbles.append(self)
        else:
            self.Add()

        self.justFull = False

        self.txtEnter, self.txtEnterRect = Modules.Function.text("Press Enter To Continue", self.colour, self.font)

    def Update(self):
        super().Update()
        if self.txtCurrent != self.txtMax:
            self.txtCurrent += self.txtMax[len(self.txtCurrent)]
            self.SetText(self.txtCurrent)
                
        if Modules.Event.GetKeyPressed(pygame.K_RETURN):
            if self.txtCurrent == self.txtMax:
                self.Remove()
            elif len(self.txtCurrent) > 2:
                self.txtCurrent = self.txtMax
                self.SetText(self.txtMax)

        if self.txtCurrent == self.txtMax and not self.justFull:
            self.timer.Add()
            self.justFull = True
                
    def Show(self):
        pygame.draw.rect(Modules.Basic.GetScreen(), self.colourFill, (self.GetPosBlit(), self.rect.size))
        pygame.draw.rect(Modules.Basic.GetScreen(), self.colour, (self.GetPosBlit(), self.rect.size), 1)
        Modules.Basic.GetScreen().blit(self.txt, self.GetPosBlit())

        if self.txtCurrent != self.txtMax:
            return
        self.txtEnterRect.centerx = self.posCam[0]+self.rect.w//2
        self.txtEnterRect.bottom = self.posCam[1]-4
        pygame.draw.rect(Modules.Basic.GetScreen(), self.colourFill, self.txtEnterRect)
        Modules.Basic.GetScreen().blit(self.txtEnter, self.txtEnterRect)

    def GetPosBlit(self):
        if type(self.where) == tuple:
            pos = self.where
        elif hasattr(self.where, "rect"):
            pos = self.where.rect.midtop
        self.rect.midbottom = pos

        sw, sh = Modules.Background.BackgroundSize()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > sw:
            self.rect.right = sw
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > sh:
            self.rect.bottom = sh
        self.posCam = Modules.Object.GetObjectVar({"Name":"Camera"}).GetPosCam(self.rect.topleft)
        return self.posCam
