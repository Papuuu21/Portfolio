import reflex as rx 
from portfolio.styles.styles import Size, IMAGE_HEIGHT, EmSize
from portfolio.components.heading import heading
from portfolio.data import Extras


def card_detail(extra: Extras) -> rx.Component:
    return rx.card(
        rx.link(
        rx.inset(   #* El inset es un componente que sirve para añadir padding
            rx.image(
                src = extra.image,
                height = "100px",
                width = "100%",
                object_fit = "cover", #* Para que el image se ajuste al tamaño del card
                padding_bottom = EmSize.DEFAULT.value
            ),
        pb = Size.DEFAULT.value,  #* Padding bottom
        ),
        rx.text.strong(
            extra.title,
        ),
        rx.text(
            extra.description,
            size =  Size.SMALL.value,
            color_scheme = "gray",
        ),
        ),
    width = "100%",
    href = extra.url,
    is_external = True
    )