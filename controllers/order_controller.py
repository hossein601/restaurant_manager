from models.base_model import SessionLocal
from models.menu_model import Menu
from models.order_menu_model import OrderMenu
from models.order_model import Order
from models.staff_model import Staff

db = SessionLocal()

class OrderController:
    def get_order(self ,order_id):
        order = db.query(OrderMenu).filter_by(order_id=order_id).first()
        return order

    def create_order(self , menu_items: list, customer: str, total_price: int, staff_id):
        staff = db.query(Staff).filter(Staff.id == staff_id).first()
        if not staff:
            raise ValueError(f'staff not founded with this{staff_id}')

        new_menu_item = []
        for item_id in menu_items:
            menu_item = db.query(Menu).filter_by(Menu.id==item_id).first()
            if not menu_item:
                raise ValueError(f'menu item not founded with this{item_id}')
            new_menu_item.append(menu_item)
        new_order =Order(customer=customer,total_price=total_price,staff_id=staff_id)
        new_order.menu_items.eextend(new_menu_item)
        db.add(new_order)
        db.commit()
        return new_order
    def update_order(self, order_id, menu_items: list = None, customer: str = None, total_price: float = None):
        order = db.query(Order).filter_by(order_id=order_id).first()
        if not order:
            raise ValueError(f'Order with ID {order_id} not found.')

        if customer:
            order.customer = customer
        if total_price:
            order.total_price = total_price
        if menu_items:
            db.query(OrderMenu).filter_by(order_id=order_id).delete()
            for item_id in menu_items:
                menu_item = db.query(Menu).filter_by(id=item_id).first()
                if not menu_item:
                    raise ValueError(f'Menu item with ID {item_id} not found.')
                order_menu = OrderMenu(order_id=order_id, menu_id=menu_item.id)
                db.add(order_menu)

        db.commit()
        return order

    def delete_order(self, order_id):
        order = db.query(Order).filter_by(order_id=order_id).first()
        if not order:
            raise ValueError(f'Order with ID {order_id} not found.')
        db.query(OrderMenu).filter_by(order_id=order_id).delete()
        db.delete(order)
        db.commit()
        return f'Order ID {order_id} deleted successfully.'

    def list_orders(self):
        return db.query(Order).all()


















