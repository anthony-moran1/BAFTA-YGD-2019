from Modules.PlayerItem import *

class Sword(PlayerItem):
    def __init__(self, colour):
        super().__init__("Sword", colour)
        self.Sound = Modules.Audio.sword

class Red(Sword):
    def __init__(self):
        super().__init__("Red")

class Yellow(Sword):
    def __init__(self):
        super().__init__("Yellow")

class Green(Sword):
    def __init__(self):
        super().__init__("Green")

class Blue(Sword):
    def __init__(self):
        super().__init__("Blue")

def RandomSword():
    swords = [Red, Yellow, Green, Blue]
    return random.choice(swords)()
