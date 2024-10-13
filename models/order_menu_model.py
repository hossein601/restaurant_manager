from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import Base

class OrderMenu(Base):
    __tablename__ = 'order_menu'

    id = Column(Integer, primary_key=True)
    menu_id = Column(Integer, ForeignKey('menu.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship('Order', back_populates='menu_items')
    menu = relationship('Menu', back_populates='orders')
