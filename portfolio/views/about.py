import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading

def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mi"),
        rx.text(description)
    )