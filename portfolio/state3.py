import reflex as rx
import json
from typing import List, Optional

# Definir modelos usando rx.Model para serialización adecuada
class Technology(rx.Model):
    icon: str
    name: str

class Media(rx.Model):
    email: str
    cv: str
    github: str
    likedin: str

class Info(rx.Model):
    icon: str  
    title: str
    subtitle: str
    description: str = ""
    date: str = ""
    certificate: str = ""
    technologies: List[Technology] = []
    image: str = ""
    url: str = ""
    github: str = ""

class Extras(rx.Model):
    image: str
    title: str
    description: str
    url: str

class PortfolioState(rx.State):
    # Propiedades básicas
    title: str = ""
    description: str = ""
    image: str = ""
    avatar: str = ""
    name: str = ""
    skill: str = ""
    location: str = ""
    email: str = ""
    cv: str = ""
    github: str = ""
    likedin: str = ""
    about: str = ""
    
    # Listas de objetos
    technologies: List[Technology] = []
    experience: List[Info] = []
    projects: List[Info] = []
    training: List[Info] = []
    extras: List[Extras] = []

    @rx.event
    async def on_load(self):
        with open("assets/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
            # Cargar propiedades básicas
            self.title = data["title"]
            self.description = data["description"]
            self.image = data["image"]
            self.avatar = data["avatar"]
            self.name = data["name"]
            self.skill = data["skill"]
            self.location = data["location"]
            
            # Cargar media
            self.email = data["media"]["email"]
            self.cv = data["media"]["cv"]
            self.github = data["media"]["github"]
            self.likedin = data["media"]["likedin"]
            
            self.about = data["about"]
            
            # Cargar listas como modelos
            self.technologies = [Technology(**tech) for tech in data["technologies"]]
            self.experience = [Info(**exp) for exp in data["experience"]]
            self.projects = [Info(**proj) for proj in data["projects"]]
            self.training = [Info(**train) for train in data["training"]]
            self.extras = [Extras(**extra) for extra in data["extras"]]

    @rx.var
    def get_technologies(self) -> List[Technology]:
        return self.technologies

    @rx.var(cache=True)
    def get_tech(self) -> str:
        return self.technologies[0].name if self.technologies else ""

    @rx.var(cache=True)
    def get_email(self) -> str:
        return self.email

    @rx.var(cache=True)
    def get_github(self) -> str:
        return self.github

    @rx.var(cache=True)
    def get_cv(self) -> str:
        return self.cv

    @rx.var(cache=True)
    def get_lk(self) -> str:
        return self.likedin
