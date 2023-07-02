import pygame
import Modules.Background
import Modules.Bath, Modules.BathMat

def BathBathMatOriginal(bath, bathMat, posBath, posBathMat):
    bath.BathMat = bathMat
    bathMat.Bath = bath

    bath.rect.topleft = Modules.Background.GetPosBackground(posBath)
    bathMat.rect.topleft = Modules.Background.GetPosBackground(posBathMat)

    bath.Add()
    bathMat.Add()

    bath.rectOriginal = pygame.Rect(bath.rect)

def BathBathMat(posBath, posBathMat):
    bath = Modules.Bath.Bath()
    bathMat = Modules.BathMat.BathMat()
    BathBathMatOriginal(bath, bathMat, posBath, posBathMat)

def BathBathMatParents(posBath, posBathMat):
    BathBathMatOriginal(Modules.Bath.BathParents(),
                        Modules.BathMat.BathMatParents(),
                        posBath, posBathMat)
