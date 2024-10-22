from models.base import db
from models.user import User
from models.wallet_history import WalletHistory


class UserController:

    @staticmethod
    def create_user(name, phone_number, wallet):
        new_user = User(name=name, phone_number=phone_number, wallet=wallet)
        db.add(new_user)
        db.commit()

        return f'user {name} created .'

    @staticmethod
    def get_all_users():
        users = db.query(User).all()
        if users:
            return users

        return 'not user found.'

    @staticmethod
    def get_user_by_phone_number(phone_number):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            return user

        return 'user not found.'

    @staticmethod
    def update_user_by_phone_number(phone_number, name=None, wallet=None):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            if name:
                user.name = name
            if wallet is not None:
                user.wallet = wallet
            db.commit()
            return f'user {user.name} updated.'

        return f'user not found.'

    @staticmethod
    def delete_user_by_phone_number(phone_number):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            db.delete(user)
            db.commit()
            return f'user with {user.name}:{user,phone_number}  been deleted.'

        return f'user not found.'

    @staticmethod
    def add_wallet(phone_number, amount):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            user.wallet += amount
            db.flush()

            new_wallet_history = WalletHistory(type = 'increase',user_id=user.id,
                                               old_balance=user.wallet-amount,new_balance=user.wallet)
            db.add(new_wallet_history)
            db.commit()
            return f'{amount} add {user.phone_number}\ {user.wallet}'

        return 'user not found.'

    @staticmethod
    def decrease_wallet(phone_number, amount):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            if user.wallet >= amount:
                user.wallet -= amount
                db.commit()
                new_wallet_history = WalletHistory(type='decrease', user_id=user.id,
                                                   old_balance=user.wallet + amount, new_balance=user.wallet)
                db.add(new_wallet_history)
                db.commit()

                return f'decrease_wallet{user.name}:{user.wallet}'


    @staticmethod
    def get_wallet(phone_number):
        user = db.query(User).filter(User.phone_number == phone_number).one_or_none()
        if user:
            user.update_time()
            return f'Wallet balance for {user.name}: {user.wallet}'

        return 'User not found.'
