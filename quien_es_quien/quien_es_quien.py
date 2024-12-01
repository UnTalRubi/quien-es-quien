import reflex as rx
from rxconfig import config


def cabecera() -> rx.Component:
    return rx.heading("¿Quién es Quién?", as_="h1", size="8", margin="1em")


def tablero() -> rx.Component:
    #Tablero personajes
    return rx.grid(
        rx.foreach(
            rx.Var.range(24),
            lambda i: rx.card(f"Personaje {i + 1}", height="13em", width="7.5em"),
        ),
            columns="8",
            rows="3",
            spacing="3",
    )


def jugador() -> rx.Component:
    #Carta jugador
    return rx.card("Jugador", height="17em", width="10em", margin_left="5em")


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