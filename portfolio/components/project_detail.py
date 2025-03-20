# portfolio/components/projects_detail.py
import reflex as rx
from portfolio.styles.styles import Size, EmSize
from portfolio.components.icon_badge import icon_badge
from portfolio.components.icon_button import icon_button
from portfolio.components.devicon_badge import devicon_badge

estilo_card = {
    "background_color": "#283747",
    "border": "3px solid #F4D03F",
    "border_radius": "20px",
    "box_shadow": "4px 8px #4E1511",
    "width": "100%",
    #"max_width" : "400px",
    "overflow": "hidden"
}

def projects_detail(info) -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                # Left section (information)
                rx.vstack(
                    rx.text(
                        info.title,
                        weight="bold",
                        color_scheme="cyan",
                        width="100%"
                    ),
                    rx.text(
                        info.subtitle,
                        weight="bold",
                        color_scheme="cyan",
                        width="100%"
                    ),
                    rx.text(
                        info.description,
                        size='2',
                        weight="bold",
                        width="100%",
                        color = 'tomato'
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
                                        rx.icon(tag='computer')
                                    ),
                                    tech.name,
                                    align="center",
                                    size='1',
                                    color_scheme='cyan',
                                    radius='full',
                                    variant='soft',
                                    color = 'cyan',
                                    spacing = '2',
                                    padding_x = '2',
                                ),
                        ),
                        justify="start",
                        wrap="wrap",
                        spacing='3',
                        width="100%"
                    ),
                    align_items="flex-start",
                    width="70%",
                    spacing="2"
                ),
                # Right section: image, date and GitHub link
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
                            hasattr(info, "github") and info.github != "",
                            rx.badge(
                                icon_button(
                                    "github",
                                    info.github,
                                    solid=False,
                                ),
                                variant="soft",
                                size='3',
                            ),
                        ),
                        rx.cond(
                            hasattr(info, "url") and info.url != "",
                            rx.badge(
                                icon_button(
                                    "link-2",
                                    info.url,
                                    solid=False,
                                ),
                                variant="soft",
                                size='2',
                            ),
                        ),
                        width="100%",
                        align_items="center",
                        spacing="2"
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
