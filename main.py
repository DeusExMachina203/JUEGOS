
import random

def generador(matriz,alto,ancho):
    for i in range(alto):
        matriz.append([0]*ancho)
        return matriz

alto=int(input())
ancho=int(input())
numminas=int(input())
matriz=[]
cont=0
pene=[]
if numminas<alto*ancho:
    for i in range(alto):
        matriz.append([0]*ancho)
        pene.append([0]*ancho)

    while cont<numminas:
        x=random.randint(0,ancho-1)
        y=random.randint(0,alto-1)
        if matriz[y][x]==0:
            matriz[y][x]='B'
            cont+=1
        else:
            cont+=0

    for x in matriz:
        print(*x, sep=" ")
else:
    print('invalid input')
print(' ')
for x in pene:
    print(*x, sep=' ')
for y in range(len(matriz)):
    for x in range(ancho):
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
