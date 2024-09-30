from models.base_model import engine, Base, SessionLocal
from models.chef import Chef
from models.menu_model import Menu
from models.order_model import Order
from models.staff_model import Staff
from models.order_menu_model import OrderMenu
from models.waiters import Waiters

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    try:
        staff1 = Waiters(name='Ali', position='Waiter', section='Dining Room')
        db.add(staff1)

        staff2 = Chef(name='hassan', position='chef', specialty='head')
        db.add(staff2)
        db.flush()

        order1 = Order(customer='sara', total_price=160, staff_id=staff1.id)
        order2 = Order(customer='hossein', total_price=140, staff_id=staff2.id)
        db.add(order1)
        db.add(order2)
        db.flush()

        burger = Menu(item='Burger', price=10.0)
        kabab = Menu(item='Kabab', price=5.0)
        ghorme = Menu(item='Ghorme', price=7.5)
        gheime = Menu(item='Gheime', price=2.0)
        db.add_all([burger, ghorme, gheime, kabab])
        db.flush()

        order_menu1 = OrderMenu(order=order1, menu=burger)
        order_menu2 = OrderMenu(order=order2, menu=kabab)
        db.add_all([order_menu1, order_menu2])

        db.commit()

    except Exception as e:
        db.rollback()
        print(e)


