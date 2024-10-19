from models.base import db
from models.user import User

class UserController:

    @staticmethod
    def create_user(name, phone_number, wallet):
        new_user = User(name=name, phone_number=phone_number, wallet=wallet)
        db.add(new_user)
        db.commit()

    @staticmethod
    def get_all_users():
        user = db.query(User).all()
        if user:
            return user
        return 'There is not user'

    @staticmethod
    def update_user_by_phone_number(phone_number, name=None, wallet=None):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            if name:
                user.name = name
            if wallet:
                user.wallet = wallet
            db.commit()
            return f'User has been updated'
        return f'User not found'

    @staticmethod
    def delete_user_by_phone_number(phone_number):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            db.delete(user)
            db.commit()
            return f'User deleted'
        return f'User not found'

