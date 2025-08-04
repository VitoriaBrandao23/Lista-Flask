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
            return True
        except Exception as e:
            db.session.rollback()
            return False