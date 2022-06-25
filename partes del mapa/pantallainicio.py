import pygame
import sys
import random

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def pantalla1():
        T=True
        #el while mantiene la pantalla andando#
        while T:
            ventana.fill((31,99,79))
            pygame.display.flip()
            for event in pygame.event.get():
                #el evento KEYDOWN significa presionar cualquier tecla
                if event.type==pygame.KEYDOWN:
                    T=False

        #como todavia no tenemos tiles para el suelo esto se asegura de que
        #la "pantalla principal" no se vea en la siguiente pantalla
        ventana.fill((0,0,0))
        pygame.display.flip()

