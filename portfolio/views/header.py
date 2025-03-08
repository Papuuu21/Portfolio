import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.media import social_media
from portfolio.state3 import PortfolioState

def header() -> rx.Component:
    return rx.hstack(
            rx.avatar(
                src = PortfolioState.avatar,
                size = '5',
            ),
            rx.vstack(
                heading(
                    PortfolioState.name, 
                    True,
                ),
                heading(
                    PortfolioState.skill,
                ),
                rx.text(
                    rx.icon(
                        "sun",
                        color = "yellow",
                    ),
                    PortfolioState.location,
                    weight = "bold",
                    display = "inherit",   
                ),
                social_media({
                    "email": PortfolioState.email,
                    "cv": PortfolioState.cv,
                    "github": PortfolioState.github,
                    "likedin": PortfolioState.likedin
                }),
                spacing='1',
            ),
            spacing = '1',
        )
