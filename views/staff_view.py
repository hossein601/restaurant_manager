class StaffView:
    def display_staff(self,new_staff):
        display = 'show staff/n'
        for staff in new_staff:
            display+=' staff id is {staff.id},staff name is {staff.name},staff position is {staff.position},staff speciality is {staff.speciality} and staff section isn{staff.section}'
        return display