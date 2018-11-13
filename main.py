import random

alto=int(input())
ancho=int(input())
numminas=int(input())
pene=[]
def generador(alto,ancho,numminas):
    cont=0
    matriz=[]
    if numminas<alto*ancho:
        for i in range(alto):
            matriz.append([0]*ancho)
            pene.append([0]*ancho)

        while cont<numminas:
            x=random.randint(0,ancho-1)
            y=random.randint(0,alto-1)
            if matriz[y][x]==0:
                matriz[y][x]=9
                cont+=1
            else:
                cont+=0

    for y in range(len(matriz)):
        for x in range(ancho):
            if matriz[y][x]==9:
                pass
            elif x==0 and y==0:
                if matriz[y][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x+1]==9:
                    matriz[y][x]+=1
            elif x==ancho-1 and y==alto-1:
                if matriz[y-1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x]==9:
                    matriz[y][x]+=1
                if matriz [y][x-1]==9:
                    matriz[y][x]+=1
            elif x==0 and y==alto-1:
                if matriz[y-1][x]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y][x+1]==9:
                    matriz[y][x]+=1
            elif x==ancho and y==0:
                if matriz[y][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x]==9:
                    matriz[y][x]+=1
            elif x==0:
                if matriz[y-1][x]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x+1]==9:
                    matriz[y][x]+=1
            elif x==ancho-1:
                if matriz[y-1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x]==9:
                    matriz[y][x]+=1
                if matriz[y][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x]==9:
                    matriz[y][x]+=1
            elif y==0:
                if matriz[y][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x+1]==9:
                    matriz[y][x]+=1
            elif y==alto-1:
                if matriz[y-1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y][x+1]==9:
                    matriz[y][x]+=1
            else:
                if matriz[y-1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x]==9:
                    matriz[y][x]+=1
                if matriz[y-1][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y][x+1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x-1]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x]==9:
                    matriz[y][x]+=1
                if matriz[y+1][x+1]==9:
                    matriz[y][x]+=1
    for y in range(len(matriz)):
        matriz[y]=[i+10 for i in matriz[y]]


    return matriz
matriz = generador(alto,ancho, numminas)
