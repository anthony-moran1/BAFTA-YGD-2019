from Modules.GameObject import *

class GuiBar(GameObject):
    def SetFrame(self, frame):
        for sprite in self.Sprites:
            sprite.SetFrame(frame)
            
    def __init__(self):
        super().__init__()
        self.depthLayer = "Gui"
        
        self.SpriteBackground = Modules.GameSprite.GuiBackground()
        self.SpriteBar = Modules.GameSprite.GuiBar()
        self.SpriteIcon = Modules.GameSprite.GuiIcon()
        self.Sprites = [self.SpriteBackground,
                        self.SpriteBar,
                        self.SpriteIcon]

        self.valMax = 0
        self.valCurrent = 0

    def Update(self):
        super().Update()
        self.SpriteBackground.frameRect.w = self.SpriteBackground.frameWidth*(self.valCurrent/self.valMax)

    def Show(self):
        screen = Modules.Basic.GetScreen()
        screen.blit(self.SpriteBackground.sprite, self.rect.topleft,
                    self.SpriteBackground.frameRect)
        screen.blit(self.SpriteBar.sprite, self.rect.topleft,
                    self.SpriteBar.frameRect)
        screen.blit(self.SpriteIcon.sprite, self.rect.topleft,
                    self.SpriteIcon.frameRect)

class Enemy(GuiBar):
    def __init__(self):
        super().__init__()
        self.SetFrame(0)

        self.valMax = 10

class Timer(GuiBar):
    def __init__(self):
        super().__init__()
        self.SetFrame(1)

        self.valMax = 10
        self.valCurrent = self.valMax
