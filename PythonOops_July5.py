'''
1. Design a class hierarchy for a Library System.
Base class: Item (with title, author, ID)
Subclasses: Book, Magazine, DVD
Implement methods like check_out() and return_item()
Use inheritance and polymorphism.
'''

class Item:
    def __init__(self, title, author, id):
        self.title = title
        self.author = author
        self.id = id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out")
        else:
            print(f"{self.title} is already checked out")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was not checked out")

class Book(Item):
    def __init__(self, title, author, id, pages):
        Item.__init__(self, title, author, id)
        self.pages = pages

class Magazine(Item):
    def __init__(self, title, author, id, issue):
        Item.__init__(self, title, author, id)
        self.issue = issue

class DVD(Item):
    def __init__(self, title, author, id, duration):
        Item.__init__(self, title, author, id)
        self.duration = duration

book1 = Book("Inspection","Nolan","11111","100")
magazine1 = Magazine("Interstellar","Nolan","22222",1)
dvd1 = DVD("Inspection","Nolan","33333",183)

book1.check_out()
magazine1.check_out()
dvd1.check_out()

book1.return_item()


print('......................................................................2')

'''
2. Create a Billing System for an Online Store.

Class Product: name, price
Class Cart: list of products, add/remove item, calculate total
Apply encapsulation for price calculation logic
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        if price > 0:
            self.__price = price      #using price private method....
        else:
            self.__price = 0

    def get_price(self):
        return self.__price
    def __str__(self):
        return f"{self.name} - {self.__price}"

class Cart:
    def __init__(self):
        self.products = []

    def add_item(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart")

    def remove_item(self, productName):
        for product in self.products:
            if product.name == productName:
                self.products.remove(product)
                print(f"{productName} removed from cart")

                return print(f"{productName} not found in cart")

    def __calulateTotal(self):
        total = sum(product.get_price() for product in self.products)
        return total

    def show_cart(self):
        print("\n Items in cart:")
        for product in self.products:
            print("-",product)
        print(f"Total: {self.__calulateTotal()}")


p1 = Product("mobile",10000)
p2 = Product("computer",99000)
p3 = Product("TV",9000)

cart = Cart()

#adding products to cart
cart.add_item(p1)
cart.add_item(p2)

#removing
cart.remove_item("TV")
cart.add_item(p3)
cart.remove_item("mobile")

#final cart value
cart.show_cart()


print('..................................................3')

'''
Build a Vehicle Inheritance Model.

Base class: Vehicle
Subclasses: Car, Bike, Truck
Each subclass should override a method move() with its own behavior.
'''
#polymorphism

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving on the road")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving smoothly on the road")

class Bike(Vehicle):
    def move(self):
        print(f"{self.name} is driving slowly on two wheels")

class Truck(Vehicle):
    def move(self):
        print(f"{self.name} is driving slowly with heavy loads")

car = Car("BMW")
bike = Bike("KTM")
truck = Truck("TATA")

vehicles = [car, bike, truck]

for vehicle in vehicles:
    vehicle.move()


print('..................................................4')

'''
 Implement a simple ATM System using OOP.

Class: Account (balance, pin)
Methods: check_balance(), withdraw(), deposit()
Use encapsulation to protect sensitive data
'''

class Account:
    def __init__(self, pin, balance = 0):
        self.__pin = pin
        self.__balance = balance

    def check_pin(self, entered_pin):
        return entered_pin == self.__pin

    def check_balance(self,entered_pin):
        if self.check_pin(entered_pin):
            print(f"Your account balance is: {self.__balance}")
        else:
            print("Incorrect pin")

    def deposit(self, entered_pin ,amount):
        if self.check_pin(entered_pin):
            if amount > 0:
                self.__balance += amount
                print(f"{amount} deposited successfully.Current Balance: {self.__balance}")
            else:
                print("Enter/Add valid amount")
        else:
            print("Incorrect pin")

    def withdraw(self, entered_pin ,amount):
        if self.check_pin(entered_pin):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"{amount} withdrawn successfully.Remaining Balance: {self.__balance}")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect pin")

my_account = Account(pin=1111,balance=10000)

my_account.check_balance(1111)
my_account.deposit(1111,9000)
my_account.withdraw(1111,5000)
my_account.check_balance(1111)


print('........................................................5')

'''
5. Design a Student Management System.

Class Person with attributes: name, age
Class Student inherits from Person and adds: student_id, courses
Add method to display full student details using abstraction.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#taking subclass
class Student(Person):
    def __init__(self, name, age, student_id, courses):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:")
        for course in self.courses:
            print(f"---{course}")

student1 = Student("praneeth", 25, "25Y1111", ["Python", "Mysql"])
student1.display_details()


print('............................................6')
'''
Create an Animal Sound Simulation.

Use polymorphism: each animal class (Dog, Cat, Cow) should implement make_sound()
Write a function play_sound(animal) that works for all.
'''

class Animal:
    def make_sound(self):
        print("General Animal Sound")

class Dog(Animal):
    def make_sound(self):
        print(" Dog sound: Bow Bow Bowwwwwwwwwwwww")

class Cat(Animal):
    def make_sound(self):
        print("Cat sound : Meowwwwwwwwwwwwwwww")

class Cow(Animal):
    def make_sound(self):
        print("Cow sound : ammbbaaaaaaaaaaaaaaa")

def play_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog)
play_sound(cat)
play_sound(cow)


print('..................................7')

'''
7. Build a Company Employee Hierarchy.

Class Employee with salary, name
Subclasses: Manager, Developer, Intern
Add bonus logic using method overriding.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.03

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
        print(f"Employee Bonus: {self.calculate_bonus()}")

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.30

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

class Intern(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05

emp1 = Manager("Praneeth", 50000)
emp2 = Developer("Raj", 40000)
emp3 = Intern("Ram", 20000)

employees = [emp1, emp2, emp3]
for employee in employees:
    employee.display_info()
    print('---------')


print('..............................................8')
'''
8. Develop a Movie Ticket Booking System.

Class Movie (name, seats, time)
Class Ticket to book or cancel tickets
Use encapsulation for seat management and price.
'''

class Movie:
    def __init__(self, name, time, seats, price):
        self.name = name
        self.time = time
        self.__seats = seats
        self.__price = price

    def get_details(self):
        print(f"Movie Name: {self.name}")
        print(f"Movie Time: {self.time}")
        print(f"Available Seats: {self.__seats}")
        print(f"Ticket Price: {self.__price}")

    def get_available_seats(self):
        return self.__seats

    def get_price(self):
        return self.__price

    def _reduce_seats(self,quantity):
        if quantity <= self.__seats:
            self.__seats -= quantity
            return True
        return False

    def _increase_seats(self,quantity):
        self.__seats += quantity

class Ticket:
    def book_ticket(self, movie, quantity):
        if movie._reduce_seats(quantity):
            total = quantity * movie.get_price()
            print(f"Booked:{quantity} tickets for {movie.name} at {total}")
        else:
            print(f"Not enough seats for {movie.name}.Only {movie.get_available_seats()} available.")

    def cancel_ticket(self, movie, quantity):
        movie._increase_seats(quantity)
        refund = quantity * movie.get_price()
        print(f"Cancelled {quantity} tickets for {movie.name} refund amount {refund}")

m1 = Movie("Coolie", "11:00 AM", 100, 250)

m1.get_details()
t = Ticket()
t.book_ticket(m1, 5)
t.cancel_ticket(m1, 1)
m1.get_details()


print('.........................................9')
'''
9. Create a Shape Drawing App using Abstraction.

Abstract class: Shape
Subclasses: Circle, Rectangle, Triangle with method draw()
Call them in a loop to simulate drawing.
'''

#importing abstractMethod

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")
class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.draw()


print('....................................10')
'''
10. Design a Food Delivery App Backend Classes.

Class Restaurant with menu
Class Order with cart, delivery address
Use multiple inheritance for Customer and DeliveryAgent
'''

class Restaurant:
    def __init__(self, name,menu):
        self.name = name
        self.menu = menu

    def show_menu(self):
        print(f"Menu Name: {self.name}")
        for item, price in self.menu.items():
            print(f"{item}: {price}")

class Order:
    def __init__(self, restaurant, customer, delivery_address):
        self.restaurant = restaurant
        self.customer = customer
        self.delivery_address = delivery_address
        self.cart = []

    def add_item(self, item):
        if item in self.restaurant.menu:
            self.cart.append(item)
            print(f"{item} added to cart")
        else:
            print(f"{item} not available in {self.restaurant.name}")

    def total_price(self):
        return sum(self.restaurant.menu[item] for item in self.cart)

    def summary(self):
        print("\n Order summary")
        print(f"Customer Name: {self.customer.name}")
        print(f"Delivery Address: {self.delivery_address}")
        print("Items:",",".join(self.cart))
        print(f"Total Price: {self.total_price()}")

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class DeliveryAgent:
    def __init__(self, agent_name, vehicle_name):
        self.agent_name = agent_name
        self.vehicle_name = vehicle_name

class User(Customer, DeliveryAgent):
    def __init__(self, name, phone, agent_name=None, vehicle_name=None):
        Customer.__init__(self, name, phone)
        if agent_name and vehicle_name:
            DeliveryAgent.__init__(self, agent_name, vehicle_name)

menu ={'dosa':60, 'idly':30,'puri':50}
rest =Restaurant("Taza Tiffins", menu)

cus = Customer("Praneeth",992299339944)

order = Order(rest, cus, 'DLF')
order.add_item('dosa')
order.add_item('puri')
order.summary()