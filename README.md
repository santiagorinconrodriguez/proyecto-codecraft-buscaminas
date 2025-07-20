# Proyecto-Codecraft-Buscaminas

## Mine Hunter 3000 🥊💣💥

## Introducción
### *¿En qué consiste el juego de Buscaminas?*

Buscaminas es un videojuego clásico de lógica y estrategia, comúnmente jugado en computadoras personales. El juego se desarrolla sobre una cuadrícula compuesta por varias casillas, algunas de las cuales esconden minas. 

El objetivo principal del jugador es descubrir todas las casillas que no contienen minas, evitando detonarlas. Para lograrlo, el jugador hace clic en las casillas, y si la casilla no contiene una mina, revela un número. Este número indica cuántas minas se encuentran en las casillas adyacentes (es decir, en las ocho celdas que rodean a la seleccionada). 

A partir de esta información, el jugador debe deducir la ubicación de las minas y puede marcar las casillas sospechosas con banderas, lo cual sirve como ayuda visual para no hacer clic en ellas accidentalmente. 

El juego se gana al descubrir correctamente todas las casillas libres de minas. Por el contrario, se pierde si el jugador selecciona una casilla que contiene una mina.

![image](https://github.com/user-attachments/assets/c497a985-9978-4cd7-80ae-2d9d8d919251)

## Objetivos
### *Objetivo general*

Presentar y desarrollar un juego interactivo de Buscaminas que combine lógica, estrategia y entretenimiento, implementando una interfaz intuitiva que facilite al usuario la toma de decisiones basadas en pistas numéricas para descubrir las celdas seguras, evitando las minas ocultas y completando el desafío dentro de una experiencia funcional y accesible.

### *Objetivos específicos*

1. Desarrollar una interfaz intuitiva que permita al usuario interactuar con el juego mediante clics, como el marcar o reiniciar juego.
2. Diseñar la estructura del tablero y establecer la lógica de distribución aleatoria de minas según los diferentes niveles de dificultad.
3. Implementar un sistema que calcule y muestre correctamente la cantidad de minas cercanas a cada celda descubierta.
4. Incorporar elementos visuales para aquellas acciones clave que el jugador realiza como: marcar mina(mediante un símbolo de bandera), descubrir celda, ganar o perder.
5. Poner en práctica todos los conocimientos adquiridos durante el curso programación de computadores.

## *Lógica del juego*

- Mostrar pantalla principal.
- Preguntar al usuario si desea ver las instrucciones:
    Si elige "Sí", mostrar texto con las reglas del juego.
    Si elige "No", Seguir con el siguiente proceso.
- Continuar con la selección de dificultad.
- Preguntar al usuario qué dificultad desea:
    -> Principiante -> tablero 4x4, 3 minas.
  
    -> Intermedio -> tablero 8x8, 13 minas.
  
    -> Experto -> tablero 16x16, 50 minas.
- Generar el tablero vacío y colocar minas de forma aleatoria.
- El jugador selecciona una casilla.
- Evaluar la casilla:
    -> Si tiene una mina:
        - Mostrar mensaje de “Juego perdido”.
        - Ofrecer opción de volver a jugar.
    -> Si no tiene una mina:
        - Calcular y mostrar el número de minas vecinas.
- Luego de cada jugada:
    Verificar si todas las casillas sin mina han sido descubiertas.
        -> Si sí, mostrar mensaje de “¡Has ganado!”.
        -> Si no, esperar el siguiente clic.
- Tras ganar o perder:
    -> Preguntar al jugador si desea volver a jugar.
        -> Si elige Sí, reiniciar desde selección de dificultad.
        -> Si elige No,cerrar el juego.

## *Interfaz grafica*
### Pygame
- librería para el desarrollo de videojuegos en segunda dimensión 2D con el lenguaje de programación Python. Pygame está basada en SDL, que es una librería que nos provee acceso de bajo nivel al audio, teclado, ratón y al hardware gráfico de nuestro ordenador.

_Ventajas_
- Función main() o clase Game(): contenedor del videojuego.
- Control de eventos: pygame.event.get(), es decir, lista de eventos a procesar.
- Sprites: rectángulos que representan los objetos móviles o fijos del juego. Estos pueden animarse con frames o modificarse gráficamente. También se pueden detectar colisiones pygame entre ellos.
- Sonidos: pygame.mixer.Sound() y play.
- Textos: pygame.font.Font(file_path, size) y render.

### tkinter
- Módulo estándar de Python para crear interfaces gráficas de usuario (GUI). Es un "binding" de la biblioteca Tcl/Tk, lo que significa que permite usar las funcionalidades de Tk desde Python.

_Ventajas_
- Crea interfaces gráficas de usuario de forma rápida y eficiente, lo que es útil para aplicaciones de escritorio y otras herramientas. 
- Es conocido por ser relativamente sencillo de aprender y usar.

En nuestro proyecto utilizaremos pygame ya que trae más herramientas y genera una interfaz grafica de mayor calidad, permitiendonos editar detalles con el fin de obtener un resultado más estetico.


## *Diagrama de flujo del juego*

``` mermaid
---
config:
  theme: redux
---

flowchart TD
    A(["Inicio"]) --> B[Pantalla principal]
    B --> C{"¿Desea ver las instrucciones del juego?"}
    C -- Sí --> D[/Mostrar instrucciones/]
    C -- No --> F
    D --> F{"Escoga una dificultad"}
    F -- Principiante --> G[/Mostrar tablero 4 x 4 con 3 minas/]
    F -- Intermedio --> H[/Mostrar tablero 8 x 8 con 13 minas/]
    F -- Experto --> I[/Mostrar tablero 16 x 36 con 50 minas/]
    G --> J[seleccione una casilla]
    H --> J
    I --> J
    J --> K{"¿La casilla tiene mina?"}
    K -- Sí --> L[/Mostrar mensaje de juego perdido/]
    L --> Q
    K -- No --> M[/Mostrar número de minas cercanas/]
    M --> N{"¿Ha descubierto todas las casillas?"}
    N -- No -->J
    N -- Sí --> O[/Mostrar mensaje de juego ganado/]
    O --> Q{"¿Desea volver a jugar?"}
    Q -- Sí -->F
    Q -- No --> P(["Fin"])
```
## Plan de desarrollo
### Cronograma

|  Semana  |          Fecha          | Tema                                                                                           |
|----------|-------------------------|------------------------------------------------------------------------------------------------|
| Semana 10| 09/06/2025 - 15/06/2025 | ✅ Diseño del preproyecto: ideas del juego, reglas, diagramas de flujo                         |
| Semana 11| 16/06/2025 - 22/06/2025 | 📋 Revisión de avances: presentación del diagramas de flujo y retroalimentación del profesor   |
| Semana 12| 23/06/2025 - 29/06/2025 | 🧠 Estructura base del juego: lógica, funciones principales, etc                               |
| Semana 13| 30/07/2025 - 06/07/2025 | 🐞 Depuración y validación: comprobar que el buscaminas funcione bien                          |
| Semana 14| 07/07/2025 - 13/07/2025 | 🎨 Inicio de interfaz gráfica con tkinter o pygame                                             |
| Semana 15| 14/07/2025 - 20/07/2025 | 🧪 Integración y pruebas: conectar lógica + interfaz                                           |
| Semana 16| 21/07/2025 - 27/07/2025 | 🧾 Presentación final del proyecto: mostrar funcionalidades completas y exponer                | 

## Comó ejecutar el código.
El primer paso es descargar los archivos que vamos a necesitar ( Código, interfaz e imágenes), que se encuentran subidas en el inicio del repositorio como se ve acontinuación.

<img width="899" height="248" alt="image" src="https://github.com/user-attachments/assets/17c8d650-bddc-47f3-8a17-a4f0a774e844" />


Luego, ubicamos los archivos y el código dentro de una carpeta y los ordenamos de la siguiente manera.

<img width="637" height="103" alt="image" src="https://github.com/user-attachments/assets/6ed185e2-0c31-4d24-91a6-241748f8aec4" />


En la carpeta de imagenes lo acomodamos de esta manera.

<img width="576" height="132" alt="image" src="https://github.com/user-attachments/assets/58fe54a5-7542-4c6c-96b9-cf1579c36ce3" />


En la carpeta de letras de esta otra manera.

<img width="363" height="145" alt="image" src="https://github.com/user-attachments/assets/cfaace36-5383-4a45-9b82-680f1c059bf4" />


Ahora viene lo más importante. ¿ Cómo ejecutar el código?
Nos dirigimos al programa Visual Studio Code, y nos dirigimos hacia la parte superior izquierda en la barra de herramientas y seleccionamos la opción “File” y luego seleccionamos la opción “Open Folder” o en el teclado seleccionamos las teclas ctrl + K Ctrl + O.

<img width="516" height="635" alt="image" src="https://github.com/user-attachments/assets/b7fb8606-5b24-4c2c-bd44-d179f545f271" />


Aquí seleccionamos la carpeta en la cual guardamos los el código y los archivos.

<img width="1161" height="658" alt="image" src="https://github.com/user-attachments/assets/6f27982c-0098-4c90-8069-6f695be28ad1" />
<img width="227" height="372" alt="image" src="https://github.com/user-attachments/assets/a26a01c4-681c-4b19-a16d-c56ffb0ead42" />

En este punto seleccionamos los 2 códigos y verificamos que los 2 se ejecuten con normalidad.

<img width="1917" height="1037" alt="image" src="https://github.com/user-attachments/assets/50a76b71-80d6-454b-83b2-06d8627c1f0f" />

Aquí notaremos que el código de la interfaz presenta un error como se verá a continuación.

<img width="1159" height="151" alt="image" src="https://github.com/user-attachments/assets/5adbb00e-7b38-4b57-8971-ffb3371de254" />


Para este caso lo único que debemos hacer es instalar la biblioteca pygame, porque fue la que utilizamos para hacer la interfaz gráfica. Para eso, escribimos “ pip install pygame” como se ve en la imagen, ya con la biblioteca instalada podremos ejecutar el código de la interfaz.


<img width="1161" height="154" alt="image" src="https://github.com/user-attachments/assets/2a313ab7-1a55-4848-a50c-226ef5f2fa1b" />
<img width="1226" height="210" alt="image" src="https://github.com/user-attachments/assets/5a11b808-f056-46e7-b503-af3a75b19752" />

Ahora simplemente ejecutamos el código y procedemos a iniciar el juego.

<img width="1890" height="851" alt="image" src="https://github.com/user-attachments/assets/323c4aff-5a69-485a-b10d-4f2582ef5b68" />



## Menú del juego:
El menú principal es la pantalla inicial del juego desde donde el jugador puede acceder a las diferentes funciones antes de comenzar a jugar.

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/d9f21f26-2de3-4755-abc5-d2ee9f90bfcc" />

En el menú del juego se presentan dos opciones principales: ‘Continuar’ e ‘Instrucciones’. La opción ‘Continuar’ permite acceder a los diferentes niveles de dificultad que ofrece el juego, mientras que la opción ‘Instrucciones’ proporciona una guía con las indicaciones necesarias para aprender a jugar Mine Hunter 3000.

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/81b45f9c-78aa-4253-9151-703c78bd62de" />

En el caso de la opción ‘Instrucciones’, esta dirige al jugador a una pantalla donde se explican las reglas y mecánicas del juego. Al finalizar la lectura, se mostrará un botón llamado ‘Continuar’, el cual, al igual que la opción principal del menú, permite acceder a los distintos niveles de dificultad del juego.

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/fd66167f-abcf-4301-86a5-6c48013fb3a8" />

Posteriormente, el juego dirige al usuario a la selección de niveles de dificultad, permitiéndole escoger aquel que mejor se adapte a su experiencia o interés.

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/e05f3297-2336-413a-8834-2be017ce403f" />

## Niveles de dificultad
En la pantalla de niveles de dificultad se presentan tres opciones, Principiante, Intermedio y Experto

### *Nivel Principiante:* 
La primera es el nivel ‘Principiante’, que cuenta con un tablero de 4 x 4 casillas y un total de 3 minas distribuidas aleatoriamente. Este nivel está diseñado para usuarios que están empezando a familiarizarse con el juego.

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/5420fb24-1de7-427c-ab1b-83684b389f19" />

### *Nivel Intermedio:* 
Luego se encuentra el nivel ‘Intermedio’, el cual presenta un tablero de 8 x 8 casillas y contiene un total de 13 minas. Este nivel representa un mayor desafío, ideal para jugadores con algo más de experiencia en el juego.

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/4cd56461-c4dd-4731-9425-c53fee5f632a" />

### *Nivel Experto:* 
Y finalmente, está el nivel de dificultad ‘Experto’, que cuenta con un tablero de 16 x 16 casillas y un total de 50 minas. Este nivel está diseñado para jugadores avanzados que buscan un reto mucho más complejo y estratégico.

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/e41b2cb9-c1f1-4a09-ac8d-467d58e0949b" />

## ¿Como se juega?
Al ingresar a un nivel de dificultad, el jugador podrá seleccionar las casillas del tablero haciendo clic izquierdo sobre ellas. Al hacerlo, se revelará el contenido de la casilla: si no hay una mina, se mostrará un número que indica cuántas minas hay en las casillas adyacentes. Esta información permite al jugador deducir la ubicación de las minas y avanzar con mayor estrategia.

<img width="300" height="190" alt="image" src="https://github.com/user-attachments/assets/4f8a16c0-df92-41dc-8bc3-8df494593d36" />

Si el jugador, después de revelar ciertas casillas, sospecha que hay una mina en una ubicación específica, podrá hacer clic derecho sobre esa casilla para colocar una bandera. Esta bandera indica que el jugador cree que hay una mina en ese lugar y sirve como una marca visual para evitar seleccionarla accidentalmente.

<img width="340" height="260" alt="image" src="https://github.com/user-attachments/assets/78ced2a0-6bfa-4176-87d5-e284c1546619" />

En caso de que el jugador logre marcar correctamente todas las minas ocultas y revelar todas las casillas restantes sin errores, el juego mostrará el siguiente mensaje:

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/03eda773-e77c-44b2-94f6-7971f1b2ae37" />

En cambio, si el jugador selecciona una casilla que contiene una mina, el juego finalizará inmediatamente y se mostrará el siguiente mensaje:

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/9bbd9265-0f3f-46f1-af30-22d42c4f906b" />

### Opciones al finalizar el juego:
Al finalizar el juego, ya sea en caso de victoria o derrota, se presentan dos opciones en pantalla:

- Salir: permite cerrar el juego por completo y regresar al escritorio.

- Jugar de nuevo: redirige al jugador a la pantalla de selección de niveles de dificultad, para que pueda elegir un nuevo modo y volver a intentarlo.

# Autores:
- [Brayan Santiago Rincón Rodríguez](https://github.com/santiagorinconrodriguez)
- [Nelson Manuel Amaya Diaz](https://github.com/ingnelama)
- [Sebastian Carvajal Rojas](https://github.com/sebascarvajalr)
- [Wilder Poscue Labio](https://github.com/wilder-29)
