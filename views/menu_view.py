class MenuView:
    def display_menu(self, menu_items=None):
        display = 'Menu/n'
        for item in menu_items:
            display +='This item has{item.id} and name is{item.item}and  price is {item.price}'
        return display
    


