import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.training_detail import training_detail
from portfolio.state import Info

def training(title: str, infos: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title, True),
        rx.foreach(
            infos,
            lambda info: training_detail(info)
        ),
        spacing=Size.DEFAULT.value,
        width="100%",
    )
