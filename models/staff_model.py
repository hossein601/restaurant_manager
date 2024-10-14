from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import Base


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    type = Column(String)
    orders = relationship('Order', back_populates='')
    reservations = relationship('Reserve', back_populates='staff')

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'staff',
    }

