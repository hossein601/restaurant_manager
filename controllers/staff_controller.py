from models.base_model import db
from models.chef import Chef
from models.staff_model import Staff
from models.waiter import Waiters


class StaffController:
    @staticmethod
    def make_new_staff(name: str, position: str, section=None, specialty=None):
        if position.lower() == 'chef':
            new_staff = Chef(name=name, position=position, specialty=specialty)
        elif position.lower() == 'waiter':
            new_staff = Waiters(name=name, position=position, section=section)
        else:
            new_staff = Staff(name=name, position=position)
        db.add(new_staff)
        db.commit()

        return new_staff

    @staticmethod
    def get_staff():
        return db.query(Staff).all()

    @staticmethod
    def update_staff(staff_id, name=None, position=None, section=None, specialty=None):
        staff_member = db.query(Staff).filter_by(id=staff_id).first()
        if not staff_member:
            return 'staff not found'

        if name:
            staff_member.name = name
        if position:
            staff_member.position = position
        if section:
            staff_member.section = section
        if specialty:
            staff_member.specialty = specialty
        db.commit()

        return staff_member

    @staticmethod
    def delete_staff(staff_id):
        staff_member = db.query(Staff).filter_by(id=staff_id).first()
        if staff_member:
            db.delete(staff_member)
            db.commit()

            return 'staff deleted'

        return 'staff not found'
