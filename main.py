import random


def Menu():
    running = True
    while running:
        print('Bienvenido a Minasjaj')
        print('Por Favor Elija Dificultad:')
        print('-----------------------------')
        print('1) Facil')
        print('2) Medio')
        print('3) Dificil')
        print('4) Personalizado')
        dificultad = int(input('Ingrese Numero de Dificultad: '))
        if dificultad == 1:
            alto = 8
            ancho = 8
            numminas = 10
            running = False
        elif dificultad == 2:
            alto = 16
            ancho = 16
            numminas = 40
            running = False
        elif dificultad == 3:
            alto = 16
            ancho = 30
            numminas = 99
            running = False
        elif dificultad == 4:
            alto = int(input('Numero de Filas: '))
            ancho = int(input('Numero de Columnas: '))
            numminas = int(input('Numero de Minas: '))
            if numminas>=alto*ancho or alto<2 or ancho<2 :
                print('')
                print('Invalid input')
                print('')
            else:
                running = False
        else:
            print('Invalid input')
    return (alto, ancho, numminas)


def generador(alto, ancho, numminas):
    cont = 0
    matriz = []

    if numminas < alto * ancho:
        for i in range(alto):
            matriz.append([0] * ancho)

        while cont < numminas:
            x = random.randint(0, ancho - 1)
            y = random.randint(0, alto - 1)
            if matriz[y][x] == 0:
                matriz[y][x] = 9
                cont += 1
            else:
                cont += 0

    for y in range(len(matriz)):
        for x in range(ancho):
            if matriz[y][x] == 9:
                pass
            elif x == 0 and y == 0:
                if matriz[y][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x + 1] == 9:
                    matriz[y][x] += 1
            elif x == ancho - 1 and y == alto - 1:
                if matriz[y - 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y][x - 1] == 9:
                    matriz[y][x] += 1
            elif x == 0 and y == alto - 1:
                if matriz[y - 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y][x + 1] == 9:
                    matriz[y][x] += 1
            elif x == ancho and y == 0:
                if matriz[y][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x] == 9:
                    matriz[y][x] += 1
            elif x == 0:
                if matriz[y - 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x + 1] == 9:
                    matriz[y][x] += 1
            elif x == ancho - 1:
                if matriz[y - 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x] == 9:
                    matriz[y][x] += 1
            elif y == 0:
                if matriz[y][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x + 1] == 9:
                    matriz[y][x] += 1
            elif y == alto - 1:
                if matriz[y - 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y][x + 1] == 9:
                    matriz[y][x] += 1
            else:
                if matriz[y - 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y - 1][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y][x + 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x - 1] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x] == 9:
                    matriz[y][x] += 1
                if matriz[y + 1][x + 1] == 9:
                    matriz[y][x] += 1
    for y in range(len(matriz)):
        matriz[y] = [i + 10 for i in matriz[y]]

    return matriz


def revelar(matriz, y, x, vic):
    vic = 0
    if matriz[y][x] == 10:
        matriz[y][x] = 0
        if y == 0:
            if x == 0:
                if matriz[y][x + 1] == 10:
                    revelar(matriz, y, x + 1, vic)
                if matriz[y + 1][x] == 10:
                    revelar(matriz, y + 1, x, vic)
                if matriz[y + 1][x + 1] == 10:
                    revelar(matriz, y + 1, x + 1, vic)

                if matriz[y][x + 1] in range(11, 19):
                    matriz[y][x + 1] -= 10
                if matriz[y + 1][x] in range(11, 19):
                    matriz[y + 1][x] -= 10
                if matriz[y + 1][x + 1] in range(11, 19):
                    matriz[y + 1][x + 1] -= 10

            elif x == len(matriz[y]) - 1:
                if matriz[y][x - 1] == 10:
                    revelar(matriz, y, x - 1, vic)
                if matriz[y - 1][x - 1] == 10:
                    revelar(matriz, y - 1, x - 1, vic)
                if matriz[y - 1][x] == 10:
                    revelar(matriz, y - 1, x, vic)

                if matriz[y][x - 1] in range(11, 19):
                    matriz[y][x - 1] -= 10
                if matriz[y - 1][x - 1] in range(11, 19):
                    matriz[y - 1][x - 1] -= 10
                if matriz[y - 1][x] in range(11, 19):
                    matriz[y - 1][x] -= 10
            else:
                if matriz[y][x - 1] == 10:
                    revelar(matriz, y, x - 1, vic)
                if matriz[y][x + 1] == 10:
                    revelar(matriz, y, x + 1, vic)
                if matriz[y + 1][x - 1] == 10:
                    revelar(matriz, y + 1, x - 1, vic)
                if matriz[y + 1][x] == 10:
                    revelar(matriz, y + 1, x, vic)
                if matriz[y + 1][x + 1] == 10:
                    revelar(matriz, y + 1, x + 1, vic)

                if matriz[y][x - 1] in range(11, 19):
                    matriz[y][x - 1] -= 10
                if matriz[y][x + 1] in range(11, 19):
                    matriz[y][x + 1] -= 10
                if matriz[y + 1][x - 1] in range(11, 19):
                    matriz[y + 1][x - 1] -= 10
                if matriz[y + 1][x] in range(11, 19):
                    matriz[y + 1][x] -= 10
                if matriz[y + 1][x + 1] in range(11, 19):
                    matriz[y + 1][x + 1] -= 10
        elif y == len(matriz) - 1:
            if x == 0:
                if matriz[y - 1][x] == 10:
                    revelar(matriz, y - 1, x, vic)
                if matriz[y - 1][x + 1] == 10:
                    revelar(matriz, y - 1, x + 1, vic)
                if matriz[y][x + 1] == 10:
                    revelar(matriz, y, x + 1, vic)

                if matriz[y - 1][x] in range(11, 19):
                    matriz[y - 1][x] -= 10
                if matriz[y - 1][x + 1] in range(11, 19):
                    matriz[y - 1][x + 1] -= 10
                if matriz[y][x + 1] in range(11, 19):
                    matriz[y][x + 1] -= 10

            elif x == len(matriz[y]) - 1:
                if matriz[y - 1][x - 1] == 10:
                    revelar(matriz, y - 1, x - 1, vic)
                if matriz[y - 1][x] == 10:
                    revelar(matriz, y - 1, x, vic)
                if matriz[y][x - 1] == 10:
                    revelar(matriz, y, x - 1, vic)

                if matriz[y - 1][x - 1] in range(11, 19):
                    matriz[y - 1][x - 1] -= 10
                if matriz[y - 1][x] in range(11, 19):
                    matriz[y - 1][x] -= 10
                if matriz[y][x - 1] in range(11, 19):
                    matriz[y][x - 1] -= 10
            else:
                if matriz[y][x - 1] == 10:
                    revelar(matriz, y, x - 1, vic)
                if matriz[y - 1][x] == 10:
                    revelar(matriz, y - 1, x, vic)
                if matriz[y - 1][x + 1] == 10:
                    revelar(matriz, y - 1, x + 1, vic)
                if matriz[y][x - 1] == 10:
                    revelar(matriz, y, x - 1, vic)
                if matriz[y][x + 1] == 10:
                    revelar(matriz, y, x + 1, vic)

                if matriz[y][x - 1] in range(11, 19):
                    matriz[y][x - 1] -= 10
                if matriz[y - 1][x] in range(11, 19):
                    matriz[y - 1][x] -= 10
                if matriz[y - 1][x + 1] in range(11, 19):
                    matriz[y - 1][x + 1] -= 10
                if matriz[y][x - 1] in range(11, 19):
                    matriz[y][x - 1] -= 10
                if matriz[y][x + 1] in range(11, 19):
                    matriz[y][x + 1] -= 10
        else:
            if x == 0:
                if matriz[y - 1][x] == 10:
                    revelar(matriz, y - 1, x, vic)
                if matriz[y - 1][x + 1] == 10:
                    revelar(matriz, y - 1, x + 1, vic)
                if matriz[y][x + 1] == 10:
                    revelar(matriz, y, x + 1, vic)
                if matriz[y + 1][x] == 10:
                    revelar(matriz, y + 1, x, vic)
                if matriz[y + 1][x + 1] == 10:
                    revelar(matriz, y + 1, x + 1, vic)

                if matriz[y - 1][x] in range(11, 19):
                    matriz[y - 1][x] -= 10
                if matriz[y - 1][x + 1] in range(11, 19):
                    matriz[y - 1][x + 1] -= 10
                if matriz[y][x + 1] in range(11, 19):
                    matriz[y][x + 1] -= 10
                if matriz[y + 1][x] in range(11, 19):
                    matriz[y + 1][x] -= 10
                if matriz[y + 1][x + 1] in range(11, 19):
                    matriz[y + 1][x + 1] -= 10

            elif x == len(matriz[y]) - 1:
                if matriz[y - 1][x - 1] == 10:
                    revelar(matriz, y - 1, x - 1, vic)
                if matriz[y - 1][x] == 10:
                    revelar(matriz, y - 1, x, vic)
                if matriz[y][x - 1] == 10:
                    revelar(matriz, y, x - 1, vic)
                if matriz[y + 1][x - 1] == 10:
                    revelar(matriz, y + 1, x - 1, vic)
                if matriz[y + 1][x] == 10:
                    revelar(matriz, y + 1, x, vic)

                if matriz[y - 1][x - 1] in range(11, 19):
                    matriz[y - 1][x - 1] -= 10
                if matriz[y - 1][x] in range(11, 19):
                    matriz[y - 1][x] -= 10
                if matriz[y][x - 1] in range(11, 19):
                    matriz[y][x - 1] -= 10
                if matriz[y + 1][x - 1] in range(11, 19):
                    matriz[y + 1][x - 1] -= 10
                if matriz[y + 1][x] in range(11, 19):
                    matriz[y + 1][x] -= 10

            else:

                if matriz[y - 1][x - 1] == 10:
                    revelar(matriz, y - 1, x - 1, vic)
                if matriz[y - 1][x] == 0:
                    revelar(matriz, y - 1, x, vic)
                if matriz[y - 1][x + 1] == 10:
                    revelar(matriz, y - 1, x + 1, vic)
                if matriz[y][x - 1] == 10:
                    revelar(matriz, y, x - 1, vic)
                if matriz[y][x + 1] == 10:
                    revelar(matriz, y, x + 1, vic)
                if matriz[y + 1][x - 1] == 10:
                    revelar(matriz, y + 1, x - 1, vic)
                if matriz[y + 1][x] == 10:
                    revelar(matriz, y + 1, x, vic)
                if matriz[y + 1][x + 1] == 10:
                    revelar(matriz, y + 1, x + 1, vic)

                if matriz[y - 1][x - 1] in range(11, 19):
                    matriz[y - 1][x - 1] -= 10
                if matriz[y - 1][x] in range(11, 19):
                    matriz[y - 1][x] -= 10
                if matriz[y - 1][x + 1] in range(11, 19):
                    matriz[y - 1][x + 1] -= 10
                if matriz[y][x - 1] in range(11, 19):
                    matriz[y][x - 1] -= 10
                if matriz[y][x + 1] in range(11, 19):
                    matriz[y][x + 1] -= 10
                if matriz[y + 1][x - 1] in range(11, 19):
                    matriz[y + 1][x - 1] -= 10
                if matriz[y + 1][x] in range(11, 19):
                    matriz[y + 1][x] -= 10
                if matriz[y + 1][x + 1] in range(11, 19):
                    matriz[y + 1][x + 1] -= 10
        return matriz, vic

    if matriz[y][x] in range(11, 19):
        matriz[y][x] -= 10

        return matriz, vic

    if matriz[y][x] == 19:
        print('-----------------------------')

        print('Selecciono una bomba')

        print('')

        print('El sistema exploto')

        print('')

        print('Esto es totalmente su culpa')

        print('')

        print('Que tiene 5 años?')

        print('')

        print('Aprenda a jugar!')

        print('')

        print('Dele a Run para jugar de nuevo')

        print('-----------------------------')

        vic=1
        game_over(matriz)
        return matriz, vic
    else:
        print('')
        print('Invalid input')
        return matriz, vic



def bandera(matriz, y, x):
    if matriz[y][x] > 10 and matriz[y][x] < 20:
        matriz[y][x] += 10
    elif matriz[y][x] > 19:
        matriz[y][x] -= 10

    return matriz


def game_over(matriz):
    for i in range(len(matriz)):
        for z in range(len(matriz[i])):
            if matriz[i][z] == 19:
                matriz[i][z] -= 10
    print('-----------------------------')
    print('Perdiste')
    print('-----------------------------')
    face(matriz, len(matriz), len(matriz[0]))

def victoria(matriz,numminas,vic):
    contador=0
    vic=0
    for i in range(len(matriz)):
        for z in range(len(matriz[i])):
            if matriz[i][z] in range(10,30):
                contador+=1
    if contador==numminas:
        print('')
        face(matriz, len(matriz), len(matriz[0]))
        print('FELICIDADES!!!')
        print('USTED HA GANADO')
        vic=1
    return vic

def face(matriz, alto, ancho):
    skin = []
    for i in range(alto):
        skin.append([0] * ancho)
    for i in range(len(skin)):
        for o in range(len(skin[i])):
            if matriz[i][o] in range(10,20):
                skin[i][o] = '■'
            elif matriz[i][o] in range(20,30):
                skin[i][o] = '🅵'
            elif matriz[i][o] == 0:
                skin[i][o] = '□'
            elif matriz[i][o] == 1:
                skin[i][o] = '①'
            elif matriz[i][o] == 2:
                skin[i][o] = '②'
            elif matriz[i][o] == 3:
                skin[i][o] = '③'
            elif matriz[i][o] == 4:
                skin[i][o] = '④'
            elif matriz[i][o] == 5:
                skin[i][o] = '⑤'
            elif matriz[i][o] == 6:
                skin[i][o] = '⑥'
            elif matriz[i][o] == 7:
                skin[i][o] = '⑦'
            elif matriz[i][o] == 8:
                skin[i][o] = '⑧'
            elif matriz[i][o] == 9:
                skin[i][o] = '☒'

    print(' ')
    for i in skin:
        print(*i, sep="")
    print(' ')


def main():
    (alto, ancho, numminas) = Menu()
    matriz = generador(alto, ancho, numminas)
    vic = 0


    face(matriz, alto, ancho)
    while True and vic!=1:

        print('1) Revelar')
        print('2) Marcar')
        print('-----------------------------')
        opcion = int(input('Elija Opcion: '))

        if opcion in range(1, 3):
            if opcion == 1:
                y = int(input('Elija Fila de la casilla a Revelar: ')) - 1
                x = int(input('Elija Columna de la casilla a Revelar: ')) - 1
                if y not in range(len(matriz)) or x not in range(len(matriz[0])):
                    print('Invalid input')
                elif matriz[y][x] in range(0,9) or matriz[y][x] in range(20,30) and y not in range(len(matriz)) and x not in range(len(matriz[y])):
                    print('')
                    print('Invalid input')
                else:
                    matriz, vic = revelar(matriz, y, x, vic)
                    if vic == 1:
                        break
                    else: vic=victoria(matriz,numminas,vic)
                    if vic==1:
                        break

            elif opcion == 2:
                y = int(input('Elija Fila de la casilla a Marcar: ')) - 1
                x = int(input('Elija Columna de la casilla a Marcar: ')) - 1
                if y>len(matriz) or x>len(matriz[0]):
                    print('')
                    print('Invalid input')
                elif matriz[y][x] in range(0, 9):
                    print('')
                    print('Invalid input')
                else:
                    if y in range(len(matriz)) and x in range(len(matriz[y])):
                        matriz = bandera(matriz, y, x)
                    else:
                        print('')
                        print('Invalid input')
            else:
                print('')
                print('Invalid input')

        else:
            print('')
            print('Invalid input')

        face(matriz, alto, ancho)


main()
