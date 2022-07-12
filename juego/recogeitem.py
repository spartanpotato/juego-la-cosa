import pygame
import sys
import random

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))

def recogerItem(x,y,lista):
    if lista[y][x]==4:
        lista[y][x]=2
    return (lista)
