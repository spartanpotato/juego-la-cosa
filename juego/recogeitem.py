import pygame
import sys
import random
from pygame import mixer

def recogerItem(x,y,lista):
    picksound=mixer.Sound("pickup.wav")
    if lista[y][x]==4:
        lista[y][x]=2
        picksound.play()
    return (lista)
