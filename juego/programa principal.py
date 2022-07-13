import pygame
import sys
import random
import pantallainicio
import gameplay
import os

ANCHOVENTANA=720
ALTOVENTANA=640
def loop():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    pygame.display.set_caption("test")
    running=True
    while running:
        pantallainicio.pantalla1()
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            running=False

    pygame.quit()
    os._exit(1)
loop()
        
