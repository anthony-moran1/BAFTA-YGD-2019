import pygame

class Sprite:
    def SetFramesMax(self, frames):
        self.framesMax = frames
        self.frameRect.w = self.sprite.get_size()[0]/self.framesMax
        
    def __init__(self, name, frames=1, frameRate=1, scale=1):
        self.name = name
        
        self.filename = "Sprites/"+self.name+".png"
        self.sprite = pygame.image.load(self.filename)

        self.scale = scale
        w, h = self.sprite.get_size()
        w *= self.scale
        h *= self.scale
        self.sprite = pygame.transform.scale(self.sprite, (w, h))

        self.framesMax = frames
        self.framesCurrent = 0
        self.frameRateMax = frameRate
        self.frameRateCurrent = 0

        self.frameWidth = w/self.framesMax
        self.frameHeight = h
        self.frameRect = pygame.Rect((0,0), (self.frameWidth, self.frameHeight))

        self.Animate = True

    def Update(self):
        if not self.Animate:
            return
        
        if self.frameRateCurrent < self.frameRateMax:
            self.frameRateCurrent += 1
            return
        self.frameRateCurrent = 0
        self.NextFrame()

    def SetFrame(self, frame):
        self.framesCurrent = frame
        self.frameRect.x = self.framesCurrent*self.frameRect.w

    def NextFrame(self):
        frame = self.framesCurrent+1
        if frame > self.framesMax-1:
            frame = 0
        self.SetFrame(frame)
