def contadoritems(lista):
    contador=0
    for i in range (20):
        for j in range (20):
            if lista[i][j]==4:
                contador=contador+1
    if contador==0:
        return(True)
            
                
            
