import reflex as rx 
from portfolio.styles.styles import Size, IMAGE_HEIGHT, EmSize
from portfolio.components.icon_badge import icon_badge
from portfolio.components.icon_button import icon_button
from portfolio.state3 import Info, Technology

def info_details() -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(Info.icon),
            rx.vstack(
                rx.text.strong(Info.title), 
                rx.text(Info),
                rx.text(
                    Info.description,
                    size =  Size.SMALL.value,
                    color_scheme = "gray"
                ),
                rx.cond(
                    Info.technologies,
                    rx.flex(
                    *[
                        rx.badge(
                            rx.box(class_name = Technology.icon),
                            Technology.name,
                            color_scheme= "gray",
                        )
                        #for technology in info.technologies
                    ],
                wrap = "wrap",
                spacing = Size.SMALL.value,                    
                ),
                ),
                rx.hstack( 
                    rx.cond(
                        Info.url != "",
                    icon_button(
                        "link",
                        Info.url,
                    ),
                    ),
                    rx.cond(
                        Info.github != "",
                    icon_button(
                        "github",
                        Info.github,
                    ),
                    ),
                ),
            spacing = Size.SMALL.value,
            width = "100%", 
            ),
        spacing = Size.DEFAULT.value,
        width = "100%", 
        ),
        rx.cond(
            Info.image != "",
            rx.image(
                    src = Info.image,
                    height = "100px",
                    width = "25%",
                    border_radius = EmSize.DEFAULT.value,
                    object_fit = "cover", #* Para que el image se ajuste al tamaño del card                   
                ),
        ),
                rx.vstack(
                    rx.cond(
                        Info.date != "",
                        rx.badge(Info.date),
                    ),
                    rx.cond(
                        Info.certificate != "",
                        icon_button(
                            "shield-check",
                            Info.certificate,
                            solid =  True,
                            ),
                        ),
        spacing=Size.SMALL.value,
        ),
    flex_direction = ["column-reverse", "row"],
    width = "100%",
    spacing=Size.SMALL.value,
    )