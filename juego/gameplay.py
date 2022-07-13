#integrantes:
#Daniela Huenuman 21.431.336-7
#Francisco Caceres 21.379.893-6
#Ezequiel Carrasco 18.976.450-2
#Felipe Henriquez 21.464.670-6

import os
import pygame
import sys
import random
import funcionitems
import crearmapa
import obstaculos
import restriccion
import movimientonpc
import recogeitem
import contadoritems
import matar
import victoriacientifico
import victoriasimbionte


#dimensiones de la ventana

def partida():
    ANCHOVENTANA=720
    ALTOVENTANA=640
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    simbionte=random.randint(1,4)
    pan=True
    while pan:
        if simbionte==1:
            ventana.fill((34,146,8))
        else:
            ventana.fill((135,20,80))
        pygame.display.flip()

        for event in pygame.event.get():
                            
            if event.type == pygame.KEYDOWN:      
                if event.key==pygame.K_RETURN:
                    pan=False
    ventana.fill((0,0,0))
                    
                
        
        
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


    #definen las imagenes del jugador y los npc
    Player=pygame.image.load('personaje1.png')
    npc=pygame.image.load('personaje.png')

    #la funcion obstaculos toma la lista la lista y inicial y la recorre, cada vez que encuentra
    #un 1 tiene una chance de cambiar ese uno por un 3, termina cuando cambio al menos 10 valores
    #o cambio 15, devuelve la nueva lista
    #la funcion items toma la nueva lista y la recorre, cuando encuentra un 1 o 2 tiene una chance
    #cambiarlo por un 4, termina cuando cambio al menos 30 valores o cuando cambio 50, devuelve la
    #nueva lista
    lista=obstaculos.obstaculos(lista)    
    lista=funcionitems.items(lista)


    #se definen coordenadas al azar para los personajes, si estas no estan en un 1 o 2 de la lista
    #se asignan nuevas hasta que si lo esten
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
    pause = False
    running = True
    playeralive=True
    npc1alive=True
    npc2alive=True
    npc3alive=True
    muertos=0
    pantalla="no"
    while running:

        #en cada frame del gampeplay se copia la imagen de los personajes en sus coordenadas actuales
        #antes de eso se copia el mapa para borrar la imagen anterior y se vea movimiento
        #la funcion crearmapa va a dibujar las paredes, el piso, y encima de el piso los obstaculos e items
        #(mas info en su modulo)
        crearmapa.crearmapa(lista)

        #copia los sprites de los personajes en la pantalla
        if playeralive:
            ventana.blit(Player, ((xPlayer*32)+40,yPlayer*32))
        if npc1alive:
            ventana.blit(npc, ((xnpc1*32)+40,ynpc1*32))
        if npc2alive:
            ventana.blit(npc, ((xnpc2*32)+40,ynpc2*32))
        if npc3alive:
            ventana.blit(npc, ((xnpc3*32)+40,ynpc3*32))
        
        #actualiza los cambios en la pantalla
        pygame.display.flip()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    tecla_presionada=pygame.key.name(event.key)
                    if tecla_presionada== "p":
                        pause=False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(1)

        

        #los npc se mueven cada x(controlmovimiento) frames, dependiendo de una variable al azar se pueden mover
        #o quedarse quietos. La funcion restriccion funciona igual como con el personaje del jugador
        if controlmovimiento==20:
            controlmovimiento=0       
            if npc1alive:
                xnpc1,ynpc1=movimientonpc.movimientoaleatorio(xnpc1,ynpc1,lista)
            if npc2alive:
                xnpc2,ynpc2=movimientonpc.movimientoaleatorio(xnpc2,ynpc2,lista)
            if npc3alive: 
                xnpc3,ynpc3=movimientonpc.movimientoaleatorio(xnpc3,ynpc3,lista)

        controlmovimiento=controlmovimiento+1

        #el programa identifica cuando el jugador presiona una tecla de movimiento y cambia las coordenadas
        #donde se va a copiar el personaje en el siguiente frame para que se mueva
        #cada vez que ocurre un movimiento se ejecuta un if que llama a la funcion restriccion, esta detecta
        #si las nuevas coordenadas estan en un lugar prohibido(fuera del tablero, en una pared, u obstaculo)
        #si detecta esto devuelve un True al if y se contrarresta el movimiento antes de que se actualice la pantalla
        for event in pygame.event.get():
                            
            if event.type == pygame.KEYDOWN:      
                tecla_presionada= pygame.key.name(event.key)
                
                if tecla_presionada == 'w' and playeralive:
                    yPlayer = yPlayer-1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        yPlayer = yPlayer+1
                        
                if tecla_presionada == 'a' and playeralive:                    
                    xPlayer = xPlayer-1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        xPlayer = xPlayer+1
                if tecla_presionada == 's' and playeralive:
                    yPlayer = yPlayer+1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        yPlayer = yPlayer-1
                if tecla_presionada == 'd' and playeralive:
                    xPlayer = xPlayer+1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        xPlayer = xPlayer-1


                if tecla_presionada == "p":
                    pause=True
                if tecla_presionada=='r':
                    pantalla="reinicio"
                    running=False
            if (event.type == pygame.QUIT):
                running=False


        lista=recogeitem.recogerItem(xnpc1,ynpc1,lista)
        lista=recogeitem.recogerItem(xnpc2,ynpc2,lista)
        lista=recogeitem.recogerItem(xnpc3,ynpc3,lista)
        lista=recogeitem.recogerItem(xPlayer,yPlayer,lista)
        if contadoritems.contadoritems(lista):
            pantalla="cientifico"
            running=False

        muerte=matar.matar(xnpc1,ynpc1,xnpc2,ynpc2,xnpc3,ynpc3,xPlayer,yPlayer,simbionte)
        if muerte==0 and playeralive:
            playeralive=False
            muertos=muertos+1
        if muerte==1 and npc1alive:
            npc1alive=False
            muertos=muertos+1
        if muerte==2 and npc2alive:
            npc2alive=False
            muertos=muertos+1
        if muerte==3 and npc3alive:
            npc3alive=False
            muertos=muertos+1
        if muertos==3:
            pantalla="simbionte"
            running=False
        
    if pantalla=="cientifico":
        victoriacientifico.victoriacientifico()
    if pantalla=="simbionte":
        victoriasimbionte.victoriasimbionte()
    if pantalla=="reinicio":
        partida()
   
                
            
    pygame.quit()
    os._exit(1)
        



