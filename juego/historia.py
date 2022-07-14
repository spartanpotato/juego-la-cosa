import pygame
import sys
import random
import pantallainicio
import os
from pygame import mixer

ANCHOVENTANA=720
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))



def pantalla3():
        pygame.mixer.init()

        #asigna sonido a variable
        back_sound=mixer.Sound("back.ogg")
        
        #asigna imagen a variable
        imagenhistoria=pygame.image.load("phistoria.png")

        #asigna volumen
        mixer.Sound.set_volume(back_sound, 0.3)
        
        T=True
        while T:

            #dibuja imagen    
            ventana.blit(imagenhistoria,(0,0))
            pygame.display.flip()
            
            for event in pygame.event.get():
                #si presiona backspace se vuelve a pantallainicio
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:

                            #activa sonido
                            back_sound.play()
                            
                            T=False
                            
                if event.type==pygame.QUIT:
                        pygame.quit()
                        os._exit(1)

        
