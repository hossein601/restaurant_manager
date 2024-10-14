from sqlalchemy import Column, Integer, String, ForeignKey
from models.staff_model import Staff


class Waiters(Staff):
    __tablename__ = 'waiter'

    id = Column(Integer, ForeignKey('staff.id'), primary_key=True)
    section = Column(String(30), nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'waiter',
    }
