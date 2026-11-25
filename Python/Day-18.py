#------------------------------[ 25, Nov. 2026 ]----------------------------------------

#Method overriding - Polymorphism (one name, many duties)
class Employee:
    def role(self):
        print("General employee")
class Developer(Employee):
    def role(self):
        print("Dev Employee")


# #it never throws error on multiple declaration, it uses the latest declaration
# dev1 = Developer()
# dev2 = Employee()
# dev1.role()
# dev2.role()

#Abstraction - hiding the needed information and only exposing the information which needs to reveal to the world
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def area(self):
        #pass
        return self.a * self.b

a1 = Rectangle(50,10)
#a2 = Shape()
print(a1.area())

#Polymorphism

class SMSSender:
    def send(self):
        print("SMS sent")

class EmailSender:
    def send(self):
        print("Sent Email")

for notification in [SMSSender(),EmailSender()]:
    notification.send()
