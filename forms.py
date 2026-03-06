from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, TextAreaField, SelectField
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
    
class MaestrosForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1000, max=10000, message="Imgrese valor valido")
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
    ])
    apellidos=StringField("Apellidos", [
        validators.DataRequired(message="El campo es requerido")
    ])
    especialidad=StringField("Especialidad",[
        validators.DataRequired(message="El campo es requerido")
    ])
    email=EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])
    
class CursoForm(Form):
    id = IntegerField("id")
    nombre = StringField("Nombre del Curso", [
        validators.DataRequired("Ingresa el nombre del curso"),
        validators.length(min=3, max=150, message="Ingresa un nombre válido")
    ])
    descripcion = TextAreaField("Descripción")
    # SelectField para elegir qué maestro da el curso
    maestro_id = SelectField("Maestro Asignado", coerce=int, validators=[
        validators.DataRequired("Debes seleccionar un maestro")
    ])

class InscripcionForm(Form):
    # SelectFields para relacionar un alumno con un curso
    alumno_id = SelectField("Alumno", coerce=int, validators=[
        validators.DataRequired("Selecciona un alumno")
    ])
    curso_id = SelectField("Curso", coerce=int, validators=[
        validators.DataRequired("Selecciona un curso")
    ])