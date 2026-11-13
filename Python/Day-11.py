#-------------------------------------[ Nov. 13, 2026 ]----------------------------------------

#Functions - pre-defined function/in-built , user-defined function and lambda function
#4. Function with Default parameter
def calc_price(price, tax_amount = 0.18):
    return price+price*tax_amount

print(calc_price(1000))
calc_price(1000,0.05)

def greet(name = "Class"):
    print("Good morning", name, "!!")

greet("Kritika", "Raghav")

#5. Keyword argument
def print_details(name, role, city):
    print("Name:- ", name)
    print("Role:- ", role)
    print("City:- ", city)

print_details(role = "Dev", name = "Akash", city = "YNR")
print_details("Dev", "Akash", "YNR")

#6. *args (any number of argument) and **kwargs (any number of keyword arguement)
def total(*numbers):
    return sum(numbers)

def show_details(**details):
    print(details)

total(10,20,30)
show_details(name="Asha", role="Analyst")
show_details(name="Asha")
show_details(name="Asha",city = "YNR", role = "Dev")
show_details("Asha","QA")

def total(**numbers):
    return sum(numbers.values())

# def show_details(**details):
#     print(details)

print(total(num1 = 10,num2 = 20,num3 = 30, num4 = 50, num5 = 100))


#7. Lambda function - 
square = lambda num:num*num
def sqr(num): return num*num
add = lambda a,b: a+b

print(sqr(7))
print(square(7))
print(add(7,8))
print(type(add))

Lambda sort function
emp = [("Ravi", 70000),("Ankit", 90000),("Jagmeet", 65000),("Rahul",78000)]
emp.sort(key=lambda emp:emp[0])
print(emp)
