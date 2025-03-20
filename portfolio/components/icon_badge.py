# portfolio/components/icon_badge.py
import reflex as rx 
from portfolio.styles.styles import Size, EmSize

def icon_badge(icon: str) -> rx.Component:
    """
    Crea un badge con un icono de Lucide.
    
    Args:
        icon: El nombre del icono de Lucide (ej: "python", "cloud", "database")
        
    Returns:
        Un componente badge con el icono de Lucide
    """
    return rx.badge(
        rx.icon(
            tag=icon,
            size="32px",
        ),
        aspect_ratio="1",
        variant="soft",
    )
