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
        mixer.music.load("menu.mp3")

        #asigna volumen
        mixer.music.set_volume(0.3)
        mixer.Sound.set_volume(press_sound, 0.3)


        #activa musica
        mixer.music.play(-1)
        
        
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
                        T=False
                        
                        #activa sonido
                        press_sound.play()
                        
                    if tecla_presionada =="i":
          
                        press_sound.play()
                        instrucciones.pantalla2()
                        
                    if tecla_presionada =="o":
              
                        press_sound.play()
                        historia.pantalla3()
                        
                if (event.type==pygame.QUIT):
                        pygame.quit()
                        os._exit(1)
        
        gameplay.partida()
pantalla1()

                    
                

        
        

