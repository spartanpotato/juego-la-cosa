import pygame
import sys
import random


def obstaculos(lista):       
        contadorobstaculo=0       

        #numero representa cantidad minima de obstaculos
        while contadorobstaculo<10:

            #recorre la lista hasta encontrar un 1
            for i in range(20):
                for j in range(20):
                    if lista [j][i]==1:

                        #rango mayor da mayor distribucion de obstaculo pero reduce probabilidad
                        #de que aparezcan mas de 10, lo mismo si el x<numero es mas pequeño
                        x=random.randint(0,100)
                        if x<7:
                                
                            contadorobstaculo=contadorobstaculo+1

                            #cambia el valor de la lista#
                            lista[j][i]=3

                            #valor maximo, la funcion termina al instante si llega a este
                            if contadorobstaculo==15:
                                    return lista
        #se devuelve la nueva lista                        
        return lista
                    
                


