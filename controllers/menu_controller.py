from models.menu_model import Menu
from models.base_model import db

class MenuController:

    @staticmethod
    def get_menu_items():
        return db.query(Menu).all()

    @staticmethod
    def add_menu_item(name, price):
        new_item = Menu(item=name, price=price)
        db.add(new_item)
        db.commit()

        return new_item

    @staticmethod
    def delete_menu_item(food_id):
        item = db.query(Menu).filter_by(id=food_id).one_or_none()
        if item:
            db.delete(item)
            db.commit()

            return f'{food_id} was deleted.'

        return f'{food_id} not found.'

    @staticmethod
    def update_menu_item(food_id, name, price):
        new_item = db.query(Menu).filter_by(id=food_id).one_or_none()
        if new_item:
            if name:
                new_item.name = name
            if price:
                new_item.price = price
            db.commit()

            return f'{food_id} was updated.'

        return f'{food_id} not found.'

    @staticmethod
    def filter_by_name(food_name):
        food_item =db.query(Menu).filter(Menu.item==food_name)
        item = ''
        if food_item:
            for food in food_item:
                item += f'{food.id}. {food.item}. {food.price}\n'
            return item

        return f'{food_name} not found.'




