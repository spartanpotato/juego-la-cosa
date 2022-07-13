import pygame
import sys
import random


#la funcion toma la lista modificada que nos dejo la funcion obstaculos
def items(lista):
        
        contadoritems=0

        #la funcion continua hasta que hayan por lo menos 30 items
        while contadoritems<30:
            for i in range(20):
                for j in range(20):

                    #esta funcion no puede cambiar valores que ya cambio la funcion obstaculos

                    #recorre la lista y cuando esta en un valor 1 o 2 tiene una chance de cambiar ese valor
                    #a un 4
                    if lista [j][i]==1 or lista [j][i]==2:
                        x=random.randint(0,100)
                        if x<10:                           
                            contadoritems=contadoritems+1

                            lista[j][i]=4
                            
                            #si la funcion cambia 50 valores termina automaticamente
                            if contadoritems==50:
                                    return lista

     
        return (lista)

                    
                

