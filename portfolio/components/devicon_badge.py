# portfolio/components/devicon_badge.py
import reflex as rx 
from portfolio.styles.styles import Size, EmSize

def devicon_badge(icon: str) -> rx.Component:
    """
    Crea un badge con un icono de Devicon.
    
    Args:
        icon: El nombre del icono de Devicon (ej: "devicon-python-plain")
        
    Returns:
        Un componente badge con el icono de Devicon
    """
    return rx.hstack(
        rx.html(
            f"""<i class="{icon}" style="font-size: 16px;"></i>""",
            dangerously_set_inner_html=True,
        ),
        aspect_ratio="1",
        size="1",
    )
