from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from models.base_model import Base

class Reserve(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    numbers = Column(Integer, nullable=False)
    duration = Column(String, nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    staff = relationship('Staff', back_populates='reservation')
