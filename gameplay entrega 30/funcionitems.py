import pygame
import sys
import random

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))

#la funcion toma la lista modificada que nos dejo la funcion obstaculos
def items(lista):
        lista=lista
        
        contadoritems=0

        while contadoritems<30:
            for i in range(20):
                for j in range(20):

                    #como la funcion obstaculos cambio el valor de la lista a 3 donde copio una imagen
                    #esta funcion no puede copiar otra imagen en las mismas coordenadas
                    if lista [j][i]==1 or lista [j][i]==2:
                        x=random.randint(0,100)
                        if x<10:                           
                            contadoritems=contadoritems+1

                            #igual que con los obstaculos cambiamos el valor de la lista donde aparecen items
                            #esto ayudara mas tarde a que el personaje los pueda "recolectar"
                            lista[j][i]=4

                            if contadoritems==50:
                                    return lista

     
        return lista
                    
                

