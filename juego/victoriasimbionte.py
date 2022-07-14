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



def victoriasimbionte():
        pygame.mixer.init()

        #asigna sonido a variables
        press_sound=mixer.Sound("press.ogg")
        back_sound=mixer.Sound("back.ogg")
        
        T=True
        #el while mantiene la pantalla andando#
        while T:

            #dibuja imagen    
            ventana.fill((196,0,0))
            pygame.display.flip()
            
            for event in pygame.event.get():

                #si presiona r se repite el gameplay, si presiona enter vuelve a pantalla inicio
                if event.type==pygame.KEYDOWN:
                    tecla_presionada=pygame.key.name(event.key)
                    if tecla_presionada=="r":

                            #activa sonido
                            press_sound.play()
                            
                            gameplay.partida()
                    if event.key == pygame.K_RETURN:

                            #activa sonido
                            back_sound.play()
                            
                            pantallainicio.pantalla1()
                            
                            
                if event.type==pygame.QUIT:
                        pygame.quit()
                        os._exit(1)

        
