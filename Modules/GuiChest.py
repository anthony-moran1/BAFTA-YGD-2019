from Modules.GameObject import *

class GuiChest(GameObject):
    def Add(self):
        Control.AddFantasyObject(self)

    def Remove(self):
        Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.depthLayer = "Gui"
        self.Solid = False
        self.CanCollide = False
        
        self.SetSprite(GameSprite.GuiChest())
        self.SpriteBar = GameSprite.GuiChestBar()
        self.SpriteBarOffsetX = self.Sprite.sprite.get_size()[0]-self.SpriteBar.sprite.get_size()[0]

    def Update(self):
        super().Update()
        numberOfCoins = Object.GetObjectVar({"Name":"Radio"}).numberOfCoins
        width = numberOfCoins/Control.CoinsMax*self.SpriteBar.sprite.get_size()[0]
        self.SpriteBar.frameRect.w = width

    def Show(self):
        Basic.GetScreen().blit(self.Sprite.sprite, self.rect.topleft)
        Basic.GetScreen().blit(self.SpriteBar.sprite,
                               (self.rect.x+self.SpriteBarOffsetX, self.rect.y),
                               self.SpriteBar.frameRect)
