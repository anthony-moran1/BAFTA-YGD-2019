from Modules.Lifeform import *
import Modules.Wall, Modules.Ball, Modules.SpeechBubble

class Player(Lifeform):
    def __init__(self):
        super().__init__()
        self.Name = "Player"
        self.SetSprite(Modules.GameSprite.PlayerPirate())

        self.lkOriginal = self.lk = pygame.K_LEFT
        self.rkOriginal = self.rk = pygame.K_RIGHT
        self.ukOriginal = self.uk = pygame.K_UP
        self.dkOrigianl = self.dk = pygame.K_DOWN

        self.fantasyKey = pygame.K_q
        self.ItemKey = pygame.K_SPACE
        
        self.hspdOriginal = self.vspdOriginal = self.hspd = self.vspd = 7
        self.xMove = self.yMove = 0

        self.Items = []
        self.ItemsFollow = []
        self.LockOn = None

        self.Map = None

    def Update(self):
        if not self.UPDATE:
            return
        super().Update()
        self.UpdateInput()

        if self.INPUT:
            xDir = Modules.Event.GetKey(self.rk)-Modules.Event.GetKey(self.lk)
            yDir = Modules.Event.GetKey(self.dk)-Modules.Event.GetKey(self.uk)
            self.xMove = xDir*self.hspd
            self.yMove = yDir*self.vspd

            self.Move(self.xMove, 0)
            self.Move(0, self.yMove)

        self.UpdateFollowItems()

        if self == Modules.Object.GetObjectVar({"Name":"Camera"}).target:
            self.KeepOnScreen()

        self.InteractControl()

        if Modules.Control.Fantasy:
            for Item in self.Items:
                if not Item.target:
                    Item.dest = (self.rect.centerx+Item.rectOffset.centerx,
                                self.rect.centery+Item.rectOffset.centery)
        else:
            for Item in self.Items:
                if Item.target:
                    Item.NoTarget()
                Item.rect.center = (self.rect.centerx+Item.rectOffset.centerx,
                                   self.rect.centery+Item.rectOffset.centery)

        self.LockOnControl()

        if Modules.Event.GetKeyPressed(self.ItemKey) and self.LockOn.target:
            Modules.SpeechBubble.ResetSpeech()

##        if Event.GetKeyPressed(pygame.K_1):
##            self.SetSprite(GameSprite.Player())
##        elif Event.GetKeyPressed(pygame.K_2):
##            self.SetSprite(GameSprite.PlayerBatMan())
##        elif Event.GetKeyPressed(pygame.K_3):
##            self.SetSprite(GameSprite.PlayerCaptainAmerica())
##        elif Event.GetKeyPressed(pygame.K_4):
##            self.SetSprite(GameSprite.PlayerIronMan())
##        elif Event.GetKeyPressed(pygame.K_5):
##            self.SetSprite(GameSprite.PlayerSpiderMan())
##        elif Event.GetKeyPressed(pygame.K_6):
##            self.SetSprite(GameSprite.PlayerMoana())
##        elif Event.GetKeyPressed(pygame.K_7):
##            self.SetSprite(GameSprite.PlayerMaui())

        if Modules.Event.GetKeyPressed(pygame.K_p):
            self.AddFollowItem(Modules.Ball.Ball())

    def UpdateInput(self):
##        if Modules.Object.GetObjectVar({"Name":"SpeechBubble"}):
##            self.INPUT = False
##            return
        self.INPUT = True

    def AddItem(self, Item):
        Item.Add()
        self.Items.append(Item)

        radius = max(self.Sprite.sprite.get_size())*1.1
        for i in range(len(self.Items)):
            angle = (math.pi*2)*(i/len(self.Items))
            x = math.sin(angle)*radius
            y = math.cos(angle)*radius
            self.Items[i].rectOffset.center = (x, y)

    def AddRandomItem(self, itemType):
        options = [itemType.Red,
                   itemType.Yellow,
                   itemType.Green,
                   itemType.Blue]
        item = random.choice(options)()
        self.AddItem(item)

    def RemoveRandomItem(self):
        index = random.randint(0, len(self.Items)-1)
        item = self.Items[index]
        
        self.Items.remove(item)
        item.Remove()

    def AddFollowItem(self, item):
        item.Solid = False
        item.Add()
        self.ItemsFollow.append(item)
        if hasattr(item, "AddFollowFunc"):
            item.AddFollowFunc()

    def RemoveFollowItem(self, name):
        objectRemove = None
        for obj in self.ItemsFollow:
            if obj.Name == name:
                objectRemove = obj
                break
        if not objectRemove:
            return
        self.ItemsFollow.remove(objectRemove)
        if hasattr(objectRemove, "RemoveFollowFunc"):
            objectRemove.RemoveFollowFunc()

    def CheckFollowItemExists(self, itemName):
        for obj in self.ItemsFollow:
            if obj.Name == itemName:
                return True
        return False

    def UpdateFollowItems(self):
        for item in self.ItemsFollow:
            index = self.ItemsFollow.index(item)
            if index == 0:
                objectFollow = self
            else:
                objectFollow = self.ItemsFollow[index-1]
            dest = objectFollow.rect.center
            
            xDir = dest[0]-item.rect.centerx
            yDir = dest[1]-item.rect.centery

            if abs(xDir) < 20:
                xDir = 0
            if abs(yDir) < 20:
                yDir = 0

            if item.CheckCollide(objectFollow) or abs(xDir) < 20 and  abs(yDir) < 20:
                continue
            
            xMove = (xDir)*.1
            yMove = (yDir)*.1
            item.rect.centerx += xMove
            item.rect.centery += yMove

    def ItemDeployControl(self):
        if not(Modules.Event.GetKeyPressed(self.ItemKey) and Modules.Control.Fantasy and self.LockOn.target):
            return
        
        possibleItems = []
        for Item in self.Items:
            if not Item.canUse:
                continue
            possibleItems.append(Item)
        if len(possibleItems) == 0:
            return
        
        close = None
        for Item in possibleItems:
            if close == None:
                close = Item
                continue
            d1 = Modules.Function.dist(Item.rect.center, self.LockOn.target.rect.center)
            d2 = Modules.Function.dist(close.rect.center, self.LockOn.target.rect.center)
            if d1 < d2:
                close = Item

        close.SetTarget(self.LockOn.target)

    def InteractControl(self):
        if not self.INPUT:
            return
        
        if Modules.Control.Fantasy:
            self.ItemDeployControl()
            return
        
        if not Modules.Event.GetKeyPressed(self.ItemKey) or not self.LockOn.target:
            return
        self.LockOn.target.PlayerItemFunc()

    def GetLockOnTargetsAvoid(self):
        return Modules.Object.GetObjectsVar({"PLAYERITEMFUNC":False})

    def LockOnControl(self):
        if self.LockOn.LOCK:
            return
            
        closest = None
        for o in Modules.Object.GetObjectsButs(self.GetLockOnTargetsAvoid()):
            if not self.LockOn.CheckValidTarget(o):
                continue
            if closest == None:
                closest = o
                continue
            
            d1 = Modules.Function.dist(self.rect.center, o.rect.center)
            d2 = Modules.Function.dist(self.rect.center, closest.rect.center)
            if d1 < d2:
                closest = o
                
        if closest == None:
            self.LockOn.NoTarget()
            return

        if closest == self.LockOn.target:
            return
        self.LockOn.SetTarget(closest)
