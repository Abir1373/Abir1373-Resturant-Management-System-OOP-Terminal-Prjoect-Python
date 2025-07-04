from food_item import FoodItem 
from menu import Menu 
from users import Customer , Admin , Employee 
from restaurant import Restaurant 
from order import Order

mamar_restaurant = Restaurant('Mamar Restaurant')

def customer_menu() :
    name = input('Enter your name = ')
    email = input('Enter your email = ')
    phone = input('Enter your phone = ')
    address = input('Enter your address = ')
    customer = Customer(name = name , email = email , phone = phone , address = address) 

    while True :
        print(f'Welcome {customer.name}!!!')
        print('1.View Menu\n2.Add Item to Cart\n3.View Cart\n4.Pay Bill\n5.Exit\n') 
        choice = int(input('Enter your choice = '))
        if choice == 1 :
            customer.view_menu(mamar_restaurant) 
        elif choice == 2 :
            item_name = input('Enter item name = ') 
            item_quantity = int(input('Enter item quantity = '))
            customer.add_to_cart(mamar_restaurant,item_name,item_quantity)
        elif choice == 3 :
            customer.view_cart() 
        elif choice == 4 :
            customer.pay_bill()
        elif choice == 5 :
            break 
        else :
            print('Invalid Input')

def admin_menu() :
    name = input('Enter your name = ')
    email = input('Enter your email = ')
    phone = input('Enter your phone = ')
    address = input('Enter your address = ')
    admin = Admin(name = name , email = email , phone = phone , address = address) 

    while True :
        print(f'Welcome {admin.name}!!!')
        print('1.Add New Item\n2.Add New Employee\n3.View Employee\n4.View Items\n5.Delete Item\n6.Exit\n') 
        choice = int(input('Enter your choice = '))
        if choice == 1 :
            item_name = input('Enter item name = ')
            item_price = int(input('Enter item price = '))
            item_quantity = int(input('Enter item quantity = '))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurant,item)  
        elif choice == 2 :
            name = input('Enter employee name = ')
            phone = input('Enter employee phone = ')
            email = input('Enter employee email = ')
            designation = input('Enter employee designation = ')
            age = int(input('Enter employee age = '))
            salary = int(input('Enter employee salary = '))
            address = input('Enter employee address = ')
            employee = Employee(name,phone,email,designation,age,salary,address)
            admin.add_employee(mamar_restaurant,employee)

        elif choice == 3 :
            admin.view_employees(mamar_restaurant)
        elif choice == 4 :
            admin.view_menu(mamar_restaurant)
        elif choice == 5 :
            item_name = input('Enter item name')
            admin.delete_item(mamar_restaurant,item_name)
        elif choice == 6 :
            break 
        else :
            print('Invalid Input')



while True :
    print('--- Welcome --- ')
    print('1.Customer\n2.Admin\n3.Exit')
    choice = int(input('Enter your choice = ')) 
    if choice==1 :
        customer_menu()
    elif choice==2:
        admin_menu() 
    elif choice==3 :
        break 
    else :
        print('Invalid Input')
