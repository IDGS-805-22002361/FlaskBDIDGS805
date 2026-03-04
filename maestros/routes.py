from . import maestros
from flask import render_template, request, redirect, url_for
# from flask_wtf.csrf import CSRFProtect

from models import db, Maestros

import forms


@maestros.route("/maestros", methods=["GET", "POST"])
def maestro():
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMest.html", maestros=maestros)


@maestros.route("/maestros/crear", methods=["GET", "POST"])
def crear():
    create_form = forms.MaestrosForm(request.form)
    if request.method == "POST":
        maes=Maestros(matricula=create_form.matricula.data,
                      nombre=create_form.nombre.data,
                      apellidos=create_form.apellidos.data,
                      especialidad=create_form.especialidad.data,
                      email=create_form.email.data)
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for("maestros.maestro"))
    return render_template("maestros/crear.html")

@maestros.route("/maestros/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.MaestrosForm(request.form)
    if request.method == "GET":
        matricula = request.args.get("matricula")
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first() 
        create_form.matricula.data = matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email

    if request.method == "POST":
        matricula = create_form.matricula.data
        maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        maes.nombre=create_form.nombre.data
        maes.apellidos=create_form.apellidos.data
        maes.especialidad=create_form.especialidad.data
        maes.email=create_form.email.data
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for("maestros.maestro"))
    
    return render_template("maestros/modificar.html", form=create_form)

@maestros.route("/maestros/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.MaestrosForm(request.form)
    
    if request.method == "GET":
        matricula = request.args.get("matricula")
        create_form.matricula.data = matricula
        maes1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        nombre=maes1.nombre
        apellidos=maes1.apellidos
        especialidad=maes1.especialidad
        email=maes1.email
        return render_template("maestros/eliminar.html", form=create_form, nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)
    if request.method == "POST":
        matricula = create_form.matricula.data
        maes=db.session.query(Maestros).get(matricula)
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for("maestros.maestro"))
    
    
@maestros.route("/maestros/detalles", methods=["GET", "POST"])
def detalles():
    matricula=request.args.get('matricula')
    maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
    nombre=maes.nombre
    apellidos=maes.apellidos
    especialidad=maes.especialidad
    email=maes.email
    return render_template("maestros/detalles.html", nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)





@maestros.route("/perfil/<nombre>")
def perfil(nombre):
    return f"Perfil de {nombre}"
