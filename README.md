# ¿Quién es Quién?

**Tabla de contenidos**

-   [**Introducción**](#introducción)
-   [**Manual**](#manual)
    -   [**Pre-requisitos**](#pre-requisitos)
    -   [**Instalación**](#instalación)
    -   [**Uso**](#uso)
-   [**Metodología**](#metodología)
-   [**Descripción técnica**](#descripción-técnica)
    -   [**Requisitos funcionales/no funcionales, NOT LIST**](#requisitos-funcionalesno-funcionales-not-list)
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
-   [**Análisis del tiempo invertido**](#análisis-del-tiempo-invertido)
    -   [**Wakatime**](#wakatime)
    -   [**Justificación temporal**](#justificación-temporal)
-   [**Conclusiones**](#conclusiones)
    -   [**Posibles mejoras**](#posibles-mejoras)
    -   [**Dificultades**](#dificultades)
---
# **Introducción**

Proyecto de programación dirigida a eventos empleando el framework de ***reflex*** que permite el desarrollo simultáneo del front end y back end de una página web empleando el lenguaje python.

La parte fundamental de trabajo es logar que el usuario pueda interactuar con el entorno web mediante eventos y que empleando lógica ***python*** la página cambie acorde a las acciones del jugador. 

El programa consiste en el clásico juego de mesa de **¿Quién es quién?** para un solo jugador, quien tratará de adivinar su personaje introduciendo características que reduzcan la cantidad de personajes en los paneles que se presentan hasta que logre adivinar el suyo. 

***Capturas de la aplicación:***

![inicio_partida](/images/captura1.png)
---
**Comienzo de la partida, donde se asigna un personaje al jugador y se muestra el tablero.**

![partida_avanzada](/images/captura2.png)
---
**Partida avanzada en la que ya se han tumbado personajes introduciendo características sobre su apariencia.**

![fin_partida](/images/captura3.png)
---
**Fin de la partida en la que el jugador ha adivinado el personaje y se muestra un mensaje de victoria con su puntuación.**

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
---
A continuación activaremos el entorno virtual:

- En Windows:
```
.\venv\Scripts\activate
```
- En Linux:
```
source venv/bin/activate
```
---
Lo último que necesitamos es instalar las dependencias. Hemos creado un archivo requirements.txt que incluye reflex y todos sus componentes necesarios para el proyecto. Para ello ejecutamos el siguiente comando:
```
pip install -r requirements.txt
```

## **Uso**

1) Lo primero que debemos hacer es, una vez dentro del entorno virtual, ejecutar reflex:
```
reflex run
```
---
2) Tardará un tiempo en compilar el programa y crear la web en nuestro localhost. Una vez haya terminado nos dirá en que puerto se encuenta la página. Por lo general será en uno de los siguientes dos:
```
localhost:3000 
```

```
localhost:3001
```
---
3) El juego comenzará asignándonos un personaje aleatorio que deberemos adivinar. También se mostrarán todos los personajes posibles.
---
4) Introduciremos las características que creamos que podría tener nuestro personaje. En caso de acierto obtendremos puntos y en caso de que no equivoquemos se irán restando puntos a nuestra puntuación.
---
5) Una vez enviemos el texto se nos indica si nuestro personaje tiene o no la característica que hemos tratado de adivinar. Se ocultarán los personajes que no tengan la misma característica que el nuestro.
---
6) Continuaremos tratando de adivinar características y ocultando personajes no posibles hasta que solo quede uno y descubramos quienes somos.
---
7) En caso de que así queramos también podemos tratar de adivinar con antelación el personaje que creamos ser enviando su nombre.
---
8) El juego nos mostrará finalmente nuestro personaje en la carta de la derecha y nos dará un mensaje de victoria o derrota dependiendo de si hemos acertado o no, además de mostrarnos nuestra puntuación final.
---
9) Una vez terminada la partida podemos darle al botón de "Reiniciar Partida" para que se vuelvan a mostrar todos los personajes, se restablezca la puntuación y se nos asigne un nuevo personaje.

# **Metodología**

Para llevar a cabo el proyecto hemos empleado la metodología de desarrollo ágil de ***TDD***, que consiste en emplear casos test para determinar el comportamiento de cada uno de los módulos que vamos a programar. Este método de trabajo nos ha permitido desarrollar el código de forma más clara y mantenible, además de forzarnos a planificar mejor el desarrollo antes de ponernos a picar código.

La otra metodología que utilizamos es ***Kanban***, que nos ha ayudado a organizar mejor la carga de trabajo al tener una visualización más clara de las diferentes partes de la aplicación y las funcionalidades que debíamos programar, así como asignar más firmemente las prioridades.

# **Descripción técnica**

## **Requisitos funcionales/no funcionales, NOT LIST**

El juego de quién es quién consta de 24 tarjetas donde el usuario tiene que adivinar un personaje según las características físicas mediante:
- Una pantalla de juego con el tablero de los personajes.
- Selección aleatoria del personaje a adivinar.
- Cuadro de texto para inputar las preguntas sobre las características de los personajes.

---

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
|Animaciones y efectos visuales|
|Interfaz personalizable|

## **Historias de usuario**

|**¿Quién?** | **¿Qué quiere hacer?** | **¿Para qué lo quiere hacer?** |
|:-:|:-:|:-:|
|  El jugador  |  Elegir una carta volteada / Asignar una carta aleatoria  |  Para comenzar a jugar la partida tratando de adivinar su personaje  |
|  El jugador  |  Introducir características en una caja de texto  |  Para filtrar los personajes del tablero que no son el suyo  |
|  El jugador  |  Elegir el último personaje en pie  |  Para finalizar la partida  |
|  El jugador  |  Adivinar al personaje antes de tiempo |  Para ganar o perder la partida  | 
|  El jugador  |  Elegir si quiere volver a jugar  |  Para comenzar una nueva partida  |

## **Critererios de aceptación**

1) Historia de Usuario: Elegir una carta volteada / Tener asignada una carta aleatoria.
- El jugador debe elegir una carta volteada.
- Asignada aleatoriamente.
- El juego debe comenzar cuando el jugador tenga la carta asignada.
---
2) Historia de Usuario: Introducir características en una caja de texto.
- El jugador debe intoducir las posibles características en un cuadro de texto.
- Al introducirla debe ser filtrada y mostrar solo los personajes que tengan esa caracerística.
---
3) Historia de Usuario: Elegir el último personaje en pie. 
- Debe quedar un único personaje en el tablero.
- Gana automáticamente la partida. 
---
4) Historia de usuario: Adivinar al personaje antes de tiempo.
- El jugador puede introducir un nombre en la caja  de texto.
- Si el nombre introducido es correcto, gana la partida.
- Si el nombre introducido es incorrecto, pierde la partida.
---
5) Historia de Usuario: Elegir si quiere volver a jugar. 
- Al finalizar cada partida el jugador debe poder elegir si quiere o no volver a jugar. 
- Si elige volver a jugar debe reiniciarse el juego y empezar una nueva partida. 
- El tablero de juego debe ser restablecido a su estado inicial.

## **Arquitectura de la aplicación**

Contiene:
- El **Frontend**, es el encargado de la interfaz de usuario. Todo con lo que interactúa el usuario y refleja el estado de la aplicación.

1. Reflex compila el frontend a [Next.js](https://nextjs.org/) que es un framewok React y lo envia a un puerto al que podemos acceder. 

2. Reflex proporciona múltiples componentes propios que permiten crear de forma rápida sus respectivos elementos html en la página web, y están basados en [Radix](https://www.radix-ui.com/), una librería open source de componentes React.

3. Para su estilo, existe la posibilidad de emplear temas para cambiar la apariencia de la web, así como asignar diferentes props ``CSS`` a sus componentes propios a través de la librería [Emotion](https://emotion.sh/docs/introduction).

- El **Backend**, es la lógica de la aplicación donde el controlador actúa como intermediario entre la vista y el modelo. El controlador recibe las solicitudes del usuario, procesa la lógica a través del modelo, que se realiza en la clase ``State`` y devuelve la respuesta a la vista para actualizarse.

- **App**, es la interacción entre el Frontend y el Backend. El Frontend presenta los datos al usuario y el Backend los maneja con la lógica de la aplicación. En Reflex, nuestro *frontend* `quien_es_quien` establece la estructura de la web con la que el usuario interactúa, y añade *estilo* y personalización a sus componentes a través de `style.py`. Todos los eventos del *backend* se llevan a cabo en `state.py`, que importa los diferentes módulos *python* que procesan los eventos del programa.

## **Diseño**

La estructura del proyecto es la siguiente:

```
quien-es-quien/
├── assets/                             # Imágenes para las cartas
│   └── personajes.png                  
├── images/                             # Imagenes del README
│   └── capturas.png                    
├── quien_es_quien/
│   ├── logica/                         # Lógica python
│   │   ├── adivinar_personaje.py
│   │   ├── caracteristicas.py
│   │   ├── devolver_nombres.py
│   │   ├── evaluar_respuesta.py
│   │   └── personaje_random.py
│   ├── variables/                      # Variables globales
│   │   ├── lista_nombres.py
│   │   └── lista_personajes.py
│   ├── __init__.py
│   ├── quien_es_quien.py               # Punto de entrada de la app
│   ├── state.py                        # Gestión del estado
│   └── style.py                        # Estilo de la web
├── test/                               # Test de pytest
│   ├── __init__.py
│   ├── test_adivinar_personaje.py
│   ├── test_caracteristicas.py
│   ├── test_devolver_nombres.py
│   ├── test_evaluar_respuesta.py
│   └── test_personaje_random.py
├── .gitignore
├── LICENSE
├── README.md                           # Documentación
├── requirements.txt                    # Dependencias
└── rxconfig.py
```
---
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

|Lenguaje empleado|Framework|Herramientas|
|:-:|:-:|:-:|
|[Python 3](https://www.python.org/)|[Reflex](https://reflex.dev/)| [Git](https://git-scm.com/), [Github](https://github.com/), [VSCode](https://code.visualstudio.com/), [Discord](https://discord.com/)|

**Git: como sistema de control de versiones.**

**GitHub: para compartir el repositorio y almacenarlo en la nube. También su apartado de projects para llevar a cabo una metodología kanban.**

**Visual Studio Code: para el desarrollo de la aplicación.**

**Discord: como medio de comunicación en el equipo.**

## **Backend**

- FastAPI
- WebSockets
- SQLite
- ASGI

## **Frontend**
- React
- Next.js
- TypeScript
- CSS (Tailwind)

# **Pruebas**

Hemos creado casos test para cada uno de los módulos que realizan operaciones de lógica python a medida que los desarrollábamos para tener certeza de que tanto el input como el resultado que nos devolvía cada función era el que esperábamos. También establecimos inputs que claramente eran absurdos para asegurarnos de que cubríamos al peor de los jugadores.

Cabe también mencionar que el test para determinar si funcionaba correctamente la función de asignar un personaje aleatorio es el más complejo de todos, pues para hacerlo tuvimos que crear una función en el propio test para realizar muchas veces la aleatorización del personaje, guardar los resultados en una lista, borrar duplicados, ordenarla y comprobar que efectivamente con suficiente cantidad de intentos llegaban a salir todos los personajes posibles.

Todos los test se encuentran en el directorio de: ``/quien_es_quien/test``

## **Coverage**

![tests](/images/coverage.png)

- Logramos cubrir al ***100%*** los casos test propuestos. 

## **Test de unidad**

Durante el desarrollo empleamos test de unidad como el siguiente:

- test_adivinar_personaje

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
---
- test_caracteristicas
```python
@pytest.mark.parametrize(
        "input, expected",
        [
            ("¿Tiene la boca grande?", "boca grande"),
            ("Es una mujer?", "mujer"),
            ("¿Tiene boca?", ""),
            ("Tiene el pelo negro y corto?", "negro"),
            ("¿Lleva GaFa:s?", "gafas"),
            ("¿Tiene la nariz pequeña?", "nariz pequeña"),
            ("¿Tiene pequeña la nariz?", ""),
            ("¿Está ConTenta?", "contenta")
        ]
)

def test_caracteristicas(input,expected):
    
    assert extraer_palabras_clave(input) == expected
```
---
- test_devolver_nombres
```python
@pytest.mark.parametrize(
        "input1, input2, expected",
        [
            ("mujer", "Tom", ["Susan","Claire","Anne","Anita","Maria"]),
            ("boca grande", "Philip", ["Claire","Anne","Anita","Joe","Bill","Alfred","Tom","Sam","Richard","Paul","Maria","Frans","Herman","Bernard"]),
            ("","Anne",[])
        ]
)

def test_caracteristicas(input1,input2,expected):
    
    assert comprobar_respuesta(input1, input2) == expected
```
---
- test_evaluar_respuesta
```python
@pytest.mark.parametrize(
        "input1, input2, expected",
        [
            ("mujer", "Tom", "incorrecto"),
            ("boca grande", "Philip", "correcto"),
            ("sombrero", "Maria", "correcto"),
            ("","Anne","invalido")
        ]
)

def test_caracteristicas(input1,input2,expected):
    
    assert correccion(input1, input2) == expected
```
---
Y el que más nos rompió la cabeza:

- test_personaje_random

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

**No empleamos test de integración, puesto que los diferentes módulos de lógica del proyecto no se comunican entre ellos; se llaman y relacionan a través de state.**


# **Análisis del tiempo invertido**

Según el log de **Wakatime**, el tiempo invertido en este proyecto es:

![tiempo global](/images/wakatime_global.png)

*Que equivaldría a unos 246 tokens.*

## **Wakatime**

![Captura 29 Noviembre](/images/wakatime_29N.png)
*Captura del 29 de Noviembre.*

---
![Captura 06 Diciembre](/images/wakatime_06D.png)
*Captura del 06 de Diciembre.*

---
![Captura 29 Noviembre](/images/wakatime_11D.png)
*Captura del 11 de Diciembre.*

---
## **Justificación temporal**

* Durante la primera semana el tiempo que empleamos fue principalmente definir la NOT LIST, las historias de usuario, establecer las características que emplearíamos para cada personaje y la función que nos permitiría asignar un personaje aleatorio al jugador. Además de que creamos la estructura básica de la página con reflex.

* La segunda semana comenzamos con la función para poder filtrar los personajes según sus características y que nos devolvuelva los nombres de personajes a tumbar, un botón para reinciar la partida, y continuamos ampliando los componentes de la página de reflex. Lo que más tiempo requirió fue mostrar las imágenes en las cartas del grid mediante un foreach y que se asignasen correctamente los nombres. Teniendo en cuenta que todavía estábamos comenzando a usar el framework no comprendíamos las limitaciones del mismo.

* En la recta final del proyecto completamos la función para adivinar según el nombre del personaje y así dimos por finalizadas las historias de usuario que establecimos al principio del proyecto. A mayores añadimos funcionalidades extra como el sistema de puntuación, el botón para mostrar el nombre del personaje del jugador y un editor básico de la interfaz para tener modo día/noche, bordes y colores personalizados. El resto del tiempo lo dedicamos a completar la documentación.

# **Conclusiones**

Este proyecto, aunque de primeras pareciese inabarcable, ha resultado ser una puesta a prueba de todo lo que hemos trabajado durante el trimestre, además de que nos ha forzado a investigar y buscar soluciones a problemas a los que nos enfrentaríamos constantemente en un proyecto real. Además, el hecho de que haya sido una propuesta tan desafiante me ha motivado todavía más a verla realizada, forzándo a activar el *modo diablo* aunque eso haya podido repercutir a mi estabilidad física y mental por el escaso tiempo del que disponíamos para hacerla. Necesito dormir.

## **Posibles mejoras**
El proyecto podría mejorarse añadiendo ciertas funcionalidades a la app:

- Logramos crear un sistema de puntuación, pero sería interesante crear un **leaderboard** con las puntuaciones de partidas pasadas.

- Añadir **efectos visuales** en cada interacción del ususario con la interfaz, así como emplear efectos de **sonido**.

- Con un método de **ajuste de la dificultad**; bien sea añadiendo o quitando personajes según la dificultad deseada o obligando al jugador a tumbar a los personajes de forma manual, dándole únicamente una contestación a su input, otorgando así el beneficio de la duda a cada personaje del tabero.

- La posibilidad de **personalizar los personajes** del tablero añadiendo nuevos y/o intoducir fotos.

## **Dificultades**
Algunas de las dificultades encontradas al desarrollar el proyecto han sido:

- Entender la forma en la que interactúan los componentes de ***reflex***, y no poder emplear funciones complejas desde dentro de ellos, limitando las capacidades de comunicación entre diferentes módulos a únicamente variables de ``state``.

- La introducción de las ***características*** de los personajes, ya que, no todos los jugadores intoducirían la misma característica con las mismas palabras, lo que nos obligó a ofrecer diferentes soluciones para posibles inputs.

- El framework ***Reflex*** es un castillo de naipes, y cualquiera de sus múltiples dependencias pueden provocar que explote todo. En una ocasíon se generó un error en una dependencia de Next.js que obligó a borrar el proyecto local y volverlo a clonar con git. Lo más gracioso es que dicho error surgió por ajustar el márgen del estilo de un componente mientras estaba compilando en segundo plano.