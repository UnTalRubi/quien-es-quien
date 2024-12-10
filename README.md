# ¿Quién es Quién?


**Tabla de contenidos**

-   [**Introducción**](#introducción)
-   [**Manual**](#manual)
    -   [**Pre-requisitos**](#pre-requisitos)
    -   [**Instalación**](#instalación)
    -   [**Uso**](#uso)
-   [**Metodología**](#metodología)
-   [**Descripción técnica**](#descripción-técnica)
    -   [**Requisitos funcionales/no funcionales, NOT LIST**](#partes-interesadas-y-requisitos-funcionalesno-funcionales)
    -   [**Historias de usuario**](#historias-de-usuario)
    -   [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
-   [**Diseño**](#diseño)
    -   [**Diagrama de Componentes**](#componentes)
-   [**Implementacion**](#implementacion)
    -   [**Tecnologías y Herramientas utilizadas**](#tecnologías-y-herramientas-utilizadas)
    -   [**Backend**](#backend)
    -   [**Frontend**](#frontend)
-   [**Pruebas**](#pruebas)
    -   [**Coverage**](#coverage)
    -   [**Test de unidad**](#test-de-unidad)
    -   [**Test de integración**](#test-de-integración)
-   [**Análisis del tiempo invertido**](#Tiempo-invertido)
    -   [**Clockify + Wakatime**](#clockify)
    -   [**Justificación temporal**](#justificación-temporal)
-   [**Conclusiones**](#conclusiones)
    -   [**Posibles mejoras**](#posibles-mejoras)
    -   [**Dificultades**](#dificultades)


# **Introducción**

Proyecto de programación dirigida a eventos empleando el framework de ***reflex*** que permite el desarrollo simultáneo del front end y back end de una página web empleando el lenguaje python.

La parte fundamental de trabajo es logar que el usuario pueda interactuar con el entorno web mediante eventos y que empleando lógica python la página cambie acorde a las acciones del jugador. 

El programa consiste en el clásico juego de mesa de **¿Quién es quién?** para un solo jugador, quien tratará de adivinar su personaje introduciendo características que reduzcan la cantidad de personajes en los paneles que se presentan hasta que logre adivinar el suyo. 

- *Capturas de la aplicación:*

![captura1](/images/captura1.png)

![captura2](/images/captura2.png)

![captura3](/images/captura3.png)


# **Manual**

## **Pre-requisitos**

-   [Git](https://git-scm.com)
-   [Python3](https://www.python.org)
-   [Pip3](https://pypi.org/project/pip/)

## **Instalación**

Reflex requiere del uso de un ***entorno virtual*** para su ejecución en visual studio. En nuestro caso hemos empleado el entorno venv. Los pasos para llevar a cabo la instalación necesaria del proyecto es la siguiente:

Desde vscode clonaremos el repositorio de github:

```
 git clone https://github.com/UnTalRubi/quien-es-quien.git
```

Ahora instalaremos el entorno virtual venv:
```
 python -m venv venv
```

A continuación activaremos el entorno virtual:

- En Windows:
```
.\venv\Scripts\activate
```
- En Linux:
```
source venv/bin/activate
```

Lo último que necesitamos es instalar las dependencias. Hemos creado un archivo requirements.txt que incluye reflex y todos sus componentes necesarios para el proyecto. Para ello ejecutamos el siguiente comando:
```
pip install -r requirements.txt
```

## **Uso**

1) Lo primero que debemos hacer es, una vez dentro del entorno virtual, ejecutar reflex:
```
reflex run
```
2) Tardará un tiempo en compilar el programa y crear la web en nuestro localhost. Una vez haya terminado nos dirá en que puerto se encuenta la página. Por lo general será en uno de los siguientes dos:
```
localhost:3000 
```

```
localhost:3001
```
3) El juego comenzará asignándonos un personaje aleatorio que deberemos adivinar. También se mostrarán todos los personajes posibles.

4) Introduciremos las características que creamos que podría tener nuestro personaje. En caso de acierto obtendremos puntos y en caso de que no equivoquemos se irán restando puntos a nuestra puntuación.

5) Una vez enviemos el texto se nos indica si nuestro personaje tiene o no la característica que hemos tratado de adivinar. Se ocultarán los personajes que no tengan la misma característica que el nuestro.

6) Continuaremos tratando de adivinar características y ocultando personajes no posibles hasta que solo quede uno y descubramos quienes somos.

7) En caso de que así queramos también podemos tratar de adivinar con antelación el personaje que creamos ser enviando su nombre.

8) El juego nos mostrará finalmente nuestro personaje en la carta de la derecha y nos dará un mensaje de victoria o derrota dependiendo de si hemos acertado o no, además de mostrarnos nuestra puntuación final.

9) Una vez terminada la partida podemos darle al botón de "Reiniciar Partida" para que se vuelvan a mostrar todos los personajes, se restablezca la puntuación y se nos asigne un nuevo personaje.

# **Descripción técnica**

## **Requisitos funcionales/no funcionales, NOT LIST**

El juego de quién es quién consta de 24 tarjetas donde el usuario tiene que adivinar un personaje según las características físicas mediante:
- Una pantalla de juego con el tablero de los personajes.
- Selección aleatoria del personaje a adivinar.
- Cuadro de texto para inputar las preguntas sobre las características de los personajes.

Con estos criterios básicos creamos la siguiente **NOT LIST**:

| **EN SCOPE** | **FUERA DE SCOPE** |
|:-:|:-:|
|Asignar un personaje aleatorio|Guardar la partida|
|Introducir características|Insertar personajes personalizados|
|Eliminar personajes|Multijugador en linea|
|Adivinar personaje|Sistema de ranking|
|Reiniciar partida||

| **SIN RESOLVER** |
|:-:|
|Sistema de puntuación|
|Música y SFX|
|Animaciones para girar las cartas de los personajes|
|Interfaz personalizable|

## **Historias de usuario**

|**¿Quién?** | **¿Qué quiere hacer?** | **¿Para qué lo quiere hacer?** |
|:----------:|:----------------------:|:------------------------------:|
|  El jugador  |  Elegir una carta volteada / Tener asignada una carta aleatoria  |  Para comenzar a jugar la partida adivinando su personaje  |
|  El jugador  |  Introducir características en una caja de texto  |  Para filtrar los personajes del tablero que no son el suyo  |
|  El jugador  |  Elegir el último personaje en pie  |  Para ganar la partida  |
|  El jugador  |  Elegir si quiere volver a jugar  |  Para comenzar una nueva partida  |

## **Critererios de aceptación**

1) Historia de Usuario: Elegir una carta volteada / Tener asignada una carta aleatoria.
- El jugador debe elegir una carta volteada.
- Asignada aleatoriamente.
- El juego debe comenzar cuando el jugador tenga la carta asignada.

2) Historia de Usuario: Introducir características en una caja de texto.
- El jugador debe intoducir las posibles características en un cuadro de texto.
- Al introducirla debe ser filtrada y mostrar solo los personajes que tengan esa caracerística.

3) Historia de Usuario: Elegir el último personaje en pie. 
- El jugador debe seleccionar el último personaje presente en el tablero.
- Al seleccionar al personaje se debe verificar si coincide o no con el personaje elegido en la historia 1. 
- Si es correcto gana la partida. 
- Si es incorrecto pierde la partida. 

4) Historia de Usuario: Elegir si quiere volver a jugar. 
- Al finalizar cada partida el jugador debe poder elegir si quiere o no volver a jugar. 
- Si elige volver a jugar debe reiniciarse el juego y empezar una nueva partida. 
- El tablero de juego debe ser restablecido a su estado inicial.

## **Arquitectura de la aplicación**

Contiene:
- El **Frontend**, es el encargado de la interfaz de usuario. Todo con lo que interactúa el usuario y puede contener HTML, CSS y JavaScript. 
- El **Backend**, es la lógica de la aplicación donde el controlador actúa como intermediario entre la vista y el modelo. El controlador recibe las solicitudes del frontend procesa la lógica a través del modelo y devuelve lass respuestas a la vista para actualizarse.
- **App**, es la interacción entre el Frontend y el Backend. El Frontend presenta los datos al usuario y el Backend los maneja con la lógica de la aplicación.

## **Diseño**

![diagrama](/images/diagrama_dependencias.png)

## **Componentes**

- **`quien_es_quien`** Módulo principal del proyecto. Contiene la estructura de la página web y las estructuras de reflex que se comunican con el resto de componentes.

- **`style`** Se trata de un componente que asigna la apariencia de los distintos objetos de la página mediante estilos **css**.

- **`state`** Es el módulo que se comunica con el resto de funciones que albergan la lógica python y sirve como puente entre el front end (`quien_es_quien`) y el back end. Se encarga de llamar a las distintas funciones, albergar variables que van cambiando y realiza operaciones básicas con dichas variables.

- **`lista_nombres`** Un archivo que contiene una variable global que es una lista de todos los nombres de los personajes ordenados como el tablero.

- **`lista_personajes`** Un archivo que contiene una variable global que es una matriz donde se almacena cada uno de los personajes y todas sus características.

- **`personaje_random`** Es una función que devuelve un personaje aleatorio de entre todos los que se establecen en `lista_personajes`. Ese será el personaje que se le asigna al jugador.

- **`caracteristicas`** Filtra la frase que envíe el jugador para eliminar caracteres especiales, convertir el string de la frase en una lista de palabras y comprueba si alguna de esas palabras es una característica de los personajes y la asigna a un string.

- **`devolver_nombres`** Comprueba el string que devuelve `caracteristicas` y evalúa si el personaje jugador tiene o no esa característica. En caso afirmativo devuelve una lista de nombres que tienen la característica, y en  caso negativo devuelve los que no la tienen.

- **`evaluar_respuesta`** En base a la función anterior se evalúa el intento como correcto, incorrecto o inválido en caso de que no se encuentre una característica.

- **`adivinar_personaje`** Cumple una función similar a características, sin embargo, en lugar de evaluar rasgos, comprueba si el input del jugador tiene el nombre de algún personaje y lo compara con el nombre del personaje asignado al jugador. Determinando si ha ganado o perdido.

# **Implementacion**

## **Tecnologías y Herramientas utilizadas**

- Lenguaje de Programación: Python.
- Framework: Reflex.
- Herramientas de Desarrollo: Git como sistema de control de versiones, GitHub y Visual Studio Code.

## **Backend**
- Modelo: Gestiona el estado del juego y la lógica de la aplicación.
- Controlador: Maneja las acciones del usuario y actualiza el estado del juego.

## **Frontend**
- Vista: Es la interfaz del usuario donde el usuario interactúa con la aplicación.

# **Pruebas**

Hemos creado casos test para cada uno de los módulos que realizan operaciones de lógica python a medida que los desarrollábamos para tener certeza de que tanto el input como el resultado que nos devolvía cada función era el que esperábamos. También establecimos inputs que claramente eran absurdos para asegurarnos de que cubríamos al peor de los jugadores.

Cabe también mencionar que el test para determinar si funcionaba correctamente la función de asignar un personaje aleatorio es el más complejo de todos, pues para hacerlo tuvimos que crear una función en el propio test para realizar muchas veces la aleatorización del personaje, guardar los resultados en una lista, borrar duplicados, ordenarla y comprobar que efectivamente con suficiente cantidad de intentos llegaban a salir todos los personajes posibles.

Todos los test se encuentran en el directorio de: ``/quien_es_quien/test``

## **Coverage**

![tests](/images/coverage.png)

- Logramos cubrir al ***100%*** los casos test propuestos. 

## **Test de unidad**

Durante el desarrollo empleamos test de unidad como el siguiente:

```python
@pytest.mark.parametrize(
        "input1, input2, expected",
        [
            ("","Tom", ""),
            ("El personaje es Susan?","Susan", "correcto"),
            ("Sam","Alex", "incorrecto"),
            ("Tiene que ser Claire o Anne","Anne", "incorrecto"),
            ("¿El personaje con gafas se trata de Philip?","Philip", "correcto"),
            ("Joe tiene canas?","Alex", "incorrecto")
        ]
)

def test_adivinar_personaje(input1,input2,expected):
    
    assert adivinar(input1,input2) == expected
```

Y el que más nos rompió la cabeza:

```python
@pytest.mark.parametrize(
        "expected",
        [
            ['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom']
        ]
)

def test_personaje_random(expected):
    
    random_list=[]
    for _ in range(300):
        random_list.append(random_pj())

    random_list = set(random_list)
    random_list = list(random_list)
    random_list.sort()

    assert random_list == expected
```

## **Test de integración**


![aaa](/images/xdd.png)
















# ¿Quién es Quién?

Este repositorio contiene el código fuente del juego *¿Quién es quién?* desarrollado con la ayuda del framework **Reflex**.
## Descripción 🚀

Proyecto de programación dirigida a eventos empleando el framework de ***reflex*** que permite el desarrollo simultáneo del front end y back end de una página web empleando únicamente el lenguaje python.

El programa consiste en el clásico juego de mesa de **¿Quién es quién?** para un solo jugador, quien tratará de adivinar su personaje introduciendo características que reduzcan la cantidad de personajes en los paneles que se presentan hasta que logre adivinar el suyo.

### Características principales

- Nada por el momento
## Instalación y configuración 🛠

### Prerrequisitos

- **Python 3.X**

### Instalación

1. Clonar este repositorio

     ```bash
     $ git clone https://github.com/UnTalRubi/quien-es-quien
     $ cd quien-es-quien
     ```

2. Instalar el entorno virtual

     ```bash
     $ py -m venv venv
     ```

3. Activa el entorno virtual

     ```bash
     $ .\venv\Scripts\activate
     ```

4. Instala el framework reflex

     ```bash
     $ pip install reflex
     ```

5. Ejecuta reflex

     ```bash
     $ reflex run
     ```

6. Accede a la página web

     ```bash
     localhost:3000
     ```
## Screenshots 📸

![Alt text](/path/to/image.jpg)

"Breve descripción de lo que muestra la captura."
## Historias de usuario 🎭


|**¿Quién?** | **¿Qué quiere hacer?** | **¿Para qué lo quiere hacer?** |
|:----------:|:----------------------:|:------------------------------:|
|  El jugador  |  Elegir una carta volteada / Tener asignada una carta aleatoria  |  Para comenzar a jugar la partida adivinando su personaje  |
|  El jugador  |  Introducir características en una caja de texto  |  Para filtrar los personajes del tablero que no son el suyo  |
|  El jugador  |  Elegir el último personaje en pie  |  Para ganar la partida  |
|  El jugador  |  Elegir si quiere volver a jugar  |  Para comenzar una nueva partida  |



## Estructura de proyecto 📂

```
quien-es-quien/
├── .gitignore/
├── LICENSE/
└── README/
```

##  Créditos 🎬

### Este proyecto ha sido desarrollado por:

- **María Alonso Alonso**
   
    [@avedado](https://github.com/avedado)

- **Rubén Quintas Alonso**
    
    [@untalrubi](https://github.com/UnTalRubi)

### Reconocimientos adicionales:

**Framework Reflex**

https://reflex.dev/

# Utilidades

https://readme.so/es/editor