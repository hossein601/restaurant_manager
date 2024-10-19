from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True, index=True)
    wallet = Column(Integer, nullable=False)

    orders = relationship('Order', back_populates='user')
    reservations = relationship('Reserve', back_populates='user')


