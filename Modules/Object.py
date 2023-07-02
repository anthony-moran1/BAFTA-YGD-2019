import pygame, copy

def Initialise():
    global Objects, Removes
    Objects = []
    Removes = []
def ResetObjects():
    global Objects
    Objects = []

def AddObject(obj):
    if obj in Objects:
        return 0
    Objects.append(obj)

def RemoveObject(obj):
    if obj in Removes or obj not in Objects:
        return 0
    Removes.append(obj)

def SetObjects(objs):
    global Objects
    Objects = objs
    
def GetObjects():
    objs = []
    for obj in Objects:
        if obj in Removes:
            continue
        objs.append(obj)
    return objs
def GetObjectsBut(obj):
    objects = copy.copy(GetObjects())
    if obj in objects:
        objects.remove(obj)
    return objects
def GetObjectsButs(objs):
    objects = copy.copy(GetObjects())
    for obj in objs:
        if obj not in objects:
            continue
        objects.remove(obj)
    return objects

def GetObjectVar(var):
    objs = GetObjectsVar(var)
    if len(objs) == 0:
        return None
    return objs[0]

def GetObjectsVar(var):
    objects = []
    for o in GetObjects():
        add = True
        for v in var:
            if o.__dict__[v] != var[v]:
                add = False
                break
        if add:
            objects.append(o)
    return objects

def UpdateObject(obj):
    obj.Update()
    obj.Show()

def UpdateObjects():
    global Removes
    for o in Objects:
        UpdateObject(o)
    for r in Removes:
        if r not in Objects:
            continue
        Objects.remove(r)
    Removes = []
