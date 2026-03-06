from flask import Blueprint

alumnos = Blueprint(
    "alumnos", 
    __name__, 
    template_folder="template"
)

from . import routes