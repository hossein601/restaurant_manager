from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from models.base_model import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    orders = relationship('OrderMenu', back_populates='menu')
