import pygame
import sys
import random
import pantallainicio
import os

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def pantalla3():
        T=True
        #el while mantiene la pantalla andando#
        while T:
            ventana.fill((32,133,0))
            pygame.display.flip()
            for event in pygame.event.get():
                #el evento KEYDOWN significa presionar cualquier tecla
                if event.type==pygame.KEYDOWN:
                    tecla_presionada=pygame.key.name(event.key)
                    if tecla_presionada=="i":
                            pantallainicio.pantalla1()
                if event.type==pygame.QUIT:
                        pygame.quit()
                        os._exit(1)

        
