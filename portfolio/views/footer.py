import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.media import social_media
from portfolio.state3 import PortfolioState

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            "© 2024 Pablo DeAlva - Created with only Python and framework Reflex.dev",
            weight = "bold",
        ),
    social_media({
                "email": PortfolioState.email,
                "cv": PortfolioState.cv,
                "github": PortfolioState.github,
                "likedin": PortfolioState.likedin
            }),
    spacing=Size.SMALL.value,
    )