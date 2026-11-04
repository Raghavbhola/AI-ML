#--------------------------------------[ Nov. 4, 2026 ]------------------------------------------------------- 

#tuple and its operation
Employee = (101, "Anita", "Dev") #Packing of elements
emp_id,name,role = Employee #Unpacking of elements
#tuple is immutable in nature - you can't change the values in future, in list its possible - mutable in nature
Employee[2] = "Shubham"
print(Employee)
print(name,"works as", role)

values = (10,20,30,10,40,10,50, 10, 40)
#Tuple has only two public methods:- count and index
print("Count of occurance of 10:", values.count(10))
print("Index of 10:-", values.index(10))

#Tuple operations that doesn't modify the tuple
x = len(values) - 1
print(values[x])
print("First value:-", values[0])
print("Last value:-", values[-1])
print("First three values", values[:3])
print("lenght of tuple", len(values))
print("Max value:-", max(values))
print("Min value:-", min(values))
print("Sum value:-", sum(values))

#Tuple unpacking
Employee = (101, "Anita", "Dev") #Packing of elements
emp_id,name,role = Employee #Unpacking of elements
print("Unpacked values:- ", emp_id,name,role)

#Extended unpacking
first, *middle, last = values
print("First:-", first)
print("Middle:-", middle)
# print("Last:-", last)
