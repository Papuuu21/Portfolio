import reflex as rx

def social_media(media: dict) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.icon("alarm_smoke"),
            href=f"mailto:{media['email']}",
            is_external=True,
        ),
        rx.link(
            rx.icon("alarm_smoke"),
            href=media['cv'],
            is_external=True,
        ),
        rx.link(
            rx.icon("alarm_smoke"),
            href=media['github'],
            is_external=True,
        ),
        rx.link(
            rx.icon("alarm_smoke"),
            href=media['likedin'],
            is_external=True,
        ),
        spacing="1",
    )
