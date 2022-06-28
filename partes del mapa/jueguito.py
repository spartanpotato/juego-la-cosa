import pygame
import sys

#tamaño de la ventana#
ANCHOVENTANA=640
ALTOVENTANA=640


def main():
    pygame.init()
    #funcion para creac la ventana y nombre#
    ventana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    pygame.display.set_caption("test")
    
    xPlayer = 0
    yPlayer = 4
    pygame.draw.rect(ventana, (255,255,255), pygame.Rect(xPlayer,yPlayer,20,20))

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


    #asigna la imagen a una variable
    wallimg = pygame.image.load('tile 1.png')
    floorimg = pygame.image.load("piso1.png")

    #blit se usa para copiar la imagen en las cordenadas dadas
    for i in range(20):
        for j in range(20):
            if lista[j][i]==0:
                ventana.blit(wallimg, (32*i,32*j))
            if lista[j][i]==1 or lista[j][i]==2:
                ventana.blit(floorimg, (32*i, 32*j))


    
#se usa para generar cambios#
    pygame.display.flip()

    

    running = True
    while running:

        for i in range(20):
            for j in range(20):
                if lista[j][i]==0:
                    ventana.blit(wallimg, (32*i,32*j))
                if lista[j][i]==1 or lista[j][i]==2:
                    ventana.blit(floorimg, (32*i, 32*j))
        pygame.draw.rect(ventana, (255,255,255), pygame.Rect(xPlayer*32,yPlayer*32,32,32))
        

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
             
                tecla_presionada= pygame.key.name(event.key)
                
                if tecla_presionada == 'w':
                    yPlayer = yPlayer-1
                if tecla_presionada == 'a':
                    xPlayer = xPlayer-1
                if tecla_presionada == 's':
                    yPlayer = yPlayer+1
                if tecla_presionada == 'd':
                    xPlayer = xPlayer+1


                

                
            if (event.type == pygame.QUIT):
             running=False
    sys.exit()

main()
