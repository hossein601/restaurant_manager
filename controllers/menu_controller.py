from controllers.order_controller import session
from models.menu_model import Menu
from models.base_model import SessionLocal


class MenuController:
    def __init__(self):
        self.session = SessionLocal()
        
    def get_menu_items(self):
        return session.query(Menu).all()

    def add_menu_item(self, name, price):
        new_item = Menu(item=name, price=price)
        session.add(new_item)
        session.commit()
        return new_item

    def delete_menu_item(self, food_id):
        item = SessionLocal.query(Menu).filter_by(id=food_id).first()
        if item:
            session.delete(item)
            session.commit()
            return f'{food_id} was deleted.'
        return f'{food_id} not found.'
    def update_menu_item(self, food_id, name, price):
        new_item = session.query(Menu).filter_by(id=food_id).first()
        if new_item:
            if name:
                new_item.name = name
            if price:
                new_item.price = price
            session.commit()
            return f'{food_id} was updated.'
        return f'{food_id} not found.'


