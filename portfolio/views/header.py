import reflex as rx 
from portfolio.styles.styles import Size, EmSize
from portfolio.components.heading import heading
from portfolio.components.media import social_media
from portfolio.state import PortfolioState

def header() -> rx.Component:
    return rx.hstack(
            rx.image(
                src = 'data/avatargta1.jpg',
                height="150px",
                width="auto",
                align='center',
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover",
    ),
            rx.vstack(
                heading(
                    'Pablo Díaz de Alva', 
                    True,
                ),
                heading(
                    'Data Analyst, Data Science & IA Developer',
                ),
                rx.text(
                    'Málaga Andalucía España',
                    weight = "bold",
                    display = "inherit", 
                    size = '4',
                    text_shadow ='2px 5px #000000',
                    color = '#F4D03F',
                    padding_bottom = '1em'
                ),
                social_media(
                    {
                    "email": PortfolioState.email,
                    "cv": PortfolioState.cv,
                    "github": PortfolioState.github,
                    "likedin": PortfolioState.likedin
                },
                ),
                spacing='1',
            ),
            spacing = '5',
        )
