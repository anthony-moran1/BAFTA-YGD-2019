from Modules.Sprite import *
import Modules.Control

class GameSprite(Sprite):
    def SetRectCollision(self, rectCollision):
        x, y = self.rectCollision.topleft
        w, h = self.rectCollision.size
        x, y = x*self.scale, y*self.scale
        w, h = w*self.scale, h*self.scale
        self.rectCollision = pygame.Rect(x, y, w, h)
            
    def __init__(self, name, frames=1, frameRate=1, scale=4, rectCollision=None):
        super().__init__(name, frames, frameRate, scale)
        
        self.rectCollision = rectCollision
        if not self.rectCollision:
            self.rectCollision = pygame.Rect((0,0), self.frameRect.size)
        else:
            self.SetRectCollision(rectCollision)
            
        try:
            self.Fantasy = Sprite(name+"Fantasy", frames, frameRate, scale)
        except Exception as e:
            self.Fantasy = self

class Bck(GameSprite):
    def __init__(self, name, plan=True):
        super().__init__(name)

        if not plan:
            return
        self.plan = Sprite(name+"Plan", scale=1)
        self.Fantasy.plan = Sprite(name+"FantasyPlan", scale=1)

class BckTitleScreen(Bck):
    def __init__(self):
        super().__init__("TitleScreen", plan=False)
        
class BckBedroom(Bck):
    def __init__(self):
        super().__init__("BckBedroom")

class BckHouse(Bck):
    def __init__(self):
        super().__init__("BckHouse")

class ArrowPrompt(GameSprite):
    def __init__(self):
        super().__init__("ArrowPrompt", frames=4)
        self.Animate = False

class ArrowMenuSelect(GameSprite):
    def __init__(self):
        super().__init__("ArrowMenuSelect")

class Alert(GameSprite):
    def __init__(self):
        super().__init__("Alert")

class GuiChest(GameSprite):
    def __init__(self):
        super().__init__("GuiChest")

class GuiChestBar(GameSprite):
    def __init__(self):
        super().__init__("GuiChestBar")

class Player(GameSprite):
    def __init__(self):
        super().__init__("Player", rectCollision=pygame.Rect(1, 13, 10, 6))

class PlayerPirate(GameSprite):
    def __init__(self):
        super().__init__("PlayerPirate", rectCollision=pygame.Rect(1, 13, 10, 6))

class Pirate1(GameSprite):
    def __init__(self):
        super().__init__("Pirate1", rectCollision=pygame.Rect(1, 13, 10, 6))

class Pirate2(GameSprite):
    def __init__(self):
        super().__init__("Pirate2", rectCollision=pygame.Rect(1, 13, 10, 6))
        
class PlayerBatMan(GameSprite):
    def __init__(self):
        super().__init__("PlayerBatMan")

class PlayerCaptainAmerica(GameSprite):
    def __init__(self):
        super().__init__("PlayerCaptainAmerica")

class PlayerIronMan(GameSprite):
    def __init__(self):
        super().__init__("PlayerIronMan")

class PlayerSpiderMan(GameSprite):
    def __init__(self):
        super().__init__("PlayerSpiderMan")

class PlayerZombie(GameSprite):
    def __init__(self):
        super().__init__("PlayerZombie")

class PlayerMoana(GameSprite):
    def __init__(self):
        super().__init__("PlayerMoana")
        
class PlayerMaui(GameSprite):
    def __init__(self):
        super().__init__("PlayerMaui")

class Mum(GameSprite):
    def __init__(self):
        super().__init__("Mum")

class CircleVision(GameSprite):
    def __init__(self):
        super().__init__("CircleVision")

class Orb(GameSprite):
    def __init__(self, colour):
        super().__init__("Orb"+colour)

class OrbRed(Orb):
    def __init__(self):
        super().__init__("Red")

class OrbYellow(Orb):
    def __init__(self):
        super().__init__("Yellow")

class OrbGreen(Orb):
    def __init__(self):
        super().__init__("Green")

class OrbBlue(Orb):
    def __init__(self):
        super().__init__("Blue")

class OrbGrey(Orb):
    def __init__(self):
        super().__init__("Grey")

class Sword(GameSprite):
    def __init__(self, colour):
        super().__init__("Sword"+colour)

class SwordRed(Sword):
    def __init__(self):
        super().__init__("Red")

class SwordYellow(Sword):
    def __init__(self):
        super().__init__("Yellow")

class SwordGreen(Sword):
    def __init__(self):
        super().__init__("Green")

class SwordBlue(Sword):
    def __init__(self):
        super().__init__("Blue")

class SwordGrey(Sword):
    def __init__(self):
        super().__init__("Grey")

class LockOn(GameSprite):
    def __init__(self):
        super().__init__("LockOn", frames=2)
        self.Animate = False

class Croissant(GameSprite):
    def __init__(self, colour):
        super().__init__("Croissant"+colour, rectCollision=pygame.Rect(0, 8, 14, 4))

class CroissantRed(Croissant):
    def __init__(self):
        super().__init__("Red")

class CroissantOrange(Croissant):
    def __init__(self):
        super().__init__("Orange")

class Boat(GameSprite):
    def __init__(self):
        super().__init__("Boat")

class Radio(GameSprite):
    def __init__(self):
        super().__init__("Radio")

class RadioEnemy(GameSprite):
    def __init__(self):
        super().__init__("RadioEnemy")

class Coin(GameSprite):
    def __init__(self):
        super().__init__("Coin")

class Coins(GameSprite):
    def __init__(self):
        super().__init__("Coins")

class Bridge(GameSprite):
    def __init__(self):
        super().__init__("Bridge", frames=2)
        self.Animate = False

class Map(GameSprite):
    def __init__(self):
        super().__init__("Map")

class MapKey(GameSprite):
    def __init__(self):
        super().__init__("MapKey")
        
class MapCollectable(GameSprite):
    def __init__(self):
        super().__init__("MapCollectable")

class Box(GameSprite):
    def __init__(self):
        super().__init__("Box")

class Bed(GameSprite):
    def __init__(self):
        super().__init__("Bed")
        
class BedParents(GameSprite):
    def __init__(self):
        super().__init__("BedParents")

class Table(GameSprite):
    def __init__(self):
        super().__init__("Table")

class TableBig(GameSprite):
    def __init__(self):
        super().__init__("TableBig")

class Wardrobe(GameSprite):
    def __init__(self):
        super().__init__("Wardrobe")

class Ball(GameSprite):
    def __init__(self):
        super().__init__("Ball")

class Carpet(GameSprite):
    def __init__(self):
        super().__init__("Carpet")
        self.Fantasy.SetFramesMax(2)
        self.Fantasy.Animate = False

class Bath(GameSprite):
    def __init__(self, name="Bath"):
        super().__init__(name)

class BathParents(Bath):
    def __init__(self):
        super().__init__("BathParents")

class BathMat(GameSprite):
    def __init__(self):
        super().__init__("BathMat")

class BathMatParents(GameSprite):
    def __init__(self):
        super().__init__("BathMatParents")

class Toilet(GameSprite):
    def __init__(self):
        super().__init__("Toilet")

class Taps(GameSprite):
    def __init__(self):
        super().__init__("Taps")

class Mirror(GameSprite):
    def __init__(self):
        super().__init__("Mirror")

class TeddyBear(GameSprite):
    def __init__(self):
        super().__init__("TeddyBear")

class Pirate1Bridge(GameSprite):
    def __init__(self):
        super().__init__("Pirate1Bridge")

class Plant(GameSprite):
    def __init__(self):
        super().__init__("Plant")

class Coconut(GameSprite):
    def __init__(self):
        super().__init__("Coconut")

class Fireplace(GameSprite):
    def __init__(self):
        super().__init__("Fireplace")

class Wind(GameSprite):
    def __init__(self):
        super().__init__("Wind")

class DiscoFloor(GameSprite):
    def __init__(self):
        super().__init__("DiscoFloor", frames=3, frameRate=4)

class GuiBackground(GameSprite):
    def __init__(self):
        super().__init__("GuiBackground", frames=2)
        self.Animate = False

class GuiBar(GameSprite):
    def __init__(self):
        super().__init__("GuiBar", frames=2)
        self.Animate = False

class GuiIcon(GameSprite):
    def __init__(self):
        super().__init__("GuiIcon", frames=2)
        self.Animate = False

class EnemySpawn(GameSprite):
    def __init__(self):
        super().__init__("EnemySpawn")
