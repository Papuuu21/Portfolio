import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading

estilo_card = {
    "background_color": "#283747",
    "border": "3px solid #F4D03F",
    "border_radius": "20px",
    "box_shadow": "4px 8px #4E1511",
    "width": "100%",
    "overflow": "hidden"
}

def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("ABOUT ME", True),
        rx.card(
        rx.text(
            '''
            Soy un profesional junior con formación en Big Data, ML e IA que me ha proporcionado habilidades avanzadas en Python, SQL, 
            Power BI, R, ETL, técnicas de análisis de datos, desarrollo de modelos predictivos de Machine Learning y Deep Learning, 
            procesamiento de lenguaje natural (NLP) y aplicaciones IA. 
            
            Mi formación universitaria en Marketing e Investigación de Mercados me ha proporcionado una visión estratégica que aplico al 
            análisis de datos para identificar insights relevantes que puedan traducirse en acciones de alto impacto.
            
            Me apasiona trabajar con datos, descubrir patrones y transformar información compleja en soluciones prácticas que aporten 
            valor. Tengo un gran interés en aplicar estas habilidades al mundo del deporte, un sector que me motiva enormemente y en el 
            que aspiro a desarrollar mi carrera profesional.
            
            Además, cuento con experiencia en la visualización de datos mediante Power BI y Python (Seaborn, Matplotlib), así como en la 
            implementación de aplicaciones IA con herramientas como OpenAI y Google Cloud.
            
            Soy autodidacta, analítico y siempre busco oportunidades para seguir aprendiendo y perfeccionando mis competencias en Data 
            Science e IA. Estoy decidido a contribuir al éxito de proyectos innovadores mediante el uso de datos para la toma de 
            decisiones inteligentes y basadas en la evidencia aportada por los datos.
            ''',
            size  = '1',
            color = '#876505',
            align="center", 
            padding_bottom = '1em',
            white_space="pre-line",
            style={"font_family": "Open Sans Medium 500"},
            
            
            ),
        _hover={"transform": "translateY(-5px)", "transition": "transform 0.3s ease"},
        style = estilo_card,
        background_color = "#202248",
        ),
    )