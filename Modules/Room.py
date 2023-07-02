import pygame, math, random

import Modules.Basic, Modules.Object, Modules.Function
import Modules.Control, Modules.GameSprite
import Modules.Background, Modules.Camera, Modules.SpeechBubble
import Modules.Player, Modules.LockOn, Modules.Alert

import Modules.Mum
import Modules.GuiChest, Modules.Sword, Modules.WallBoat
import Modules.Timer, Modules.Radio, Modules.Croissant
import Modules.Bed, Modules.Table, Modules.Wardrobe, Modules.Carpet
import Modules.BathBathMat, Modules.Toilet, Modules.Taps, Modules.Mirror
import Modules.CollisionBox, Modules.BoatBox, Modules.Map, Modules.MapCollectable, Modules.Box
import Modules.Pirate1, Modules.TeddyBear, Modules.Pirate1Bridge, Modules.Ball
import Modules.Plant
import Modules.DiscoFloor, Modules.Pirate2
import Modules.Coins

class Room:
    def __init__(self, player=True):        
        Modules.Object.Objects = []
        
        bck = Modules.Background.Background()
        bck.Add()

        cam = Modules.Camera.Camera()
        cam.Add()

        Modules.Audio.childSong.Play()

        if not player:
            return
        player = Modules.Player.Player()
        sw, sh = Modules.Basic.GetScreenSize()
        player.rect.center = (sw//2, sh//2)
        player.Add()
        
        for i in range(3):
            player.AddRandomItem(Modules.Sword)
        
        player.LockOn = Modules.LockOn.LockOn()
        player.LockOn.Add()

        cam.SetTarget(player)

    def StartRoom(self):
        pass

def Add(obj, pos):
    obj.rect.topleft = Modules.Background.GetPosBackground(pos)
    obj.Add()
