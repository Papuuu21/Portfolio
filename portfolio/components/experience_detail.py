# portfolio/components/experience_detail.py
import reflex as rx
from portfolio.styles.styles import Size, EmSize
from portfolio.components.icon_badge import icon_badge
from portfolio.components.icon_button import icon_button
from portfolio.components.devicon_badge import devicon_badge

estilo_card = {
    "background_color" : "#202248",
    "border": "3px solid #F4D03F",
    "border_radius": "20px",
    "box_shadow": "4px 8px #4E1511",
    "width": "100%",
    "overflow": "hidden"
}

def experience_detail(info) -> rx.Component:
    return rx.card(
            rx.flex(
                rx.hstack(
                    # Left section (information)
                    rx.vstack(
                        rx.text(
                            info.title,
                            weight="bold",
                            color = "#5da730", 
                            width="100%"
                        ), 
                        rx.text(
                            info.subtitle,
                            weight="bold",
                            color = "#5da730",
                            width="100%"
                        ),
                        rx.text(
                            info.description,
                            size='1',
                            width="100%",
                            color = '#876505',
                            white_space="pre-line",
                            style={"font_family": "Open Sans Medium 500"},
                        ),
                        # Technologies section
                        rx.flex(
                            rx.foreach(
                                info.technologies,
                                lambda tech:
                                    rx.badge(
                                        rx.cond(
                                            tech.type == "devicon",
                                            devicon_badge(tech.icon),
                                            rx.icon(
                                                tag='computer', 
                                                color = 'orange'
                                            )
                                        ),
                                        tech.name,
                                        align="center",
                                        size='1',
                                        color = '#5da730',
                                        radius='full',
                                        variant='surface',
                                        spacing = '2',
                                        padding_x = '2',
                                    ),
                            ),
                            justify="start",
                            wrap="wrap",
                            spacing='3',
                            width="100%",
                            color = '#202248'
                        ),
                        align_items="flex-start",
                        width="70%",
                        spacing="2"
                    ), 
                    # Right section: image, date and links
                    rx.vstack(
                        rx.cond(
                            info.image != "",
                            rx.image(
                                src=info.image,
                                align='center',
                                border_radius=EmSize.DEFAULT.value,
                                object_fit="cover",
                            ),
                        ),
                        rx.vstack(
                            rx.cond(
                                info.date != "",
                                rx.badge(
                                    info.date,
                                    size='2',
                                    variant='surface',
                                    color = '#5da730'
                                ),
                            ),
                            width="100%",
                            align_items="center",
                            spacing="2",
                        ),
                        width="30%",
                        align_items="center",
                        justify_content="center",
                        height="100%",
                    ),
                    width="100%",
                    align_items="stretch",
                    spacing="3"
                ),
                width="100%",
            ),
        _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"}, #* _hover = {"background_color": "#2ECC71","cursor": "pointer"}
        style = estilo_card,
        spacing = '2',
        
        )
