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
    F -- Principiante --> G[/Mostrar tablero 8 x 8 con 10 minas/]
    F -- Intermedio --> H[/Mostrar tablero 16 x 16 con 40 minas/]
    F -- Experto --> I[/Mostrar tablero 16 x 36 con 99 minas/]
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

|  Semana  |          Fecha          | Tema                                                                                |
|----------|-------------------------|-------------------------------------------------------------------------------------|
| Semana 10| 09/06/2025 - 15/06/2025 | ✅ Diseño del preproyecto: ideas del juego, reglas, diagramas de flujo              |
| Semana 11| 16/06/2025 - 22/06/2025 | 📋 Revisión de avances: presentación de diagramas, retroalimentación del docente    |
| Semana 12| 23/06/2025 - 29/06/2025 | 🧠 Estructura base del juego: lógica, funciones principales                         |
| Semana 13| 30/07/2025 - 06/07/2025 | 🐞 Depuración y validación: comprobar que el buscaminas básico funcione bien        |
| Semana 14| 07/07/2025 - 13/07/2025 | 🎨 Inicio de interfaz gráfica con tkinter o pygame                                  |
| Semana 15| 14/07/2025 - 20/07/2025 | 🧪 Integración y pruebas: conectar lógica + interfaz, ajustar errores               |
| Semana 16| 21/07/2025 - 27/07/2025 | 	🧾 Presentación final del proyecto: mostrar funcionalidades completas y exponer    | 

# Autores:
- [Brayan Santiago Rincón Rodríguez](https://github.com/santiagorinconrodriguez)
- [Nelson Manuel Amaya Diaz](https://github.com/ingnelama)
- [Sebastian Carvajal Rojas](https://github.com/sebascarvajalr)
