#integrantes:
#Daniela Huenuman 21.431.336-7
#Francisco Caceres 21.379.893-6
#Ezequiel Carrasco 18.976.450-2
#Felipe Henriquez 21.464.670-6
import pygame
import sys
import random
import pantallainicio
import gameplay
import os

#define dimensiones ventana
ANCHOVENTANA=720
ALTOVENTANA=640
def loop():
    pygame.init()

    #crea la ventana
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    pygame.display.set_caption("test")
    running=True
    while running:

        #llama a la primera pantalla
        pantallainicio.pantalla1()
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            running=False

    pygame.quit()
    os._exit(1)
loop()
        
