import pygame
import sys
import random
import pantallainicio
import funcionitems


ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    
                
def crearmapa():
    lista=[[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
        [0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
        [1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
        [1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],
        [0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
        [0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
        [0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
        [0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
        [0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
        [2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
        [2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
        [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]]

    #image load le asigna una imagen a una variable
    wallimg = pygame.image.load('tile 1.png')

    #lo que hace este for anidado es recorrer la lista y copiar
    #la imagen cada vez se encuentra con un 0
    for i in range(20):
        for j in range(20):
            if lista[j][i]==0:

                #blit copia la imagen en las coordenadas dadas
                ventana.blit(wallimg, (32*i,32*j))
                

    pygame.display.flip()

    

    
