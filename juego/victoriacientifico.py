import pygame
import sys
import random
import pantallainicio
import os
import gameplay
import pantallainicio

ANCHOVENTANA=720
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def victoriacientifico():
        T=True
        #el while mantiene la pantalla andando#
        while T:
            ventana.fill((0,200,200))
            pygame.display.flip()
            for event in pygame.event.get():
                #el evento KEYDOWN significa presionar cualquier tecla
                if event.type==pygame.KEYDOWN:
                    tecla_presionada=pygame.key.name(event.key)
                    if tecla_presionada=="r":
                            gameplay.partida()
                    if event.key == pygame.K_RETURN:
                            pantallainicio.pantalla1()
                            
                            
                if event.type==pygame.QUIT:
                        pygame.quit()
                        os._exit(1)

        
