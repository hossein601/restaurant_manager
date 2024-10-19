from models.base import db
from models.order import Order
from models.item import Item
from models.staff import Staff
from models.user import User


class OrderController:

    @staticmethod
    def create_order(customer_name, phone_number, menu_items, total_price, staff_id, user_id):
        staff = db.query(Staff).filter_by(id=staff_id).one_or_none()
        if not staff:
            return f'Staff not found {staff_id}'

        user = db.query(User).filter_by(id=user_id).one_or_none()
        if not user:
            return f'User not found {user_id}'

        new_order = Order(customer_name=customer_name, phone_number=phone_number, total_price=total_price,
                          staff_id=staff_id, user_id=user_id)

        for item in menu_items:
            menu_item = db.query(Item).filter_by(name=item).one_or_none()
            if menu_item:
                new_order.order_items.append(menu_item)

        db.add(new_order)
        db.commit()

        return new_order

    @staticmethod
    def list_orders():
        return db.query(Order).all()

    @staticmethod
    def get_order(order_id):
        order = db.query(Order).filter_by(id=order_id).one_or_none()
        if order:
            return order

        return f'Order {order_id} not found.'

    @staticmethod
    def update_order(order_id, customer_name=None, phone_number=None, menu_items=None, total_price=None, staff_id=None, user_id=None):
        order = db.query(Order).filter_by(id=order_id).one_or_none()
        if not order:
            return f'Order {order_id} not found.'

        if customer_name:
            order.customer_name = customer_name
        if phone_number:
            order.phone_number = phone_number
        if total_price:
            order.total_price = total_price
        if staff_id:
            staff = db.query(Staff).filter_by(id=staff_id).one_or_none()
            if staff:
                order.staff_id = staff_id
            else:
                return f'Staff not found {staff_id}'

        if user_id:
            user = db.query(User).filter_by(id=user_id).one_or_none()
            if user:
                order.user_id = user_id
            else:
                return f'User not found {user_id}'

        if menu_items:
            order.order_items.clear()
            for item in menu_items:
                menu_item = db.query(Item).filter_by(name=item).one_or_none()
                if menu_item:
                    order.order_items.append(menu_item)
        db.commit()

        return order

    @staticmethod
    def delete_order(order_id):
        order = db.query(Order).filter_by(id=order_id).one_or_none()
        if not order:
            return f'Order {order_id} not found.'
        db.delete(order)
        db.commit()

        return f'Order {order_id} deleted .'
















