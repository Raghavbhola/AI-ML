#-----------------------------------{Day-3 , [Nov. 03, 2026]}-----------------------------------------------------

#Replacing and splitting and joining strings ---------------------
updated_text = string.replace("fox", "Lion") #it looks for whole string and sub-string too
print(updated_text)
updated_words = updated_text.split()
print("Updated words :- ", updated_words)

li = ['Kunal', 'Akash', 'Kirtika', 'Lion', 'Rat - raghav']
print(type(li))
joined_text = " -@- ".join(li)
print("Joined string:- ",joined_text)

#Formatting a string
course = "Python programming"
joinees = 6
print("Format:- ", "{} persons are attending {} course".format(joinees, course))
print(f"F-string:- {course} has {joinees} participants")

#List and its operations
#List - its dynamic in nature, no size restriction

abc = [1,2.0,"Akash", True, 2+3j, 'w']
li = []
courses = ["Python","Excel", "SQL"]
print(len(courses))
courses.append("PowerBI")
print(courses)
print(len(courses))
print("First course:-", courses[3])


#List and its operations
numbers = [30,10,20,40]
numbers.append(40)
numbers.append([40,50,60])
print("Appended list:- ",numbers)
numbers.insert(1,15)
print(numbers)
numbers.remove(30) #it works on element
print(numbers)
numbers.sort()
print(numbers)
print("Removed:- ", numbers.pop()) #it work on indexes

courses = ["Python","Excel", "SQL", "Python"]
courses.append("Django")
print("After append:- ", courses)
courses.extend(["Git", "Linux", "SQLite"])
print("After extend:- ", courses)
courses.insert(1, "Java")

# courses.remove("Excel")
# courses.pop()

print(courses.index("SQL"))
print(courses.count("Python"))
courses.sort()
print(courses)
courses.reverse()
print(courses)

backup_li = courses.copy()
courses.clear()
print(courses)
