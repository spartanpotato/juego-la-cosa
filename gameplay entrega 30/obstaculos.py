import pygame
import sys
import random

ANCHOVENTANA=640
ALTOVENTANA=640
ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))


def obstaculos(lista):       
        contadorobstaculo=0       

        #el while se asegura de que se creen por lo menos 10 obstaculos
        while contadorobstaculo<10:

            #recorre la lista y tiene una chance de copiar el valor 3 cada vez que encuentra un 1
            for i in range(20):
                for j in range(20):
                    if lista [j][i]==1:

                        #asigna la probabilidad de copiar la imagen#
                        x=random.randint(0,100)
                        if x<7:
                                
                            contadorobstaculo=contadorobstaculo+1

                            #cambia el valor de la lista#
                            lista[j][i]=3

                            #si se copian 15 valores la funcion termina automaticamente
                            if contadorobstaculo==15:
                                    return lista
        #se devuelve la nueva lista                        
        return lista
                    
                


