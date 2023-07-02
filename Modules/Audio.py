import pygame
pygame.init()

class Song:
    def __init__(self, name):
        self.name = name
        self.filename = "Music/"+self.name+".wav"

    def Play(self):        
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play(-1)
memeSong = Song("Meme")
pirateSong = Song("Pirate")
childSong = Song("Child")

class Sound:
    def __init__(self, name):
        self.name = name
        self.filename = "Sounds/"+self.name+".wav"

        self.sound = pygame.mixer.Sound(self.filename)

    def Play(self):
        self.sound.play()

alert = Sound("Alert")
sword = Sound("Sword")

def GetPlaying():
    return pygame.mixer.music.get_busy()

def StopPlaying():
    pygame.mixer.music.stop()

def StartPlaying():
    pygame.mixer.music.play(-1)

def SetVolume(val):
    pygame.mixer.music.set_volume(val)

def Pause():
    global PAUSE
    PAUSE = True
    pygame.mixer.music.pause()

def UnPause():
    global PAUSE
    PAUSE = False
    pygame.mixer.music.unpause()

PAUSE = False
def PlayPause():
    if not GetPlaying():
        memeSong.Play()
        return
    
    if PAUSE:
        UnPause()
    else:
        Pause()
