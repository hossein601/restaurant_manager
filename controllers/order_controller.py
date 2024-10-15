from models.base_model import db
from models.menu_model import Menu
from models.order_menu_model import OrderMenu
from models.order_model import Order
from models.staff_model import Staff


class OrderController:

    @staticmethod
    def create_order(customer , menu_items, total_price, staff_id):
        staff = db.query(Staff).filter_by(id=staff_id).one_or_none()
        if not staff:
            return f'Staff not found {staff_id}'

        new_menu_items = []
        for item_order in menu_items:
            menu_item = db.query(Menu).filter_by(item=item_order).first()
            new_menu_items.append(menu_item)
        if len(new_menu_items) == 0:
            return f'Menu item not found {menu_items}'

        new_order = Order(customer=customer, total_price=total_price, staff_id=staff_id)

        new_order.menu_items.extend(new_menu_items)
        db.add(new_order)
        db.commit()

        return new_order

    @staticmethod
    def update_order( order_id, menu_items: list = None, customer: str = None, total_price: float = None):
        order = db.query(Order).filter_by(order_id=order_id).one_or_none()
        if not order:
            return f'order  {order_id} not found.'

        if customer:
            order.customer = customer
        if total_price:
            order.total_price = total_price
        if menu_items:
            db.query(OrderMenu).filter_by(order_id=order_id).delete()
            for item_id in menu_items:
                menu_item = db.query(Menu).filter_by(id=item_id).one_or_none()
                if not menu_item:
                    return  f'menu item {item_id} not found.'

        db.commit()

        return order

    @staticmethod
    def delete_order(order_id):
        order = db.query(Order).filter_by(id=order_id).first()
        if not order:
            return f'order  {order_id} not found.'

        db.query(OrderMenu).filter_by(id=order_id).delete()
        db.delete(order)
        db.commit()
        return f'order {order_id} deleted .'

    @staticmethod
    def list_orders():
        return db.query(Order).all()


















