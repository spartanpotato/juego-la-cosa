#toma coordenadas de los personajes y variable simbionte
#la variable simbionte indica que personaje puede matar al resto

def matar(x1,y1,x2,y2,x3,y3,x,y,sim):

    #la funcion regresa un numero correspondiente a un personaje si
    #esta en las mismas coordenadas del jugador
    if sim==0:
        if x==x1 and y==y1:
            return (1)
        if x==x2 and y==y2:
            return (2)
        if x==x3 and y==y3:
            return (3)

    #la funcion regresa un numero correspondiente a un personaje si
    #esta en las mismas coordenadas del npc1    
    if sim==1:
        if x1==x and y1==y:
            return (0)
        if x1==x2 and y1==y2:
            return (2)
        if x1==x3 and y1==y3:
            return(3)

    #la funcion regresa un numero correspondiente a un personaje si
    #esta en las mismas coordenadas del npc2    
    if sim==2:
        if x2==x and y2==y:
            return (0)
        if x2==x1 and y2==y1:
            return (1)
        if x2==x3 and y2==y3:
            return(3)

    #la funcion regresa un numero correspondiente a un personaje si
    #esta en las mismas coordenadas del npc3    
    if sim==3:
        if x3==x and y3==y:
            return (0)
        if x3==x1 and y3==y1:
            return (1)
        if x3==x2 and y3==y2:
            return(2)
    
