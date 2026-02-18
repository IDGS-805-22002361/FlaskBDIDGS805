from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField("id", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Imgrese valor valido")
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese nombre valido")
    ])
    apaterno=StringField("Aparteno",[
        validators.DataRequired(message="El campo es requerido")
    ])
    email=EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])