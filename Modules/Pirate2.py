from Modules.Lifeform import *
import Modules.Sword, Modules.GuiBar, Modules.Timer, Modules.BoatBox, Modules.EnemySpawn

class Pirate2(Lifeform):
    def Add(self):
        Modules.Control.AddFantasyObject(self)

    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Pirate2())
        self.Finish = True

    def Update(self):
        super().Update()
        self.PLAYERITEMFUNC = Modules.BoatBox.Boat not in Modules.Object.GetObjects() and self.Finish

    def PlayerItemFunc(self):
        self.Finish = False
        self.PLAYERITEMFUNC = False
        
        self.Speak("Hey there, welcome to the party room!")
        self.Speak("My challenge for you is simple")
        self.Speak("Keep the enemy forces at bay unitl the timer runs out!")
        self.Speak("Are you ready? Let's do this!", self.StartGame)

    def StartGame(self):        
        player = Modules.Control.Player()
        player.SetPosition((150, 514))

        self.SwordsExtra = 15-len(player.Items)
        for i in range(self.SwordsExtra):
            player.AddRandomItem(Modules.Sword)

        self.guiBarEnemy = Modules.GuiBar.Enemy()
        self.guiBarTimer = Modules.GuiBar.Timer()

        sw, sh = Modules.Basic.GetScreenSize()

        self.guiBarTimer.rect.midtop = (sw//2, 8)
        self.guiBarEnemy.rect.midtop = (sw//2, self.guiBarTimer.rect.bottom+64)

        self.guiBarTimer.Add()
        self.guiBarEnemy.Add()

        def GoodFinishCheck():
            return self.guiBarTimer.valCurrent <= 0
        self.goodFinishCheck = Modules.Timer.Check(GoodFinishCheck,
                                              self.GoodFinish)
        def BadFinishCheck():
            return self.guiBarEnemy.valCurrent >= self.guiBarEnemy.valMax
        self.badFinishCheck = Modules.Timer.Check(BadFinishCheck,
                                             self.BadFinish)

        self.goodFinishCheck.Add()
        self.badFinishCheck.Add()

        def UpdateTimer():
            if self.guiBarTimer.valCurrent <= 0:
                return
            self.guiBarTimer.valCurrent -= 1
            Modules.Timer.Timer(1, UpdateTimer).Add()
        self.updateTimer = Modules.Timer.Timer(1, UpdateTimer)

        def UpdateEnemy():
            self.guiBarEnemy.valCurrent = len(Modules.Object.GetObjectsVar({"Name":"Enemy"}))
        self.updateEnemy = Modules.Timer.DoForever(UpdateEnemy)

        self.updateTimer.Add()
        self.updateEnemy.Add()

        self.enemySpawnsPositions = [(69, 519), (231, 519)]
        self.enemySpawns = [Modules.EnemySpawn.EnemySpawn() for i in range(len(self.enemySpawnsPositions))]
        for i in range(len(self.enemySpawnsPositions)):
            pos = self.enemySpawnsPositions[i]
            enemySpawn = self.enemySpawns[i]
            enemySpawn.SetPosition(pos)
            enemySpawn.Add()

        self.wallTemp = Modules.Wall.WallGood((141, 569), (169, 570))
        self.wallTemp.Add()

    def FinishGame(self):
        def SetFinish():
            self.Finish = True
        Modules.Timer.Timer(3, SetFinish).Add()
        
        self.guiBarTimer.Remove()
        self.guiBarEnemy.Remove()

        self.goodFinishCheck.Remove()
        self.badFinishCheck.Remove()

        self.updateTimer.Remove()
        self.updateEnemy.Remove()

        self.wallTemp.Remove()

        for enemySpawn in self.enemySpawns:
            enemySpawn.Remove()
        
        for i in range(self.SwordsExtra):
            Modules.Control.Player().RemoveRandomItem()

        for enemy in Modules.Object.GetObjectsVar({"Name":"Enemy"}):
            enemy.Remove()

    def GoodFinish(self):
        self.FinishGame()
        self.Speak("Well done! That was impressive")

    def BadFinish(self):
        self.FinishGame()
        self.Speak("The croissants got the better of you eh? You can try again if you want!")
