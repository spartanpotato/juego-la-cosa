#este archivo solo sirve para probar como funcionan los modulos en conjunto
#no es el programa principal que vamos a entregar

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

    #crea la ventana y le da nombre
    pygame.init()
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    pygame.display.set_caption("test")

    #crea la "pantalla principal", se vera mejor con imagen
    pantallainicio.pantalla1()
    
    #crea el mapa#
    crearmapa.crearmapa()
    
    #crea los obstaculos y guarda una lista modificada
    lista=obstaculos.obstaculos()          

    #toma la lista modificada y crea items que no estaran en las mismas
    #coordenadas que los obstaculos
    lista=funcionitems.items(lista)                   
        
    pygame.display.flip()

    #hace Que no se cierre
    running = True
    while running:

        
        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running=False
    sys.exit()

main()
