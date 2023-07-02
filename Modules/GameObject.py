import pygame, math, random
import Modules.Basic, Modules.Event, Modules.Object, Modules.Audio
import Modules.Function, Modules.Control, Modules.Background, Modules.GameSprite

class GameObject:
    def Add(self):
        Modules.Object.AddObject(self)

    def Remove(self):
        Modules.Object.RemoveObject(self)
        
    def __init__(self):
        self.Name = ""
        self.UPDATE = True
        self.SHOW = True
        self.Perisis = False

        self.PLAYERITEMFUNC = False
        self.Fantasy = False
        self.Solid = True
        self.CanCollide = True
        
        self.Sprite = None
        self.rect = pygame.Rect(0,0,0,0)
        self.rectCollision = pygame.Rect(self.rect)
        self.posCam = self.rect.topleft

        self.depth = 0
        self.depthLayer = "Mid"

    def Update(self):
        if not self.UPDATE:
            return

        self.UpdateRectCollision()
        self.posCam = Modules.Object.GetObjectVar({"Name":"Camera"}).GetPosCam(self.rect.topleft)
        self.depth = self.rect.bottom

    def Show(self):
        if Modules.Control.DEBUGGING:
            pygame.draw.rect(Modules.Basic.GetScreen(), (0,255,0), (Modules.Object.GetObjectVar({"Name":"Camera"}).GetPosCam(self.rectCollision.topleft),
                                                            self.rectCollision.size), 1)
        if self.Sprite == None or not self.SHOW:
            return
        
        if Modules.Control.Fantasy:
            sprite = self.Sprite.Fantasy
        else:
            sprite = self.Sprite
        sprite.Update()
        Modules.Basic.GetScreen().blit(sprite.sprite, self.posCam, sprite.frameRect)

    def UpdateRectCollision(self):
        if self.Sprite:
            self.rectCollision.x = self.Sprite.rectCollision.x+self.rect.x
            self.rectCollision.y = self.Sprite.rectCollision.y+self.rect.y

    def SetSprite(self, sprite):
        if self.Sprite != None:
            if self.Sprite.name == sprite.name:
                return 0
        self.Sprite = sprite
        self.rect.size = self.Sprite.frameRect.size
        
        self.rectCollision = pygame.Rect(self.Sprite.rectCollision)
        self.rectCollision.x += self.rect.x
        self.rectCollision.y += self.rect.y

    def SetPosition(self, pos):
        self.rect.topleft = Modules.Background.GetPosBackground(pos)

    def CheckCollide(self, o, mustBeSolid=True):
        if mustBeSolid and not o.Solid or not self.CanCollide:
            return False
        self.UpdateRectCollision()
        o.UpdateRectCollision()
        return self.rectCollision.colliderect(o.rectCollision)

    def CheckCollideAnything(self, mustBeSolid=True):
        for o in Modules.Object.GetObjectsBut(self):
            if self.CheckCollide(o, mustBeSolid):
                return True
        return False

    def Move(self, x, y):
        if x == 0 and y == 0:
            return
        
        mx = max(abs(x), abs(y))
        xMove = Modules.Function.sign(x)
        yMove = Modules.Function.sign(y)
        
        for i in range(mx):
            self.rect.x += xMove
            self.rect.y += yMove
            if self.CheckCollideAnything():
                self.rect.x -= xMove
                self.rect.y -= yMove
                break

    def UnStick(self):
        for o in Modules.Object.GetObjectsBut(self):
            if not self.CheckCollide(o):
                continue
            xDif = self.rectCollision.centerx-o.rectCollision.centerx
            yDif = self.rectCollision.centery-o.rectCollision.centery
            if xDif == 0 and yDif == 0:
                xDif = random.choice([-1, 1])
                yDif = random.choice([-1, 1])
            self.rect.x += Modules.Function.sign(xDif)
            self.rect.y += Modules.Function.sign(yDif)

    def KeepOnScreen(self):
        sw, sh = Modules.Basic.GetScreenSize()
        left = self.posCam[0]
        right = self.posCam[0]+self.rect.w
        top = self.posCam[1]
        bottom = self.posCam[1]+self.rect.h
        
        if left < 0:
            self.rect.left -= left
        if right > sw:
            self.rect.right -= right-sw

        if top < 0:
            self.rect.top -= top
        if bottom > sh:
            self.rect.bottom -= bottom-sh

    def KeepOnRoom(self):
        rw, rh = Modules.Object.GetObjectVar({"Name":"Background"}).Sprite.frameRect.size

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > rw:
            self.rect.right = rw
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > rh:
            self.rect.bottom = rh

    def PlayerItemFunc(self):
        pass
