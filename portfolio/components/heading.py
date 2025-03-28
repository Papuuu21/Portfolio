import reflex as rx 
from portfolio.styles.styles import Size

def heading(text: str, h1 = False) -> rx.Component:
    return rx.heading(
        text, 
        as_ = "h1" if h1 else "h2", 
        size = Size.BIG.value if h1 else Size.DEFAULT.value,
        text_shadow ='2px 5px #000000',
        color = '#d1d975'
    )