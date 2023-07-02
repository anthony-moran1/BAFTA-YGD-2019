from Modules.GameObject import *
import Modules.Timer, Modules.SpeechBubble

class Radio(GameObject):
    class Coin(GameObject):
        def Add(self):
            Modules.Control.AddFantasyObject(self)
        def Remove(self):
            Modules.Control.RemoveFantasyObject(self)
            
        def __init__(self):
            super().__init__()
            self.SetSprite(Modules.GameSprite.Coin())

            self.Solid = False
            self.CanCollide = False

            self.hspd = random.randint(2, 3)
            self.vspd = random.randint(5, 8)
            self.xdir = random.choice([-1, 1])

            self.lifetimeMax = Modules.Basic.GetClock()
            self.lifetimeCurrent = 0

        def Update(self):
            super().Update()
            
            if self.lifetimeCurrent >= self.lifetimeMax:
                self.Remove()
                return
            self.lifetimeCurrent += 1
            
            self.Move(round(self.hspd*self.xdir), 0)
            self.Move(0, -round(self.vspd))

            self.vspd -= .5
            
    def __init__(self):
        super().__init__()
        self.Name = "Radio"
        
        self.SetSprite(Modules.GameSprite.Radio())

        self.numberOfCoins = 10
        self.coinSprite = Modules.GameSprite.Coin()
        self.coinRect = pygame.Rect((0,0), self.coinSprite.frameRect.size)

        self.message = None
        self.timerDone = True

    def Update(self):
        super().Update()
        self.PLAYERITEMFUNC = Modules.Control.Fantasy and self.timerDone

    def Show(self):
        super().Show()
        if not self.SHOW or self.numberOfCoins <= 0 or not Modules.Control.Fantasy:
            return
        self.coinRect.midbottom = self.rect.midtop
        Modules.Basic.GetScreen().blit(self.coinSprite.sprite,
                               Modules.Object.GetObjectVar({"Name":"Camera"}).GetPosCam(self.coinRect.topleft))

    def PlayerItemFunc(self):
        if Modules.Control.Fantasy:
            self.PlayerItemFuncFantasy()
        else:
            self.PlayerItemFuncNonFantasy()
        self.SetTimerDone(False)
        Modules.Timer.Timer(5, lambda:self.SetTimerDone(True)).Add()

    def SetTimerDone(self, trueFalse):
        self.timerDone = trueFalse

    def PlayerItemFuncNonFantasy(self):
        Modules.Audio.PlayPause()

    def PlayerItemFuncFantasy(self):
        self.CoinScatter()

    def CoinScatter(self):
        for i in range(random.randint(4, 8)):
            coin = self.Coin()
            coin.rect.center = self.rect.center
            coin.Add()

    def Steal(self, who):
        if not hasattr(who, "stealImmune"):
            who.stealImmune = False
            
        if who.stealImmune or self.numberOfCoins <= 0:
            return
        self.numberOfCoins -= 1
        self.CoinScatter()
        
        who.stealImmune = True
        def func():
            who.stealImmune = False
        Timer.Timer(random.randint(6, 8), func).Add()

        enemyChest = random.choice(Object.GetObjectsVar({"Name":"RadioEnemy"}))
        enemyChest.numberOfCoins += 1

class RadioEnemy(Radio):
    def Add(self):
        Control.AddFantasyObject(self)

    def Remove(self):
        Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.Name = "RadioEnemy"
        
        self.SetSprite(Modules.GameSprite.RadioEnemy())
        self.Solid = False

        self.numberOfCoins = 0

    def Update(self):
        super().Update()
        if not self.UPDATE:
            return
        self.PLAYERITEMFUNC = self.numberOfCoins > 0

    def PlayerItemFunc(self):
        if self.numberOfCoins <= 0:
            return
        
        self.CoinScatter()
        self.numberOfCoins -= 1
        chest = Object.GetObjectVar({"Name":"Radio"})
        chest.numberOfCoins += 1
