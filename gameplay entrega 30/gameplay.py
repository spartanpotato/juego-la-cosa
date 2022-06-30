
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

    Player=pygame.image.load('personaje1.png')
    npc=pygame.image.load('personaje.png')

    #primero se crea el mapa, luego la variable obstaculos crea entre 10 y 15 de estos en habitaciones
    #y cambia la el valor de la lista donde se crean a 3, para que que luegon funcionen las restricciones
    #y la funcion items no cree estos encima de un obstaculo, luego la variable crea entre 30 y 50 de estos
    #en espacios libres en habitaciones y pasillos
    lista=obstaculos.obstaculos(lista)
    
    lista=funcionitems.items(lista)                   

    #definimos las coordenadas iniciales del personaje y los npc
    xPlayer=random.randint(0,19)
    yPlayer=random.randint(0,19)
    while lista[yPlayer][xPlayer]!= 1 and lista[yPlayer][xPlayer]!= 2:
        xPlayer=random.randint(0,19)
        yPlayer=random.randint(0,19)
        
    xnpc1=random.randint(0,19)
    ynpc1=random.randint(0,19)
    while lista[ynpc1][xnpc1]!= 1 and lista[ynpc1][xnpc1]!= 2:
        xnpc1=random.randint(0,19)
        ynpc1=random.randint(0,19)
    
    xnpc2=random.randint(0,19)
    ynpc2=random.randint(0,19)
    while lista[ynpc2][xnpc2]!= 1 and lista[ynpc2][xnpc2]!= 2:
        xnpc2=random.randint(0,19)
        ynpc2=random.randint(0,19)
    
    xnpc3=random.randint(0,19)
    ynpc3=random.randint(0,19)
    while lista[ynpc3][xnpc3]!= 1 and lista[ynpc3][xnpc3]!= 2:
        xnpc3=random.randint(0,19)
        ynpc3=random.randint(0,19)

    controlmovimiento=0

    running = True
    while running:

        #en cada frame del gampeplay se copia la imagen de los personajes en sus coordenadas actuales
        #antes de eso se copia el mapa para borrar la imagen anterior y se vea movimiento
        crearmapa.crearmapa(lista)
        ventana.blit(Player, (xPlayer*32,yPlayer*32))
        ventana.blit(npc, (xnpc1*32,ynpc1*32))
        ventana.blit(npc, (xnpc2*32,ynpc2*32))
        ventana.blit(npc, (xnpc3*32,ynpc3*32))
        



        pygame.display.flip()

        #el programa identifica cuando el jugador presiona una tecla de movimiento y cambia las coordenadas
        #donde se va a copiar el personaje en el siguiente frame para que se mueva
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

        #los npc se mueven dependiendo de la variable genera la funcion random, cada frame pueden movese al azar
        #o no moverse, no dependen del jugador
        if controlmovimiento==10:
            controlmovimiento=0
            random1=random.randint(0,4)
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

            random1=random.randint(0,4)
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

            random1=random.randint(0,4)
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

        controlmovimiento=controlmovimiento+1
        
        
        #el gameplay esta dentro de un while que termina cuando se cierra la ventana, en etapas posteriores
        #se acabara cuando se cumpla una condicion de derrota o victoria
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running=False
    sys.exit()

gameplay()
