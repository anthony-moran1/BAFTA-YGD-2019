from Modules.InvisibleObject import *

class Timer(InvisibleObject):
    def __init__(self, time, func):
        super().__init__()
        
        self.time = Modules.Basic.GetClock()*time
        self.func = func

    def Update(self):
        if not self.UPDATE:
            return
        
        super().Update()

        if self.time > 0:
            self.time -= 1
            return
        self.func()
        self.Remove()

class TimerDo(Timer):
    def Update(self):
        if not self.UPDATE:
            return

        super().Update()

        if self.time > 0:
            self.time -= 1
            self.func()
            return
        self.Remove()

class DoForever(InvisibleObject):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def Update(self):
        super().Update()
        self.func()

class Check(InvisibleObject):
    def __init__(self, check, func):
        super().__init__()

        self.check = check
        self.func = func

    def Update(self):
        super().Update()
        if self.check():
            self.func()
            self.Remove()
