
## **Restaurant Manager System**


This is resturant manager that have 4 base calss menu,reserve,staff,order.They include CRUD features for create, read ,update,delete instance each  of each object.

## **Installation**

First should install requirement.txt. Then create new database and add yoour database. create your own database.


```bash
pip install psycopg2-binary
pip install SQLAlchemy
pip install python-dotenv
```
## Usage
First install database and create new database with your specific username and password,add it to file 'base_model'

### from source
```bash
git clone https://github.com/hossein601/restaurant_manager.git
cd restaurant
pip install -e .
```

## CLI
```bash
>python main.py -h

usage: main.py [-h] {menu,order,reserve,staff} ...
options:
  -h, --help            show this help message and exit
positional arguments:
  {menu,order,reserve,staff}
                        commands
    menu                Manage items
    order               Manage orders
    reserve             Manage reservations
    staff               Manage staff
```
```bash
>python main.py menu -h

options:
  -h, --help            show this help message and exit
positional arguments:
  {list,add,update,delete,filter}
                        Menu commands
    list                List all menu items
    add                 Add a new menu item
    update              Update menu item
    delete              Delete a menu item
    filter              Filter menu items
```
```bash
>python main.py order -h

positional arguments:
  {list,add,update,delete}
                        Order commands
    list                List all orders
    add                 Create a new order
    update              Update an existing order
    delete              Delete an order

options:
  -h, --help            show this help message and exit
```
```bash
>python main.py reserve -h

positional arguments:
  {menu,order,reserve,staff}
                        commands
    menu                Manage items
    order               Manage orders
    reserve             Manage reservations
    staff               Manage staff

options:
  -h, --help            show this help message and exit      
```
```bash
>python main.py staff -h

positional arguments:
  {list,add,update,delete,filter}
                        Staff commands
    list                List all staff members
    add                 Add a new staff member
    update              Update an existing staff member
    delete              Delete a staff member
    filter              staff for each order

options:
  -h, --help            show this help message and exit     
```

