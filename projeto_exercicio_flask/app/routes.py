from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Medico
from app.forms.medico_form import MedicoForm
from app.controllers.MedicoController import MedicoController


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/medicos/novo', methods = ['GET', 'POST'])
def medicoNovo():
    formulario = MedicoForm()
    if formulario.validate_on_submit():
        sucesso = MedicoController.salvar(formulario)
        if sucesso:
            flash("Médico cadastrado com sucesso!", category="success")
            return render_template("index.html")
        else:
            flash("Erro ao cadastrar novo médico.", category="error")
            return render_template("medico_form.html", form = formulario)
    return render_template('medico_form.html', titulo='Cadastro de Médico', form = formulario)

@app.route('/medicos', methods = ['GET'])
def ver_medicos():
    lista_medicos = MedicoController.listar_medicos()
    return render_template('medico_lista.html', medicos = lista_medicos)

@app.route('/medico/<int:id>', methods = ['GET'])
def dado_medico(id):
    medico = MedicoController.buscar_por_medico(id)  
    return render_template("medico_detalhes.html", medico = medico)