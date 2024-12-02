import reflex as rx
from quien_es_quien.state import State
from quien_es_quien.nombre_personaje import nombre_pj

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
                        src=f"{i + 1}.jpg",
                        width="100%",
                        height="auto",
                    ),
                ),
                #f"Personaje {i + 1}",
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
                src="/" + State.personaje_jugador + ".jpg",
                width="100%",
                height="auto",
            ),
        ),
        #State.personaje_jugador,
        height="17em", 
        width="10em", 
        margin_left="5em"
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
        align="center"
    )


app = rx.App()
app.add_page(index)