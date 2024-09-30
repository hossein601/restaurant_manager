class ReserveView:
    def show_reservation(self,reservation):
        display = 'show reservation/n'
        for item in reservation:
            display+='The reserve id is{item.id} , the reserve name is{item.name} ,the reserve number is{item.number}, the reserve  duration is {item.duration}'
        return display
