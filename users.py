from abc import ABC 
from restaurant import Restaurant
from order import Order
from food_item import FoodItem

class User(ABC):

    def __init__(self,name,phone,email,address):
        self.name = name 
        self.phone = phone 
        self.email = email 
        self.address = address 

class Employee(User):

    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age 
        self.designation = designation 
        self.salary = salary

class Admin(User):

    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []
    
    def add_employee(self,restaurant,employee):
        restaurant.add_employees(employee) 
    
    def view_employees(self,restaurant):
        restaurant.view_employees() 

    def add_new_item(self,restaurant,item) :
        restaurant.menu.add_menu_item(item)
    
    def delete_item(self,restaurant,item) :
        restaurant.menu.remove_item(item)

    def view_menu(self,restaurant) :
        restaurant.menu.show_menu()


class Customer(User) : 

    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address) 
        self.cart = Order()
    
    def view_menu(self,restaurant) :
        restaurant.menu.show_menu() 
    
    def add_to_cart(self,restaurant,item_name,quantity) :
        item = restaurant.menu.find_item(item_name) 
        if item :
            if quantity > item.quantity :
                print('Item quality exceeded')
            else :
                item.quantity = quantity 
                self.cart.add_item(item) 
                print('item added') 
        else :
            print('Item Not Found')
    
    def view_cart(self) :
        print('*** View Cart ***') 
        print("Name\t price \t quantity")
        for item,quantity in self.cart.items.items() :
            print(f'{item.name} {item.price} {quantity}')
        print(f'Total Price : {self.cart.total_price}')

    def pay_bill(self) :
        print(f'Total {self.cart.total_price} paid successfully')
        self.cart.clear()

