from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    customer = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'))

    staff = relationship('Staff', back_populates='orders')
    menu_items = relationship('OrderMenu', back_populates='order')
