import reflex as rx
from portfolio.components.heading import heading
from portfolio.components.devicon_badge import devicon_badge
from portfolio.styles.styles import EmSize
from reflex_simpleicons import simpleicons

estilo_card = {
    "background_color": "#202248",
    "border": "3px solid #F4D03F",
    "border_radius": "20px",
    "box_shadow": "4px 8px #4E1511",
    "width": "100%",
    "max_width" : "400px",
    "overflow": "hidden"
}

estilo_flex = {
    "background_color": "#8C333A",
    "border": "3px solid #F4D03F",
    "border_radius": "20px",
    "width": "100%",
    "max_width" : "400px",
    'padding_top' : "1em",
    'padding_bottom': "1em",
    "overflow": "hidden"
}

brand_color=True
size = 25

def da_ds() -> rx.Component:
    return rx.flex(
        simpleicons("r", brand_color=brand_color, size=size),
        simpleicons("postgresql", brand_color=brand_color, size=size),
        simpleicons("pandas", brand_color=brand_color, size=size),
        simpleicons("numpy", brand_color=brand_color, size=size),
        simpleicons("scikitlearn", brand_color=brand_color, size=size),
        simpleicons("pytorch", color='blue', size=size),
        class_name="demo-brands",
        wrap="wrap",
        justify="center",
        gap="1rem",
        style = estilo_flex
    )

def ia() -> rx.Component:
    return rx.flex(
        simpleicons("ollama", brand_color=brand_color, size=size),
        simpleicons("tensorflow", color='blue', size=size),
        simpleicons("huggingface", brand_color=brand_color, size=size),
        simpleicons("openai", brand_color=brand_color, size=size),
        simpleicons("langchain", brand_color=brand_color, size=size),
        simpleicons("googlegemini", brand_color=brand_color, size=size),
        simpleicons("spacy", brand_color=brand_color, size=size),
        class_name="demo-brands",
        wrap="wrap",
        justify="center",
        gap="1rem",
        style = estilo_flex
    )

def bigdata() -> rx.Component:
    return rx.flex(
        simpleicons("fastapi", brand_color=brand_color, size=size),
        simpleicons("scala", color='blue', size=size),
        simpleicons("apachespark", color='blue', size=size),
        simpleicons("apachehadoop", brand_color=brand_color, size=size),
        simpleicons("docker", brand_color=brand_color, size=size),
        simpleicons("googlecloud", brand_color=brand_color, size=size),
        simpleicons("mlflow", brand_color=brand_color, size=size),
        simpleicons("mongodb", brand_color=brand_color, size=size),
        class_name="demo-brands",
        wrap="wrap",
        justify="center",
        gap="1rem",
        style = estilo_flex
    )

def general() -> rx.Component:
    return rx.flex(
        simpleicons("python", brand_color=brand_color, size=size),
        simpleicons("git", color='blue', size=size),
        simpleicons("github", brand_color=brand_color, size=size),
        simpleicons("googlebigquery", brand_color=brand_color, size=size),
        simpleicons("kubernetes", brand_color=brand_color, size=size),
        simpleicons("css3", brand_color=brand_color, size=size),
        simpleicons("amazonwebservices", brand_color=brand_color, size=size),
        simpleicons("jira", brand_color=brand_color, size=size),
        class_name="demo-brands",
        wrap="wrap",
        justify="center",
        gap="1rem",
        style = estilo_flex
    )

def card_daDs():
    return rx.card(
        rx.vstack(
            rx.image(
                src='data/da_ds.jpg',
                height="100px",
                width="100%",
                object_fit="fill",
                padding_bottom=EmSize.DEFAULT.value,
                #display = 'block'
            ),
            rx.heading('DA & DS', color = '#d1d975', font_size = '1.5em', text_shadow =' 2px 4px #000000'),
            da_ds(),
            align_items="flex-start",
            padding="1rem",
        ),
    style = estilo_card,
    _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"},
) 

def card_ia():
    return rx.card(
        rx.vstack(
            rx.image(
                src='data/AI.jpg',
                height="100px",
                width="100%",
                object_fit="fill",
                padding_bottom=EmSize.DEFAULT.value
            ),
            rx.heading('IA-NLP', color = '#d1d975', font_size = '1.5em', text_shadow =' 2px 4px #000000'),
            ia(),
            align_items="flex-start",
            padding="1rem",
        ),
    style = estilo_card,
    _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"},
)

def card_bigdata():
    return rx.card(
        rx.vstack(
            rx.image(
                src='data/bigdata.png',
                height="100px",
                width="100%",
                object_fit="fill",
                padding_bottom=EmSize.DEFAULT.value
            ),
            rx.heading('BIG DATA', color = '#d1d975', font_size = '1.5em', text_shadow =' 2px 4px #000000'),
            bigdata(),
            align_items="flex-start",
            padding="1em",
        ),
    _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"}, #* _hover = {"background_color": "#2ECC71","cursor": "pointer"}
    style = estilo_card
)

def card_general():
    return rx.card(
        rx.vstack(
            rx.image(
                src='data/general.jpg',
                height="100px",
                width="100%",
                object_fit="fill",
                padding_bottom=EmSize.DEFAULT.value
            ),
            rx.heading('GERERAL', color = '#d1d975', font_size = '1.5em', text_shadow =' 2px 4px #000000'),
            general(),
            align_items="flex-start",
            padding="1em",
        ),
    _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"}, #* _hover = {"background_color": "#2ECC71","cursor": "pointer"}
    style = estilo_card
)