from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.time_record import TimeRecord


class OrderItem(TimeRecord,Base):
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer, nullable=False)

    order = relationship('Order', back_populates='order_items')
    item = relationship('Item', back_populates='order_items')
