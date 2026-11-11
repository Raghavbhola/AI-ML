#----------------------[ Nov. 11, 2026 ]-------------------------

#Iteration, Iterators - doing a task continously until a specific sitaution to be met
#1. Basic for loop body
courses = ["Python", "SQL", "Excel", "Java"]
for i in courses: #no data-type needed varible, no initialization, (auto-increment - its dedicatedly only for FOR loop)
    print(i)

#2. Range function
for i in range(2,60,2): #range functionality - start,end,jump - is any parameter mandatory (yes, end is mand.)
    print(i)

#3. While loop
count = 1
while count <= 5:
    print(count)
    count +=1
  
#4. Break statement
for ab in range(1,11):
    if ab == 6:
        break
    print(number)
