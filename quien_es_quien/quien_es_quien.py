import reflex as rx

from rxconfig import config


def cabecera() -> rx.Component:
    return rx.heading(
        rx.container(
            rx.heading("¿Quién es Quién?", as_="h1", size="8"),
        )
)


def tablero() -> rx.Component:
    #Tablero personajes
    return rx.box(
        rx.grid(
            rx.foreach(
                rx.Var.range(24),
                lambda i: rx.card(f"Personaje {i + 1}", height="13em", width="7.5em"),
            ),
                columns="8",
                rows="3",
                spacing="3",
        )
    )

def index() -> rx.Component:
    #Página inicial
    return rx.box(
        rx.vstack(
            cabecera(),
            tablero(),
            align="center",
        )
    )

app = rx.App()
app.add_page(index)