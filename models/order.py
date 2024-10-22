from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime, timezone
from models.time_record import TimeRecord


class Order(TimeRecord,Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    phone_number = Column(String(15), nullable=False)
    total_price = Column(Integer, nullable=False)
    time = Column(DateTime, default=datetime.now(timezone.utc))
    user_id = Column(Integer, ForeignKey('user.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))

    user = relationship('User', back_populates='orders')
    staff = relationship('Staff', back_populates='orders')
    order_items = relationship('OrderItem', back_populates='order')

    def calculate_total_price(self):
        total_price = 0
        for order_item in self.order_items:
            item = order_item.item
            item.decrease_stock(order_item.quantity)
            total_price += item.price * order_item.quantity
        self.total_price = total_price
        return total_price
