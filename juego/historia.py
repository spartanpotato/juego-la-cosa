import pygame
import sys
import random
import pantallainicio
import os

ANCHOVENTANA=720
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def pantalla3():
        imagenhistoria=pygame.image.load("phistoria.png")
        T=True
        #el while mantiene la pantalla andando#
        while T:
            ventana.blit(imagenhistoria,(0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                #el evento KEYDOWN significa presionar cualquier tecla
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                            pantallainicio.pantalla1()
                if event.type==pygame.QUIT:
                        pygame.quit()
                        os._exit(1)

        