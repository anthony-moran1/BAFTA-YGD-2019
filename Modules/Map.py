from Modules.GameObject import *
import Modules.Background

class Map(GameObject):
    def Add(self):
        Modules.Control.AddFantasyObject(self)

    def Remove(self):
        Modules.Control.RemoveFantasyObject(self)
        
    def __init__(self):
        super().__init__()
        self.SetSprite(Modules.GameSprite.Map())
        self.SpriteKey = Modules.GameSprite.MapKey()
        self.depthLayer = "Gui"

        self.Solid = False
        self.CanCollide = False
        
        sw, sh = Modules.Basic.GetScreenSize()
        self.rect.center = (sw//2, sh//2)

        self.showKey = pygame.K_m

        self.roomCenters = {
            "StudyRoom":Modules.Background.GetPosBackground((376, 94)),
            "LivingRoom":Modules.Background.GetPosBackground((376, 508)),
            "BedroomParents":Modules.Background.GetPosBackground((96, 255)),
            "ToyRoom":Modules.Background.GetPosBackground((376, 252)),
            "DiningRoom":Modules.Background.GetPosBackground((218, 666))
            }

        self.surf = pygame.Surface(self.Sprite.frameRect.size, pygame.SRCALPHA)
        self.pointSize = 4
        self.points = []

        self.colourPlayer = (0,0,255)

        self.rectMiniMap = pygame.Rect((0,0), (self.rect.w/2,
                                               self.rect.w/2))
        self.rectMiniMap.topright = (Modules.Basic.GetScreenSize()[0]-8, 8)

        self.rectMiniMapShow = pygame.Rect(self.rectMiniMap)

        self.SHOWFULL = False

    def Update(self):
        self.SHOWFULL = Modules.Event.GetKey(self.showKey) and Modules.Object.GetObjectVar({"Name":"Player"}).Map
        super().Update()
        if not self.UPDATE:
            return

        player = Modules.Object.GetObjectVar({"Name":"Player"})
        self.posPlayer = self.GetPosMap(player.rect.center)

        self.rectMiniMapShow.center = self.posPlayer

    def Show(self):        
        if not self.SHOW:
            return
        self.surf.blit(self.Sprite.sprite, (0,0))
        
        pygame.draw.rect(self.surf, self.colourPlayer, pygame.Rect(self.posPlayer, (self.pointSize*2,
                                                                                    self.pointSize*2)))
        for point in self.points:
            topleft = self.GetPosMap(point[1])
            size = (self.pointSize*2, self.pointSize*2)
            pygame.draw.rect(self.surf, point[0], pygame.Rect(topleft, size))
        
        Modules.Basic.GetScreen().blit(self.surf, self.rectMiniMap.topleft,
                                       self.rectMiniMapShow)
        pygame.draw.rect(Modules.Basic.GetScreen(), (0,0,0), self.rectMiniMap, 1)

        if not self.SHOWFULL:
            return
        
        Modules.Basic.GetScreen().blit(self.surf, self.rect.topleft)
        Modules.Basic.GetScreen().blit(self.SpriteKey.sprite, (self.rect.right+8,
                                                               self.rect.top))

    def AddPoint(self, colour, where):
        self.points.append((colour, where))

    def AddEnemyBase(self, room):
        self.AddPoint((255,0,0), self.roomCenters[room])

    def AddChallenger(self, room):
        self.AddPoint((0,255,255), self.roomCenters[room])

    def AddTreasure(self, room):
        self.AddPoint((255,255,0), self.roomCenters[room])

    def GetPosMap(self, pos):
        sw, sh = Modules.Background.BackgroundSize()
        px = pos[0]/sw*(self.rect.w-4*self.Sprite.scale)
        py = pos[1]/sh*(self.rect.h-4*self.Sprite.scale)
        posNew = (px-self.pointSize+2*self.Sprite.scale,
                  py-self.pointSize+2*self.Sprite.scale)
        return posNew
