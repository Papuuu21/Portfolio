# portfolio/components/icon_button.py
import reflex as rx

def icon_button(icon: str, url: str, solid: bool = False) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon,  # Usar tag en lugar de pasar el icono como argumento posicional
            size=16,
            color = '#5da730' 
        ),
        href=url,
        is_external=True,
        color="rgb(107, 99, 246)" if solid else None,
    )
