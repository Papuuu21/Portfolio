import reflex as rx 
from portfolio.styles.styles import MAX_WIDTH, Size, EmSize, BASE_STYLE, STYLE_SHEETS
from portfolio.components.heading import heading
from portfolio.views.header import header
from portfolio.views.footer import footer
from portfolio.views.about import about
from portfolio.views.experience import experience
from portfolio.views.projects import projects
from portfolio.views.training import training
from portfolio.views.skills import skills
from portfolio.state import PortfolioState

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            about(PortfolioState.about),
            rx.divider(size = '4', color_scheme='tomato'),
            skills(),
            rx.divider(size = '4', color_scheme='tomato'),
            experience("EXPERIENCIA", PortfolioState.experience), 
            rx.divider(size = '4', color_scheme='tomato'),
            projects("PROYECTOS", PortfolioState.projects),
            rx.divider(size = '4', color_scheme='tomato'),
            training("FORMACIÓN", PortfolioState.training),
            rx.divider(size = '4', color_scheme='tomato'),
            footer(),
            spacing=Size.LARGE.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%",
            on_mount=PortfolioState.on_load,
        ), 
    )

# Configuración de estilos
GOOGLE_FONTS = "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"
DEVICON_STYLESHEET = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
STYLE_SHEETS = [DEVICON_STYLESHEET, GOOGLE_FONTS]  # Añadimos la nueva

# Estilos base (asumiendo que ya tienes esto definido)
BASE_STYLE = {
    "font_family": "'Press Start 2P', monospace",
    "background_color": "#283747",
    "color": "#F5F5DC",
}

app = rx.App(
    stylesheets=STYLE_SHEETS,  # Usar la lista actualizada
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="blue",
    )
)

app.add_page(
    index,
    title="Portfolio",
    description="Mi portfolio profesional",
    image="/favicon.ico",
)
