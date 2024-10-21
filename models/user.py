from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base, db
from models.time_record import TimeRecord


class WalletHistory(Base):
    __tablename__ = 'wallet_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    wallet = Column(Float, nullable=False)
    user = relationship('User', back_populates='history_records')

class User(TimeRecord, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, index=True)
    wallet = Column(Float, nullable=False, default=0.0)

    orders = relationship('Order', back_populates='user')
    reservations = relationship('Reserve', back_populates='user')
    history_records = relationship('UserHistory', back_populates='user')

    def history(self):
        history_record = WalletHistory(user_id=self.id,name=self.name, phone_number=self.phone_number,wallet=self.wallet)
        db.add(history_record)
        db.commit()


