import reflex as rx 
from portfolio.styles.styles import EmSize
from portfolio.components.heading import heading
from portfolio.state3 import PortfolioState

def tech_stacks() -> rx.Component:
    return rx.vstack(
        heading("Tech Stacks"),
        rx.foreach(
            PortfolioState.get_technologies,
            lambda tech: rx.hstack(
                rx.icon('alarm_smoke'),  # Usar notación de punto, no tech["icon"]
                rx.text(tech.name),      # Usar notación de punto, no tech["name"]
                spacing="1",
            ),
        ),
        spacing="1",
    )
