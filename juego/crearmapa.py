import pygame
import sys
import random




ANCHOVENTANA=720
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    
                
def crearmapa(lista):

    #asigna imagenes a variables
    wallimg = pygame.image.load('pared2.png')
    floorimg= pygame.image.load("piso10.png")
    obstaculo= pygame.image.load("obs2.png")
    itemimg  = pygame.image.load("item5.png")
    

    #recorre lista y dependiendo del valor que encuentra, dibuja un sprite en las coordenadas correspondientes de la ventana
    #multiplica coordenadas de la lista por 32 para dibujar por que se usan sprites de 32x32 pixeles
    #en caso de coordenadas x adicionalmente suma 40 pixeles para centrar la imagen, porque hay espacio vacio en la ventana
    for i in range(20):
        for j in range(20):

            #dibuja paredes cuando encuentra 0
            if lista[j][i]==0:
                ventana.blit(wallimg, ((32*i)+40,32*j))

            #dibuja el suelo
            #va a copiar el suelo en cada valor que era 1 o 2 en la lista original 
            if lista[j][i]==1 or lista[j][i]==2 or lista[j][i]==3 or lista[j][i]==4:
                ventana.blit(floorimg, ((32*i)+40,32*j))

            #dibuja obstaculos
            #como la funcion ya copio el suelo en la misma coordenadas esta imagen se copia  encima
            #para que no este en un fondo negro, esto tambien se aplica a la siguiente imagen 
            if lista[j][i]==3:
                ventana.blit(obstaculo, ((32*i)+40,32*j))

            #dibuja items
            if lista[j][i]==4:
                ventana.blit(itemimg, ((32*i)+40,32*j))
    
            
                

   

    

    
