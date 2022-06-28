
import pygame
import sys
import random
import funcionitems
import crearmapa
import obstaculos
import restriccion


ANCHOVENTANA=640
ALTOVENTANA=640
def gameplay():
    ubicacion=[]
    lista=[[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
        [0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
        [1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
        [1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],
        [0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
        [0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
        [0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
        [0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
        [0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
        [2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
        [2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
        [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]]

    pygame.init()
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    pygame.display.set_caption("test")
    
    crearmapa.crearmapa(lista)
    
    lista=obstaculos.obstaculos()          

    lista=funcionitems.items(lista)                   
        
    pygame.display.flip()

    xPlayer=1
    yPlayer=3
    
    xnpc1=12
    ynpc1=18
    
    xnpc2=15
    ynpc2=3
    
    xnpc3=9
    ynpc3=7

    running = True
    while running:
        crearmapa.crearmapa(lista)
        pygame.draw.rect(ventana, (255,255,255), pygame.Rect(xPlayer*32,yPlayer*32,32,32))
        pygame.draw.rect(ventana, (242,95,227), pygame.Rect(xnpc1*32,ynpc1*32,32,32))
        pygame.draw.rect(ventana, (242,95,227), pygame.Rect(xnpc2*32,ynpc2*32,32,32))
        pygame.draw.rect(ventana, (242,95,227), pygame.Rect(xnpc3*32,ynpc3*32,32,32))
         
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:      
                tecla_presionada= pygame.key.name(event.key)
                if tecla_presionada == 'w':
                    yPlayer = yPlayer-1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        yPlayer = yPlayer+1
                if tecla_presionada == 'a':
                    xPlayer = xPlayer-1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        xPlayer = xPlayer+1
                if tecla_presionada == 's':
                    yPlayer = yPlayer+1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        yPlayer = yPlayer-1
                if tecla_presionada == 'd':
                    xPlayer = xPlayer+1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        xPlayer = xPlayer-1

        random1=random.randint(0,10)
        if random1==0:
            xnpc1=xnpc1+1
            if restriccion.restriccion(xnpc1,ynpc1,lista):
                xnpc1=xnpc1-1
        if random1==1:
            xnpc1=xnpc1-1
            if restriccion.restriccion(xnpc1,ynpc1,lista):
                xnpc1=xnpc1+1
        if random1==2:
            ynpc1=ynpc1+1
            if restriccion.restriccion(xnpc1,ynpc1,lista):
                ynpc1=ynpc1-1
        if random1==3:
            ynpc1=ynpc1-1
            if restriccion.restriccion(xnpc1,ynpc1,lista):
                ynpc1=ynpc1+1

        random1=random.randint(0,10)
        if random1==0:
            xnpc2=xnpc2+1
            if restriccion.restriccion(xnpc2,ynpc2,lista):
                xnpc2=xnpc2-1
        if random1==1:
            xnpc2=xnpc2-1
            if restriccion.restriccion(xnpc2,ynpc2,lista):
                xnpc2=xnpc2+1
        if random1==2:
            ynpc2=ynpc2+1
            if restriccion.restriccion(xnpc2,ynpc2,lista):
                ynpc2=ynpc2-1
        if random1==3:
            ynpc2=ynpc2-1
            if restriccion.restriccion(xnpc2,ynpc2,lista):
                ynpc2=ynpc2+1

        random1=random.randint(0,10)
        if random1==0:
            xnpc3=xnpc3+1
            if restriccion.restriccion(xnpc3,ynpc3,lista):
                xnpc3=xnpc3-1
        if random1==1:
            xnpc3=xnpc3-1
            if restriccion.restriccion(xnpc3,ynpc3,lista):
                xnpc3=xnpc3+1
        if random1==2:
            ynpc3=ynpc3+1
            if restriccion.restriccion(xnpc3,ynpc3,lista):
                ynpc3=ynpc3-1
        if random1==3:
            ynpc3=ynpc3-1
            if restriccion.restriccion(xnpc3,ynpc3,lista):
                ynpc3=ynpc3+1
        
        
            
        
     
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running=False
    sys.exit()

gameplay()
