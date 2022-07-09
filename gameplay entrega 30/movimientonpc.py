import os
import pygame
import sys
import random
import restriccion

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
    return (xnpc,ynpc)

    

        
        

        
        
         

           
