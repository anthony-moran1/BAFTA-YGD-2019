from Modules.GameObject import *
import Modules.SpeechBubble

class Lifeform(GameObject):
    def Update(self):
        super().Update()
        self.UnStick()
        self.KeepOnRoom()

    def Speak(self, txt, func=lambda:None):
        Modules.SpeechBubble.SpeechBubble(txt, self, func)
