from app import db
import sqlalchemy as sa
from app.models import Medico

class MedicoController:
    
    def salvar(form):
        try:
            medico = Medico()
            form.populate_obj(medico)
            
            db.session.add(medico)
            db.session.commit()
            print("Médico salvo com sucesso:", medico)
            return True
        except Exception as e:
            db.session.rollback()
            print("Erro ao salvar médico:", e)
            return False
    
    def listar_medicos():
        query = sa.select(Medico)
        medicos = db.session.scalars(query)
        return medicos
    
    def buscar_por_medico(id):
        print(f"Buscando médico com ID: {id}")
        query = sa.select(Medico).where(Medico.id == id)
        medico = db.session.scalars(query).first()
        print("Médico encontrado" if medico else "Nenhum médico com esse ID.")
        return medico