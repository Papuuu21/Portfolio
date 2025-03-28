import reflex as rx
from portfolio.components.heading import heading
from portfolio.styles.styles import Size
from portfolio.components.cardSkills import card_daDs, card_ia, card_general, card_bigdata

# Componente para mostrar todas las tarjetas
def skills() -> rx.Component:
    return rx.vstack(
        heading('SKILLS', True),
        rx.flex(
        card_daDs(),
        card_ia(),
        card_bigdata(),
        card_general(),
        wrap = 'wrap',
        spacing = '3',
        align = 'center',
        justify = 'center'
    ))