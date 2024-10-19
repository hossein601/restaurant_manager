from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String, index=True)
    name = Column(String)
    position = Column(String, nullable=False)

    orders = relationship('Order', back_populates='staff')
    reservations = relationship('Reserve', back_populates='staff')

