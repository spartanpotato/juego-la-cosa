import pygame
import sys
import random

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def pantalla1():
        T=True
        while T:
            ventana.fill((31,99,79))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    T=False

