x=0
for y in range(len(matriz)):
    for x in range(len(matriz[y]
        if matriz[y][x]=="B":
           pass
        elif x==0 and y==0:
           if matriz[y][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x+1]=="B":
                matriz[y][x]+=1
        elif x==ancho-1 and y==alto-1:
            if matriz[y-1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x]=="B":
                matriz[y][x]+=1
            if matriz [y][x-1]=="B":
                matriz[y][x]+=1
        elif x==0 and y==alto-1:
            if matriz[y-1][x]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y][x+1]=="B":
                matriz[y][x]+=1
        elif x==ancho and y==0:
            if matriz[y][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x]=="B":
                matriz[y][x]+=1
        elif x==0:
            if matriz[y-1][x]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x+1]=="B":
                matriz[y][x]+=1
        elif x==ancho-1:
            if matriz[y-1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x]=="B":
                matriz[y][x]+=1
            if matriz[y][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x]=="B":
                matriz[y][x]+=1
        elif y==0:
            if matriz[y][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x+1]=="B":
                matriz[y][x]+=1
        elif y==alto-1:
            if matriz[y-1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y][x+1]=="B":
                matriz[y][x]+=1
        else:
            if matriz[y-1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x]=="B":
                matriz[y][x]+=1
            if matriz[y-1][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y][x+1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x-1]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x]=="B":
                matriz[y][x]+=1
            if matriz[y+1][x+1]=="B":
                matriz[y][x]+=1
print(' ')
for i in matriz:
    print(*i, sep=' ')
