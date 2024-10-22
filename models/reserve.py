from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime, timezone
from models.time_record import TimeRecord


class Reserve(TimeRecord,Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))

    user = relationship('User', back_populates='reservations')
    staff = relationship('Staff', back_populates='reservations')
