import datetime
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so


class Medico(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome_completo: so.Mapped[str] = so.mapped_column(sa.String(150), nullable=False)
    crm: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False, unique=True)
    especialidade: so.Mapped[str] = so.mapped_column(sa.String(50), nullable=False)
    criado_em: so.Mapped[datetime.datetime] = so.mapped_column(sa.DateTime, default=datetime.datetime.utcnow)
    consultas: so.Mapped['Consulta'] = db.relationship(back_populates='medico')