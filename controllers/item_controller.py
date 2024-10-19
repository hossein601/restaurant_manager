from models.base import db
from models.item import Item


class ItemController:
    @staticmethod
    def get_menu_items():
        return db.query(Item).all()

    @staticmethod
    def add_menu_item(name, price, description, stock):
        new_item = Item(name=name, price=price, description=description, stock=stock)
        db.add(new_item)
        db.commit()

        return new_item

    @staticmethod
    def delete_menu_item(food_name):
        item = db.query(Item).filter(Item.name==food_name).one_or_none()
        if item:
            db.delete(item)
            db.commit()

            return True

        raise ValueError ("food_id is invalid")

    @staticmethod
    def update_menu_item(name, price=None,description=None,stock=None):
        new_item = db.query(Item).filter(Item.name==name).one_or_none()
        if new_item:
            if name:
                new_item.name = name
            if price:
                new_item.price = price
            if description:
                new_item.description = description
            if stock:
                new_item.quantity = stock
            db.commit()

            return f'{name} was updated.'

        return f'{name} not found.'


    @staticmethod
    def filter_by_name(name):
        food_item =db.query(Item).filter(Item.name==name)
        item = ''
        if food_item:
            for food in food_item:
                item += f'{food.id}. {food.item}. {food.price}.{food.description}.{food.image}.{food.quantity}\n'
            return item

        return f'{name} not found.'





