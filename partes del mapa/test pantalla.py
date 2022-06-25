import pygame
import sys
import random
import pantallainicio
import funcionitems
import crearmapa
import obstaculos

ANCHOVENTANA=640
ALTOVENTANA=640


def main():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    pygame.display.set_caption("test")

    pantallainicio.pantalla1()

    ventana.fill((0,0,0))
    pygame.display.flip()

    crearmapa.crearmapa()

    lista=obstaculos.obstaculos()          

    lista=funcionitems.items(lista)                   
        
    pygame.display.flip()

    
    running = True
    while running:

        
        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running=False
    sys.exit()

main()
