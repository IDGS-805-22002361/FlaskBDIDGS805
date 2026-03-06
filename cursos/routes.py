from . import cursos

from flask import render_template, request, redirect, url_for
# from flask_wtf.csrf import CSRFProtect

from models import db, Curso, Maestros, Alumnos
import forms

@cursos.route("/cursos", methods=["GET", "POST"])
def index():
    cursos = Curso.query.all()
    return render_template("cursos/index.html", cursos=cursos)

@cursos.route("/cursos/crear", methods=["GET", "POST"])
def crear():
    create_form = forms.CursoForm(request.form)
    if request.method == "POST":
        curso = Curso(nombre=create_form.nombre.data, descripcion=create_form.descripcion.data, maestro_id=create_form.maestro_id.data)
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for("cursos.index"))
    maestros = Maestros.query.all()
    return render_template("cursos/crear.html", form=create_form, maestros=maestros)

@cursos.route("/cursos/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.CursoForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        curso1 = db.session.query(Curso).filter(Curso.id == id).first() 
        create_form.id.data = id
        create_form.nombre.data = curso1.nombre
        create_form.descripcion.data = curso1.descripcion
        create_form.maestro_id.data = curso1.maestro_id

    if request.method == "POST":
        id = request.args.get("id")
        curso=db.session.query(Curso).filter(Curso.id==id).first()
        curso.nombre=create_form.nombre.data
        curso.descripcion=create_form.descripcion.data
        curso.maestro_id=create_form.maestro_id.data
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for("cursos.index"))
    
    maestros = Maestros.query.all()
    return render_template("cursos/modificar.html", form=create_form, maestros=maestros)

@cursos.route("/cursos/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.CursoForm(request.form)
    
    if request.method == "GET":
        id = request.args.get("id")
        curso1 = db.session.query(Curso).filter(Curso.id == id).first() 
        return render_template("cursos/eliminar.html", form=create_form, curso=curso1)

    if request.method == "POST":
        id = request.args.get("id")
        curso=db.session.query(Curso).filter(Curso.id==id).first()
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for("cursos.index"))
    
    return render_template("cursos/eliminar.html", form=create_form)

@cursos.route("/cursos/detalles", methods=["GET", "POST"])
def detalles():
    id=request.args.get('id')
    curso=db.session.query(Curso).filter(Curso.id==id).first()
    
    if request.method == "POST":
        # Agregar alumno al curso
        alumno_id = request.form.get("alumno_id")
        alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
        curso.alumnos.append(alumno)
        db.session.commit()
        return redirect(url_for("cursos.detalles", id=curso.id))

    alumnos_disponibles = db.session.query(Alumnos).filter(~Alumnos.cursos.any(Curso.id == curso.id)).all()
    alumnos = curso.alumnos    
    return render_template("cursos/detalles.html", curso=curso, alumnos=alumnos, alumnos_disponibles=alumnos_disponibles)
    
@cursos.route("/cursos/remover_alumno", methods=["POST"])
def remover_alumno():
    curso_id = request.args.get("curso_id")
    alumno_id = request.args.get("alumno_id")
    curso = db.session.query(Curso).filter(Curso.id == curso_id).first()
    alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
    curso.alumnos.remove(alumno)
    db.session.commit()
    return redirect(url_for("cursos.detalles", id=curso.id))