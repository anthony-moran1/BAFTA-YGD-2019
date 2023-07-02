import pygame, pickle, math, random
from datetime import datetime

import Modules.Basic, Modules.Event, Modules.Object, Modules.Background, Modules.Room
Modules.Basic.Initialise()
Modules.Basic.SetScreenSize(960, 540)
Modules.Object.Initialise()

import Modules.Control
Modules.Control.Initialise()

import Modules.RoomTitleScreen, Modules.RoomHouse
Modules.RoomTitleScreen.room()

def Update():
    Modules.Basic.FillScreen((0,0,0))
    Modules.Control.DepthSort()
    
    Modules.Object.UpdateObjects()

Modules.Basic.StartLoop(Update)
