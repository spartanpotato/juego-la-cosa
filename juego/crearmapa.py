import pygame
import sys
import random




ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    
                
def crearmapa(lista):

    #image load le asigna una imagen a una variable
    wallimg = pygame.image.load('pared2.png')
    floorimg= pygame.image.load("piso10.png")
    obstaculo= pygame.image.load("obs2.png")
    itemimg  = pygame.image.load("item5.png")
    

    #la funcion recorre la lista ya modificada por funcion obstaculos y funcion items
    #dependiendo del valor de la lista que se encuentre va a copiar una imagen en esas coordenadas
    #como las coordenadas son numeros pequeños, la funcion las multiplica por 32(ya que estamos usando imagenes con esa resolucion)
    #antes de copiar la imagen
    for i in range(20):
        for j in range(20):

            #copia paredes#
            if lista[j][i]==0:
                #blit copia la imagen en las coordenadas dadas
                ventana.blit(wallimg, (32*i,32*j))

            #copia el suelo
            #va a copiar el suelo en cada valor que era 1 o 2 en la lista original 
            if lista[j][i]==1 or lista[j][i]==2 or lista[j][i]==3 or lista[j][i]==4:
                ventana.blit(floorimg, (32*i,32*j))

            #copia obstaculos
            #como la funcion ya copio el suelo en la misma coordenadas esta imagen se copia  encima
            #para que no este en un fondo negro, esto tambien se aplica a la siguiente imagen 
            if lista[j][i]==3:
                ventana.blit(obstaculo, (32*i,32*j))

            #copia items
            if lista[j][i]==4:
                ventana.blit(itemimg, (32*i, 32*j))
    
            
                

   

    

    
