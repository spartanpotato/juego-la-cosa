import pygame
import sys
import random
import gameplay
import os
import instrucciones
import historia
from pygame import mixer

ANCHOVENTANA=720
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def pantalla1():
        pygame.mixer.init()
        #asigna imagen a variable
        imageninicio=pygame.image.load("pantallainicio.png")
        #asigna sonido a variable
        press_sound=mixer.Sound("press.ogg")
        
        siguiente=""
        T=True
        while T:
            #dibuja imagen
            ventana.blit(imageninicio, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                #reconoce una tecla y actua dependiendo de esta    
                if event.type==pygame.KEYDOWN:
                    tecla_presionada= pygame.key.name(event.key)
                    if event.key == pygame.K_RETURN:
                        siguiente="jugar"
                        T=False
                        
                        #activa sonido
                        press_sound.play()
                        
                    if tecla_presionada =="i":
                        siguiente="controles"
                        T=False
                        press_sound.play()
                    if tecla_presionada =="o":
                        siguiente="historia"
                        T=False
                        press_sound.play()
                if (event.type==pygame.QUIT):
                        pygame.quit()
                        os._exit(1)
        #dependiendo de la tecla presionada aparece una diferente pantalla
        if siguiente=="jugar":
                gameplay.partida()
        if siguiente=="controles":
                instrucciones.pantalla2()
        if siguiente=="historia":
                historia.pantalla3()
pantalla1()

                    
                

        
        

