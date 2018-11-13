x=0
for y in range(matriz):
    if x==0 and y==0:
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
    x+=1
