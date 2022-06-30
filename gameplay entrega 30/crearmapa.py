import pygame
import sys
import random
import pantallainicio
import funcionitems


ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    
                
def crearmapa(x):
    lista1=x

    #image load le asigna una imagen a una variable
    wallimg = pygame.image.load('pared2.png')
    floorimg= pygame.image.load("piso10.png")
    obstaculo= pygame.image.load("obs2.png")
    itemimg  = pygame.image.load("item5.png")
    

    #lo que hace este for anidado es recorrer la lista y copiar
    #la imagen cada vez se encuentra con un 0
    for i in range(20):
        for j in range(20):
            if lista1[j][i]==0:
                #blit copia la imagen en las coordenadas dadas
                ventana.blit(wallimg, (32*i,32*j))

            if lista1[j][i]==1 or lista1[j][i]==2 or lista1[j][i]==3 or lista1[j][i]==4:
                ventana.blit(floorimg, (32*i,32*j))

            if lista1[j][i]==3:
                ventana.blit(obstaculo, (32*i,32*j))

            if lista1[j][i]==4:
                ventana.blit(itemimg, (32*i, 32*j))
    
            
                

   

    

    
