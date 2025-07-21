# Se importa pygame y sys, los cuales nos ayudarán con la interfaz gráfica del juego
import pygame
import sys
# Se importa random, el cual nos ayudará a generar de forma aleatoria las minas en el tablero
import random

pygame.init()

# Se declara e inicialiaza el nombre de mi pantalla principal del juego 
pantalla_actual = "menu"

# Se declaran tados los rectángulos que vamos a usar en el programa como botones
# Primero se le dice sus posiciones en el eje X y Y, para luego indicarle el ancho y alto
boton_jugar = pygame.Rect(100, 520, 200, 50)
boton_instrucciones = pygame.Rect(500, 520, 250, 50)
boton_principiante = pygame.Rect(80, 180, 250, 50)
boton_intermedio = pygame.Rect(280, 380, 250, 50)
boton_experto = pygame.Rect(480, 180, 250, 50)
boton_continuar_2 = pygame.Rect(270, 500, 250, 50)
boton_quitar = pygame.Rect(100, 520, 200, 50)
boton_volver = pygame.Rect(500, 520, 200, 50)

# Se declaran todos los colores a usar a lo largo del programa en RGB
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
BLANCO = (255, 255, 255)
GRIS_OSCURO = (66, 73, 73)
NARANJA = (254, 123, 0)
AZUL = (0, 142, 254)
VERDE = (73, 254, 0)
AZUL_CLARO = (0, 153, 255)
ROJO_OSCURO = (200, 0, 0)
ROJO_BRILLANTE = (254, 19, 0)

# Tamaño de la pantalla
ancho_pantalla : int = 800 # Se define una constante como entero, la cual será la encargada del ancho de nustra pantalla
alto_pantalla : int = 600 # Esta constante será la encargada del largo de nuestra pantalla
PANTALLA = pygame.display.set_mode((ancho_pantalla , alto_pantalla)) # En esta linea creamos nuestra pantalla principal, la cual será de 800 x 600
pygame.display.set_caption("Mine Hunter 3000 🥊💣💥") # Escribimos el nombre del juego, el cual aparecerá en la esquina superior derecha de la pantalla

# Cargamos la imagen de fondo en nuestra pantalla princiapl, la cual está en el la carpeta imágenes
Fondo = pygame.image.load("imagenes/fondo.png").convert() 
Fondo = pygame.transform.scale(Fondo, (ancho_pantalla, alto_pantalla))
# Inicializamos reloj y la cantidad de fps, para que las animaciones no vayan con la máxima velocidad posible, sino que sea controlable
FPS : int = 200
RELOJ = pygame.time.Clock()

# Título principal, una vez descargada la fuente, le indicamos la carpeta y el tamaño de la fuente
fuente_titulo = pygame.font.Font("letras/Fixedsys62.ttf", 80)
# Usamos dos tipos de texto, uno con negro y otro con blanco para que se superpongan los textos y se vea sombreado
texto_sombra = fuente_titulo.render("Mine Hunter 3000", True, (NEGRO))
texto_titulo = fuente_titulo.render("Mine Hunter 3000", True, (BLANCO))
# Dibujamos un rectángulo, el cual será de color blanco y se le dan sus coordenadas y dimensiones (alto y largo)
pygame.draw.rect(PANTALLA, (BLANCO), (150, 300, 500, 200))

# Se declaran todos los fondos e íconos dentro del juego a usar
imagen_bandera = pygame.image.load("imagenes/bandera.png").convert_alpha()
imagen_mina = pygame.image.load("imagenes/mina.png").convert_alpha()
Fondo_derrota = pygame.image.load("imagenes/derrota.png").convert()
Fondo_victoria = pygame.image.load("imagenes/victoria.png").convert()

# Obtener rectángulo para centrar
rect_titulo = texto_titulo.get_rect(center=(ancho_pantalla//2, 100))

# Se declaran e inicializan algunas variables a usar, como coordenadas, cantidad de filas y columnas, imágenes y listas que serán parte de las matrices
desplazamiento_x: int = 0
set_x : int
set_y : int
size = 50
imagen_bandera = pygame.transform.scale(imagen_bandera, (size - 10, size - 10))
imagen_mina = pygame.transform.scale(imagen_mina, (size - 10, size - 10))
tablero = []
visible = []
FILAS: int = 0
COLUMNAS: int = 0
MINAS: int = 0

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


# El programa entrará a un ciclo para que la pantalla se esté mostrando continuamente
while True:
    # Con el desplazamiento definido cada vez que el programa entre de nuevo el el ciclo se le restará 1, y se reiniciará cuando sea menor o igual al ancho de la pantalla
    desplazamiento_x = desplazamiento_x - 1
    if desplazamiento_x <= -ancho_pantalla:
        desplazamiento_x = 0
    # Se asigna un ciclo for, el cual recorre cada evento que sucede en el programa como dar un click, cerrar una ventana, etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Este condicional entra si el evento obtenido fue hacer click 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # El mouse_pos detecta en qué parte de la pantalla se hizo el click
            mouse_pos = pygame.mouse.get_pos()

            # Por medio de un condicional se le pregunta al flujo del programa que entre si está en la pantalla principal
            if pantalla_actual == "menu":
                # Si está dentro de la pantalla evalua una nueva condición, gracias al collidepoint, se evalua si le le hizo click al rectángulo, botón_jugar
                if boton_jugar.collidepoint(mouse_pos):
                    # Si se le hizo click a este, ahora se ingresará a la nueva pantalla llamada juego
                    pantalla_actual = "juego"
                 # Si está dentro de la pantalla evalua una nueva condición, gracias al collidepoint, se evalua si le le hizo click al rectángulo, botón_instrucciones
                elif boton_instrucciones.collidepoint(mouse_pos):
                    # Si se hizo click dentro de este rectángulo, el juego mostrará la pantalla donde se darán las instrucciones
                    pantalla_actual = "instrucciones"

            # Ahora, si estamos en la pantalla llamada instrucciones, solo tenemos una opción, esta es hacer click en jugar
            elif pantalla_actual == "instrucciones":
                # Si se presiona jugar, se entrará a la pantalla juego
                if boton_continuar_2.collidepoint(mouse_pos):
                    pantalla_actual = "juego"

            # Una vez en la pantalla del juego, el programa controlará los siguientes eventos si hacemos click
            elif pantalla_actual == "juego":
                # si hacemos click dentro del botón de principiante, pasará lo siguiente
                if boton_principiante.collidepoint(mouse_pos):
                    # Se pasará a una nueva pantalla, donde el juego contará con rectángulos, que serán el tablero del juego
                    # Tendrá, 4 filas, 4 columnas con 3 minas. Size controla el tamaño, set_x y set_y controlarán su posición en X y Y respectivamente 
                    FILAS = 4
                    COLUMNAS = 4 
                    MINAS = 3
                    size = 50
                    set_x, set_y = 300, 200
                # si hacemos click dentro del botón de dificultad intermedia, pasará lo siguiente
                elif boton_intermedio.collidepoint(mouse_pos):
                    # Se pasará a una nueva pantalla, donde el juego contará con rectángulos, que serán el tablero del juego
                    # Tendrá, 8 filas, 8 columnas con 13 minas. Size controla el tamaño, set_x y set_y controlarán su posición en X y Y respectivamente 
                    FILAS = 8
                    COLUMNAS = 8 
                    MINAS = 13
                    size = 45
                    set_x, set_y = 250, 180
                # si hacemos click dentro del botón de dificultad experto, pasará lo siguiente
                elif boton_experto.collidepoint(mouse_pos):
                    # Se pasará a una nueva pantalla, donde el juego contará con rectángulos, que serán el tablero del juego
                    # Tendrá, 8 filas, 8 columnas con 13 minas. Size controla el tamaño, set_x y set_y controlarán su posición en X y Y respectivamente 
                    FILAS = 16
                    COLUMNAS = 16 
                    MINAS = 50
                    size = 30
                    set_x, set_y = 160, 100
                else:
                    continue  # Si no hizo clic en ningún botón de dificultad, omite lo demás

                # Cargamos la bandera como una imagen png con image.load, luego con pygame.scale cambiamos su tamaño para que se ajuste a las casillas del juego
                imagen_bandera = pygame.transform.scale(
                    pygame.image.load("imagenes/bandera.png").convert_alpha(),
                    (size - 10, size - 10)
                )
                # Cargamos la bomba como una imagen png con image.load, luego con pygame.scale cambiamos su tamaño para que se ajuste a las casillas del juego
                imagen_mina = pygame.transform.scale(
                    pygame.image.load("imagenes/mina.png").convert_alpha(),
                    (size - 10, size - 10)
                )

                # Ahora llamamos a la función generar tablero con las filas o columnas seleccionadas según la dificultad
                tablero = generar_tablero(FILAS, COLUMNAS, MINAS)
                # Ahora empieza a generar una matriz con las filas y columnas indicadas, cada celda inicia como ■
                visible = [['■' for _ in range(COLUMNAS)] for _ in range(FILAS)]
                # Cambia el estado de la pantalla actual a partida
                pantalla_actual = "partida"
            # Una vez en la pantalla partida, entra al siguiente condicional
            elif pantalla_actual == "partida":
                # Gracias al get_pos, a través de las variables mouse_x y mouse_y, se guardan las coordenadas donde se hizo un click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Ahora se recorren las filas
                for f in range(FILAS):
                    # Con este ciclo for se recorre cada elemento de la fila fijada anteriormente
                    for c in range(COLUMNAS):
                        # En esta linea, se contruye un rectángulo (sin dibujarlo) para ubicar su posición en pantalla, según su posición en el tablero (x,y) y cuánto debe moverse en el mismo según la fila y la columna
                        rect = pygame.Rect(set_x + c * size, set_y + f * size, size, size)
                        # Ahora se detecta en qué tecla se hizo click
                        if rect.collidepoint(mouse_x, mouse_y):
                            # Si el clik realizado fue un click izquierdo, se entrará al siguiente condicional
                            if event.button == 1:
                                # Ahora entramos a este condicional si presionamos una casilla donde no haya una bandera puesta
                                if visible[f][c] != 'F':
                                    # revelamos esa casilla
                                    revelar(tablero, visible, f, c)
                                    # Si la casilla es una "M" (mina), pasamos inmediatamente a la pantalla de derrota
                                    if tablero[f][c] == 'M':
                                        pantalla_actual = "derrota"
                                    # Ahora, se llama a la función verificar_victoria, donde revisa si todas las casillas sin mina fueron descubiertas, de ser así nos llevará a la pantalla victoria
                                    elif verificar_victoria(tablero, visible):
                                        pantalla_actual = "victoria"
                            # Si el evento fue dar un clic derecho, se entrará al siguiente condicional
                            elif event.button == 3:
                                # Si la casilla donde dimos click, era una casilla sin revelar, se pone una bandera
                                if visible[f][c] == '■':
                                    visible[f][c] = 'F'
                                # Si la casilla donde damos el click, era una casilla con bandera, ahora se quita esa bandera
                                elif visible[f][c] == 'F':
                                    visible[f][c] = '■'

            # Ahora controlamos un evento en la pantalla victoria y derrota, por medio de un condicional
            if pantalla_actual == "victoria" or pantalla_actual == "derrota":
                # Ahora si el clik que realizamos, está sobre el rectángulo declarado como boton_volver, nos lleva a la pantalla juego
                if boton_volver.collidepoint(mouse_pos):
                    # Ir a pantalla de escoger dificultad
                    pantalla_actual = "juego"
                # Si el click realizado está sobre el botón declarado como boton_quitar, terminaremos el programa
                elif boton_quitar.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    # Una vez configurados todos los eventos, seguimos con la interfaz gráfica. Si estamos es la pantalla menu entramos dentro de este condicional
    if pantalla_actual == "menu":
        # Se dibuja el fondo dos veces, la primera vez se va desplazando a la izquierda
        PANTALLA.blit(Fondo, (desplazamiento_x, 0))
        # esta segunda vez aparece seguidamente del anterior fondo, dando el efecto de un fondo infinito
        PANTALLA.blit(Fondo, (desplazamiento_x + ancho_pantalla, 0))
        # Ahora se crea un rectángulo de color blanco, con las coordenadas 150, 300 píxeles. 500 de ancho y 200 de largo
        pygame.draw.rect(PANTALLA, (BLANCO), (150, 300, 500, 200))
        # Se carga el tipo de letra y la fuente tendrá un tamaño de 25
        fuente_texto = pygame.font.Font("letras/Fixedsys62.ttf", 25)
        # Ahora, se escriben tres lineas de texto de color negro
        linea1 = fuente_texto.render("¡Hola! nosotros somos Code Craft,", True, (NEGRO))
        linea2 = fuente_texto.render("Este es nuestro buscaminas retro.", True, (NEGRO))
        linea3 = fuente_texto.render("Ten cuidado con las minas!", True, (NEGRO))
        # Se les indica las coordenadas (x,y) de la linea en pantalla
        PANTALLA.blit(linea1, (170, 320))
        PANTALLA.blit(linea2, (170, 360))
        PANTALLA.blit(linea3, (170, 400))
        # Se dibuja primero el título sombreado desplazado dos pixeles más para dar efecto de sombra
        PANTALLA.blit(texto_sombra, (rect_titulo.x + 2, rect_titulo.y + 2))
        # Luego se dibuja el título principal blanco centrado encima de la sombra
        PANTALLA.blit(texto_titulo, rect_titulo)
        # Se dibujan los rectángulos que representan los botones de "Continuar" e "Instrucciones" en color gris oscuro
        pygame.draw.rect(PANTALLA, (GRIS_OSCURO), boton_jugar)
        pygame.draw.rect(PANTALLA, (GRIS_OSCURO), boton_instrucciones)
        # Ahora se escriben dos lineas de texto: continuar e instrucciones de color blanco
        texto_jugar = fuente_texto.render("Continuar", True, (BLANCO))
        texto_salir = fuente_texto.render("Instrucciones", True, (BLANCO))
        # Se ubican esas lineas de texto dentro de su respectivo rectángulo aumentando 50 pixeles en X y en Y respecto al rectángulo para que los dos textos queden centrados
        PANTALLA.blit(texto_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
        PANTALLA.blit(texto_salir, (boton_instrucciones.x + 50, boton_instrucciones.y + 10))

    # Si estamos en la pantalla de instrucciones el programa entrará a este condicional
    elif pantalla_actual == "instrucciones":
        # Se dibuja el fondo dos veces, la primera vez se va desplazando a la izquierda
        PANTALLA.blit(Fondo, (desplazamiento_x, 0))
         # esta segunda vez aparece seguidamente del anterior fondo, dando el efecto de un fondo infinito
        PANTALLA.blit(Fondo, (desplazamiento_x + ancho_pantalla, 0))
        # Se carga el tipo de letra y la fuente tendrá un tamaño de80
        fuente_titulo = pygame.font.Font("letras/Fixedsys62.ttf", 80)
        # Se agregan dos textos (Minu Hunter), uno de color blaco y otro de color negro
        texto_sombra = fuente_titulo.render("Mine Hunter", True, (NEGRO))
        texto_titulo = fuente_titulo.render("Mine Hunter", True, (BLANCO))
        # Se posicionan en la pantalla de tal manera que da la sensación de que el texto negro es una sombre del blanco
        PANTALLA.blit(texto_sombra, (150 + 2, 100 + 2))
        PANTALLA.blit(texto_titulo, (150, 100))
        # Se hace un rectángulo de color blanco con las respectivas coordenadas y dimensiones
        pygame.draw.rect(PANTALLA, (BLANCO), (100, 200, 600, 350))
        # Se carga el tipo de letra y el tamaño de fuente del texto que tendrá ese rectángulo
        fuente_texto = pygame.font.Font("letras/Fixedsys62.ttf", 20)
        # Se escriben 5 lineas de color negro y con la misma posición en el eje x (a excepción de la última)
        PANTALLA.blit(fuente_texto.render("Haz clic en las casillas para descubrirlas sin explotar", True, (NEGRO)), (130, 220))
        PANTALLA.blit(fuente_texto.render("una mina. Usa los números para saber cuántas minas hay", True, (NEGRO)), (130, 260))
        PANTALLA.blit(fuente_texto.render("alrededor y marca las que encuentres con banderas. Gana", True, (NEGRO)), (130, 300))
        PANTALLA.blit(fuente_texto.render("cuando descubras todas las casillas seguras.", True, (NEGRO)), (130, 340))
        PANTALLA.blit(fuente_texto.render("Good luck!!!", True, (NEGRO)), (330, 440))
        # Se crea otro rectángulo de color naranja, el cual será un botón de continuar controlado por el evento ya definido anteriormente.
        pygame.draw.rect(PANTALLA, (NARANJA), boton_continuar_2)
        # Cargamos el tipo de letra y tamaño de fuente
        texto_jugar = pygame.font.Font("letras/Fixedsys62.ttf", 25).render("Continuar", True, (BLANCO))
        # Ubicamos el texto, de tal manera que quede centrado en el rectángulo anteriormente dibujado
        PANTALLA.blit(texto_jugar, (boton_continuar_2.x + 70, boton_continuar_2.y + 10))

    # Si estamos en la pantalla juego, entraremos a este condicional
    elif pantalla_actual == "juego":
        # Se dibuja el fondo dos veces, la primera vez se va desplazando a la izquierda
        PANTALLA.blit(Fondo, (desplazamiento_x, 0))
        # esta segunda vez aparece seguidamente del anterior fondo, dando el efecto de un fondo infinito
        PANTALLA.blit(Fondo, (desplazamiento_x + ancho_pantalla, 0))
        # Se carga el tipo de letra y el tamaño de fuente del texto que se escribirá dentro de un rectángulo
        fuente_titulo = pygame.font.Font("letras/Fixedsys62.ttf", 50)
        # Se agregan dos textos (Mine Hunter), uno de color blaco y otro de color negro
        texto_sombra = fuente_titulo.render("Escoge una dificultad", True, (NEGRO))
        texto_titulo = fuente_titulo.render("Escoge una dificultad", True, (BLANCO))
        # Se posicionan en la pantalla de tal manera que da la sensación de que el texto negro es una sombre del blanco
        PANTALLA.blit(texto_sombra, (152, 102))
        PANTALLA.blit(texto_titulo, (150, 100))
        # Se crean tres rectas con los colores y dimensiones ya definidos al inicio del programa, estos serán controlados por un evento de click ya definido anteriormente
        pygame.draw.rect(PANTALLA, (AZUL), boton_principiante)
        pygame.draw.rect(PANTALLA, (VERDE), boton_intermedio)
        pygame.draw.rect(PANTALLA, (ROJO_BRILLANTE), boton_experto)
        # Se carga el tipo de letra y tamaño de la fuente
        fuente_texto = pygame.font.Font("letras/Fixedsys62.ttf", 25)
        # Se escribe el texto que llevará, posicionando todo de tal manera que quede centrado respecto al rectángulo hecho
        PANTALLA.blit(fuente_texto.render("Principiante", True, (BLANCO)), (boton_principiante.x + 50, boton_principiante.y + 10))
        pygame.draw.rect(PANTALLA, (BLANCO), (100, 250, 200, 100))
        PANTALLA.blit(fuente_texto.render("Tablero 4 x 4", True, (NEGRO)), (120, 270))
        PANTALLA.blit(fuente_texto.render("3 minas", True, (NEGRO)), (120, 310))
        PANTALLA.blit(fuente_texto.render("Intermedio", True, (BLANCO)), (boton_intermedio.x + 50, boton_intermedio.y + 10))
        pygame.draw.rect(PANTALLA, (BLANCO), (300, 450, 200, 100))
        PANTALLA.blit(fuente_texto.render("Tablero 8 x 8", True, (NEGRO)), (310, 460))
        PANTALLA.blit(fuente_texto.render("13 minas", True, (NEGRO)), (310, 500))
        PANTALLA.blit(fuente_texto.render("Experto", True, (BLANCO)), (boton_experto.x + 70, boton_experto.y + 10))
        pygame.draw.rect(PANTALLA, (BLANCO), (500, 250, 200, 100))
        PANTALLA.blit(fuente_texto.render("Tablero 16 x 16", True, (NEGRO)), (500, 270))
        PANTALLA.blit(fuente_texto.render("50 minas", True, (NEGRO)), (520, 310))

    # Si nos encontramos en la pantalla partida, entraremos a este condicional
    elif pantalla_actual == "partida":
        # Se dibuja el fondo dos veces, la primera vez se va desplazando a la izquierda
        PANTALLA.blit(Fondo, (desplazamiento_x, 0))
        # esta segunda vez aparece seguidamente del anterior fondo, dando el efecto de un fondo infinito
        PANTALLA.blit(Fondo, (desplazamiento_x + ancho_pantalla, 0))
        # Se carga el tipo de letra y el tamaño de fuente del texto que se escribirá dentro de un rectángulo
        fuente_titulo = pygame.font.Font("letras/Fixedsys62.ttf", 40)
        # Se agregan dos textos (Mine Hunter), uno de color blaco y otro de color negro
        texto_sombra = fuente_titulo.render("Mine Hunter 3000", True, (NEGRO))
        texto_titulo = fuente_titulo.render("Mine Hunter 3000", True, (BLANCO))
        # Se posicionan en la pantalla de tal manera que da la sensación de que el texto negro es una sombre del blanco
        PANTALLA.blit(texto_sombra, (260 + 2, 30 + 2))
        PANTALLA.blit(texto_titulo, (260, 30))
        # Con ayuda de este ciclo for, recorremos las filas
        for f in range(FILAS):
            # Luego pasamos a elemento por elemento de la fila en la que estamos
            for c in range(COLUMNAS):
                # Ahora se dibuja un rectángulo, el cual estará poscicionado donde está el tablero en x o y, desplazado hacia la derecha o abajo, dependiendo de la fila y columna
                rect = pygame.Rect(set_x + c * size, set_y + f * size, size, size)
                # Ahora se le da color a esos rectángulos, uno será gris y se le da un borde de 2 de grosor de color negro
                pygame.draw.rect(PANTALLA, (GRIS), rect)
                pygame.draw.rect(PANTALLA, (NEGRO), rect, 2)
                # Se define el tablero visible como letra
                letra = visible[f][c]
                # Si la celda ya ha sido revelada o marcada se entrará al condicional
                if letra != '■':
                    # Si la celda está marcada por F (contralado por el evento explicado anteriormente), se coloca la iamgen de la bandera de tal manera que quede ubicado en el cuadrado
                    if letra == 'F':
                        PANTALLA.blit(imagen_bandera, (rect.x + 5, rect.y + 5))
                    # Si la celda, tiene una mina, se dibuja la imagen de la mina. ubicándola de tal manera que quede dentro de la celda
                    elif letra == 'M':
                        PANTALLA.blit(imagen_mina, (rect.x + 5, rect.y + 5))
                    # Si no es bandera ni mina, significa que tiene un número. Se renderiza el número con una fuente proporcional al tamaño de la celda (size * 0.5).
                    else:
                        texto = pygame.font.Font("letras/Fixedsys62.ttf", int(size * 0.5)).render(letra, True, (NEGRO))
                        PANTALLA.blit(texto, (rect.x + 15, rect.y + 10))

    # Si el usuario ha ganado entrará a este condicional
    elif pantalla_actual == "victoria":
        # Se dibuja un nuevo fondo dos veces, la primera vez se va desplazando a la izquierda
        PANTALLA.blit(Fondo_victoria, (desplazamiento_x, 0))
        # esta segunda vez aparece seguidamente del anterior fondo, dando el efecto de un fondo infinito
        PANTALLA.blit(Fondo_victoria, (desplazamiento_x + ancho_pantalla, 0))
        # Se escriben dos texto de tal manera que como antes, quede el de color negro como sombra del blanco
        texto_sombra = fuente_titulo.render("You are way too good!!", True, (NEGRO))
        texto_titulo = fuente_titulo.render("You are way too good!!", True, (BLANCO))
        PANTALLA.blit(texto_sombra, (210 + 2, 70 + 2))
        PANTALLA.blit(texto_titulo, (210, 70))
        # Se dibujan dos rectángulos, los cuales serán botonoes, ya controlados anteriormente como eventos
        pygame.draw.rect(PANTALLA, (AZUL_CLARO), boton_volver)
        pygame.draw.rect(PANTALLA, (ROJO_OSCURO), boton_quitar)
        # Escribimos los textos que tendrán estos botonos
        texto_volver = fuente_texto.render("Jugar de nuevo", True, (BLANCO))
        texto_quitar = fuente_texto.render("Salir", True, (BLANCO))
        # Se posicionan de tal manera que queden dentro del su respectivo rectángulo
        PANTALLA.blit(texto_volver, (boton_volver.x + 10, boton_volver.y + 10))
        PANTALLA.blit(texto_quitar, (boton_quitar.x + 70, boton_quitar.y + 10))

    # Si el usuario perdió, entrará en este condicional
    elif pantalla_actual == "derrota":
        # Se dibuja un nuevo fondo dos veces, la primera vez se va desplazando a la izquierda
        PANTALLA.blit(Fondo_derrota, (desplazamiento_x, 0))
        # esta segunda vez aparece seguidamente del anterior fondo, dando el efecto de un fondo infinito
        PANTALLA.blit(Fondo_derrota, (desplazamiento_x + ancho_pantalla, 0))
        # Se escriben dos texto de tal manera que como antes, quede el de color negro como sombra del blanco
        texto_sombra = fuente_titulo.render("BOOM!! womp womp, Get good", True, (NEGRO))
        texto_titulo = fuente_titulo.render("BOOM!! womp womp, Get good", True, (BLANCO))
        PANTALLA.blit(texto_sombra, (170 + 2, 70 + 2))
        PANTALLA.blit(texto_titulo, (170, 70))
        # Se dibujan dos rectángulos, los cuales serán botonoes, ya controlados anteriormente como eventos
        pygame.draw.rect(PANTALLA, (AZUL_CLARO), boton_volver)
        pygame.draw.rect(PANTALLA, (ROJO_OSCURO), boton_quitar)
        # Escribimos los textos que tendrán estos botonos
        texto_volver = fuente_texto.render("Jugar de nuevo", True, (BLANCO))
        texto_quitar = fuente_texto.render("salir", True, (BLANCO))
        # Se posicionan de tal manera que queden dentro del su respectivo rectángulo
        PANTALLA.blit(texto_volver, (boton_volver.x + 10, boton_volver.y + 10))
        PANTALLA.blit(texto_quitar, (boton_quitar.x + 70, boton_quitar.y + 10))
    # Esta linea, hace que todo lo que dibujamos anteriormente se haga visible
    pygame.display.update()
    # Finalmente, limitamos los fps de las animaciones con RELOJ.tick. Según los fps establecidos al inicio del programa
    RELOJ.tick(FPS)
