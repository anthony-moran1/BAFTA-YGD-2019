from Modules.GameObject import *

class LockOn(GameObject):
    def __init__(self):
        super().__init__()
        self.Solid = False
        
        self.SetSprite(Modules.GameSprite.LockOn())
        self.depthLayer = "Gui"

        self.LOCK = False
        self.target = None
        self.SHOW = self.target != None

        self.lockKey = pygame.K_LCTRL
        self.txtColour = (51,51,51)
        self.fillColour = (255,255,255)
        self.font = Modules.Control.FontLockOn
        self.txtSpacebar, self.txtSpacebarRect = Modules.Function.text("Spacebar", self.txtColour, self.font)

    def Update(self):        
        super().Update()
        if self.target == None:
            return

        if not self.CheckValidTarget(self.target):
            self.NoTarget()
            return
        
        if Modules.Event.GetKeyPressed(self.lockKey):
            self.LockUnLock()

        self.rect.center = self.target.rect.center

    def Show(self):
        super().Show()
        if not self.SHOW:
            return
        self.txtSpacebarRect.midbottom = self.rect.midtop
        posCam = Modules.Object.GetObjectVar({"Name":"Camera"}).GetPosCam(self.txtSpacebarRect.topleft)
        pygame.draw.rect(Modules.Basic.GetScreen(),
                         self.fillColour,
                         pygame.Rect(posCam, self.txtSpacebarRect.size))
        Modules.Basic.GetScreen().blit(self.txtSpacebar, posCam)
        

    def Lock(self):
        self.LOCK = True
        self.Sprite.SetFrame(1)

    def UnLock(self):
        self.LOCK = False
        self.Sprite.SetFrame(0)

    def LockUnLock(self):
        if self.LOCK:
            self.UnLock()
            return
        self.Lock()

    def SetTarget(self, target):
        self.target = target
        self.SHOW = True

    def NoTarget(self):
        self.target = None
        self.SHOW = False
        self.UnLock()

    def CheckValidTarget(self, target):
        if target not in Modules.Object.GetObjects():
            return False
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        if Modules.Function.dist(player.rect.center, target.rect.center) > 160:
            return False
        return True
