import pygame
import sys
import random

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))


def restriccion(x,y,lista):
        lista1=lista
        stay=False
        
        if x<0 or x>19 or y<0 or y>19:
                stay=True
                return stay
        if lista1[y][x]==0 or lista1[y][x]==3:
                stay=True
                return stay

                            
          
                    
                


