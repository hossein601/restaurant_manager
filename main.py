import argparse
from controllers.item_controller import ItemController
from controllers.order_controller import OrderController
from controllers.reserve_controller import ReserveController
from controllers.staff_controller import StaffController
from controllers.user_controller import UserController
from models.base import engine, Base
from models.order import Order


Base.metadata.create_all(bind=engine)

parser = argparse.ArgumentParser(description='Manage restaurant operations.')
subparsers = parser.add_subparsers(dest='command', help='commands')

menu_parser = subparsers.add_parser('item', help='Manage items')
menu_subparsers = menu_parser.add_subparsers(dest='item_command', help='Item commands')
menu_subparsers.add_parser('list', help='List all items')
add_menu_parser = menu_subparsers.add_parser('add', help='Add a new item')
add_menu_parser.add_argument('name', type=str, help='Name of the menu item')
add_menu_parser.add_argument('price', type=int, help='Price of the menu item')
add_menu_parser.add_argument('description', type=str, help='Description of the menu item')
add_menu_parser.add_argument('stock', type=int, help='stock of the item')

update_menu_parser = menu_subparsers.add_parser('update', help='update a new item')
update_menu_parser.add_argument('name', type=str, help='Name of the menu item')
update_menu_parser.add_argument('--price', type=int, help='Price of the menu item')
update_menu_parser.add_argument('--description', type=str, help='Description of the menu item')
update_menu_parser.add_argument('--stock', type=int, help='stock of the item')

delete_menu_parser = menu_subparsers.add_parser('delete', help='Delete an item')
delete_menu_parser.add_argument('name', type=str, help='Name of the menu item to delete')

filter_menu_parser = menu_subparsers.add_parser('filter', help='Filter menu items by name')
filter_menu_parser.add_argument('name', type=str, help='Name of the menu item to filter')




order_parser = subparsers.add_parser('order', help='Manage orders')
order_subparsers = order_parser.add_subparsers(dest='order_command', help='Order commands')
order_subparsers.add_parser('list', help='List all orders')
add_order_parser = order_subparsers.add_parser('add', help='Create a new order')
add_order_parser.add_argument('customer', type=str, help='Customer name')
add_order_parser.add_argument('phone_number', type=str, help='Customer phone_number')
add_order_parser.add_argument('menu_items', type=str, help='List of menu items (comma-separated)')
add_order_parser.add_argument('total_price', type=float, help='Total price of the order')
add_order_parser.add_argument('staff_id', type=int, help='Staff ID')
add_order_parser.add_argument('user_id', type=int, help='user_id')


reserve_parser = subparsers.add_parser('reserve', help='Manage reservations')
reserve_subparsers = reserve_parser.add_subparsers(dest='reserve_command', help='Reservation commands')
reserve_subparsers.add_parser('list', help='List all reservations')
add_reserve_parser = reserve_subparsers.add_parser('add', help='Create a new reservation')
add_reserve_parser.add_argument('name', type=str, help='Reservation name')
add_reserve_parser.add_argument('numbers', type=int, help='Number of people')
add_reserve_parser.add_argument('duration', type=str, help='Duration of the reservation')
add_reserve_parser.add_argument('staff_id', type=int, help='Staff ID')

staff_parser = subparsers.add_parser('staff', help='Manage staff')
staff_subparsers = staff_parser.add_subparsers(dest='staff_command', help='Staff commands')
staff_subparsers.add_parser('list', help='List all staff members')
add_staff_parser = staff_subparsers.add_parser('add', help='Add a new staff member')
add_staff_parser.add_argument('phone_number', type=str, help='phone_number ')
add_staff_parser.add_argument('name', type=str, help='Staff name')
add_staff_parser.add_argument('position', type=str, help='Staff position')

update_staff_parser = staff_subparsers.add_parser('update', help='updating existing staff')
update_staff_parser.add_argument('phone_number', type=str, help='insert staff phone number')
update_staff_parser.add_argument('--name', type=str, help='Staff name')
update_staff_parser.add_argument('--position', type=str, help='Staff position')

delete_staff_parser = staff_subparsers.add_parser('delete', help='delete staff')
delete_staff_parser.add_argument('phone_number', type=str, help='insert staff phone number')





user_parser = subparsers.add_parser('user', help='Manage users')
user_subparsers = user_parser.add_subparsers(dest='user_command', help='User commands')

add_user_parser = user_subparsers.add_parser('add', help='Create a new user')
add_user_parser.add_argument('name', type=str, help='User name')
add_user_parser.add_argument('phone_number', type=str, help='User phone number')
add_user_parser.add_argument('wallet', type=float, help='User wallet balance')

user_subparsers.add_parser('list', help='get users')

update_user_parser = user_subparsers.add_parser('update', help='Update user by phone number')
update_user_parser.add_argument('phone_number', type=str, help='User phone number')
update_user_parser.add_argument('--name', type=str, help='New name of the user')
update_user_parser.add_argument('--wallet', type=float, help='Updated wallet balance')

delete_user_parser = user_subparsers.add_parser('delete', help='Delete a user by phone number')
delete_user_parser.add_argument('phone_number', type=str, help='User phone number')

calc_price_parser = user_subparsers.add_parser('calculate_price', help='Calculate total price of user orders')
calc_price_parser.add_argument('user_id', type=int, help='User ID')

args = parser.parse_args()

if args.command == 'item':
    menu_controller = ItemController()
    if args.item_command == 'list':
        items = menu_controller.get_menu_items()
        for item in items:
            print(f'{item.id}: {item.name} /{item.price} /{item.description}/{item.stock}')
    elif args.item_command == 'add':
        menu_controller.add_menu_item(args.name, args.price, args.description, args.stock)
        print(f'Menu item {args.name} added.')
    elif args.item_command == 'update':
        updated_item = menu_controller.update_menu_item(args.name, args.price, args.description, args.stock)
        print(f'Menu item {updated_item} updated.')
    elif args.item_command == 'delete':
        message = menu_controller.delete_menu_item(args.name)
        print(message)
    elif args.item_command == 'filter':
        filter_item = menu_controller.filter_by_name(args.name)
        print(f'Menu item {filter_item} filtered.')

elif args.command == 'order':
    order_controller = OrderController()
    if args.order_command == 'list':
        orders = order_controller.list_orders()
        for order in orders:
            print(f'Order {order.order_id}: {order.customer} - {order.total_price}')
    elif args.order_command == 'add':
        new_order = order_controller.create_order(args.customer, args.phone_number,args.menu_items, args.total_price, args.staff_id,args.user_id)
        print(f'Order {new_order} created.')
    elif args.order_command == 'update':
        updated_order = order_controller.update_order(args.id, args.menu_items, args.customer, args.total_price)
        print(f'Order {updated_order.order_id} updated.')
    elif args.order_command == 'delete':
        message = order_controller.delete_order(args.id)
        print(message)

elif args.command == 'reserve':
    reserve_controller = ReserveController()
    if args.reserve_command == 'list':
        reserves = reserve_controller.get_all_reservations()
        for reserve in reserves:
            print(f'Reservation {reserve.id}: {reserve.name} - {reserve.numbers} people')
    elif args.reserve_command == 'add':
        new_reserve = reserve_controller.make_reservation(args.name, args.numbers, args.duration, args.staff_id)
        print(f'Reservation {new_reserve.id} created.')
    elif args.reserve_command == 'update':
        updated_reserve = reserve_controller.update_reservation(args.id, args.name, args.numbers, args.duration, args.staff_id)
        print(f'Reservation {updated_reserve.id} updated.')
    elif args.reserve_command == 'delete':
        message = reserve_controller.delete_reservation(args.id)
        print(message)

elif args.command == 'staff':
    staff_controller = StaffController()
    if args.staff_command == 'list':
        staff_members = staff_controller.get_staff()
        for staff in staff_members:
            print(f'{staff.id}: {staff.phone_number} /{staff.name}/ {staff.position}/')
    elif args.staff_command == 'add':
        new_staff = staff_controller.make_new_staff(args.phone_number,args.name, args.position)
        print(f'Staff member {new_staff.name} added.')
    elif args.staff_command == 'update':
        updated_staff = staff_controller.update_staff(args.phone_number, args.name, args.position)
        print(f'Staff member {updated_staff} updated.')
    elif args.staff_command == 'delete':
        message = staff_controller.delete_staff(args.phone_number)
        print(message)
    elif args.staff_command == 'filter':
        message = staff_controller.filter_staff_assigned_to_orders(args.staff_name)
        print(message)

elif args.command == 'user':
    user_controller = UserController()
    if args.user_command == 'list':
        users = user_controller.get_all_users()
        for user in users:
            print(f'User :{user.name}/{user.phone_number}/{user.wallet}')
    elif args.user_command == 'add':
        user_controller.create_user(args.name, args.phone_number, args.wallet)
        print(f'User {args.name} added.')

    elif args.user_command == 'update':
        user_controller.update_user_by_phone_number(args.phone_number, name=args.name, wallet=args.wallet)
        print(f'User with phone number {args.phone_number} updated.')
    elif args.user_command == 'delete':
        message = user_controller.delete_user_by_phone_number(args.phone_number)
        print(message)

