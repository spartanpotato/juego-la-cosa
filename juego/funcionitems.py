import pygame
import sys
import random


#la funcion toma la lista modificada que nos dejo la funcion obstaculos
def items(lista):      
        contadoritems=0

        #numero representa cantidad minima de items
        while contadoritems<30:

            #recorre lista hasta encontrar 1 o 2
            #por ende no cambia valores afectados por funcion obstaculos    
            for i in range(20):
                for j in range(20):   
                    if lista [j][i]==1 or lista [j][i]==2:

                        #rango mayor da mayor distribucion de obstaculo pero reduce probabilidad
                        #de que aparezcan mas de 10, lo mismo si el x<numero es mas pequeño    
                        x=random.randint(0,100)
                        if x<10:
                                
                            contadoritems=contadoritems+1

                            #cambia valor de la lista
                            lista[j][i]=4
                            
                            #valor maximo, la funcion termina al instante si llega a este
                            if contadoritems==50:
                                    return lista

        #devuelve la nueva lista
        return (lista)

                    
                

