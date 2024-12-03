import reflex as rx
from quien_es_quien.state import State


def cabecera() -> rx.Component:
    return rx.heading(
        "¿Quién es Quién?", 
        as_="h1", size="8", 
        margin="1em"
    )


def tablero() -> rx.Component:
    #Tablero personajes
    return rx.grid(
        rx.foreach(
            rx.Var.range(24),
            lambda i: rx.card(
                rx.inset(
                    rx.image(
                        src= f"{State.obtener_personajes}",
                        width="100%",
                        height="auto",
                    ),
                ),
                State.imagen_personaje,
                height="13em", 
                width="7.5em"
            ),
        ),
        columns="8",
        rows="3",
        spacing="3",
    )


def jugador() -> rx.Component:
    #Carta jugador
    return rx.card(
        rx.inset(
            rx.image(
                src=State.personaje_jugador + ".jpg",
                width="100%",
                height="auto",
            ),
        ),
        height="17em", 
        width="10em", 
        margin_left="5em"
    )


def boton_panico() -> rx.Component:
    return rx.button(
        "Test",
        on_click = State.obtener_jugador,
    )


def index() -> rx.Component:
    #Página inicial
    return rx.vstack(
        cabecera(),
        rx.hstack(
            tablero(),
            jugador(),
            align="center",
        ), 
        rx.heading(State.personaje_jugador, font_size="2em"),
        boton_panico(),
        align="center"
    )


app = rx.App()
app.add_page(index)