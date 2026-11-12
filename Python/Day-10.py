#---------------------------------[ Nov. 12, 2026 ]-----------------------------------------

#Functions - pre-defined function/in-built , user-defined function and lambda function
st = 'Python is so good'
number = [30,50,10,16,6]
print("Count:- ", len(number))
print("Sum:-", sum(number))
print(min(number))
print(max(number))
print(sorted(number))
print(list(reversed(number)))
print(abs(-25))
print(round(12.567,2))
print(pow(2,5))
attendance = [True, True, False, False, True]
#[0, False, None, ""]
print("Anyone present:- ", any(attendance))
print("Everyone present:- ", all(attendance))
value = 100
#print(type(value))
print(isinstance(value, int))

value1 = 100
print(type(value1))
value = input("Enter a number")
num = int(value)
print("Square of the number is:- ", num*num)

#zip function is also a part of inbuilt function - enumerate


#1. Simple function
def greet():
    print("Welcome to Python")

greet()

#2. Parameter function
def greet_person(Name):
    print("Welcome to Python tutorial,", Name)

greet_person("Shubham")

#3. Return function
def add(num1, num2):
    return num1+num2

add(20,30)
