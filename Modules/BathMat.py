from Modules.GameObject import *

class BathMat(GameObject):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.BathMat())
        self.Solid = False
        self.depthLayer = "Low"

        self.Bath = None
        self.rectOriginalPlayer = None

    def Update(self):
        super().Update()
        self.Solid = Modules.Control.Fantasy

        if self.Bath:
            self.PLAYERITEMFUNC = bool(self.Bath.target)
        else:
            self.PLAYERITEMFUNC = False

    def PlayerItemFunc(self):
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        Modules.Control.FantasySwap()

        self.Bath.rect.topleft = self.Bath.rectOriginal.topleft
        self.Bath.target = None
        if self.rectOriginalPlayer:
            player.rect.topleft = self.rectOriginalPlayer.topleft

        Modules.BoatBox.Boat = None

    def ForceNonFantasy(self):
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        posPlayer = player.rect.topleft
        self.PlayerItemFunc()
        player.rect.topleft = posPlayer

class BathMatParents(BathMat):
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.BathMatParents())
