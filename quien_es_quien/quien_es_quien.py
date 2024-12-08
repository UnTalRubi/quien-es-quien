import reflex as rx
from quien_es_quien.state import State
from quien_es_quien.lista_nombres import nombres_personajes

def cabecera() -> rx.Component:
    return rx.heading(
        "¿Quién es Quién?", 
        as_= "h1", size= "8", 
        margin= "1em"
    )


def tablero() -> rx.Component:
    #Tablero personajes
    return rx.grid(
        rx.foreach(
            nombres_personajes,
            lambda nombre:
            carta(nombre),
        ),
        columns= "8",
        rows= "3",
        spacing= "3",
    )


def carta(nombre) -> rx.Component:
    return rx.card(
        rx.inset(
            rx.cond(
                State.personajes_tumbados.contains(nombre),
                rx.image(
                    src= "ocultar.jpg", 
                    width= "100%", 
                    height= "auto"
                )
            ),
            rx.cond(
                ~State.personajes_tumbados.contains(nombre),
                rx.image(
                    src=nombre + ".jpg", 
                    width= "100%", 
                    height= "auto"
                )
            )
        ),
        height= "12em", 
        width= "7.5em"
    )


def jugador() -> rx.Component:
    #Carta jugador
    return rx.card(
        rx.inset(
            rx.cond(
                State.mostrar_jugador,
                rx.image(
                    src= State.personaje_jugador + ".jpg",
                    width= "100%",
                    height= "auto",
                ),
            rx.cond(
                ~State.mostrar_jugador,
                rx.image(
                    src= "ocultar.jpg",
                    width= "100%",
                    height= "auto",
                ),
            )
            )
        ),
        height= "17em", 
        width= "10em", 
        margin_left="5em"
    )


def input_texto() -> rx.Component:
    return rx.hstack(
        rx.form(
            rx.input(
                placeholder= "Introduce una característica",
                value= State.pregunta,
                on_change= State.set_pregunta,
                type= "text"
            ),
            on_submit=State.obtener_caracteristicas,
            reset_on_submit=True,
        ),
        rx.button("Preguntar", type= "submit", on_click= State.obtener_caracteristicas),
    )


def boton_reiniciar() -> rx.Component:
    return rx.button(
        "Reiniciar partida",
        on_click= State.reiniciar_partida
    )

@rx.page(on_load= State.obtener_jugador)
def index() -> rx.Component:
    #Página inicial
    return rx.vstack(
        cabecera(),
        rx.hstack(
            tablero(),
            jugador(),
            align="center",
        ),
        rx.heading("Tu personaje es " + State.personaje_jugador, font_size= "2em"),
        boton_reiniciar(),
        input_texto(), 
        align="center"
    )


app = rx.App()
app.add_page(index)