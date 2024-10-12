from sqlalchemy import Column, Integer, String, ForeignKey
from models.staff_model import Staff


class Chef(Staff):
    __tablename__ = 'chef'

    id = Column(Integer, ForeignKey('staff.id'), primary_key=True)
    specialty = Column(String(30), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'chef',
    }

