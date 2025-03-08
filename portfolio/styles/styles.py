import reflex as rx 
from enum import Enum

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"
MAX_WIDTH2 = "100vh"  #* Para que el contenido no se expanda más allá de 100vh

class Size(Enum):
    ZER0 = "0"  #0px
    SMALL = "2"  #8px
    DEFAULT = "4" #*16px/1em (tamaño base de texto en la web)
    LARGE = "6" #32px
    BIG = "8"  #64px

class EmSize(Enum):
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"

STYLE_SHEETS = {
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"  #* Hoja de estilos para la pagima devicons
}

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer",
    }
}