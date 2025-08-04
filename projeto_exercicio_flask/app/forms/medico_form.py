from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email

especialidades = ['Cardiologia', 'Dermatologia', 
                  'Ginecologia', 'Neurologia', 
                  'Ortopedia', 'Pediatria', 
                  'Psiquiatria', 'Urologia', 
                  'Oftalmologia', 'Otorrinolaringologia', 
                  'Endocrinologia', 'Gastroenterologia', 
                  'Pneumologia', 'Reumatologia', 
                  'Oncologia', 'Radiologia', 
                  'Anestesiologia', 'Cirurgia Geral', 
                  'Medicina Interna', 'Medicina de Família']

class MedicoForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired(), Length(min=5, max=100)])
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=5, max=100)])
    crm = StringField('CRM', validators=[DataRequired(), Length(min=8, max=8)])
    especialidade = SelectField('Especialidade', choices = especialidades)
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Cadastrar Médico')
