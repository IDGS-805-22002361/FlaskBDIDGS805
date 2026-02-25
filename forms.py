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
    apellidos=StringField("Apellidos",[
        validators.DataRequired(message="El campo es requerido")
    ])
    email=EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])
    telefono=IntegerField("Telefono",[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1000000000, max=10000000000, message="Imgrese valor valido")
    ])