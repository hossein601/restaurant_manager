from models.reserve_model import Reserve
from models.base_model import SessionLocal
from models.staff_model import Staff

db = SessionLocal()

class ReserveController:

    @staticmethod
    def make_reservation( name, numbers, duration, staff_id):
        staff = db.query(Staff).filter_by(id=staff_id).first()
        if not staff:
            raise ValueError(f'staff  {staff_id} not found.')
        new_reserve = Reserve(name=name, numbers=numbers, duration=duration, staff_id=staff_id)
        db.add(new_reserve)
        db.commit()
        return new_reserve

    @staticmethod
    def get_all_reservations():
        return db.query(Reserve).all()


    @staticmethod
    def update_reservation( reservation_id, name=None, numbers=None, duration=None, staff_id=None):
        reserve = db.query(Reserve).filter_by(id=reservation_id).first()
        if not reserve:
            return f'reservation {reservation_id} not found.'

        if name:
            reserve.name = name
        if numbers:
            reserve.numbers = numbers
        if duration:
            reserve.duration = duration
        if staff_id:
            staff = db.query(Staff).filter_by(id=staff_id).first()
            if not staff:
                return f'staff  {staff_id} not found.'

            reserve.staff_id = staff_id
        db.commit()

        return reserve

    @staticmethod
    def delete_reservation( reservation_id):
        reserve = db.query(Reserve).filter_by(id=reservation_id).first()
        if not reserve:
            return f'reservation  {reservation_id} not found.'

        db.delete(reserve)
        db.commit()

        return f'reservation  {reservation_id} deleted .'



