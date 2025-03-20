import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading

estilo_card = {
    "background_color": "#283747",
    "border": "3px solid #F4D03F",
    "border_radius": "20px",
    "box_shadow": "4px 8px #4E1511",
    "width": "100%",
    "overflow": "hidden"
}

def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("ABOUT ME", True),
        rx.card(
        rx.text(
            description,  
            weight = "bold",
            size  = '2',
            color = 'tomato',
            align="center",
        ),
        _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"},
        style = estilo_card,
        ),
    )