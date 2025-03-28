import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.media import social_media
from portfolio.state import PortfolioState

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            "© 2024 Pablo DeAlva - Created with only Python and framework Reflex.dev",
            weight = "bold",
            size = '4',
            text_shadow ='2px 5px #000000',
            color = '#d1d975',
            padding_bottom = '1em'
        ),
    social_media({
                "email": PortfolioState.email,
                "cv": PortfolioState.cv,
                "github": PortfolioState.github,
                "likedin": PortfolioState.likedin
            }),
    )