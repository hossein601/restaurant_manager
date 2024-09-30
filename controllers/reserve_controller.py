from models.reserve_model import Reserve
from models.base_model import SessionLocal
from models.staff_model import Staff

class ReserveController:
    def __init__(self):
        self.session = SessionLocal()

    def make_reservation(self, name, numbers, duration, staff_id):
        staff = self.session.query(Staff).filter_by(id=staff_id).first()
        if not staff:
            raise ValueError(f'Staff with ID {staff_id} not found.')
        new_reserve = Reserve(name=name, numbers=numbers, duration=duration, staff_id=staff_id)
        self.session.add(new_reserve)
        self.session.commit()
        return new_reserve

    def get_all_reservations(self):
        return self.session.query(Reserve).all()

    def get_reservation(self, reservation_id):
        return self.session.query(Reserve).filter_by(id=reservation_id).first()

    def update_reservation(self, reservation_id, name=None, numbers=None, duration=None, staff_id=None):
        reserve = self.session.query(Reserve).filter_by(id=reservation_id).first()
        if not reserve:
            raise ValueError(f'Reservation with ID {reservation_id} not found.')

        if name:
            reserve.name = name
        if numbers:
            reserve.numbers = numbers
        if duration:
            reserve.duration = duration
        if staff_id:
            staff = self.session.query(Staff).filter_by(id=staff_id).first()
            if not staff:
                raise ValueError(f'Staff with ID {staff_id} not found.')
            reserve.staff_id = staff_id

        self.session.commit()
        return reserve

    def delete_reservation(self, reservation_id):
        reserve = self.session.query(Reserve).filter_by(id=reservation_id).first()
        if not reserve:
            raise ValueError(f'Reservation with ID {reservation_id} not found.')
        self.session.delete(reserve)
        self.session.commit()
        return f'Reservation ID {reservation_id} deleted successfully.'



