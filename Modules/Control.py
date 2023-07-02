import pygame
import Modules.Object

def Debug(txt):
    if not DEBUGGING:
        return
    print(txt)

def Initialise():
    global DEBUGGING
    DEBUGGING = False
    
    global Fantasy, FantasyObjects
    Fantasy = False
    FantasyObjects = []

    global FontSpeechBubble, FontLockOn
    FontSpeechBubble = pygame.font.SysFont("", 26)
    FontLockOn = pygame.font.SysFont("", 22)

    global Pirate1QuestStarted, Pirate1QuestFinished
    Pirate1QuestStarted = False
    Pirate1QuestHelp = False
    Pirate1QuestFinished = False

    global BedroomParentsComplete
    BedroomParentsComplete = False

    global StudyRoomComplete
    StudyRoomComplete = False

    global FirstCoconutReceived
    FirstCoconutReceived = True

def EnterRoom(room):
    if room.Visited:
        ResumeRoom(room)
    else:
        StartRoom(room)

def StartRoom(room):
    room.AddObjects()

def FantasySwap():
    global Fantasy
    Fantasy = not Fantasy
    if Fantasy:
        for obj in FantasyObjects:
            Modules.Object.AddObject(obj)
        Modules.Audio.pirateSong.Play()
    else:
        for obj in FantasyObjects:
            Modules.Object.RemoveObject(obj)
        Modules.Audio.childSong.Play()
def AddFantasyObject(obj):
    if obj not in FantasyObjects:
        FantasyObjects.append(obj)
    if Fantasy:
        Modules.Object.AddObject(obj)
def RemoveFantasyObject(obj):
    if obj in FantasyObjects:
        FantasyObjects.remove(obj)
    if Fantasy:
        Modules.Object.RemoveObject(obj)

def DepthSort():
    Sort = {"Bck":[],
            "Low":[],
            "Mid":[],
            "Hih":[],
            "Gui":[]}
    
    for obj in Modules.Object.GetObjects():
        SortObjects = Sort[obj.depthLayer]
        if len(SortObjects) == 0:
            SortObjects.append(obj)
            continue
        
        for pastObject in SortObjects:
            if obj.depth >= pastObject.depth:
                continue
            index = SortObjects.index(pastObject)
            SortObjects.insert(index, obj)
            break
        if obj in SortObjects:
            continue
        SortObjects.append(obj)

    newObjects = []
    for sort in Sort:
        for obj in Sort[sort]:
            newObjects.append(obj)
    Modules.Object.SetObjects(newObjects)

def Player():
    return Modules.Object.GetObjectVar({"Name":"Player"})
