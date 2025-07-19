import random

# Se hace una función llamafa generar_tablero, al cual le entran tres valores: filas, columnas y minas
def generar_tablero(filas, columnas, minas):
    # Crea una matriz de según los valores con los que se ingresó a la función llena de '■' (casillas ocultas)
    tablero = [['■' for _ in range(columnas)] for _ in range(filas)]
    # se inicializa un contador para saber cuántas minas se han puesto
    minas_colocadas = 0
    # Mientras que no estén todas las minas puestas se entra a este ciclo
    while minas_colocadas < minas:
        # Escoge una fila y columna aleatoria 
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)
        # Si en esa posición no hay una mina todavía, se colocar
        if tablero[f][c] != 'M':
            tablero[f][c] = 'M'
            # Se va aumentando el contador y repetir el ciclo hasta que las minas colocadas sea igual a la cantidad de minas seleccionadas
            minas_colocadas = minas_colocadas + 1
    # Me retorna el tablero con las minas
    return tablero

# Se crea una nueva función para contar las minas que hay alrededor
def contar_minas_alrededor(tablero, f, c):
    # Se crea una lista con todas las direcciones posibles alrededor de cada casilla
    direcciones = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    # Ahora, hacemos un contador de minas
    cuenta = 0
    # con este ciclo for recorremos los índices las casillas vecinas a [i][j], en este caso [f][c]
    for fila_vecina, columna_vecina in direcciones:
        # Ahora declaramos dos variables, estás variables nos permitiran desplazarnos en las filas vecinas para evaluarlas
        nueva_fila = f + fila_vecina
        nueva_columna = c + columna_vecina
        # se verifican tres cosas:
        # primero que el índice donde estamos no es menor a 0, es decir que no se salga del tablero por arriba, además que no sea mayor que la última fila (no se salga por abajo)
        # Ahora, se hace un análisis similar con las columnas. Que no sea menor que 0 (no se sale por la izquierda), y que no sea mayor que la última columna (no se salga por la derecha)
        # Finalmente, si hay una mina en la casilla evaluada y cumple las otras dos condiciones se va actualizando el contador 
        if 0 <= nueva_fila < len(tablero) and 0 <= nueva_columna < len(tablero[0]) and tablero[nueva_fila][nueva_columna] == 'M':
            cuenta = cuenta + 1
    # Finalmente me retorna el contador de minas
    return cuenta

# Definimos otra función llamada revelar, el cual contiene al tablero, al tablero visible, y los índices f,c
def revelar(tablero, visible, f, c):
    # Si (f, c) está fuera de los límites, sale sin hacer nada.
    if not (0 <= f < len(tablero) and 0 <= c < len(tablero[0])):
        return
    # Igualmente se sale si la casilla ya está marcada o revelada
    if visible[f][c] != '■':
        return

    # Si en el tablero oculto esa celda es 'M' (mina), se le asigna también al tablero visible
    if tablero[f][c] == 'M':
        visible[f][c] = 'M'
    else:
        # Se llama a la función contar minas para ver cuántas minas hay alrededor del tablero en la casilla en donde se está evaluando
        cuenta = contar_minas_alrededor(tablero, f, c)
        # Pone ese número en la matriz visible
        visible[f][c] = str(cuenta)
        # Si el contador de minas es 0, entra en este condicional, el cual me servirá para expandir el tablero del buscaminas
        if cuenta == 0:
            # Dentro de este condicional se hace una lista con las casillas alrededor de la casilla evaluada
            direcciones = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            # Por medio de este for recorremos esas direcciones
            for desplazamiento_fila, desplazamiento_columna in direcciones:
                # Hacemos una llamada recursiva a la función revelar
                # Se suma el desplazamiento a la fila y columna actuales para moverse a la casilla vecina
                # de esta manera se propagará la revelación
                # expandiendo el área descubierta hasta que no haya más casillas vacías conectadas.
                revelar(tablero, visible, f + desplazamiento_fila, c + desplazamiento_columna)

# Ahora se hace una nueva función para verificar la victoria
def verificar_victoria(tablero, visible):
    # se recorren las filas
    for f in range(len(tablero)):
        # Y ahora, se recorre cada elemento de las fila (las columnas)
        for c in range(len(tablero[0])):
            # Si se encuentra una casilla que no es mina y aún está oculta, significa que no se ha descubierto todo, por eso retorna False
            if tablero[f][c] != 'M' and visible[f][c] == '■':
                return False
    # De lo contario, retorna True
    return True
