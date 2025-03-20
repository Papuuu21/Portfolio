import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.experience_detail import experience_detail
from portfolio.state import Info

def experience(title: str, infos: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title, True),
            rx.foreach(
            infos,
            lambda info: experience_detail(info)
        ),
        spacing='5',
        width="100%",
    ) 
