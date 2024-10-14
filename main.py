import argparse
from controllers.menu_controller import MenuController
from controllers.order_controller import OrderController
from controllers.reserve_controller import ReserveController
from controllers.staff_controller import StaffController


parser = argparse.ArgumentParser(description="Manage restaurant operations.")
subparsers = parser.add_subparsers(dest="command", help=" commands")
menu_parser = subparsers.add_parser("menu", help="Manage  items")
menu_subparsers = menu_parser.add_subparsers(dest="menu_command", help="Menu commands")
menu_subparsers.add_parser("list", help="List all menu items")
add_menu_parser = menu_subparsers.add_parser("add", help="Add a new menu item")
add_menu_parser.add_argument("name", type=str, help="Name of the menu item")
add_menu_parser.add_argument("price", type=float, help="Price of the menu item")
update_menu_parser = menu_subparsers.add_parser("update", help="Update   menu item")
update_menu_parser.add_argument("id", type=int, help="id of the menu item")
update_menu_parser.add_argument("--name", type=str, help="name of the menu item")
update_menu_parser.add_argument("--price", type=float, help=" price of the menu item")
delete_menu_parser = menu_subparsers.add_parser("delete", help="Delete a menu item")
delete_menu_parser.add_argument("id", type=int, help="id of the menu item to delete")


order_parser = subparsers.add_parser("order", help="Manage orders")
order_subparsers = order_parser.add_subparsers(dest="order_command", help="Order commands")
order_subparsers.add_parser("list", help="List all orders")
add_order_parser = order_subparsers.add_parser("add", help="Create a new order")
add_order_parser.add_argument("customer", type=str, help="Customer name")
add_order_parser.add_argument("menu_items", nargs='+', type=str, help="List of menu item IDs")
add_order_parser.add_argument("total_price", type=float, help="Total price of the order")
add_order_parser.add_argument("staff_id", type=int, help="Staff ID")
update_order_parser = order_subparsers.add_parser("update", help="Update an existing order")
update_order_parser.add_argument("id", type=int, help="ID of the order")
update_order_parser.add_argument("--menu_items", type=str, help="Updated customer name")
update_order_parser.add_argument("--customer", nargs='+', type=int, help="Updated list of menu item IDs")
update_order_parser.add_argument("--total_price", type=float, help="Updated total price")
delete_order_parser = order_subparsers.add_parser("delete", help="Delete an order")
delete_order_parser.add_argument("id", type=int, help="ID of the order to delete")


reserve_parser = subparsers.add_parser("reserve", help="Manage reservations")
reserve_subparsers = reserve_parser.add_subparsers(dest="reserve_command", help="Reserve commands")
reserve_subparsers.add_parser("list", help="List all reservations")
add_reserve_parser = reserve_subparsers.add_parser("add", help="Create a new reservation")
add_reserve_parser.add_argument("name", type=str, help="Name of the person making the reservation")
add_reserve_parser.add_argument("numbers", type=int, help="Number of people for the reservation")
add_reserve_parser.add_argument("duration", type=str, help="Duration of the reservation")
add_reserve_parser.add_argument("staff_id", type=int, help="Staff ID")
update_reserve_parser = reserve_subparsers.add_parser("update", help="Update an existing reservation")
update_reserve_parser.add_argument("id", type=int, help="ID of the reservation")
update_reserve_parser.add_argument("--name", type=str, help="Updated name")
update_reserve_parser.add_argument("--numbers", type=int, help="Updated number of people")
update_reserve_parser.add_argument("--duration", type=str, help="Updated duration")
update_reserve_parser.add_argument("--staff_id", type=int, help="Updated staff ID")
delete_reserve_parser = reserve_subparsers.add_parser("delete", help="Delete a reservation")
delete_reserve_parser.add_argument("id", type=int, help="ID of the reservation to delete")


staff_parser = subparsers.add_parser("staff", help="Manage staff")
staff_subparsers = staff_parser.add_subparsers(dest="staff_command", help="Staff commands")
staff_subparsers.add_parser("list", help="List all staff members")
add_staff_parser = staff_subparsers.add_parser("add", help="Add a new staff member")
add_staff_parser.add_argument("name", type=str, help="Name of the staff member")
add_staff_parser.add_argument("position", type=str, help="Position of the staff member")
add_staff_parser.add_argument("--section", type=str, help="Section ")
add_staff_parser.add_argument("--specialty", type=str, help="Specialty ")
update_staff_parser = staff_subparsers.add_parser("update", help="Update an existing staff member")
update_staff_parser.add_argument("id", type=int, help="id of the staff member")
update_staff_parser.add_argument("--name", type=str, help="update name")
update_staff_parser.add_argument("--position", type=str, help="update position")
update_staff_parser.add_argument("--section", type=str, help="update section")
update_staff_parser.add_argument("--specialty", type=str, help="update specialty")
delete_staff_parser = staff_subparsers.add_parser("delete", help="Delete a staff member")
delete_staff_parser.add_argument("id", type=int, help="ID of the staff member to delete")


args = parser.parse_args()
if args.command == "menu":
    menu_controller = MenuController()
    if args.menu_command == "list":
        items = menu_controller.get_menu_items()
        for item in items:
            print(f"{item.id}: {item.item} - {item.price}")

    elif args.menu_command == "add":
        menu_controller.add_menu_item(args.name, args.price)
        print(f"Menu item {args.name} added.")

    elif args.menu_command == "update":
        updated_item = menu_controller.update_menu_item(args.id, args.name, args.price)
        print(f"Menu item {updated_item} updated.")

    elif args.menu_command == "delete":
        message = menu_controller.delete_menu_item(args.id)
        print(message)


elif args.command == "order":
    order_controller = OrderController()
    if args.order_command == "list":
        orders = order_controller.list_orders()
        for order in orders:
            print(f"Order {order.order_id}: {order.customer} - {order.total_price}")

    elif args.order_command == "add":
        new_order = order_controller.create_order(args.customer, args.menu_items, args.total_price, args.staff_id)
        print(f"Order {new_order} created.")

    elif args.order_command == "update":
        updated_order = order_controller.update_order(args.id, args.menu_items, args.customer, args.total_price)
        print(f"Order {updated_order.order_id} updated.")

    elif args.order_command == "delete":
        message = order_controller.delete_order(args.id)
        print(message)

elif args.command == "reserve":
    reserve_controller = ReserveController()
    if args.reserve_command == "list":
        reserves = reserve_controller.get_all_reservations()
        for reserve in reserves:
            print(f"Reservation {reserve.id}: {reserve.name} - {reserve.numbers} people")

    elif args.reserve_command == "add":
        new_reserve = reserve_controller.make_reservation(args.name, args.numbers, args.duration, args.staff_id)
        print(f"Reservation {new_reserve.id} created.")

    elif args.reserve_command == "update":
        updated_reserve = reserve_controller.update_reservation(args.id, args.name, args.numbers, args.duration, args.staff_id)
        print(f"Reservation {updated_reserve.id} updated.")

    elif args.reserve_command == "delete":
        message = reserve_controller.delete_reservation(args.id)
        print(message)

elif args.command == "staff":
    staff_controller = StaffController()
    if args.staff_command == "list":
        staff_members = staff_controller.get_staff()
        for staff in staff_members:
            print(f"{staff.id}: {staff.name} - {staff.position}")

    elif args.staff_command == "add":
        new_staff = staff_controller.make_new_staff(args.name, args.position, args.section, args.specialty)
        print(f"Staff member {new_staff.name} added.")

    elif args.staff_command == "update":
        updated_staff = staff_controller.update_staff(args.id, args.name, args.position, args.section, args.specialty)
        print(f"Staff member {updated_staff} updated.")

    elif args.staff_command == "delete":
        message = staff_controller.delete_staff(args.id)
        print(message)
