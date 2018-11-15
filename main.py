import random

def generador(alto,ancho,numminas):
    cont=0
    matriz=[]
    if numminas<alto*ancho:
        for i in range(alto):
            matriz.append([0]*ancho)

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
            elif x == 0 and y==0:
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

def Menu():
    running=True
    while running:
        print('Bienvenido a Minasjaj')
        print('Por Favor Elija Dificultad:')
        print('-----------------------------')
        print('1) Facil')
        print('2) Medio')
        print('3) Dificil')
        print('4) Personalizado')
        dificultad=int(input('Ingrese Numero de Dificultad: '))
        if dificultad==1:
            alto=8
            ancho=8
            numminas=10
            running=False
        elif dificultad==2:
            alto=16
            ancho=16
            numminas=40
            running=False
        elif dificultad==3:
            alto=16
            ancho=30
            numminas=99
            running=False
        elif dificultad==4:
            alto=int(input('Numero de Filas: '))
            ancho=int(input('Numero de Columnas: ' ))
            numminas=int(input('Numero de Minas: '))
            running=False
        else: print('Invalid input')
    return (alto, ancho, numminas)


(alto,ancho,numminas)=Menu()
matriz = generador(alto, ancho, numminas)

print(' ')
for i in matriz:
   print(*i, sep=' ')
print(' ')
yi=int(input())
xi=int(input())
rev=[matriz[yi][xi]]

while contador<:
    for y in ['']

def revelador(y,x):
    arriba=0
    abajo=0
    derecha = 0
    izquierda = 0
    while
        yi=y
        xi=x
        if matriz[y][x+1]==0:
            x+=1
            matriz[y][x]-=10
            derecha+=1
        elif matriz [y+1][x]==0:
            y+=1
            matriz[y][x]-=10fF
            arriba+=1
        elif matriz[y-1][x]==0:
            y-=1
            matriz[y][x]-=10
            abajo+=1
        elif matriz[y][x-1]==0:
            y+=1
            matriz[y][x]-=10
            izquierda+=1
        else:

