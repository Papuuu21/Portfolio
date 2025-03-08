import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.card_detail import card_detail
from portfolio.state3 import Info

def info(title: str, infos: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.foreach(
            infos,
            lambda info: card_detail(info)
        ),
        spacing=Size.DEFAULT.value,
        width="100%",
    )
