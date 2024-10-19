from models.base import db
from models.order import Order
from models.staff import Staff


class StaffController:
    @staticmethod
    def make_new_staff(name: str, phone_number: str, position:str):
        new_staff =Staff(name=name, phone_number=phone_number, position=position)
        db.add(new_staff)
        db.commit()

        return new_staff

    @staticmethod
    def get_staff():
        return db.query(Staff).all()

    @staticmethod
    def update_staff(phone_number, name=None,position=None):
        staff_member = db.query(Staff).filter(Staff.phone_number == phone_number).one_or_none()
        print(staff_member.phone_number)
        if not staff_member:
            return 'staff not found'

        if name:
            staff_member.name = name
        if position:
            staff_member.position = position
        db.commit()

        return staff_member

    @staticmethod
    def delete_staff(phone_number):
        staff_member = db.query(Staff).filter_by(phone_number=phone_number).one_or_none()
        if staff_member:
            db.delete(staff_member)
            db.commit()

            return 'staff deleted'

        return 'staff not found'

    @staticmethod
    def filter_staff_assigned_to_orders(phone_number):
        staff_order = db.query(Staff,Order).join(Order).filter(Staff.phone_number == phone_number).all()
        return staff_order
