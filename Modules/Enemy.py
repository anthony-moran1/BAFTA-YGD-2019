from Modules.Lifeform import *
import Modules.Timer

class Enemy(Lifeform):
    def StartIdle(self):
        time = random.randint(3, 5)
        self.timerDo = Modules.Timer.TimerDo(time, self.Idle)
        self.timer = Modules.Timer.Timer(time, lambda:self.ChangeState("Wander"))

    def Idle(self):
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        dist = Modules.Function.dist(self.rect.center, player.rect.center)
        if dist < 320 and dist > self.rangeChaseStop:
            self.ChangeState("Chase")
        
    def StartWander(self):
        self.xdir = random.randint(-1, 1)
        self.ydir = random.randint(-1, 1)
        if self.xdir == 0 and self.ydir == 0:
            self.StartWander()
            return
        time = random.randint(1, 2)
        self.timerDo = Modules.Timer.TimerDo(time, self.Wander)
        self.timer = Modules.Timer.Timer(time, lambda:self.ChangeState("Idle"))

    def Wander(self):
        self.Move(self.xdir*self.hspd, 0)
        self.Move(0, self.ydir*self.vspd)

    def StartChase(self):
        self.target = Modules.Object.GetObjectVar({"Name":"Player"})
        time = 5

        def CheckContinueChase():
            dist = Modules.Function.dist(self.rect.center, self.target.rect.center)
            if dist < 192 and dist > self.rangeChaseStop:
                self.ChangeState("Chase")
            else:
                self.ChangeState("Idle")
        self.timerDo = Modules.Timer.TimerDo(time, self.Chase)
        self.timer = Modules.Timer.Timer(time, CheckContinueChase)

    def Chase(self):
        self.xdir = self.target.rect.centerx-self.rect.centerx
        self.ydir = self.target.rect.centery-self.rect.centery
        total = abs(self.xdir)+abs(self.ydir)
        self.xdir /= total
        self.ydir /= total
        
        xMove = self.xdir*self.hspd
        yMove = self.ydir*self.vspd        
        self.Move(int(xMove), 0)
        self.Move(0, int(yMove))

        if Modules.Function.dist(self.rect.center, self.target.rect.center) <= self.rangeChaseStop:
            self.ChangeState("Idle")

    def ChangeState(self, stateName):
        if self.timerDo:
            Modules.Control.RemoveFantasyObject(self.timerDo)
        if self.timer:
            Modules.Control.RemoveFantasyObject(self.timer)
        
        eval("self.Start"+stateName)()
        
        if self.timerDo:
            Modules.Control.AddFantasyObject(self.timerDo)
        if self.timer:
            Modules.Control.AddFantasyObject(self.timer)

    def Add(self):
        Modules.Control.AddFantasyObject(self.timerDo)
        Modules.Control.AddFantasyObject(self.timer)
        Modules.Control.AddFantasyObject(self)

    def Remove(self):
        Modules.Control.RemoveFantasyObject(self.timerDo)
        Modules.Control.RemoveFantasyObject(self.timer)
        Modules.Control.RemoveFantasyObject(self)

    def __init__(self):
        super().__init__()
        self.Name = "Enemy"
        self.PLAYERITEMFUNC = True

        self.xdir = self.ydir = 0
        self.hspd = self.vspd = 4

        self.healthMax = 1
        self.healthCurrent = self.healthMax

        self.target = None

        self.timerDo = None
        self.timer = None
        self.StartIdle()

        self.rangeChaseStop = 96

    def PlayerItemFunc(self):
        if self.healthCurrent > 1:
            self.healthCurrent -= 1
        else:
            self.Die()

    def Die(self):
        self.Remove()
