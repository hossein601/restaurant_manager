from  sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime

class Reserve(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('user.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))

    user = relationship('User', back_populates='reservations')
    staff = relationship('Staff', back_populates='reservations')
