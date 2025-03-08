import reflex as rx 
from portfolio.styles.styles import MAX_WIDTH, Size, EmSize, BASE_STYLE, STYLE_SHEETS
from portfolio.views.header import header
from portfolio.views.footer import footer
from portfolio.views.about import about
from portfolio.views.info import info
from portfolio.views.tech_stacks import tech_stacks
from portfolio.views.extra import extra
from portfolio.state3 import PortfolioState

on_mount=PortfolioState.on_load

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),  # Pasamos el estado completo al header
            about(PortfolioState.about),  # Pasamos solo el about (texto de descripción)
            rx.divider(),
            tech_stacks(),  # Este ya accede directamente a PortfolioState.get_technologies
            rx.divider(),
            info("Experiencia", PortfolioState.experience),
            rx.divider(),
            info("Proyectos", PortfolioState.projects),
            rx.divider(),
            info("Formación", PortfolioState.training),
            rx.divider(),
            extra(PortfolioState.extras),
            rx.divider(),
            footer(),  # Pasamos el estado completo al footer
            spacing=Size.LARGE.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%",
            on_mount=PortfolioState.on_load,  # Cargar datos al montar
        ),
    )

app = rx.App(
    stylesheets=STYLE_SHEETS,
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

if __name__ == "__main__":
    app.compile()