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
import pantallainicio
from pygame import mixer


def partida():
    mixer.init()
    ANCHOVENTANA=720
    ALTOVENTANA=640
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))

    #variable simbionte, si es 0 el jugador es el simbionte, cualquier otro numero es un npc
    simbionte=random.randint(0,3)

    #asigna sonidos a variables
    death_sound=mixer.Sound("death.wav")
    press_sound=mixer.Sound("press.ogg")
    back_sound=mixer.Sound("back.ogg")
    pause_sound=mixer.Sound("pause.ogg")
    resume_sound=mixer.Sound("resume.ogg")
    player_sound=mixer.Sound("playersound.ogg")
    mixer.music.load("gamemusic.mp3")
    
    #asigna volumen
    mixer.Sound.set_volume(player_sound, 0.1)
    mixer.Sound.set_volume(death_sound, 0.3)
    mixer.Sound.set_volume(press_sound, 0.3)
    mixer.Sound.set_volume(back_sound, 0.3)
    mixer.Sound.set_volume(pause_sound, 0.3)
    mixer.Sound.set_volume(resume_sound, 0.3)
    mixer.music.set_volume(0.2)

    #activa musica de gameplay
    mixer.music.play(-1)

    #asigna imagenes a variables
    Player=pygame.image.load('personaje1.png')
    npc=pygame.image.load('personaje.png')
    erescientifico=pygame.image.load("erescientifico.png")
    eresimbionte=pygame.image.load("eresimbionte.png")
    texto=pygame.image.load("texto.png")


    #pantalla que muestra si el jugador es simbionte o cientifico
    T=True
    while T:
        if simbionte==0:
            ventana.blit(eresimbionte,(0,0))
        else:
            ventana.blit(erescientifico,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            
            #se presiona enter para continuar
            if event.type == pygame.KEYDOWN:      
                if event.key==pygame.K_RETURN:
                    press_sound.play()
                    T=False
                    
    ventana.fill((0,0,0))
                       
    #lista original, define donde hay paredes, pasillos y habitaciones    
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



    #ambas funciones toman la lista y la modifican para añadir variables correspondientes a obstaculos e items
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

    #contadores
    controlmovimiento=0
    muertos=0

    #variables de estado para pantallas
    pause = False
    running = True

    #variables de estado de personajes
    playeralive=True
    npc1alive=True
    npc2alive=True
    npc3alive=True
    
    #asigna variable para usar luego
    pantalla="no"

    #aqui ocurre el juego
    while running:

        #en cada frame del gampelay se dibuja el mapa encima de la imagen anterior y los personajes
        #en sus coordenadas nuevas encima del mapa
        crearmapa.crearmapa(lista)

        #dibuja a los personajes si estan vivos
        if playeralive:
            ventana.blit(Player, ((xPlayer*32)+40,yPlayer*32))
        if npc1alive:
            ventana.blit(npc, ((xnpc1*32)+40,ynpc1*32))
        if npc2alive:
            ventana.blit(npc, ((xnpc2*32)+40,ynpc2*32))
        if npc3alive:
            ventana.blit(npc, ((xnpc3*32)+40,ynpc3*32))

        #si eljugador muere aparece un mensaje
        if playeralive==False:
            ventana.blit(texto,(0,0))
        
        #actualiza los cambios en la pantalla
        pygame.display.flip()

        #pausa
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #se presiona p para reanudar
                    tecla_presionada=pygame.key.name(event.key)
                    if tecla_presionada== "p":
                        #activa sonido
                        resume_sound.play()
                        pause=False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(1)

        

        #mientras mas alto sea el numero mas deben esperar los npc para moverse
        if controlmovimiento==15:
            controlmovimiento=0

            #si los npc estan vivos se llama a la funcion de movimiento para darles nuevas coordenadas
            if npc1alive:
                xnpc1,ynpc1=movimientonpc.movimientoaleatorio(xnpc1,ynpc1,lista)
            if npc2alive:
                xnpc2,ynpc2=movimientonpc.movimientoaleatorio(xnpc2,ynpc2,lista)
            if npc3alive: 
                xnpc3,ynpc3=movimientonpc.movimientoaleatorio(xnpc3,ynpc3,lista)
        controlmovimiento=controlmovimiento+1
        

        #aqui aparecen cosas que puede hacer el jugador
        for event in pygame.event.get():
                            
            if event.type == pygame.KEYDOWN:      
                tecla_presionada=pygame.key.name(event.key)
                
                #si el jugador presiona una tecla WASD cambian sus coordenadas y moverse,
                #se llama la funcion restriccion, si se activa, se anula el cambio.
                #player_sound.play() genera sonido cuando se mueve
                if tecla_presionada == 'w' and playeralive:
                    yPlayer = yPlayer-1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        yPlayer = yPlayer+1
                    player_sound.play()
                if tecla_presionada == 'a' and playeralive:                    
                    xPlayer = xPlayer-1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        xPlayer = xPlayer+1
                    player_sound.play()
                if tecla_presionada == 's' and playeralive:
                    yPlayer = yPlayer+1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        yPlayer = yPlayer-1
                    player_sound.play()
                if tecla_presionada == 'd' and playeralive:
                    xPlayer = xPlayer+1
                    if restriccion.restriccion(xPlayer,yPlayer,lista):
                        xPlayer = xPlayer-1
                    player_sound.play()

                #si presiona p el juego se pausa
                if tecla_presionada == "p":
                    #activa sonido
                    pause_sound.play()
                    pause=True

                #si presiona r el juego se reinicia    
                if tecla_presionada=='r':
                    #activa sonido
                    back_sound.play()
                    pantalla="reinicio"
                    running=False

                #si presiona backspace luego de morir vuelve al menu principal
                if event.key==pygame.K_BACKSPACE and playeralive==False:
                    #activa sonido
                    back_sound.play()
                    pantallainicio.pantalla1()
                    
            if (event.type == pygame.QUIT):
                running=False

        #funcion permite que personajes recogan items
        lista=recogeitem.recogerItem(xnpc1,ynpc1,lista)
        lista=recogeitem.recogerItem(xnpc2,ynpc2,lista)
        lista=recogeitem.recogerItem(xnpc3,ynpc3,lista)
        lista=recogeitem.recogerItem(xPlayer,yPlayer,lista)

        #si se recogen todos los itemes termina el gameplay y se muestra pantalla de victoria cientificos
        if contadoritems.contadoritems(lista):
            pantalla="cientifico"
            running=False

        #funcion comprueba si el simbionte toca a otro personaje, si lo hace, dicho personaje dejara de dibujarse y moverse
        #deathsound.play() genrea sonido cada vez que un personaje muere    
        muerte=matar.matar(xnpc1,ynpc1,xnpc2,ynpc2,xnpc3,ynpc3,xPlayer,yPlayer,simbionte)
        if muerte==0 and playeralive:
            playeralive=False
            muertos=muertos+1
            death_sound.play()
        if muerte==1 and npc1alive:
            npc1alive=False
            muertos=muertos+1
            death_sound.play()
        if muerte==2 and npc2alive:
            npc2alive=False
            muertos=muertos+1
            death_sound.play()
        if muerte==3 and npc3alive:
            npc3alive=False
            muertos=muertos+1
            death_sound.play()

        #si el simbiomte mata a los otros 3 personajes termina el gameplay y se muestra pantalla de victoria simbionte    
        if muertos==3:
            pantalla="simbionte"
            running=False

    #llama pantallas de victoria    
    if pantalla=="cientifico":
        victoriacientifico.victoriacientifico()
    if pantalla=="simbionte":
        victoriasimbionte.victoriasimbionte()

    #reinicia gameplay    
    if pantalla=="reinicio":
        partida()
   
                
            
    pygame.quit()
    os._exit(1)
        



