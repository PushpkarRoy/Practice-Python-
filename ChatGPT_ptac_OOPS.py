# 🧠 Python OOP Practice Set — Class Methods, Init, Attributes, Static, Encapsulation, Abstraction


# ✅ 1. Create a Student class
# Attributes: name, age, course
# Method: display_details() to print student info
# Create 3 student objects and call their method

class Students:
    def __init__(self, name, age, course):
        self.name = name 
        self.age = age 
        self.course = course 
    
    def display_details(self):
        print("Welcome", self.name, "Your age is ", self.age, "and your course is ", self.course)

s1 = Students("Monty", 22, "B.com")
s1.display_details()

# ✅ 2. Use __init__ to automatically assign attributes
# Create a Product class with price, name, and category

sports1 = ["wicket", "bat", "ball"]
sports2 = ["Supporter", "Kit", "T_shirts"]
sports3 = ["Bat_hammer", "strickers", "Sandpaper"]
sports4 = {"earphone": 800, "Bat_handle": 400, "Cricket_ball": 400}

class Roy_sports:
    def __init__(self, name, price):
        self.name = name 
        self.price = price

    def Product_type(self):
        if self.name in sports1:
            print("Sports Category := ", self.name, "in your price := ", self.price)
        elif self.name in sports2:
            print(" Cloth Category := ", self.name, "in your price := ", self.price)
        elif self.name in sports3:
            print(" Tool Category := ", self.name, "in your price := ", self.price,)
        elif self.name in sports4:
            print("Yes we have your item", self.name, "and price is", sports4[self.name])       # print product category and price both 
        else:
            print("Your product ", self.name, " is not avalible in my store please wait ", " I note your price range also for future ", "RS", self.price)


s1 = Roy_sports("wicket", 800)
s2 = Roy_sports("T_shirts", 300)
s1.Product_type()
s2.Product_type()
s3 = Roy_sports("Football", 700)
s3.Product_type()
s4 = Roy_sports("earphone", 800)
s4.Product_type()

# ✅ 3. Class vs Instance Attribute
# Create a class BankAccount

class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name 
        self.account_no = account_no 
        self.balance = balance
    
    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs", amount, "debited from your account")

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs", amount, "Credited in your account")

    def final_balance(self):
        print("Your current balance is ", self.balance)

s1 = BankAccount("Monty", 1234, 10000)
s1.debit(3000)
s1.debit(1000)
s1.credit(200)
s1.credit(200)
s1.final_balance()

# ✅ 4. Add a method to deposit money
# Add deposit(self, amount) method to the BankAccount class
# Update the balance and print confirmation

class HDFC_bank:
    def __init__(self, name, account_no, balance):
        self.name = name 
        self.account_no = account_no 
        self.balance = balance
    
    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs", amount, "debited from your account")

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs", amount, "Credited in your account")

    def final_balance(self):
        print("Your current balance is ", self.balance)

h1 = HDFC_bank("Karan", 1234, 10000)
h1.debit(1000)
h1.debit(4000)
h1.credit(2200)
h1.credit(100)
h1.final_balance()

# ✅ 5. Create a @staticmethod
# Class: MathUtils
# Static method: square(x)
# Call it without creating an object

class Maths_class:

    @staticmethod
    def welcome_message():
        print("Welcome everyone")

m1 = Maths_class()
m1.welcome_message()

# ✅ 6. Abstraction Example
# Create an abstract class Vehicle (using abc module)
# Define an abstract method start()
# Create child classes Car, Bike that implement start()

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started...")

class Bike(Vehicle):
    def start(self):
        print("Bike started...")

c = Car()
c.start()

# ✅ 7. Encapsulation Practice
# Create a Person class
# Use __age (private variable)
# Add getter and setter methods to read/change age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("❌ Age can't be negative.")


p1 = Person("Pushpkar", 25)

print("Age:", p1.get_age())

p1.set_age(30)
print("Updated Age:", p1.get_age())

p1.set_age(-5)

# ✅ 8. Library Management System
# Create Book class with title, author, availability
# Add methods to borrow_book() and return_book()
# If book is unavailable, print message

books = ["Rich dad poor dad", "5 am club", "Belive in your self", "The power of your subconscious mind", "Atomic habits", "You can win"]

class Library():
    def __init__(self, name):
        self.name = name 

    def borrow_book(self):
        if self.name in books:
            books.remove(self.name)
            print("Yes Book is available right now. You will borrow it ", self.name)
        else:
            print("Sorry but book is not avalible right now", self.name)
            
        
    def return_book(self):
        books.append(self.name)
        print("Thank you for returing the book ", self.name)
    
    def total_available(self):
        print(books)

student2 = Library("Rich dad poor dad")
student2.borrow_book()

student3 = Library("Rich dad poor dad")
student3.borrow_book()

student4 = Library("Mahabharat")
student4.borrow_book()

student2.return_book()
student3.borrow_book()

# ✅ 9. Create a static ID generator
# In a class Employee, use a static method generate_id()
# Auto-increment employee IDs using a class-level counter

class Employee():
    
    count = 0 
    def __init__(self, name):
        self.name = name 
        Employee.count += 1

    def emp_count(self):
        print("Current Total Employee present in the office right now := ", Employee.count)

e1 = Employee("Monty")
e2 = Employee("Harsh")
e3 = Employee("Karan")
e2.emp_count()

# ✅ 10. Create a simple class hierarchy
# Base class: Appliance with power_on() method
# Child classes: Fan, AC, Heater
# Override method to print specific messages like “Fan is now running.”

class Appliance:
    def power_on(self):
        print("Appliance is powered on.")

class Fan(Appliance):
    def power_on(self):
        print("Fan is now running.")

class AC(Appliance):
    def power_on(self):
        print("AC is cooling the room.")

class Heater(Appliance):
    def power_on(self):
        print("Heater is warming the room.")

# Test
f = Fan()
f.power_on()

a = AC()
a.power_on()
