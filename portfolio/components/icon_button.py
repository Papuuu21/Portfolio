import reflex as rx 

def icon_button(icon: str, url: str, text = "", solid = False) -> rx.Component:
    return rx.button(
            rx.icon(icon),
            text,
            variant= "solid" if solid else "surface",
            on_click = rx.redirect(url, True),  #* Ya no hace falta poner rx.link para hacer clickables los botones (se sustituye por on_click)
        )
