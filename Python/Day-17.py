#===========================[ Nov. 23, 2026 ]==================================

#OOPS - is not a programming language, its a concept, its a paradigm - cpp
#KISS - keep it simple stupid.
#1. Abstraction - implement(abstract keyword we use to define the class)
#2. Inheritance - DRY (Don't repeat yourself) concept - extends 
#3. Polymorphism - one name, many duties
#4. Encapsulation - binding the data and feature in a single unit
#5. Class and Object - consider this is a basic property - object is basically a real world entity, Class is a blue-print of object

#Abstract and concrete class - we cant create child for abstract class, but the following procedure is possible for concrete class
#class_name new = child-name class-name() 
#child-name = class-name(pm)

#POpl - Procedure oriented P.l. -> pointers, 
#1991 - 
#Fortran, Cobol, Assembly,A, B, C - 
#type of PL - 1. Interpreted, 2. Compile - Java, CPP, 3. Scripting - HTML, JS, TS


#-----------------------[ 24, nov. 2026 ]----------------------------

#Class and Objects
#class - is a blueprint of object (it exists everywhere but present nowhere)
#object - is a real world entity, it will have features

class Car:
    def property(self,a,b):
        self.a = a
        self.b = b
        print("Car will have four tyres and one driver seat")

myCar = Car()
myCar.property('sedan','suv')

#python - __init__() - default constructor,  __init__(self, a, b, c) - Parameterized cons., no copy cons
class Employee:
     def __init__(self, name, role):
         self.name = name
         self.role = role

     def display(self):
         print(f"{self.name} is having the following role:- {self.role}")

emp1 = Employee("Asha","Analyst")
emp1.display()
emp2 = Employee("Nikhil","Dev")
emp2.display()
emp3 = Employee("Shiva","IOS Dev")
emp3.display()
emp4 = Employee("Amit","Tester")
emp4.display()

#instance and class variable
class myRecord:
    org = "Ericsson"
    def __init__(self, name):
        self.name = name

first = myRecord("Shubham")
second = myRecord("Palak")
print(first.name+' - '+first.org)
print(second.name+' - '+second.org)

#Inheritance - inherting/deriving the properties from top to buttom (Parent to child)
class Person:
    def intro(self):
        print("Im a Human")

class Student(Person):
    def learn(self):
        print("I'm learning to walk")

abc = Student()
abc.intro()
abc.learn()

#Encapsulation - Binding data and function in a single unit in such a way, we dont want the world know what is going inside/behind the screen
Button press and fan started moving
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance +=amount
    def getAmount(self):
        return self.__balance

Amnt = BankAccount(1000)
Amnt.deposit(500)
Amnt.getAmount()
