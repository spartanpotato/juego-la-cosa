import os
import pygame
import sys
import random
import restriccion

#toma coordenadas de un npc y la lista
#el npc tiene 80% de probabilidades de moverse en direccion cardinal
#20% probabilidades de n o moverse
#en cada movimiento se usa la funcion restriccion, si se activa se cancela el movimiento
def movimientoaleatorio(xnpc,ynpc,lista):
    random1=random.randint(0,4)
    if random1==0:
        xnpc=xnpc+1
        if restriccion.restriccion(xnpc,ynpc,lista):
            xnpc=xnpc-1
    if random1==1:
        xnpc=xnpc-1
        if restriccion.restriccion(xnpc,ynpc,lista):
            xnpc=xnpc+1
    if random1==2:
        ynpc=ynpc+1
        if restriccion.restriccion(xnpc,ynpc,lista):
            ynpc=ynpc-1
    if random1==3:
        ynpc=ynpc-1
        if restriccion.restriccion(xnpc,ynpc,lista):
            ynpc=ynpc+1

    #regresa nuevas coordenadas        
    return (xnpc,ynpc)

    

        
        

        
        
         

           
