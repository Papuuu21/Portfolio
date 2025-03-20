import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.project_detail import projects_detail
from portfolio.state import Info

def projects(title: str, infos: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title, True),
        rx.foreach(
            infos,
            lambda info: projects_detail(info)
        ),
        spacing='5',
        width="100%", 
    )
