import reflex as rx
from portfolio.components.icon_button import icon_button


def icon_button(icon: str, url: str, text = "", solid = False) -> rx.Component:
    return rx.button(
        rx.flex(
            rx.icon(icon),
            text,
            width= '100%',
            justify="center",
            align="center",
            spacing= '3',
            padding_bottom = '3em',
            padding_top = '3em',
            ),
            radius='full',
            variant='surface',
            color = '#5da730',
            spacing = '5',
            _hover = {'border_color': 'gray.500', "transform": "translateY(-5px)", 
                        "transition": "transform 0.3s ease", "background_color": "#0090FF",
                        "cursor": "pointer"
            },            
            on_click = rx.redirect(url, True),  #* Ya no hace falta poner rx.link para hacer clickables los botones (se sustituye por on_click)
        )

def social_media(media: dict) -> rx.Component:
    return rx.hstack(
        icon_button(
            icon="mail",
            url=f"mailto:{media['email']}",
            text="Email"
        ),
        icon_button(
            icon="clipboard-minus",
            url=media['cv'],
            text="CV"
        ),
        icon_button(
            icon="github",
            url=media['github'],
            text="Github"
        ),
        icon_button(
            icon="linkedin",
            url=media['likedin'],
            text="Linkedin"
        ),
        spacing="3",
        width = "100%",
    )
