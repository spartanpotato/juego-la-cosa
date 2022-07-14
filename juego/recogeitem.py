import pygame
import sys
import random
from pygame import mixer


#toma coordenadas de un personaje y la lista
def recogerItem(x,y,lista):

    #asigna sonido a una variable
    picksound=mixer.Sound("pickup.wav")

    #cuando u personaje esta en un objeto, el valor de la lista cambia
    #el objeto dejara de dibujarse
    if lista[y][x]==4:
        lista[y][x]=2

        #activa sonido
        picksound.play()

    #devuelve nueva lista    
    return (lista)
