from flask import Blueprint

maestros = Blueprint(
    "maestros", 
    __name__, 
    template_folder="template"
)

from . import routes