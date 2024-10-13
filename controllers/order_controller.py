from models.base_model import db
from models.menu_model import Menu
from models.order_menu_model import OrderMenu
from models.order_model import Order
from models.staff_model import Staff


class OrderController:

    @staticmethod
    def get_order(order_id):
        order = db.query(OrderMenu).filter_by(id=order_id).first()
        return order

    @staticmethod
    def create_order(customer:str,menu_items: list, total_price: int, staff_id):
        staff = db.query(Staff).filter_by(id = staff_id).first()
        if not staff:
            return f'staff not founded with this{staff_id}'

        new_menu_item = []
        for item_id in menu_items:
            menu_item = db.query(Menu).filter_by(item=item_id).first()
            if not menu_item:
                return f'menu item not founded with this{item_id}'

            new_menu_item.append(menu_item)

        new_order =Order(customer=customer,total_price=total_price,staff_id=staff_id)
        new_order.menu_items.extend(new_menu_item)
        db.add(new_order)
        db.commit()

        return new_order

    @staticmethod
    def update_order( order_id, menu_items: list = None, customer: str = None, total_price: float = None):
        order = db.query(Order).filter_by(order_id=order_id).first()
        if not order:
            return f'order  {order_id} not found.'

        if customer:
            order.customer = customer
        if total_price:
            order.total_price = total_price
        if menu_items:
            db.query(OrderMenu).filter_by(order_id=order_id).delete()
            for item_id in menu_items:
                menu_item = db.query(Menu).filter_by(id=item_id).first()
                if not menu_item:
                    return  f'menu item {item_id} not found.'
                order_menu = OrderMenu(order_id=order_id, menu_id=menu_item.id)
                db.add()
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


















