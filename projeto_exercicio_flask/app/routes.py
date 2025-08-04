from flask import render_template, flash, redirect, url_for
from app import app, db
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