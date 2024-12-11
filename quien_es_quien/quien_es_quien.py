import reflex as rx
from quien_es_quien.state import State
from quien_es_quien.variables.lista_nombres import NOMBRES_PERSONAJES
from quien_es_quien import style

def cabecera() -> rx.Component:
    #Título del juego
    return rx.heading(
        "¿Quién es Quién?",
        as_= "h1", size= "8",
        margin= "0.5em"
    )

def puntuacion() -> rx.Component:
    #Texto de puntuación
    return rx.box(
            rx.text(State.texto_puntuacion, size= "6")
        )


def switch_developer():
    return rx.box(
        rx.switch(on_change= State.cambiar_modo_dev),
        size= "3",
        style={"margin_right": "78em"}
    )


def tablero() -> rx.Component:
    #Tablero personajes
    return rx.grid(
        rx.foreach(
            NOMBRES_PERSONAJES,
            lambda nombre:
            carta(nombre),
        ),
        columns= "8",
        rows= "3",
        spacing= "3"
    )


def carta(nombre) -> rx.Component:
    #Carta personajes
    return rx.card(
        rx.inset(
            rx.cond(
                State.personajes_tumbados.contains(nombre),
                rx.image(
                    src= "ocultar.png", 
                    style= style.imagen_carta
                )
            ),
            rx.cond(
                ~State.personajes_tumbados.contains(nombre),
                rx.image(
                    src=nombre + ".jpg", 
                    style= style.imagen_carta
                )
            )
        ),style= style.carta_personaje
    )


def jugador() -> rx.Component:
    #Carta jugador
    return rx.card(
        rx.inset(
            rx.cond(
                State.mostrar_resultado,
                rx.image(
                    src= State.personaje_jugador + ".jpg",
                    style= style.imagen_carta
                ),
            rx.cond(
                ~State.mostrar_resultado,
                rx.image(
                    src= "ocultar.png",
                    style= style.imagen_carta
                ),
            )
            )
        ),
        style=style.carta_jugador
    )


def input_texto() -> rx.Component:
    #Caja de entrada de texto
    return rx.hstack(
        rx.form(
            rx.input(
                placeholder= "Introduce una característica",
                value= State.pregunta,
                on_change= State.set_pregunta,
                type= "text",
                width="100%"
            ),
            on_submit=[State.obtener_caracteristicas, State.mensaje_adivinar, State.comprobacion],
            reset_on_submit=True,
            width="20em"
        ),
        rx.button(
            "Preguntar",
            type= "submit",
            on_click= [State.obtener_caracteristicas, State.mensaje_adivinar, State.comprobacion],
            style=style.boton,
            _hover=style.boton_hover
        ),
    )


def boton_reiniciar() -> rx.Component:
    #Botón nueva partida
    return rx.hstack(
        rx.button(
            "Reiniciar partida",
            on_click= State.reiniciar_partida,
            style= style.boton_reset,
            _hover=style.boton_hover
        )
    )


def creditos() -> rx.Component:
    #Creditos Github
    return rx.box(
        rx.markdown("### Checkea este proyecto en [Github](https://github.com/UnTalRubi/quien-es-quien)")
    )


@rx.page(on_load= State.obtener_jugador)
def index() -> rx.Component:
    #Página principal
    return rx.vstack(
        cabecera(),
        puntuacion(),
        switch_developer(),
        rx.hstack(
            tablero(),
            jugador(),
            align="center",
        ),
        rx.cond(
            State.modo_dev,
            rx.heading(
                "Tu personaje es " + State.personaje_jugador,
                style= style.cabecera
            ),
        ),
        boton_reiniciar(),
        input_texto(),
        creditos(),
        align="center"
    )


app = rx.App(
    theme= rx.theme(
        rx.theme_panel(default_open=False)
    )
)
app.add_page(index)