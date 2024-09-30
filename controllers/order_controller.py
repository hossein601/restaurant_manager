from controllers.staff_controller import session
from models.base_model import SessionLocal
from models.menu_model import Menu
from models.order_menu_model import OrderMenu
from models.order_model import Order
from models.staff_model import Staff



class OrderController:
    def __init__(self):
        self.session = SessionLocal()

    def get_order(self, order_id):
        order = session.query(OrderMenu).filter_by(order_id=order_id).first()
        return order

    def create_order(self, menu_items: list, customer: str, total_price: int, staff_id):
        staff = self.session.query(Staff).filter(Staff.id == staff_id).first()
        if not staff:
            raise ValueError(f'staff not founded with this{staff_id}')


        new_menu_item = []
        for item_id in menu_items:
            menu_item = session.query(Menu).filter_by(Menu.id==item_id).first()
            if not menu_item:
                raise ValueError(f'menu item not founded with this{item_id}')
            new_menu_item.append(menu_item)
        new_order =Order(customer=customer,total_price=total_price,staff_id=staff_id)
        new_order.menu_items.extend(new_menu_item)
        session.add(new_order)
        session.commit()
        return new_order
    def update_order(self, order_id, menu_items: list = None, customer: str = None, total_price: float = None):
        order = self.session.query(Order).filter_by(order_id=order_id).first()
        if not order:
            raise ValueError(f'Order with ID {order_id} not found.')

        if customer:
            order.customer = customer
        if total_price:
            order.total_price = total_price
        if menu_items:
            self.session.query(OrderMenu).filter_by(order_id=order_id).delete()
            for item_id in menu_items:
                menu_item = self.session.query(Menu).filter_by(id=item_id).first()
                if not menu_item:
                    raise ValueError(f'Menu item with ID {item_id} not found.')
                order_menu = OrderMenu(order_id=order_id, menu_id=menu_item.id)
                self.session.add(order_menu)

        self.session.commit()
        return order

    def delete_order(self, order_id):
        order = self.session.query(Order).filter_by(order_id=order_id).first()
        if not order:
            raise ValueError(f'Order with ID {order_id} not found.')
        self.session.query(OrderMenu).filter_by(order_id=order_id).delete()
        self.session.delete(order)
        self.session.commit()
        return f'Order ID {order_id} deleted successfully.'

    def list_orders(self):
        return self.session.query(Order).all()


















