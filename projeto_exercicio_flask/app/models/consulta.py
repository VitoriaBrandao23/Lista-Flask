import datetime
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Consulta(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    id_medico: so.Mapped[int] = so.mapped_column(sa.ForeignKey('medico.id'), index=True, nullable=False)
    medico: so.Mapped['Medico'] = so.relationship(back_populates='consultas') 
    id_paciente: so.Mapped[int] = so.mapped_column(sa.ForeignKey('paciente.id'), index=True, nullable=False)
    paciente: so.Mapped['Paciente'] = so.relationship(back_populates='consultas')
    data_hora_marcada: so.Mapped[datetime.datetime] = so.mapped_column(sa.DateTime)
    criado_em: so.Mapped[datetime.datetime] = so.mapped_column(sa.DateTime)
