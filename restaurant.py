from menu import Menu 

class Restaurant:

    def __init__(self,name):
        self.name = name 
        self.employees = []
        self.menu = Menu()
    
    def add_employees(self,employee) :
        self.employees.append(employee)

    def view_employees(self):

        for emp in self.employees :
            print(emp.name,emp.phone,emp.email,emp.address,emp.age,emp.designation,emp.salary) 