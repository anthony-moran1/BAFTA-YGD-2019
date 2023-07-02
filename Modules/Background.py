from Modules.GameObject import *
import Modules.Wall

class Background(GameObject):
    def __init__(self):
        super().__init__()
        self.Name = "Background"
        self.depthLayer = "Bck"

        self.Solid = False
        self.Fantasy = Modules.Control.Fantasy

        self.Walls = []

    def Update(self):
        super().Update()
        if self.Fantasy != Modules.Control.Fantasy:
            self.UpdateCollision()
            self.Fantasy = Modules.Control.Fantasy

    def SetSprite(self, sprite):
        super().SetSprite(sprite)
        self.UpdateCollision()

    def UpdateCollision(self):
        for wall in self.Walls:
            wall.Remove()
        self.Walls = []

        if Modules.Control.Fantasy:
            sprite = self.Sprite.Fantasy
        else:
            sprite = self.Sprite
        if not hasattr(sprite, "plan"):
            return
        
        plan = sprite.plan.sprite

        w, h = plan.get_size()
        wallx = wally = wallw = wallh = 0
        for x in range(w-1):
            for y in range(h-1):
                col = plan.get_at((x, y))
                if col[:3] != (255,255,0):
                    continue
                right = plan.get_at((x+1, y))
                bottom = plan.get_at((x, y+1))
                if right[:3] != (255,0,0) or bottom[:3] != (255,0,0):
                    continue
                wallx, wally = x, y
                wallw = wallh = self.Sprite.scale
                for xx in range(wallx+1, w):
                    col = plan.get_at((xx, wally))
                    if col[:3] != (255,0,0):
                        break
                    wallw += self.Sprite.scale
                    if col[:3] == (255,255,0) or col[:3] == (0,255,0):
                        break
                for yy in range(wally+1, h):
                    col = plan.get_at((wallx, yy))
                    if col[:3] != (255,0,0):
                        break
                    wallh += self.Sprite.scale
                    if col[:3] == (255,255,0) or col[:3] == (0,255,0):
                        break
                wall = Modules.Wall.Wall((wallw, wallh))
                wallx, wally = wallx*self.Sprite.scale, wally*self.Sprite.scale
                wall.rect.topleft = (wallx, wally)
                wall.Add()
                self.Walls.append(wall)

def GetBackground():
    return Modules.Object.GetObjectVar({"Name":"Background"})

def BackgroundSize():
    return GetBackground().rect.size

def GetPosBackground(pos):
    scale = GetBackground().Sprite.scale
    x = pos[0]*scale
    y = pos[1]*scale
    return (x, y)
