import pygame
import sys
import random
import pantallainicio
import os
import gameplay
import pantallainicio
from pygame import mixer

ANCHOVENTANA=720
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def victoriacientifico():
        pygame.mixer.init()
        press_sound=mixer.Sound("press.ogg")
        back_sound=mixer.Sound("back.ogg")
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
                            press_sound.play()
                            gameplay.partida()
                    if event.key == pygame.K_RETURN:
                            back_sound.play()
                            pantallainicio.pantalla1()
                            
                            
                if event.type==pygame.QUIT:
                        pygame.quit()
                        os._exit(1)

        
