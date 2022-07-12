import pygame
import sys
import random

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))

#la funcion toma las coordenadas x e y del personaje y la lista actual
def restriccion(x,y,lista):

        #si no ocurre ni una restriccion se devuelve un False        
        stay=False

        #si las coordenadas del personaje (equivalentes a la lista)
        #salen del tablero se devuelve un True
        if x<0 or x>19 or y<0 or y>19:
                stay=True
                return stay

        #si las coordenadas del personaje (equivalentes a la lista)
        #estan en un valor de la lista 0 o 3 se devuelve un True
        if lista[y][x]==0 or lista[y][x]==3:
                stay=True
                return stay

        
        return stay

                            
          
                    
                


