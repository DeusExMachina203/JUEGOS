
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
