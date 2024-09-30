from models.base_model import SessionLocal
from models.chef import Chef
from models.staff_model import Staff
from models.waiters import Waiters

session = SessionLocal()


class StaffController:
    def make_new_staff(self, name, position, section=None, specialty=None):
        if position.lower() == 'chef':
            new_staff = Chef(name=name, position=position, specialty=specialty)
        elif position.lower() == 'waiters':
            new_staff = Waiters(name=name, position=position, section=section)
        else:
            new_staff = Staff(name=name, position=position)

        session.add(new_staff)
        session.commit()
        return new_staff

    def get_staff(self):
        return session.query(Staff).all()

    def update_staff(self, staff_id, name=None, position=None, section=None, specialty=None):
        staff_member = session.query(Staff).filter_by(id=staff_id).first()
        if not staff_member:
            return 'staff not found'

        if name:
            staff_member.name = name
        if position:
            staff_member.position = position
        if section and isinstance(staff_member, Waiters):
            staff_member.section = section
        if specialty and isinstance(staff_member, Chef):
            staff_member.specialty = specialty

        session.commit()
        return staff_member

    def delete_staff(self, staff_id):
        staff_member = session.query(Staff).filter_by(id=staff_id).first()
        if staff_member:
            session.delete(staff_member)
            session.commit()
            return 'staff deleted'
        return 'staff not found'
