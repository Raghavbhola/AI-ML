#--------------------------[ Nov. 19, 2026 ]-------------------------------------


file_TC = 'num.txt'
try:
    with open(file_TC, "w") as tc_f:
        tc_f.write("125")
    with open(file_TC, "r") as tc_f1:
        num = int(tc_f1.read())
    print("Twice of number:-", num*2)
except FileNotFoundError:
    print("File not found broo!!")
except ValueError:
    print("The file does not contain a valid number")
except OSError as Error:
    print("Error found", Error)
filename1 = "employees.csv"
try:
    with open(filename1, "w") as file11:
        file11.write("id,name,department\n101,Asha,IT\n102,Ravi,HR\n")
    with open(filename1, "r") as file11:
        print(file11.read())
except OSError as error:
    print("File error:", error)

Exception handling - Error handling
Error and exception - stops the execution of the program or terminate the execution flow of the program by causing some unwanted result
Error - we can't handle, we must have to resolve it for our program to work.
Error - when we are trying to manipulate Compiler logic, we used to get Error.

Exception - An unexpected problem or conldition that occur while a program is running and disrupts its normal flow
Instead of letting down the whole application crash, handle the exception gracefully - Exception handling 
print(10/0)  #it will throw an Eception
s = "Shub" + 123 - it will throw an Error
print(s)

ZeroDivisionError
try:
    print(10/0) #Exception occured here
except ZeroDivisionError:
    print("A number divide by Zero is not possible")

Value Error
try:
    n = int("twenty") #Exception occured here
except ValueError:
    print("The input can't be typecast")

IndexError
li = ['Navya', 'Kritika'] #jee
try:
    #roll = input()
    print(li[5]) #Exception occured here
except IndexError:
    print("Roll number not exist")

KeyError
dic = {'name':'Asha', 'Dept':'IT', 'Loc':'HYD'}
try:
    print(dic['salary'])
except KeyError as Error:
    print("Key missing:- ", Error)
