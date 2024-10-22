from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base, db

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, index=True)
    wallet = Column(Float, nullable=False, default=0.0)

    orders = relationship('Order', back_populates='user')
    reservations = relationship('Reserve', back_populates='user')
    wallet_history = relationship('WalletHistory', back_populates='user')


