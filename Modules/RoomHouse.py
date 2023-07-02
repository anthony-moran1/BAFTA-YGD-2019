from Modules.Room import *
import Modules.Fireplace

def GetObjectsBeforeAfter(Before, After):
    for obj in Before:
        After.remove(obj)
    return After

class room(Room):
    def __init__(self):
        super().__init__()
        Modules.Background.GetBackground().SetSprite(Modules.GameSprite.BckHouse())
        player = Modules.Object.GetObjectVar({"Name":"Player"})
        player.rect.topleft = Modules.Background.GetPosBackground((107, 115))

        #Furniture
        #BedroomChild
        Add(Modules.Bed.Bed(), (102, 68))
        Add(Modules.Table.Table(), (77, 68))
        Add(Modules.Radio.Radio(), (83, 74))
        Add(Modules.Wardrobe.Wardrobe(), (39, 51))
        Add(Modules.Ball.Ball(), (139, 140))

        #BathroomChild
        Modules.BathBathMat.BathBathMat((197, 105), (203, 135))
        Add(Modules.Toilet.Toilet(), (255, 54))
        Add(Modules.Taps.Taps(), (231, 64))
        Add(Modules.Mirror.Mirror(), (229, 45))

        #BedroomParents
        tempObjectsBefore = Modules.Object.GetObjects()
        Add(Modules.Bed.BedParents(), (71, 226))
        Add(Modules.Table.Table(), (36, 284))
        Add(Modules.Table.Table(), (128, 284))
        Add(Modules.Wardrobe.Wardrobe(), (36, 205))
        Add(Modules.Wardrobe.Wardrobe(), (119, 205))
        tempObjectsAfter = Modules.Object.GetObjects()
        ObjectsBedroomParents = GetObjectsBeforeAfter(tempObjectsBefore,
                                                      tempObjectsAfter)
        
        #BathroomParents
        Modules.BathBathMat.BathBathMatParents((197, 263), (203, 293))
        Add(Modules.Toilet.Toilet(), (255, 212))
        Add(Modules.Taps.Taps(), (231, 222))
        Add(Modules.Mirror.Mirror(), (229, 203))

        #ToyRoom
        Add(Modules.Pirate1.Pirate1(), (384, 241))
        Add(Modules.TeddyBear.TeddyBear(), (400, 234))
        Add(Modules.Pirate1Bridge.Pirate1Bridge(), (370, 232))

        #LivingRoom
        Add(Modules.Fireplace.Fireplace(), (361, 464))
        pos = [(322, 541),(322, 572),(322, 643),(322, 674),
               (412, 541),(412, 572),(412, 643),(412, 674)]
        for p in pos:
            Add(Modules.Plant.Plant(), p)

        #StudyRoom
        tempObjectsBefore = Modules.Object.GetObjects()
        Add(Modules.Table.TableBig(), (349, 68))
        Add(Modules.Carpet.Carpet(), (353, 103))
        tempObjectsAfter = Modules.Object.GetObjects()
        ObjectsStudyRoom = GetObjectsBeforeAfter(tempObjectsBefore,
                                                 tempObjectsAfter)

        #PartyRoom
        Add(Modules.DiscoFloor.DiscoFloor(), (118, 486))
        Add(Modules.Pirate2.Pirate2(), (103, 543))

        Modules.BoatBox.BoatBox((141, 569), (169, 570),
                                (150, 571), (150, 550)).Add()

        #DiningRoom
        Add(Modules.Coins.Coins(), (205, 650))

        Modules.BoatBox.BoatBox((203, 727), (231, 728),
                                (212, 729), (212, 708)).Add()

        #Kitchen
        kitchenWalls = [Modules.Wall.WallGood((75, 727), (104, 728)),
                        Modules.Wall.WallGood((155, 667), (156, 696))]
        for wall in kitchenWalls:
            wall.Add()
        def KitchenPromptCheck():
            for wall in kitchenWalls:
                dist = Modules.Function.dist(Modules.Control.Player().rect.center,
                                             wall.rect.center)
                if dist < 96:
                    return True
        def KitchenPrompt():
            Modules.Control.Player().Speak("Mummy is in there, I better stay away or I'll be caught!")
        Modules.Timer.Check(KitchenPromptCheck,
                            KitchenPrompt).Add()
        
        #House
        def RevealBottomFloorCheck():
            if not Modules.Control.BedroomParentsComplete:
                return False
            if not Modules.Control.StudyRoomComplete:
                return False
            if not Modules.Control.Pirate1QuestFinished:
                return False
            return True
        tempWall = Modules.Wall.WallTemp((281, 346), (312, 346), RevealBottomFloorCheck)
        tempWall.Add()

        def CompleteTopFloorPromptCheck():
            dist = Modules.Function.dist(Modules.Control.Player().rect.center,
                                         tempWall.rect.center)
            return dist < 64
        def CompleteTopFloorPrompt():
            Modules.Control.Player().Speak("I should complete all the activites on the top floor before descending")
        CompleteTopFloorCheck = Modules.Timer.Check(CompleteTopFloorPromptCheck,
                                                    CompleteTopFloorPrompt)
        CompleteTopFloorCheck.Add()
        def CompleteTopFloorPromptInterrupt():
            CompleteTopFloorCheck.Remove()
            Modules.Control.Player().Speak("I have finished all of the requirements from the top floor, time to descend!")
        Modules.Timer.Check(RevealBottomFloorCheck,
                            CompleteTopFloorPromptInterrupt).Add()

        #Fantasy
        #Bedroom Child
        Add(Modules.MapCollectable.MapCollectable(), (132, 68))
        Modules.BoatBox.BoatBox((155, 95), (156, 124), (157, 100), (143, 100)).Add()
        Modules.BoatBox.BoatBox((75, 155), (104, 156), (84, 157), (84, 136)).Add()

        #Bedroom Parents
        def EnemyBaseBedroomParentsStart(player):
            for obj in ObjectsBedroomParents:
                obj.Remove()
            Enemies = [Modules.Croissant.Red() for i in range(8)]
            Boxes = []

            def BoxTimer():
                boxes = Modules.Object.GetObjectsVar({"Name":"Box"})
                if len(boxes) == 0:
                    return
                box = random.choice(boxes)
                box.Open()
                Modules.Timer.Timer(2, BoxTimer).Add()
            player.Speak("No surpise that the croissant monsters would camp on hot sand beach",
                         lambda:Modules.Timer.Timer(3, BoxTimer).Add())            
            
            radius = 60*Modules.Background.GetBackground().Sprite.scale-Modules.Box.Box().rect.h//2
            for i in range(8):
                if i == 2:
                    continue
                angle = math.pi*2*(i/8)
                x, y = Modules.Background.GetPosBackground((96, 255))
                x += math.cos(angle)*radius
                y += math.sin(angle)*radius
                
                box = Modules.Box.Box()
                box.AssignItem(Enemies[i])
                box.rect.center = (x, y)
                box.Add()
                Boxes.append(box)

                Modules.Timer.Timer(5+i*2, BoxTimer).Add()

            def EnemyCheck():
                return Modules.Object.GetObjectVar({"Name":"Enemy"})
            def Enemy():
                player.Speak("A croissant monster!")
            Modules.Timer.Check(EnemyCheck, Enemy).Add()

            def FinishCheck():
                Objects = [Enemies, Boxes]
                for objects in Objects:
                    for obj in objects:
                        if obj in Modules.Object.GetObjects():
                            return False
                return True
            def Finish():
                for obj in ObjectsBedroomParents:
                    obj.Add()
                player.SetPosition((84, 286))
                player.Speak("Well done crew! We removed an Enemy Base!")
                player.AddRandomItem(Modules.Sword)
                Modules.Control.BedroomParentsComplete = True
            Modules.Timer.Check(FinishCheck, Finish).Add()
            Modules.Wall.WallTemp((74, 312), (105, 313), FinishCheck).Add()
            Modules.Wall.WallTemp((154, 252), (155, 283), FinishCheck).Add()
        enemyBaseBedroomParentsStartTrigger = Modules.CollisionBox.CollisionBox((60, 284), (127, 300), EnemyBaseBedroomParentsStart)
        enemyBaseBedroomParentsStartTrigger.Add = lambda:Modules.Control.AddFantasyObject(enemyBaseBedroomParentsStartTrigger)
        enemyBaseBedroomParentsStartTrigger.Remove = lambda:Modules.Control.RemoveFantasyObject(enemyBaseBedroomParentsStartTrigger)
        enemyBaseBedroomParentsStartTrigger.Add()
        
        Modules.BoatBox.BoatBox((155, 253), (156, 282), (157, 258), (143, 258)).Add()
        Modules.BoatBox.BoatBox((75, 313), (104, 314), (84, 315), (83, 294)).Add()

        #LivingRoom
        walls = [Modules.Wall.WallFantasy((6, 278)),
                 Modules.Wall.WallFantasy((6, 278))]
        posWalls = [(353, 448), (393, 448)]
        for wall in walls:            
            wall.SetPosition(posWalls[walls.index(wall)])
            wall.Add()

        #StudyRoom
        def EnemyBaseStudyRoomStart(player):
            for obj in ObjectsStudyRoom:
                obj.Remove()
            Enemies = [Modules.Croissant.Red() for i in range(5)]
            Boxes = []

            def BoxTimer():
                boxes = Modules.Object.GetObjectsVar({"Name":"Box"})
                if len(boxes) == 0:
                    return
                box = random.choice(boxes)
                box.Open()
                Modules.Timer.Timer(2, BoxTimer).Add()
            player.Speak("This cave is no match to my power!",
                         lambda:Modules.Timer.Timer(3, BoxTimer).Add())            
            
            radius = 60*Modules.Background.GetBackground().Sprite.scale-Modules.Box.Box().rect.h//2
            for i in range(len(Enemies)):
                angle = math.pi*2*(i/5)+math.pi/4
                x, y = Modules.Background.GetPosBackground((376, 94))
                x += math.cos(angle)*radius
                y += math.sin(angle)*radius
                
                box = Modules.Box.Box()
                box.AssignItem(Enemies[i])
                box.rect.center = (x, y)
                box.Add()
                Boxes.append(box)

                Modules.Timer.Timer(5+i*2, BoxTimer).Add()

            def EnemyCheck():
                return Modules.Object.GetObjectVar({"Name":"Enemy"})
            def Enemy():
                player.Speak("Attack!")
            Modules.Timer.Check(EnemyCheck, Enemy).Add()

            def FinishCheck():
                Objects = [Enemies, Boxes]
                for objects in Objects:
                    for obj in objects:
                        if obj in Modules.Object.GetObjects():
                            return False
                return True
            def Finish():
                for obj in ObjectsStudyRoom:
                    obj.Add()
                player.SetPosition((371, 128))
                player.Speak("Well done crew! We removed an Enemy Base!")
                player.AddRandomItem(Modules.Sword)
                Modules.Control.StudyRoomComplete = True
            Modules.Timer.Check(FinishCheck, Finish).Add()
            Modules.Wall.WallTemp((74, 312), (105, 313), FinishCheck).Add()
            Modules.Wall.WallTemp((154, 252), (155, 283), FinishCheck).Add()
        enemyBaseStudyRoomStartTrigger = Modules.CollisionBox.CollisionBox((316, 34), (435, 153), EnemyBaseStudyRoomStart)
        enemyBaseStudyRoomStartTrigger.Add = lambda:Modules.Control.AddFantasyObject(enemyBaseStudyRoomStartTrigger)
        enemyBaseStudyRoomStartTrigger.Remove = lambda:Modules.Control.RemoveFantasyObject(enemyBaseStudyRoomStartTrigger)
        enemyBaseStudyRoomStartTrigger.Add()

        Modules.BoatBox.BoatBox((361, 155),(390, 156),
                                (370, 157),(370, 136)).Add()
            
        #Tutorial
        mum = Modules.Mum.Mum()
        Add(mum, (121, 113))
        mum.Speak("Good morning Noah, how are you today?")
        player.Speak("Is it morning already?")
        mum.Speak("Yes! Now it is time to get ready for school, you can start by having a wash", lambda:mum.SetPosition((83, 681)))

        bathWall = Modules.Wall.Wall(Modules.Background.GetPosBackground((30, 2)))
        bathWall.rect.topleft = Modules.Background.GetPosBackground((75, 155))
        bathWall.Add()
        def RemoveBathWallCheck():
            return Modules.Control.Fantasy
        def RemoveBathWall():
            bathWall.Remove()
        Modules.Timer.Check(RemoveBathWallCheck,
                            RemoveBathWall).Add()

        def StartGotoBathroomPrompt():
            def MoveTutorialPrompt():
                player.Speak("Hey there! Use the arrow keys to move around!")
            moveTutorial = Modules.Timer.Timer(3, MoveTutorialPrompt)
            moveTutorial.Add()

            def MoveTutorialPromptInteruptCheck():
                return player.xMove != 0 or player.yMove != 0
            def MoveTutorialPromptInterupt():
                moveTutorial.Remove()
            Modules.Timer.Check(MoveTutorialPromptInteruptCheck,
                                MoveTutorialPromptInterupt).Add()
        
            def GotoBathroomPrompt():
                player.Speak("It's getting pretty late, I better go and have a wash")
            gotoBathroomPromptTimer = Modules.Timer.Timer(10, GotoBathroomPrompt)
            gotoBathroomPromptTimer.Add()
            def RemoveGotoBathroomTimerCheck():
                if not player.LockOn.target:
                    return False
                return player.LockOn.target.Name == "Bath"
            def RemoveGotoBathroomTimer():
                gotoBathroomPromptTimer.Remove()
            Modules.Timer.Check(RemoveGotoBathroomTimerCheck,
                                RemoveGotoBathroomTimer).Add()
        player.Speak("*Yawns*... Bath time!!", StartGotoBathroomPrompt)

        def BathPromptCheck():
            if not player.LockOn.target:
                return False
            return player.LockOn.target.Name == "Bath"
        def BathPrompt():
            player.Speak("It's time to get into the bath or what I like to call...")
            player.Speak("My Pirate Ship!!")
        Modules.Timer.Check(BathPromptCheck, BathPrompt).Add()

        def PirateStartCheck():
            return Modules.Control.Fantasy
        def PirateStart():
            player.Speak("Ahoy there me mateys, do you like my ship?")
            player.Speak("Our adventure awaits! We better sail to the shores!")
        Modules.Timer.Check(PirateStartCheck, PirateStart).Add()

        def MapPromptCheck():
            if not Modules.Control.Fantasy:
                return False
            mp = Modules.Object.GetObjectVar({"Name":"MapCollectable"})
            return player.LockOn.target == mp
        def MapPrompt():
            player.Speak("This map could be helpful, I better grab it!")
        Modules.Timer.Check(MapPromptCheck,
                            MapPrompt).Add()

        def MapTutorialCheck():
            return player.Map
        def MapTutorial():
            player.Speak("By holding the M Key I can view this map and see where I need to go")
        Modules.Timer.Check(MapTutorialCheck,
                            MapTutorial).Add()
