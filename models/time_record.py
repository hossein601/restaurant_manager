from datetime import datetime
from sqlalchemy import Column, func, text, TIMESTAMP, Integer
from models.base import Base


class TimeRecord(Base):
    __tablename__ = 'time_record'

    id = Column(Integer, primary_key=True)
    created_time = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_time = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())
