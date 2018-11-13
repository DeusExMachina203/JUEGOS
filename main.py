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
           matriz[y][x]=9
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
print(' ')
for i in matriz:
   print(*i, sep=' ')
for y in range(len(matriz)):
    matriz[y]=[i+10 for i in matriz[y]]
print(' ')
for i in matriz:
   print(*i, sep=' ')


yi=int(input())
xi=int(input())
rev=[matriz[yi][xi]]
for i in rev:
    ynd=matriz.index(i)
    for q in matriz[ynd]:
        xnd=matriz[ynd].index(q)
        if q == 10:
            q=q-10
            if ynd==0 and xnd==0:
                rev.append(matriz[ynd][xnd+1],matriz[ynd+1][xnd],matriz[ynd+1][xnd+1])
            elif ynd==alto-1 and xnd==ancho-1:
                rev.append(matriz[ynd-1][xnd-1], matriz[ynd-1][xnd], matriz[ynd][xnd-1])
            elif ynd == 0 and xnd == ancho - 1:
                rev.append(matriz[ynd][xnd - 1], matriz[ynd+1][xnd-1], matriz[ynd+1][xnd])
            elif ynd == alto - 1 and xnd == 0:
                rev.append(matriz[ynd - 1][xnd], matriz[ynd - 1][xnd+1], matriz[ynd][xnd+1])
            elif ynd == 0:
                rev.append(matriz[ynd][xnd-1], matriz[ynd][xnd+1], matriz[ynd+1][xnd-1],matriz[ynd+1][xnd],matriz[ynd+1][xnd+1])
            elif ynd == alto-1:
                rev.append(matriz[ynd-1][xnd-1], matriz[ynd-1][xnd], matriz[ynd-1][xnd+1],matriz[ynd][xnd-1],matriz[ynd][xnd+1])
            elif xnd == 0:
                rev.append(matriz[ynd-1][xnd], matriz[ynd-1][xnd+1], matriz[ynd][xnd+1],matriz[ynd+1][xnd],matriz[ynd+1][xnd+1])
            elif xnd == ancho-1:
                rev.append(matriz[ynd-1][xnd-1], matriz[ynd-1][xnd], matriz[ynd][xnd-1],matriz[ynd+1][xnd-1],matriz[ynd+1][xnd-1])
            else:
                rev.append(matriz[ynd-1][xnd-1],matriz[ynd-1][xnd],matriz[ynd-1][xnd+1],matriz[ynd][xnd-1],matriz[ynd][xnd+1],matriz[ynd+1][xnd-1],matriz[ynd+1][xnd],matriz[ynd+1][xnd+1],)
        elif q in range(11,19):
            q=q-10

for i in matriz:
   print(*i, sep=' ')

