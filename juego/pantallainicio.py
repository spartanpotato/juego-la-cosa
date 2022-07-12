import pygame
import sys
import random
import gameplay
import os
import instrucciones
import historia

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def pantalla1():
        siguiente=""
        T=True
        while T:
            ventana.fill((31,99,79))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    tecla_presionada= pygame.key.name(event.key)
                    if event.key == pygame.K_RETURN:
                        siguiente="jugar"
                        T=False
                    if tecla_presionada =="i":
                        siguiente="controles"
                        T=False
                    if tecla_presionada =="o":
                        siguiente="historia"
                        T=False
                if (event.type==pygame.QUIT):
                        pygame.quit()
                        os._exit(1)
        if siguiente=="jugar":
                gameplay.partida()
        if siguiente=="controles":
                instrucciones.pantalla2()
        if siguiente=="historia":
                historia.pantalla3()
pantalla1()

                    
                

        
        

