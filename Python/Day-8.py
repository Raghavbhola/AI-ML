#----------------------------------[ Nov. 10, 2026 ]--------------------------------------


#Condictional operations - the operation which use to follow a particular situation
#1. If statement
age = int(input("Enter your age"))
if age >= 18: #enter into the body of the function - condition { ----- }
    print("Eligible to vote")

#2. If-else statement
number = 80
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#3. If-elif-else statements
score = 5
if score >= 95 and score <=100:
    grade = "A"
elif score >=75:
    grade = "B"
elif score >= 55:
    grade = "C"
elif score >=35:
    grade = "D"
else:
    grade = "RA"

print("Grade of your ward is", grade)

#4. Nested if statement
username = "admin"
password = "admin@1234"
if username == "admin":
    if password == "admin@123":
        print("Login successfull")
    else:
        print("Password is incorrect")
else:
    print("Unknown user")

#5. And, or operator
age = 25
is_allowed = False
if age >=18 and is_allowed:
    print("Entry allow")
else:
    print("Entry restricted")

# day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Its a weekend")
else:
    print("Its a workday")

#6. Membership conditions
course_list = ["Python", "SQL", "DBMS"]
select_c = "Python"
if select_c in course_list:
    print("Course is available")
